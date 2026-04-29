# 📐 Diagramas de Classes

## Diagrama UML - Camada Model

```
┌──────────────────────────────────────────┐
│            USUARIO                       │
├──────────────────────────────────────────┤
│ - nome: str                              │
│ - email: str                             │
│ - cpf: str                               │
│ - telefone: str                          │
│ - data_cadastro: datetime                │
├──────────────────────────────────────────┤
│ + __init__(nome, email, cpf, telefone)   │
│ + para_dicionario() -> dict              │
│ + __str__() -> str                       │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│            PRODUTO                       │
├──────────────────────────────────────────┤
│ - nome: str                              │
│ - preco: float                           │
│ - quantidade: int                        │
│ - descricao: str                         │
│ - data_cadastro: datetime                │
├──────────────────────────────────────────┤
│ + __init__(nome, preco, qtd, desc)       │
│ + para_dicionario() -> dict              │
│ + __str__() -> str                       │
└──────────────────────────────────────────┘
```

## Diagrama UML - Camada Repositório (DAO)

```
┌─────────────────────────────────────────────┐
│      REPOSITORIOUSUARIOS                    │
├─────────────────────────────────────────────┤
│ - _usuarios: List[Usuario]                  │
├─────────────────────────────────────────────┤
│ + adicionar(usuario: Usuario)               │
│ + obter_todos() -> List[Usuario]            │
│ + obter_por_indice(indice) -> Usuario       │
│ + remover(indice) -> bool                   │
│ + buscar_por_cpf(cpf) -> Usuario            │
│ + cpf_existe(cpf) -> bool                   │
│ + quantidade() -> int                       │
│ + limpar()                                  │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│      REPOSITORIOFRODUTOS                    │
├─────────────────────────────────────────────┤
│ - _produtos: List[Produto]                  │
├─────────────────────────────────────────────┤
│ + adicionar(produto: Produto)               │
│ + obter_todos() -> List[Produto]            │
│ + obter_por_indice(indice) -> Produto       │
│ + remover(indice) -> bool                   │
│ + buscar_por_nome(nome) -> Produto          │
│ + produto_existe(nome) -> bool              │
│ + quantidade() -> int                       │
│ + limpar()                                  │
└─────────────────────────────────────────────┘
```

## Diagrama UML - Camada Controller

```
┌──────────────────────────────────────────────────────┐
│       CONTROLADORAPLICACAO                           │
├──────────────────────────────────────────────────────┤
│ - repo_usuarios: RepositorioUsuarios                 │
│ - repo_produtos: RepositorioProdutos                 │
├──────────────────────────────────────────────────────┤
│ # Usuários                                           │
│ + adicionar_usuario(nome, email, cpf, tel) -> (bool,str)
│ + remover_usuario(indice) -> (bool, str)            │
│ + obter_usuarios() -> list                           │
│ + total_usuarios() -> int                            │
│                                                      │
│ # Produtos                                           │
│ + adicionar_produto(nome, preco, qtd, desc) -> (bool,str)
│ + remover_produto(indice) -> (bool, str)            │
│ + obter_produtos() -> list                           │
│ + total_produtos() -> int                            │
│                                                      │
│ # Estatísticas                                       │
│ + obter_estatisticas() -> dict                       │
└──────────────────────────────────────────────────────┘
```

## Diagrama UML - Camada View

```
┌──────────────────────────────────────────────────────┐
│       JANELAAPLICACAO (tk.Tk)                        │
├──────────────────────────────────────────────────────┤
│ - controlador: ControladorAplicacao                  │
│ - notebook: ttk.Notebook                             │
│ - listbox_usuarios: tk.Listbox                       │
│ - listbox_produtos: tk.Listbox                       │
│ - (múltiplos Entry widgets)                          │
├──────────────────────────────────────────────────────┤
│ # Setup                                              │
│ + __init__()                                         │
│ + _criar_interface()                                 │
│                                                      │
│ # Abas                                               │
│ + _criar_aba_usuarios()                              │
│ + _criar_aba_produtos()                              │
│ + _criar_aba_estatisticas()                          │
│                                                      │
│ # Usuários                                           │
│ + _adicionar_usuario()                               │
│ + _remover_usuario()                                 │
│ + _limpar_usuarios()                                 │
│ + _atualizar_listbox_usuarios()                      │
│                                                      │
│ # Produtos                                           │
│ + _adicionar_produto()                               │
│ + _remover_produto()                                 │
│ + _limpar_produtos()                                 │
│ + _atualizar_listbox_produtos()                      │
│                                                      │
│ # Estatísticas                                       │
│ + _atualizar_estatisticas()                          │
└──────────────────────────────────────────────────────┘
```

## Diagrama de Relacionamento entre Classes

```
┌─────────────────────────────────────────────────────────────┐
│                   VISÃO GERAL                               │
└─────────────────────────────────────────────────────────────┘

        ┌─────────────────────────────────────┐
        │      JanelaAplicacao (View)         │
        │       (Interface Tkinter)           │
        └──────────────┬──────────────────────┘
                       │
                       │ usa
                       ▼
        ┌─────────────────────────────────────┐
        │  ControladorAplicacao (Controller)   │
        │    (Lógica de Negócio)              │
        └──────────────┬──────────────────────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐
    │ RepoUsr  │ │RepoProd  │ │ Modelo   │
    │ (DAO)    │ │ (DAO)    │ │          │
    └────┬─────┘ └────┬─────┘ └──────────┘
         │            │
         ▼            ▼
    ┌─────────────────────┐
    │ Usuario, Produto    │
    │ (Entities)          │
    └─────────────────────┘
```

## Fluxo de Dados

### Quando usuário clica "Adicionar Usuário"

```
JanelaAplicacao._adicionar_usuario()
        │
        ├─ Captura dados dos Entry widgets
        │
        ▼
ControladorAplicacao.adicionar_usuario()
        │
        ├─ Valida dados
        ├─ Cria instância de Usuario
        │
        ▼
RepositorioUsuarios.adicionar()
        │
        ├─ Adiciona à lista interna
        │
        ▼
JanelaAplicacao._atualizar_listbox_usuarios()
        │
        ├─ Atualiza interface gráfica
```

### Quando usuário clica "Remover Usuário"

```
JanelaAplicacao._remover_usuario()
        │
        ├─ Obtém índice selecionado no Listbox
        │
        ▼
ControladorAplicacao.remover_usuario()
        │
        ├─ Valida índice
        │
        ▼
RepositorioUsuarios.remover()
        │
        ├─ Remove da lista interna
        │
        ▼
JanelaAplicacao._atualizar_listbox_usuarios()
        │
        ├─ Atualiza interface gráfica
```

## Padrões de Design Utilizados

### 1. **Model-View-Controller (MVC)**
```
┌─────────────────────────────────────────────┐
│               APPLICATION                   │
├──────────┬─────────────────────┬────────────┤
│  VIEW    │   CONTROLLER        │   MODEL    │
│          │                     │            │
│ Tkinter  │ Business Logic      │ Entities   │
│ Interface│ Validations         │ DAO Pattern│
└─────────┴─────────────────────┴────────────┘
```

### 2. **Data Access Object (DAO)**
Separa a lógica de acesso a dados da lógica de negócio.

```
Controller    DAO Layer      Data
    │           │              │
    ├──Operation─→ Repository   │
    │           │              │
    │         Manipulates      │
    │           │              │
    │           ├──Store/Get──→ List
    │           │              │
    ←─Returns───┤              │
```

### 3. **Repository Pattern**
Cria uma abstração entre Controller e dados.

## Fluxo Geral da Aplicação

```
1. INICIALIZAÇÃO
   main.py
      ▼
   JanelaAplicacao.__init__()
      ├─ Cria ControladorAplicacao
      ├─ Inicializa Repositórios
      └─ Cria Interface Gráfica

2. LOOP PRINCIPAL
   mainloop()
      ├─ Aguarda eventos do usuário
      └─ Processa ações

3. AÇÃO DO USUÁRIO
   Clique em botão
      ▼
   Método View (ex: _adicionar_usuario())
      ▼
   Método Controller (ex: adicionar_usuario())
      ▼
   Método Repository (ex: adicionar())
      ▼
   Atualiza dados
      ▼
   View se atualiza automaticamente

4. ENCERRAMENTO
   Usuário fecha janela
      ▼
   mainloop() encerra
      ▼
   Dados em memória são descartados
```

---

*Documentação de arquitetura do projeto de Engenharia de Software*
