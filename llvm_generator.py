# llvm_generator.py (Versão Final e Completa com Input do Usuário)

from llvmlite import ir, binding
from tac_ir import TACInstruction, TACOperand

class LLVMGenerator:
    def __init__(self, tac_code):
        self.tac_code = tac_code
        self.module = ir.Module(name="meu_programa")
        self.int_type = ir.IntType(32)
        self.symbol_table = {}
        self.builder = None

        # Declara a função externa 'printf'
        printf_type = ir.FunctionType(self.int_type, [ir.IntType(8).as_pointer()], var_arg=True)
        self.printf = ir.Function(self.module, printf_type, name="printf")
        
        # --- ALTERAÇÃO 1: Declarar a função externa 'scanf' ---
        scanf_type = ir.FunctionType(self.int_type, [ir.IntType(8).as_pointer()], var_arg=True)
        self.scanf = ir.Function(self.module, scanf_type, name="scanf")
        # ----------------------------------------------------

    def _get_var_ptr(self, var_name):
        """ Retorna o ponteiro para uma variável, alocando-a se for a primeira vez. """
        if var_name not in self.symbol_table:
            ptr = self.builder.alloca(self.int_type, name=var_name)
            self.symbol_table[var_name] = ptr
        return self.symbol_table[var_name]

    # --- ALTERAÇÃO 2: Função auxiliar para criar strings globais ---
    def _create_global_string(self, text_val, name_prefix="str"):
        """Cria uma string global no módulo e retorna um ponteiro i8* para ela."""
        text_bytes = bytearray((text_val + '\0').encode('utf8'))
        string_type = ir.ArrayType(ir.IntType(8), len(text_bytes))
        
        # Cria a variável global para a string
        global_var = ir.GlobalVariable(self.module, string_type, name=f"{name_prefix}_{len(self.module.globals)}")
        global_var.initializer = ir.Constant(string_type, text_bytes)
        global_var.linkage = 'internal'
        global_var.global_constant = True
        
        # Retorna um ponteiro para o primeiro elemento do array (i8*)
        return global_var.gep([ir.Constant(self.int_type, 0), ir.Constant(self.int_type, 0)])
    # -----------------------------------------------------------

    def generate(self):
        main_func_type = ir.FunctionType(self.int_type, [], False)
        main_func = ir.Function(self.module, main_func_type, name="main")
        entry_block = main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(entry_block)

        label_blocks = {
            instr.result.name: main_func.append_basic_block(name=instr.result.name)
            for instr in self.tac_code if instr.opcode == 'LABEL'
        }

        # Criar a string de formato "%d" para o scanf uma única vez
        scanf_format_ptr = self._create_global_string("%d", "scanf_fmt")

        for instr in self.tac_code:
            if instr.opcode == 'COPY':
                dest_ptr = self._get_var_ptr(instr.result.name)
                try:
                    source_val = ir.Constant(self.int_type, int(instr.arg1.name))
                except ValueError:
                    source_ptr = self._get_var_ptr(instr.arg1.name)
                    source_val = self.builder.load(source_ptr)
                self.builder.store(source_val, dest_ptr)
            
            elif instr.opcode == '+':
                ptr1, ptr2 = self._get_var_ptr(instr.arg1.name), self._get_var_ptr(instr.arg2.name)
                val1, val2 = self.builder.load(ptr1), self.builder.load(ptr2)
                result = self.builder.add(val1, val2)
                result_ptr = self._get_var_ptr(instr.result.name)
                self.builder.store(result, result_ptr)

            elif instr.opcode in ['>', '<', '>=', '<=', '==', '!=']:
                ptr1, ptr2 = self._get_var_ptr(instr.arg1.name), self._get_var_ptr(instr.arg2.name)
                val1, val2 = self.builder.load(ptr1), self.builder.load(ptr2)
                result = self.builder.icmp_signed(instr.opcode, val1, val2)
                result_ptr = self._get_var_ptr(instr.result.name)
                final_value = self.builder.zext(result, self.int_type)
                self.builder.store(final_value, result_ptr)

            elif instr.opcode in ['and', 'or']:
                ptr1, ptr2 = self._get_var_ptr(instr.arg1.name), self._get_var_ptr(instr.arg2.name)
                val1, val2 = self.builder.load(ptr1), self.builder.load(ptr2)
                bool1, bool2 = self.builder.trunc(val1, ir.IntType(1)), self.builder.trunc(val2, ir.IntType(1))
                if instr.opcode == 'and':
                    result = self.builder.and_(bool1, bool2)
                else:
                    result = self.builder.or_(bool1, bool2)
                result_ptr = self._get_var_ptr(instr.result.name)
                final_value = self.builder.zext(result, self.int_type)
                self.builder.store(final_value, result_ptr)

            elif instr.opcode == 'LABEL':
                target_block = label_blocks[instr.result.name]
                if not self.builder.block.is_terminated:
                    self.builder.branch(target_block)
                self.builder.position_at_end(target_block)

            elif instr.opcode == 'GOTO':
                target_block = label_blocks[instr.result.name]
                self.builder.branch(target_block)

            elif instr.opcode == 'IF_FALSE':
                cond_ptr = self._get_var_ptr(instr.arg1.name)
                cond_val_i32 = self.builder.load(cond_ptr)
                cond_val_i1 = self.builder.trunc(cond_val_i32, ir.IntType(1))
                false_block = label_blocks[instr.result.name]
                true_block = main_func.append_basic_block(name="if_true")
                self.builder.cbranch(cond_val_i1, true_block, false_block)
                self.builder.position_at_end(true_block)

            elif instr.opcode == 'PRINT':
                text = instr.arg1.name[1:-1] # Remove aspas <>
                text_ptr = self._create_global_string(text + '\n', "print_str")
                self.builder.call(self.printf, [text_ptr])

            # --- ALTERAÇÃO 3: Adicionar a lógica para SUMMON ---
            elif instr.opcode == 'SUMMON':
                # 1. Imprime o prompt na tela
                prompt_text = instr.arg1.name[1:-1]
                prompt_ptr = self._create_global_string(prompt_text + " ", "prompt_str")
                self.builder.call(self.printf, [prompt_ptr])

                # 2. Aloca espaço para o scanf preencher
                input_buffer_ptr = self.builder.alloca(self.int_type, name="input_buffer")

                # 3. Chama scanf("%d", &input_buffer)
                self.builder.call(self.scanf, [scanf_format_ptr, input_buffer_ptr])

                # 4. Carrega o valor lido do buffer
                read_value = self.builder.load(input_buffer_ptr)
                
                # 5. Armazena o valor lido na variável de destino do TAC (ex: _t0)
                dest_ptr = self._get_var_ptr(instr.result.name)
                self.builder.store(read_value, dest_ptr)
            # ----------------------------------------------------

        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(self.int_type, 0))
            
        return str(self.module)