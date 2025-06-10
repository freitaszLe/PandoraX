# executor.py

from PandoraXVisitor import PandoraXVisitor

# =====================================================================
# 🚀 CLASSE DE EXECUÇÃO (INTERPRETADOR) 🚀
# Esta classe caminha na árvore e executa as ações da linguagem.
# =em==================================================================

class PandoraX_executor(PandoraXVisitor):
    def __init__(self):
        # Dicionário para armazenar as variáveis durante a execução
        self.variables = {}

    def visitProgram(self, ctx):
        # Visita cada uma das declarações (statements) do programa
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitOutputStatement(self, ctx):
        # Lida com a interpolação de strings para a saída
        text = ctx.INTERPOLATED_STRING().getText()[1:-1]
        while '{' in text and '}' in text:
            start = text.find('{')
            end = text.find('}')
            var_name = text[start+1:end]
            # Substitui a variável pelo seu valor armazenado
            value = self.variables.get(var_name, 'nulo') # Retorna 'nulo' se a variável não existir
            text = text.replace(f'{{{var_name}}}', str(value))
        print(text)

    def visitAssignment(self, ctx):
        # Atribui o valor de uma expressão a uma variável
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value

    def visitDeclaration(self, ctx):
        # Este método lida com a inicialização de variáveis (ex: inter a = 3)
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        # Retornar o valor é opcional, mas útil para consistência
        return value
    
    def visitIntExpr(self, ctx):
        return int(ctx.INT().getText())

    def visitIdExpr(self, ctx):
        var_name = ctx.ID().getText()
        # Retorna o valor da variável se ela existir, senão retorna None
        return self.variables.get(var_name)

    def visitConditionalStatement(self, ctx):
        # Avalia a expressão do 'when'
        condition = self.visit(ctx.expression())

        # Se a condição for verdadeira, executa o primeiro bloco (if)
        if condition:
            self.visit(ctx.block(0))
        # Senão, se existir um bloco 'whenever' (else), executa o segundo bloco
        elif ctx.WHENEVER() and len(ctx.block()) > 1:
            self.visit(ctx.block(1))  


    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '*':
            return left * right
        else:
            # Adiciona verificação para evitar divisão por zero
            if right == 0:
                raise Exception(f"Erro em tempo de execução: Divisão por zero.")
            return left // right

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '+':
            return left + right
        else:
            return left - right
            
    # Cole aqui o resto dos seus métodos 'visit' do PandoraXExecutor
    # (visitComparisonExpr, visitEqualityExpr, visitIdExpr, etc.)
    # ...