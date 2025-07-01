# llvm_generator.py (Versão Final e Completa)

from llvmlite import ir, binding
from tac_ir import TACInstruction, TACOperand
# import ctypes # ctypes não é estritamente necessário para esta implementação

class LLVMGenerator:
    def __init__(self, tac_code):
        self.tac_code = tac_code
        self.module = ir.Module(name="meu_programa")
        self.int_type = ir.IntType(32)
        self.symbol_table = {}
        self.builder = None

        # --- ALTERAÇÃO 1: Declarar a função externa 'printf' ---
        # Define a assinatura da função: i32 printf(i8*, ...)
        # i8* é um ponteiro para char (uma string em C)
        # var_arg=True permite que a função tenha um número variável de argumentos
        printf_type = ir.FunctionType(self.int_type, [ir.IntType(8).as_pointer()], var_arg=True)
        self.printf = ir.Function(self.module, printf_type, name="printf")
        # ----------------------------------------------------

    def _get_var_ptr(self, var_name):
        """ Retorna o ponteiro para uma variável, alocando-a se for a primeira vez. """
        if var_name not in self.symbol_table:
            ptr = self.builder.alloca(self.int_type, name=var_name)
            self.symbol_table[var_name] = ptr
        return self.symbol_table[var_name]

    def generate(self):
        main_func_type = ir.FunctionType(self.int_type, [], False)
        main_func = ir.Function(self.module, main_func_type, name="main")
        entry_block = main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(entry_block)

        label_blocks = {
            instr.result.name: main_func.append_basic_block(name=instr.result.name)
            for instr in self.tac_code if instr.opcode == 'LABEL'
        }

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

            # --- ALTERAÇÃO 2: Adicionar a lógica para o PRINT ---
            elif instr.opcode == 'PRINT':
                # Pega o texto da string e o prepara no formato C (com \n e \0)
                text = instr.arg1.name[1:-1]
                text_to_print = text + "\n\0"
                
                # Cria uma constante LLVM para a nossa string
                c_text = ir.Constant(ir.ArrayType(ir.IntType(8), len(text_to_print)),
                                     bytearray(text_to_print.encode("utf8")))
                
                # Aloca memória e armazena a string lá. O ponteiro 'str_ptr'
                # aqui tem o tipo [N x i8]* (ponteiro para array)
                str_ptr = self.builder.alloca(c_text.type)
                self.builder.store(c_text, str_ptr)

                # --- A CORREÇÃO ESTÁ AQUI ---
                # Converte o ponteiro para o tipo que printf espera (i8*)
                # usando bitcast.
                char_ptr = self.builder.bitcast(str_ptr, ir.IntType(8).as_pointer())
                
                # Usa o ponteiro do tipo correto na chamada da função
                self.builder.call(self.printf, [char_ptr])
        
        # Finaliza a função
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(self.int_type, 0))
            
        return str(self.module)