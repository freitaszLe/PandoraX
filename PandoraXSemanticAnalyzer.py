# semantic_analyzer.py

from PandoraXVisitor import PandoraXVisitor

# =====================================================================
#  FASE 4: ANALISADOR SEMÂNTICO 
# Classe Visitor para verificar regras semânticas (tipos, variáveis, etc.).
# =====================================================================

class PandoraXSemanticAnalyzer(PandoraXVisitor):
    def __init__(self):
        self.symbol_table = {}  # nome da variável -> tipo ('inter', 'strin', 'bool')
        self.errors = []
        self.log = []

    def visitProgram(self, ctx):
        self.log.append("Iniciando análise semântica.")
        for stmt in ctx.statement():
            self.visit(stmt)
        self.log.append("Análise semântica finalizada.")
        return self.errors, self.log

    # Visita uma declaração (com ou sem 'summon')
    # Em semantic_analyzer.py, SUBSTITUA o método visitDeclaration por este:

    # Em executor.py, SUBSTITUA o método visitDeclaration por este:

    def visitDeclaration(self, ctx):
        # --- LÓGICA ATUALIZADA PARA AS DUAS FORMAS DE DECLARAÇÃO ---

        # Forma 1: Declaração com atribuição direta (ex: inter a = 3)
        if ctx.expression():
            var_name = ctx.ID().getText()
            value = self.visit(ctx.expression())
            self.variables[var_name] = value

        # Forma 2: Declaração com input do usuário (ex: a = inter(summon.x(...)))
        else:
            var_name = ctx.ID().getText()
            target_type = ctx.typeCast().getText().lower()
            
            # Pega a mensagem do prompt e remove as aspas <>
            prompt_message = ctx.INTERPOLATED_STRING().getText()[1:-1]
            
            # Mostra a mensagem e espera o input do usuário
            user_input = input(prompt_message + " ") # Adiciona um espaço para ficar mais bonito
            
            # Tenta converter o input para o tipo esperado
            try:
                final_value = None
                if target_type == 'inter':
                    final_value = int(user_input)
                elif target_type == 'strin':
                    final_value = str(user_input) # Se um dia você usar string
                # Adicione aqui outros tipos se precisar (ex: float, bool)
                else:
                    final_value = user_input # Se o tipo não for reconhecido, salva como string

                # Armazena o valor convertido na memória do executor
                self.variables[var_name] = final_value

            except ValueError:
                # Se o usuário digitar um texto onde se esperava um número
                print(f"\nERRO DE EXECUÇÃO: Valor '{user_input}' é inválido para o tipo '{target_type}'.")
                # Em um compilador real, você poderia decidir parar a execução aqui
                # Por enquanto, vamos atribuir um valor padrão (0 ou None)
                self.variables[var_name] = 0


    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in self.symbol_table:
            self.errors.append(f"Erro na linha {ctx.start.line}: Variável '{var_name}' não foi declarada antes da atribuição.")
            return

        var_type = self.symbol_table[var_name]
        expr_type = self.visit(ctx.expression())

        if expr_type != "erro" and expr_type != var_type:
            self.errors.append(f"Erro na linha {ctx.start.line}: Tipo incompatível ao atribuir '{expr_type}' para variável '{var_name}' do tipo '{var_type}'.")

    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()
        if name not in self.symbol_table:
            self.errors.append(f"Erro na linha {ctx.start.line}: Variável '{name}' usada sem declaração.")
            return "erro"
        return self.symbol_table[name]

    def visitIntExpr(self, ctx):
        return "inter"

    def visitBoolExpr(self, ctx):
        return "bool"
        
    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != "inter" or right != "inter":
            self.errors.append(f"Erro na linha {ctx.start.line}: Operação de soma/subtração requer operandos inteiros.")
            return "erro"
        return "inter"

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        # Detectar divisão por zero literal (simples)
        if op == "/" and hasattr(ctx.expression(1), 'INT') and ctx.expression(1).getText() == "0":
            self.errors.append(f"Erro na linha {ctx.start.line}: Divisão por zero literal detectada.")
        if left != "inter" or right != "inter":
            self.errors.append(f"Erro na linha {ctx.start.line}: Operação de multiplicação/divisão requer operandos inteiros.")
            return "erro"
        return "inter"

    def visitAndExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != "bool" or right != "bool":
            self.errors.append(f"Erro na linha {ctx.start.line}: Operação 'and' requer operandos booleanos.")
            return "erro"
        return "bool"

    def visitOrExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != "bool" or right != "bool":
            self.errors.append(f"Erro na linha {ctx.start.line}: Operação 'or' requer operandos booleanos.")
            return "erro"
        return "bool"

    def visitEqualityExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != "erro" and right != "erro" and left != right:
            self.errors.append(f"Erro na linha {ctx.start.line}: Comparação de igualdade entre tipos diferentes ('{left}' e '{right}').")
            return "erro"
        return "bool"

    def visitComparisonExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != "inter" or right != "inter":
            self.errors.append(f"Erro na linha {ctx.start.line}: Comparação (>, <, >=, <=) requer operandos inteiros.")
            return "erro"
        return "bool"

    def visitNotExpr(self, ctx):
        expr = self.visit(ctx.expression())
        if expr != "bool":
            self.errors.append(f"Erro na linha {ctx.start.line}: Operação 'not' requer operando booleano.")
            return "erro"
        return "bool"

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())