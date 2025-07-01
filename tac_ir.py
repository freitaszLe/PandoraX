

class TACOperand:
    """Representa um operando: uma variável, um temporário ou uma label."""
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return str(self.name)

class TACInstruction:
    """Representa uma instrução de Três Endereços."""
    def __init__(self, opcode, result=None, arg1=None, arg2=None):
        self.opcode = opcode  # Ex: '+', '-', 'IF_FALSE', 'GOTO', 'LABEL'
        self.result = result  # TACOperand (destino)
        self.arg1 = arg1      # TACOperand
        self.arg2 = arg2      # TACOperand
        

    def __repr__(self):
       
        # Operações com 2 argumentos e 1 resultado (formato padrão)
        if self.opcode in ['+', '-', '*', '/', '>', '<', '>=', '<=', '==', '!=', 'and', 'or']:
            return f"{self.result} = {self.arg1} {self.opcode} {self.arg2}"
        
        # Operação de cópia/atribuição
        elif self.opcode == 'COPY':
            return f"{self.result} = {self.arg1}"
            
        # Desvio condicional
        elif self.opcode == 'IF_FALSE':
            return f"if_false {self.arg1} goto {self.result}"
            
        # Desvio incondicional
        elif self.opcode == 'GOTO':
            return f"goto {self.result}"
            
        # Definição de uma label
        elif self.opcode == 'LABEL':
            return f"{self.result}:"
            
        # Impressão na tela
        elif self.opcode == 'PRINT':
            return f"print {self.arg1}"
            
        # Se nenhum formato for reconhecido, mostra o opcode para depuração
        return f"opcode_desconhecido({self.opcode})"