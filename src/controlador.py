from modelo import Usuario, Produto
from repositorio import RepositorioUsuarios, RepositorioProdutos


class Controlador:
    def __init__(self):
        self.repo_usuarios = RepositorioUsuarios()
        self.repo_produtos = RepositorioProdutos()
    
    # USUÁRIOS
    def adicionar_usuario(self, nome, email, cpf, telefone):
        if not nome or not email or not cpf or not telefone:
            return False, "Preencha todos os campos!"
        
        if self.repo_usuarios.cpf_existe(cpf):
            return False, "CPF já cadastrado!"
        
        if not cpf.isdigit() or len(cpf) != 11:
            return False, "CPF inválido!"
        
        if "@" not in email:
            return False, "Email inválido!"
        
        usuario = Usuario(nome, email, cpf, telefone)
        self.repo_usuarios.adicionar(usuario)
        return True, f"Usuário {nome} adicionado!"
    
    def remover_usuario(self, indice):
        if 0 <= indice < len(self.repo_usuarios.obter_todos()):
            usuario = self.repo_usuarios.obter_todos()[indice]
            self.repo_usuarios.remover(indice)
            return True, f"{usuario.nome} removido!"
        return False, "Usuário não encontrado"
    
    def obter_usuarios(self):
        usuarios = self.repo_usuarios.obter_todos()
        lista = []
        for u in usuarios:
            lista.append(str(u))
        return lista
    
    def total_usuarios(self):
        return self.repo_usuarios.quantidade()
    
    # PRODUTOS
    def adicionar_produto(self, nome, preco, quantidade, descricao=""):
        if not nome:
            return False, "Nome do produto obrigatório!"
        
        if self.repo_produtos.produto_existe(nome):
            return False, "Produto já existe!"
        
        try:
            preco_float = float(preco.replace(",", "."))
            if preco_float <= 0:
                return False, "Preço deve ser maior que zero!"
        except:
            return False, "Preço inválido!"
        
        try:
            qtd_int = int(quantidade)
            if qtd_int < 0:
                return False, "Quantidade não pode ser negativa!"
        except:
            return False, "Quantidade inválida!"
        
        produto = Produto(nome, preco_float, qtd_int, descricao)
        self.repo_produtos.adicionar(produto)
        return True, f"Produto {nome} adicionado!"
    
    def remover_produto(self, indice):
        if 0 <= indice < len(self.repo_produtos.obter_todos()):
            produto = self.repo_produtos.obter_todos()[indice]
            self.repo_produtos.remover(indice)
            return True, f"{produto.nome} removido!"
        return False, "Produto não encontrado"
    
    def obter_produtos(self):
        produtos = self.repo_produtos.obter_todos()
        lista = []
        for p in produtos:
            lista.append(str(p))
        return lista
    
    def total_produtos(self):
        return self.repo_produtos.quantidade()
    
    def valor_total_estoque(self):
        total = 0
        for p in self.repo_produtos.obter_todos():
            total += p.preco * p.quantidade
        return total
