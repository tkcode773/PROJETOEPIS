from modelo import Usuario, Produto


class RepositorioUsuarios:
    def __init__(self):
        self._usuarios = []
    
    def adicionar(self, usuario):
        self._usuarios.insert(0, usuario)
    
    def obter_todos(self):
        return self._usuarios
    
    def remover(self, indice):
        if 0 <= indice < len(self._usuarios):
            del self._usuarios[indice]
            return True
        return False
    
    def cpf_existe(self, cpf):
        for usuario in self._usuarios:
            if usuario.cpf == cpf:
                return True
        return False
    
    def quantidade(self):
        return len(self._usuarios)


class RepositorioProdutos:
    def __init__(self):
        self._produtos = []
    
    def adicionar(self, produto):
        self._produtos.insert(0, produto)
    
    def obter_todos(self):
        return self._produtos
    
    def remover(self, indice):
        if 0 <= indice < len(self._produtos):
            del self._produtos[indice]
            return True
        return False
    
    def produto_existe(self, nome):
        for produto in self._produtos:
            if produto.nome.lower() == nome.lower():
                return True
        return False
    
    def quantidade(self):
        return len(self._produtos)
