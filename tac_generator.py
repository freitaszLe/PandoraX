## Este é o núcleo do trabalho. Cada visit não irá calcular um valor,
#  mas sim gerar instruções e retornar o TACOperand onde o resultado foi armazenado.

from PandoraXVisitor import PandoraXVisitor
from tac_ir import TACOperand, TACInstruction

class TACGenerator(PandoraXVisitor):
    def __init__(self):
        self.tac_code = []     # A lista de instruções geradas
        self.temp_count = 0    # Contador para variáveis temporárias (_t0, _t1, ...)
        self.label_count = 0   # Contador para labels (L0, L1, ...)

    def new_temp(self):
        temp_name = f"_t{self.temp_count}"
        self.temp_count += 1
        return TACOperand(temp_name)

    def new_label(self):
        label_name = f"L{self.label_count}"
        self.label_count += 1
        return TACOperand(label_name)

    # O coração da lógica estará nos métodos 'visit'

    def visitAddSubExpr(self, ctx):
    # 1. Visita os filhos para obter os operandos (que podem ser variáveis ou temporários)
        op1 = self.visit(ctx.expression(0))
        op2 = self.visit(ctx.expression(1))

        # 2. Cria um novo temporário para guardar o resultado
        result_temp = self.new_temp()
        
        # 3. Cria a instrução TAC
        opcode = ctx.getChild(1).getText() # Pega o '+' ou '-'
        instruction = TACInstruction(opcode, result_temp, op1, op2)
        
        # 4. Adiciona a instrução à lista
        self.tac_code.append(instruction)
        
        # 5. Retorna o operando temporário para a expressão pai usar
        return result_temp

    def visitParenExpr(self, ctx):
    # Apenas visita a expressão interna e retorna o resultado dela.
        return self.visit(ctx.expression())

    def visitEqualityExpr(self, ctx):
        op1 = self.visit(ctx.expression(0))
        op2 = self.visit(ctx.expression(1))
        result_temp = self.new_temp()
        opcode = ctx.getChild(1).getText() # Pega o '==' ou '!='
        
        instruction = TACInstruction(opcode, result_temp, op1, op2)
        self.tac_code.append(instruction)
        return result_temp

    def visitIntExpr(self, ctx):
        # Literais não precisam de instrução, apenas retornamos um operando
        return TACOperand(ctx.getText())

    def visitIdExpr(self, ctx):
        # Variáveis também, apenas retornamos um operando com o nome dela
        return TACOperand(ctx.getText())

    def visitConditionalStatement(self, ctx):
        # 1. Gera o código para a condição
        condition_operand = self.visit(ctx.expression())
        
        # 2. Cria labels para o 'else' e para o fim do 'if'
        else_label = self.new_label()
        end_label = self.new_label()
        
        # 3. Gera o desvio condicional
        # "Se a condição for falsa, pule para a label do else"
        if_false_instr = TACInstruction('IF_FALSE', else_label, condition_operand)
        self.tac_code.append(if_false_instr)
        
        # 4. Gera o código do bloco 'then' (o corpo do 'when')
        self.visit(ctx.block(0))
        # "Depois de executar o then, pule para o fim do if"
        goto_end_instr = TACInstruction('GOTO', end_label)
        self.tac_code.append(goto_end_instr)
        
        # 5. Marca o início do bloco 'else'
        self.tac_code.append(TACInstruction('LABEL', else_label))
        if ctx.WHENEVER():
            self.visit(ctx.block(1)) # Gera o código do 'else'
            
        # 6. Marca o fim de toda a estrutura condicional
        self.tac_code.append(TACInstruction('LABEL', end_label))
    
    def visitComparisonExpr(self, ctx):
        op1 = self.visit(ctx.expression(0))
        op2 = self.visit(ctx.expression(1))
        result_temp = self.new_temp()
        opcode = ctx.getChild(1).getText() # Pega '>', '<', '==' etc.
        
        # Instruções de comparação também geram um resultado em um temporário
        instruction = TACInstruction(opcode, result_temp, op1, op2)
        self.tac_code.append(instruction)
        return result_temp

    def visitAndExpr(self, ctx):
        op1 = self.visit(ctx.expression(0))
        op2 = self.visit(ctx.expression(1))
        result_temp = self.new_temp()
        
        instruction = TACInstruction('and', result_temp, op1, op2)
        self.tac_code.append(instruction)
        return result_temp

    # FAÇA O MESMO PARA 'visitOrExpr'
    def visitOrExpr(self, ctx):
        op1 = self.visit(ctx.expression(0))
        op2 = self.visit(ctx.expression(1))
        result_temp = self.new_temp()
        
        instruction = TACInstruction('or', result_temp, op1, op2)
        self.tac_code.append(instruction)
        return result_temp
    
    def visitBlock(self, ctx):
    # Simplesmente visita cada statement dentro do bloco
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitOutputStatement(self, ctx):
    # Para simplificar, vamos tratar a string inteira como um operando.
    # A interpolação será responsabilidade da Etapa 4.
        string_literal = TACOperand(ctx.INTERPOLATED_STRING().getText())
    
    # Gera uma instrução PRINT
        instruction = TACInstruction('PRINT', arg1=string_literal)
        self.tac_code.append(instruction)
    
    # No arquivo tac_generator.py, dentro da classe TACGenerator

    def visitDeclaration(self, ctx):
        # Pega o nome da variável como um operando de destino
        var_name_operand = TACOperand(ctx.ID().getText())
        
        # Se a declaração tiver uma expressão (ex: inter a = 5)
        if ctx.expression():
            # Visita a expressão para obter o valor/operando dela
            expr_operand = self.visit(ctx.expression())
            
            # Cria uma instrução de cópia: a = 5
            instruction = TACInstruction('COPY', var_name_operand, expr_operand)
            self.tac_code.append(instruction)

        # Se for só 'inter a;', não gera instrução, a alocação será na Etapa 4.