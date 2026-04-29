# DOCUMENTAÇÃO TÉCNICA - SISTEMA DE GERENCIAMENTO DE USUÁRIOS E PRODUTOS

## 1. INTRODUÇÃO

### 1.1 Finalidade do Projeto
Este projeto foi desenvolvido como atividade prática da disciplina de Engenharia de Software para o 2º Desenvolvimento de Sistemas (DS), com o objetivo de aplicar conceitos de arquitetura de software, orientação a objetos e desenvolvimento de interfaces gráficas.

O sistema implementa um aplicativo desktop para gerenciamento de usuários e produtos, demonstrando na prática os padrões de design, separação de responsabilidades e boas práticas de engenharia de software.

### 1.2 Objetivos Específicos

- Implementar um aplicativo funcional com interface gráfica
- Aplicar o padrão de arquitetura Model-View-Controller (MVC)
- Demonstrar separação de responsabilidades entre camadas
- Implementar validação robusta de dados
- Utilizar conceitos de Orientação a Objetos (OOP)
- Documentar todo o processo de desenvolvimento

---

## 2. INTEGRANTES DA EQUIPE

| Nome | Matrícula | Função |
|------|-----------|--------|
| (Integrante 1) | - | Desenvolvedor Full-Stack |
| (Integrante 2) | - | Desenvolvedor Backend |
| (Integrante 3) | - | Desenvolvedor Frontend |
| (Integrante 4) | - | Documentalista (opcional) |

*Preencher com dados da equipe*

---

## 3. DESCRIÇÃO DO PROJETO

### 3.1 Características Principais

O sistema implementa as seguintes funcionalidades:

**Gerenciamento de Usuários:**
- Cadastro de novos usuários com validação
- Visualização de lista completa de usuários
- Remoção de usuários cadastrados
- Validação de CPF único
- Validação de email
- Data de cadastro automática

**Gerenciamento de Produtos:**
- Cadastro de novos produtos com validação
- Visualização de lista completa de produtos
- Remoção de produtos cadastrados
- Validação de preço e quantidade
- Descrição opcional de produtos
- Data de cadastro automática

**Funcionalidades Adicionais:**
- Estatísticas em tempo real
- Interface com abas para organização
- Mensagens de feedback ao usuário
- Validação completa de entrada de dados

### 3.2 Tecnologias Utilizadas

| Tecnologia | Versão | Finalidade |
|-----------|--------|-----------|
| Python | 3.8+ | Linguagem de programação |
| Tkinter | Built-in | Framework GUI (Interface Gráfica) |
| Type Hints | PEP 484 | Documentação de tipos |
| - | - | - |

### 3.3 Requisitos do Sistema

**Requisitos Funcionais:**
- RF1: Cadastrar usuário com validação de dados
- RF2: Remover usuário da lista
- RF3: Visualizar lista de usuários
- RF4: Cadastrar produto com validação de dados
- RF5: Remover produto da lista
- RF6: Visualizar lista de produtos
- RF7: Exibir estatísticas do sistema

**Requisitos Não-Funcionais:**
- RNF1: Interface responsiva e amigável
- RNF2: Validações executadas rapidamente
- RNF3: Mensagens de erro claras
- RNF4: Código bem documentado

---

## 4. ARQUITETURA DO SISTEMA

### 4.1 Padrão de Arquitetura: MVC

O projeto utiliza o padrão **Model-View-Controller** para separar as responsabilidades:

```
┌─────────────────────────────────────────────────────────┐
│                  ARCHITECTURE (MVC)                     │
├───────────────────────────────────────────────────────┬─┤
│ VIEW (visao.py)          CONTROLLER (controlador.py) │M│
│ - Interface Tkinter      - Lógica de Negócio        │O│
│ - Captura Eventos        - Validações               │D│
│ - Exibe Dados            - Coordenação              │E│
│                                                     │L│
│                                                     │  │
│ - Não conhece Model      - Não acessa UI diretamente│(│
│ - Chama Controller       - Usa Repositórios        │m│
│                          - Retorna (bool, msg)      │o│
└─────────────────────────────────────────────────────┴─┤
│                                                       │
│  REPOSITÓRIOS (repositorio.py) + MODELOS (modelo.py)│
│  - RepositorioUsuarios              - Usuario        │
│  - RepositorioProdutos              - Produto        │
└──────────────────────────────────────────────────────┘
```

### 4.2 Camadas e Responsabilidades

#### 4.2.1 Camada de Modelo (Model)

**Arquivo:** `modelo.py`

Responsável por definir as entidades de negócio:

```python
class Usuario:
    - nome: str
    - email: str
    - cpf: str
    - telefone: str
    - data_cadastro: datetime
    
    + para_dicionario()
    + __str__()

class Produto:
    - nome: str
    - preco: float
    - quantidade: int
    - descricao: str
    - data_cadastro: datetime
    
    + para_dicionario()
    + __str__()
```

**Características:**
- Entidades simples e focadas
- Métodos para formatação de saída
- Type hints em todos os parâmetros
- Sem lógica de negócio complexa

#### 4.2.2 Camada de Persistência (Data Access Layer)

**Arquivo:** `repositorio.py`

Implementa o padrão **Data Access Object (DAO)**:

```python
class RepositorioUsuarios:
    # Operações CRUD
    + adicionar(usuario)
    + remover(indice)
    + obter_todos()
    + obter_por_indice(indice)
    # Buscas especializadas
    + buscar_por_cpf(cpf)
    + cpf_existe(cpf)
    # Consultas
    + quantidade()
    + limpar()

class RepositorioProdutos:
    # Similar ao RepositorioUsuarios
    + adicionar(produto)
    + remover(indice)
    # ... etc
```

**Características:**
- Isolamento da lógica de persistência
- Fácil de mudar para banco de dados
- Operações CRUD bem definidas
- Validações de índice

#### 4.2.3 Camada de Lógica de Negócio (Controller)

**Arquivo:** `controlador.py`

Orquestra operações entre View e Model:

```python
class ControladorAplicacao:
    - repo_usuarios: RepositorioUsuarios
    - repo_produtos: RepositorioProdutos
    
    # Métodos de Usuário
    + adicionar_usuario(nome, email, cpf, tel) -> (bool, str)
    + remover_usuario(indice) -> (bool, str)
    + obter_usuarios() -> list
    
    # Métodos de Produto
    + adicionar_produto(nome, preco, qtd, desc) -> (bool, str)
    + remover_produto(indice) -> (bool, str)
    + obter_produtos() -> list
    
    # Estatísticas
    + obter_estatisticas() -> dict
```

**Características:**
- Validações de dados
- Regras de negócio
- Retorno de mensagens explicativas
- Sem manipulação de UI

#### 4.2.4 Camada de Apresentação (View)

**Arquivo:** `visao.py`

Implementa a interface gráfica com Tkinter:

```python
class JanelaAplicacao(tk.Tk):
    - controlador: ControladorAplicacao
    - notebook: ttk.Notebook
    - listbox_usuarios: tk.Listbox
    - listbox_produtos: tk.Listbox
    
    # Interface
    + _criar_interface()
    + _criar_aba_usuarios()
    + _criar_aba_produtos()
    + _criar_aba_estatisticas()
    
    # Eventos de Usuário
    + _adicionar_usuario()
    + _remover_usuario()
    + _limpar_usuarios()
    
    # Eventos de Produto
    + _adicionar_produto()
    + _remover_produto()
    + _limpar_produtos()
    
    # Atualizações
    + _atualizar_listbox_usuarios()
    + _atualizar_listbox_produtos()
    + _atualizar_estatisticas()
```

**Características:**
- Interface com abas (Notebook)
- Widgets organizados em frames
- Validação básica antes de enviar ao Controller
- Feedback visual ao usuário

---

## 5. PADRÕES DE DESIGN

### 5.1 Model-View-Controller (MVC)

Separação clara entre apresentação, lógica e dados.

**Benefícios:**
- Fácil manutenção
- Testabilidade
- Reutilização de componentes
- Separação de responsabilidades

### 5.2 Data Access Object (DAO)

Abstração do acesso a dados.

**Benefícios:**
- Isolamento da persistência
- Fácil trocar de JSON para BD
- Centralização de operações de dados

### 5.3 Repository Pattern

Cria uma camada de abstração entre lógica e dados.

```
Controller (usa repository como interface)
    ▼
RepositorioUsuarios (implementa CRUD)
    ▼
Dados (lista em memória)
```

---

## 6. VALIDAÇÕES IMPLEMENTADAS

### 6.1 Validações de Usuário

```python
def adicionar_usuario(nome, email, cpf, telefone):
    # 1. Campos obrigatórios
    if not all([nome.strip(), email.strip(), cpf.strip(), telefone.strip()]):
        return (False, "❌ Todos os campos devem ser preenchidos!")
    
    # 2. CPF único
    if repo_usuarios.cpf_existe(cpf):
        return (False, "❌ CPF já cadastrado!")
    
    # 3. CPF válido (11 dígitos)
    if not cpf.isdigit() or len(cpf) != 11:
        return (False, "❌ CPF deve conter 11 dígitos!")
    
    # 4. Email válido
    if "@" not in email or "." not in email:
        return (False, "❌ Email inválido!")
    
    # 5. Criar usuário
    usuario = Usuario(nome, email, cpf, telefone)
    repo_usuarios.adicionar(usuario)
    return (True, f"✅ Usuário '{nome}' adicionado com sucesso!")
```

### 6.2 Validações de Produto

```python
def adicionar_produto(nome, preco, quantidade, descricao=""):
    # 1. Nome não vazio
    if not nome.strip():
        return (False, "❌ Nome do produto não pode estar vazio!")
    
    # 2. Produto único
    if repo_produtos.produto_existe(nome):
        return (False, "❌ Produto já cadastrado!")
    
    # 3. Preço válido
    try:
        preco_float = float(preco.replace(",", "."))
        if preco_float <= 0:
            return (False, "❌ Preço deve ser maior que zero!")
    except ValueError:
        return (False, "❌ Preço deve ser um número válido!")
    
    # 4. Quantidade válida
    try:
        qtd_int = int(quantidade)
        if qtd_int < 0:
            return (False, "❌ Quantidade não pode ser negativa!")
    except ValueError:
        return (False, "❌ Quantidade deve ser um número inteiro!")
    
    # 5. Criar produto
    produto = Produto(nome, preco_float, qtd_int, descricao)
    repo_produtos.adicionar(produto)
    return (True, f"✅ Produto '{nome}' adicionado com sucesso!")
```

---

## 7. FLUXOS DE FUNCIONAMENTO

### 7.1 Fluxo: Adicionar Usuário

```
Usuário preenche formulário
    ▼
Clica botão "Adicionar"
    ▼
View._adicionar_usuario() é chamado
    ├─ Coleta dados dos Entry widgets
    ├─ Chama Controller.adicionar_usuario(nome, email, cpf, tel)
    │   ├─ Valida nome, email, CPF, telefone
    │   ├─ Verifica se CPF já existe
    │   ├─ Cria instância de Usuario
    │   └─ Chama Repository.adicionar(usuario)
    │       └─ Insere na lista (índice 0)
    │
    ├─ Recebe resposta (bool, mensagem)
    ├─ Se sucesso:
    │   ├─ Exibe messageBox de sucesso
    │   ├─ Limpa campos
    │   └─ Atualiza Listbox
    └─ Se erro:
        └─ Exibe messageBox de erro

Usuário vê a confirmação e o novo usuário na lista
```

### 7.2 Fluxo: Remover Usuário

```
Usuário seleciona usuário na Listbox
    ▼
Clica botão "Remover Selecionado"
    ▼
View._remover_usuario() é chamado
    ├─ Obtém índice selecionado (curselection())
    ├─ Se nenhum selecionado: exibe aviso
    ├─ Senão:
    │   ├─ Chama Controller.remover_usuario(indice)
    │   │   └─ Chama Repository.remover(indice)
    │   │       └─ Remove da lista
    │   │
    │   ├─ Recebe resposta
    │   ├─ Exibe confirmação
    │   └─ Atualiza Listbox

Usuário vê a lista atualizada sem o usuário removido
```

---

## 8. EXEMPLOS DE CÓDIGO

### 8.1 Exemplo: Classe Usuario

```python
from datetime import datetime

class Usuario:
    """Representa um usuário do sistema"""
    
    def __init__(self, nome: str, email: str, cpf: str, telefone: str):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.data_cadastro = datetime.now()
    
    def para_dicionario(self) -> dict:
        """Converte para dicionário"""
        return {
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "data_cadastro": self.data_cadastro.strftime("%d/%m/%Y %H:%M")
        }
    
    def __str__(self) -> str:
        return f"{self.nome} - {self.email} - {self.cpf} - {self.telefone}"
```

### 8.2 Exemplo: RepositorioUsuarios

```python
class RepositorioUsuarios:
    """Gerencia persistência de usuários"""
    
    def __init__(self):
        self._usuarios: List[Usuario] = []
    
    def adicionar(self, usuario: Usuario) -> None:
        """Adiciona novo usuário no início da lista"""
        self._usuarios.insert(0, usuario)
    
    def remover(self, indice: int) -> bool:
        """Remove usuário se índice é válido"""
        if 0 <= indice < len(self._usuarios):
            del self._usuarios[indice]
            return True
        return False
    
    def cpf_existe(self, cpf: str) -> bool:
        """Verifica se CPF já está cadastrado"""
        return any(u.cpf == cpf for u in self._usuarios)
```

### 8.3 Exemplo: ControladorAplicacao

```python
class ControladorAplicacao:
    """Orquestra operações do sistema"""
    
    def __init__(self):
        self.repo_usuarios = RepositorioUsuarios()
        self.repo_produtos = RepositorioProdutos()
    
    def adicionar_usuario(self, nome: str, email: str, cpf: str, telefone: str) -> Tuple[bool, str]:
        """Adiciona usuário com validação completa"""
        
        # Validações
        if not all([nome.strip(), email.strip(), cpf.strip(), telefone.strip()]):
            return False, "❌ Todos os campos devem ser preenchidos!"
        
        if self.repo_usuarios.cpf_existe(cpf):
            return False, "❌ CPF já cadastrado!"
        
        if not cpf.isdigit() or len(cpf) != 11:
            return False, "❌ CPF deve conter 11 dígitos!"
        
        if "@" not in email or "." not in email:
            return False, "❌ Email inválido!"
        
        # Criar e adicionar
        usuario = Usuario(nome, email, cpf, telefone)
        self.repo_usuarios.adicionar(usuario)
        return True, f"✅ Usuário '{nome}' adicionado com sucesso!"
```

---

## 9. CONCEITOS DE ENGENHARIA DE SOFTWARE APLICADOS

### 9.1 SOLID Principles

#### Single Responsibility (S)
- Cada classe tem uma única responsabilidade
- Usuario é responsável apenas pelos dados do usuário
- RepositorioUsuarios é responsável apenas por persistência

#### Open/Closed (O)
- Código aberto para extensão (novos tipos de repositório)
- Fechado para modificação (interface bem definida)

#### Liskov Substitution (L)
- Se implementássemos interface, qualquer repositório poderia substituir outro

#### Interface Segregation (I)
- Interfaces específicas para cada tipo de operação

#### Dependency Inversion (D)
- Controller depende de Repositório (abstração)
- View depende de Controller (abstração)

### 9.2 DRY (Don't Repeat Yourself)

```python
# BOM: Método genérico
def obter_por_indice(self, indice: int):
    if 0 <= indice < len(self._usuarios):
        return self._usuarios[indice]
    raise IndexError(f"Índice {indice} inválido")

# Usado em remover(), obter(), etc - sem repetição
```

### 9.3 KISS (Keep It Simple, Stupid)

```python
# Simples e direto
def cpf_existe(self, cpf: str) -> bool:
    return any(u.cpf == cpf for u in self._usuarios)

# Ao invés de código complexo com loops aninhados
```

### 9.4 YAGNI (You Aren't Gonna Need It)

- Não implementamos persistência em banco de dados (não era requisito)
- Não adicionamos features não solicitadas
- Código focado apenas nos requisitos

---

## 10. TESTES E VALIDAÇÃO

### 10.1 Testes Manuais Realizados

| Teste | Entrada | Resultado Esperado | Status |
|-------|---------|-------------------|--------|
| Adicionar usuário válido | Nome, Email, CPF, Telefone | Usuário adicionado | ✅ |
| CPF duplicado | CPF existente | Mensagem de erro | ✅ |
| Email inválido | Email sem @ | Mensagem de erro | ✅ |
| CPF com letras | "12345abcde1" | Mensagem de erro | ✅ |
| Remover usuário | Índice válido | Usuário removido | ✅ |
| Remover inexistente | Índice inválido | Mensagem de erro | ✅ |
| Adicionar produto válido | Nome, Preço, Qtd | Produto adicionado | ✅ |
| Preço negativo | "-10.00" | Mensagem de erro | ✅ |
| Produto duplicado | Nome existente | Mensagem de erro | ✅ |

---

## 11. FUTURAS MELHORIAS

### 11.1 Curto Prazo
- [ ] Persistência em SQLite
- [ ] Busca e filtro de dados
- [ ] Edição de usuários/produtos
- [ ] Export para CSV/Excel

### 11.2 Médio Prazo
- [ ] Autenticação de usuários
- [ ] Interface mais moderna (customtkinter)
- [ ] Gráficos e relatórios
- [ ] Multi-idioma

### 11.3 Longo Prazo
- [ ] Versão Web (Flask/Django)
- [ ] API REST
- [ ] Aplicativo Mobile
- [ ] Sistema de permissões

---

## 12. CONCLUSÃO

Este projeto demonstra com sucesso a aplicação de conceitos fundamentais de Engenharia de Software:

1. **Arquitetura:** Padrão MVC bem definido e implementado
2. **Design:** Utilização de padrões reconhecidos (DAO, Repository)
3. **Código:** Limpo, legível e bem documentado
4. **Validação:** Robusta e com feedback ao usuário
5. **OOP:** Princípios de orientação a objetos aplicados
6. **Boas Práticas:** SOLID, DRY, KISS, YAGNI

A estrutura permite fácil expansão e manutenção futura do projeto.

---

## REFERÊNCIAS

1. MARTIN, Robert C. Clean Code: A Handbook of Agile Software Craftsmanship. Prentice Hall, 2008.

2. GAMMA, Erich et al. Design Patterns: Elements of Reusable Object-Oriented Software. Addison-Wesley, 1994.

3. Python Type Hints Documentation: https://www.python.org/dev/peps/pep-0484/

4. Tkinter Documentation: https://docs.python.org/3/library/tkinter.html

---

*Documentação elaborada conforme padrões ABNT*  
*Data: 29 de abril de 2026*  
*Versão: 1.0*
