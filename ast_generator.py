# =====================================================================
# 🌳 FASE 3: GERAÇÃO DA ÁRVORE SINTÁTICA ABSTRATA (AST) 🌳
# =====================================================================


from antlr4 import *
from antlr4.tree.Trees import Trees
from PandoraXParser import PandoraXParser
from PandoraXVisitor import PandoraXVisitor

class PandoraXASTGenerator(PandoraXVisitor):
    """Gera uma representação da AST no formato .dot para visualização."""
    def __init__(self):
        self.dot = ['digraph AST {', '  node [shape=box, fontname="Courier"];']
        self.node_count = 0
        self.parent_stack = []
        self.result = None

    def visit(self, ctx):
        if ctx is None: return None
        node_name = Trees.getNodeText(ctx, ruleNames=PandoraXParser.ruleNames).replace('"', '\\"')
        node_id = f'node{self.node_count}'
        self.node_count += 1
        self.dot.append(f'  {node_id} [label="{node_name}"];')
        if self.parent_stack:
            self.dot.append(f'  {self.parent_stack[-1]} -> {node_id};')
        self.parent_stack.append(node_id)

        if hasattr(ctx, 'children') and ctx.children is not None:
            for child in ctx.children:
                if isinstance(child, ParserRuleContext):
                    self.visit(child)
                elif isinstance(child, TerminalNode):
                    self._add_terminal_node(child)

        self.parent_stack.pop()
        if not self.parent_stack:
            self.dot.append('}')
            self.result = '\n'.join(self.dot)
        return self.result

    def _add_terminal_node(self, terminal_node):
        if terminal_node.getSymbol().type == Token.EOF: return
        node_id = f'node{self.node_count}'
        self.node_count += 1
        token_text = terminal_node.getText().replace('"', '\\"')
        self.dot.append(f'  {node_id} [label="{token_text}", shape=ellipse, color=blue];')
        if self.parent_stack:
            self.dot.append(f'  {self.parent_stack[-1]} -> {node_id};')

    def get_dot(self):
        return self.result