# tac_ir.py

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
        # Formata a instrução para ser legível, ex: "_t0 = a + b"
        if self.opcode in ['+', '-', '*', '/']:
            return f"{self.result} = {self.arg1} {self.opcode} {self.arg2}"
        elif self.opcode == 'COPY':
            return f"{self.result} = {self.arg1}"
        elif self.opcode == 'IF_FALSE':
            return f"if_false {self.arg1} goto {self.result}"
        elif self.opcode == 'GOTO':
            return f"goto {self.result}"
        elif self.opcode == 'LABEL':
            return f"{self.result}:"
        # Adicione outros opcodes aqui (print, summon, etc.)
        return f"{self.opcode}..."