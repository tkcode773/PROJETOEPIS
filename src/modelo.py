from datetime import datetime

class Usuario:
    def __init__(self, nome, email, cpf, telefone):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.data_cadastro = datetime.now()
    
    def __str__(self):
        return f"{self.nome} - {self.email} - {self.cpf} - {self.telefone}"


class Produto:
    def __init__(self, nome, preco, quantidade, descricao=""):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.descricao = descricao
        self.data_cadastro = datetime.now()
    
    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f} - Qtd: {self.quantidade}"
