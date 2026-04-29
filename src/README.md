#  Sistema de Gerenciamento de Usuários e Produtos

Projeto acadêmico de **Engenharia de Software** - Programação Desktop com Tkinter.

## 📋 Requisitos Atendidos

- ✅ Aplicativo desktop em **Tkinter**
- ✅ Cadastro de **usuários e produtos**
- ✅ **Separação de dependências** (Model-View-Controller)
- ✅ **Orientação a Objetos** bem definida
- ✅ **Arquitetura em camadas** (Model, View, Controller)
- ✅ Validação de dados robusta
- ✅ Interface amigável e intuitiva

## 📁 Estrutura do Projeto

```
ProjetoFinal/
├── src/                    # Código-fonte
│   ├── main.py            # Ponto de entrada
│   ├── modelo.py          # Classes de domínio (Usuario, Produto)
│   ├── repositorio.py     # Data Access Object (DAO)
│   ├── controlador.py     # Lógica de negócio
│   └── visao.py           # Interface Tkinter
│
├── docs/                   # Documentação
│   ├── README.md          # Este arquivo
│   ├── DIAGRAMAS.md       # Diagramas de classes
│   └── DOCUMENTACAO.pdf   # Documentação ABNT
│
└── README.md              # Este arquivo
```

## 🏗️ Arquitetura

### Pattern MVC (Model-View-Controller)

```
┌─────────────────────────────────────────┐
│           VIEW (visao.py)               │
│    - Interface Tkinter                  │
│    - Captura eventos do usuário         │
│    - Exibe dados na tela                │
└────────────────┬────────────────────────┘
                 │
                 ▼ (chama métodos)
┌─────────────────────────────────────────┐
│     CONTROLLER (controlador.py)         │
│    - Valida entrada de dados            │
│    - Implementa regras de negócio       │
│    - Coordena Model e View              │
└────────────────┬────────────────────────┘
                 │
                 ▼ (manipula)
┌─────────────────────────────────────────┐
│  MODEL (modelo.py + repositorio.py)     │
│    - Define entidades (Usuario, Produto)│
│    - Persistência de dados (DAO)        │
│    - Lógica de armazenamento            │
└─────────────────────────────────────────┘
```

## 🚀 Como Executar

### 1. Navegue até a pasta `src`
```bash
cd ProjetoFinal/src
```

### 2. Execute o programa
```bash
python main.py
```

### 3. Use a interface
- Acesse as abas: **Usuários**, **Produtos** e **Estatísticas**
- Preencha os formulários
- Clique nos botões para adicionar ou remover itens

## 📦 Funcionalidades

### Usuários
- ✅ Adicionar novo usuário (com validação)
- ✅ Remover usuário selecionado
- ✅ Validação de CPF único
- ✅ Validação de email
- ✅ Visualizar lista completa

### Produtos
- ✅ Adicionar novo produto (com validação)
- ✅ Remover produto selecionado
- ✅ Validação de preço e quantidade
- ✅ Verificar produtos duplicados
- ✅ Visualizar lista completa

### Estatísticas
- ✅ Total de usuários cadastrados
- ✅ Total de produtos cadastrados
- ✅ Valor total em estoque

## 🔍 Principais Conceitos Implementados

### 1. **Separação de Responsabilidades**
Cada camada tem uma responsabilidade específica:
- **Modelo**: Dados e persistência
- **Controlador**: Lógica de negócio
- **Visão**: Interface gráfica

### 2. **Orientação a Objetos**
```python
# Classes bem definidas
class Usuario:
    def __init__(self, nome, email, cpf, telefone)
    def para_dicionario(self)

class RepositorioUsuarios:
    def adicionar(self, usuario)
    def remover(self, indice)
    def obter_todos(self)
```

### 3. **Design Patterns**
- **DAO (Data Access Object)**: Isolamento do acesso a dados
- **MVC**: Separação de camadas
- **Singleton**: Instância única de controlador

### 4. **Validação de Dados**
- Campos obrigatórios
- Validação de CPF (11 dígitos)
- Validação de email
- Validação de preço e quantidade

### 5. **Type Hints**
```python
def adicionar_usuario(self, nome: str, email: str, cpf: str, telefone: str) -> Tuple[bool, str]:
```

## 👥 Integrantes da Equipe

*(Preencher com os nomes dos membros da equipe)*

1. Integrante 1
2. Integrante 2
3. Integrante 3
4. Integrante 4 (opcional)

## 📚 Tecnologias Utilizadas

- **Linguagem**: Python 3.8+
- **Framework GUI**: Tkinter
- **Padrão de Arquitetura**: MVC
- **Paradigma**: Orientação a Objetos

## 📖 Próximas Melhorias

- [ ] Persistência em banco de dados (SQLite)
- [ ] Exportação de dados (CSV, Excel)
- [ ] Busca e filtro de dados
- [ ] Edição de usuários/produtos
- [ ] Interface responsiva
- [ ] Autenticação de usuários

## 📝 Notas de Implementação

### Validações Implementadas

**Usuários:**
- CPF deve ter exatamente 11 dígitos
- CPF deve ser único
- Email deve conter @ e .
- Nenhum campo pode estar vazio

**Produtos:**
- Nome não pode estar vazio
- Produto com mesmo nome não pode existir
- Preço deve ser maior que 0
- Quantidade não pode ser negativa

### Feedback ao Usuário
- Mensagens de sucesso (✅)
- Mensagens de erro (❌)
- Confirmação antes de remover
- Atualização automática de listas

## ⚙️ Estrutura Interna

### `modelo.py`
Define as entidades do negócio:
- `Usuario`: Representa um usuário
- `Produto`: Representa um produto

### `repositorio.py`
Implementa o padrão DAO:
- `RepositorioUsuarios`: Gerencia usuários
- `RepositorioProdutos`: Gerencia produtos

### `controlador.py`
Implementa a lógica de negócio:
- `ControladorAplicacao`: Orquestra operações

### `visao.py`
Implementa a interface:
- `JanelaAplicacao`: Janela principal com abas

## 🎓 Aprendizados

Este projeto ensina:
1. Separação de responsabilidades
2. Design Patterns (MVC, DAO)
3. Validação de dados
4. Tratamento de erros
5. GUI com Tkinter
6. Orientação a Objetos
7. Type Hints em Python
8. Boas práticas de código

---

**Última atualização**: 29 de abril de 2026
