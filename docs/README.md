# 📚 Documentação - Índice Completo

Bem-vindo à documentação do **Sistema de Gerenciamento de Usuários e Produtos**.

---

## 📖 Documentos Disponíveis

### 1. 🎯 **GUIA DE USO** 
📄 **Arquivo:** [GUIA_USO.md](GUIA_USO.md)

**Para quem:** Usuários finais da aplicação

**Conteúdo:**
- Como iniciar a aplicação
- Como usar cada aba (Usuários, Produtos, Estatísticas)
- Validações aplicadas
- Resolvendo problemas (Troubleshooting)
- Exemplos de entrada

**Quando ler:**
- Você quer usar o aplicativo
- Recebeu uma mensagem de erro
- Quer aprender a usar cada função

---

### 2. 🏗️ **DIAGRAMAS E ARQUITETURA**
📄 **Arquivo:** [DIAGRAMAS.md](DIAGRAMAS.md)

**Para quem:** Arquitetos e desenvolvedores

**Conteúdo:**
- Diagramas UML das classes
- Padrões de design utilizados
- Fluxos de dados
- Relacionamento entre componentes
- Visão geral da arquitetura

**Quando ler:**
- Você quer entender como o sistema é organizado
- Precisa fazer modificações na arquitetura
- Quer aprender sobre padrões de design

---

### 3. 📝 **DOCUMENTAÇÃO TÉCNICA COMPLETA**
📄 **Arquivo:** [DOCUMENTACAO_TECNICA.md](DOCUMENTACAO_TECNICA.md)

**Para quem:** Desenvolvedores e revisores

**Conteúdo (12 seções):**
1. Introdução e finalidade do projeto
2. Integrantes da equipe
3. Descrição do projeto
4. Arquitetura do sistema (MVC)
5. Padrões de design (DAO, Repository)
6. Validações implementadas
7. Fluxos de funcionamento
8. Exemplos de código
9. Conceitos de Engenharia de Software (SOLID)
10. Testes realizados
11. Futuras melhorias
12. Conclusão e referências

**Quando ler:**
- Você precisa de documentação completa
- Quer entender cada linha de código
- Precisa manter o projeto
- Quer aprender sobre SOLID e boas práticas

---

### 4. 📖 **README - OVERVIEW**
📄 **Arquivo:** [README.md](README.md)

**Para quem:** Todos

**Conteúdo:**
- Visão geral do projeto
- Início rápido
- Links para outras documentações
- Estrutura de arquivos
- Conceitos principais

**Quando ler:**
- Primeiro documento a ler
- Quer uma visão geral rápida

---

### 5. 📋 **DOCUMENTAÇÃO PDF (ABNT)**
📄 **Arquivo:** `DOCUMENTACAO.pdf`

**Para quem:** Professores e apresentação

**Formato:** PDF com padrão ABNT

**Conteúdo:**
- Capa com dados da equipe
- Sumário
- Introdução
- Descrição do projeto
- Arquitetura
- Validações
- Conclusão
- Referências

**Como gerar:**
```bash
# Usando Pandoc
pandoc DOCUMENTACAO_TECNICA.md -o DOCUMENTACAO.pdf

# Ou no Word:
# Copie o conteúdo de DOCUMENTACAO_TECNICA.md
# Cole no Word
# Configure como ABNT
# Exporte como PDF
```

---

## 🗺️ Mapa de Navegação

```
┌─ Usuário Final
│  └─ Quer usar? → [GUIA_USO.md](GUIA_USO.md)
│
├─ Desenvolvedor
│  ├─ Quer entender? → [DIAGRAMAS.md](DIAGRAMAS.md) → [DOCUMENTACAO_TECNICA.md](DOCUMENTACAO_TECNICA.md)
│  └─ Quer modificar? → [DOCUMENTACAO_TECNICA.md](DOCUMENTACAO_TECNICA.md)
│
├─ Professor/Revisor
│  ├─ Quer visão geral? → [README.md](README.md)
│  ├─ Quer arquitetura? → [DIAGRAMAS.md](DIAGRAMAS.md)
│  └─ Quer tudo? → [DOCUMENTACAO_TECNICA.md](DOCUMENTACAO_TECNICA.md)
│
└─ Apresentação
   └─ Imprima → [DOCUMENTACAO.pdf](DOCUMENTACAO.pdf)
```

---

## 📊 Cronograma de Leitura

### ⏱️ 5 minutos
- Leia: [README.md](README.md)

### ⏱️ 15 minutos  
- Leia: [GUIA_USO.md](GUIA_USO.md)
- Execute: `python main.py`

### ⏱️ 30 minutos
- Leia: [DIAGRAMAS.md](DIAGRAMAS.md)
- Entenda a arquitetura

### ⏱️ 1 hora
- Leia: [DOCUMENTACAO_TECNICA.md](DOCUMENTACAO_TECNICA.md)
- Explore o código

---

## ✅ Checklist de Requisitos Atendidos

- ✅ **Aplicativo Desktop** → Implementado com Tkinter
- ✅ **Cadastro de Usuários e Produtos** → Totalmente funcional
- ✅ **Separação de Responsabilidades** → Padrão MVC aplicado
- ✅ **Orientação a Objetos** → Classes bem definidas
- ✅ **Arquitetura Definida** → MVC + DAO documentados
- ✅ **Documentação** → Este arquivo + 3 mais
- ✅ **Diagramas de Classes** → Em DIAGRAMAS.md
- ✅ **Código Comentado** → Bem documentado no fonte
- ✅ **Repositório GitHub** → [Link do seu repositório]
- ✅ **Padrão ABNT** → DOCUMENTACAO_TECNICA.md

---

## 🎯 Informações Rápidas

### Como Executar?
```bash
cd ProjetoFinal/src
python main.py
```

### Quais Tecnologias?
- Python 3.8+
- Tkinter (built-in)
- Padrões: MVC, DAO, Repository

### Quantas Linhas de Código?
- **modelo.py:** ~80 linhas
- **repositorio.py:** ~120 linhas
- **controlador.py:** ~200 linhas
- **visao.py:** ~450 linhas
- **Total:** ~850 linhas

### Qual é o Padrão Utilizado?
- **Arquitetura:** MVC (Model-View-Controller)
- **Persistência:** DAO (Data Access Object)
- **Dados:** Repository Pattern

---

## 📞 Dúvidas Frequentes

### P: Preciso instalar algo?
**R:** Não! Python e Tkinter já vêm juntos.

### P: Onde fica o código?
**R:** Em `ProjetoFinal/src/` (5 arquivos Python)

### P: Meus dados são salvos?
**R:** Não, dados estão apenas em memória. Fecha = perde dados.

### P: Como modificar o projeto?
**R:** Leia `DOCUMENTACAO_TECNICA.md` e modifique os arquivos em `src/`

### P: Qual é a melhor parte do código?
**R:** A separação em camadas (Model, View, Controller)

---

## 🚀 Próximos Passos

1. **Leia** o README principal
2. **Execute** a aplicação (`python main.py`)
3. **Use** as funcionalidades
4. **Explore** o código
5. **Estude** a arquitetura
6. **Modifique** e experimente
7. **Aprenda** com os padrões utilizados

---

## 👥 Equipe

| Nome | Função |
|------|--------|
| (Preencher) | Desenvolvedor |
| (Preencher) | Desenvolvedor |
| (Preencher) | Desenvolvedor |
| (Preencher) | Documentalista |

---

## 📅 Data e Versão

- **Data de Entrega:** 29 de Abril de 2026
- **Versão:** 1.0
- **Status:** ✅ Completo
- **Apresentação:** 09/05/2026

---

## 🎓 Disciplina

- **Matéria:** Engenharia de Software
- **Professor:** Lucas Melo
- **Série:** 2° DS (Desenvolvimento de Sistemas)
- **Instituição:** [Preencher]

---

*Para dúvidas específicas, consulte o documento relevante acima.*
