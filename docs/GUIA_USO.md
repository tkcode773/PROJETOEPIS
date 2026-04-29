# 🎯 Guia de Uso do Sistema

## 🚀 Iniciando a Aplicação

### Pré-requisitos
- Python 3.8 ou superior
- Tkinter (vem por padrão com Python)

### Passos para Executar

1. **Abra o terminal/PowerShell**
2. **Navegue até a pasta `src`**
   ```bash
   cd ProjetoFinal/src
   ```
3. **Execute o programa**
   ```bash
   python main.py
   ```

A janela da aplicação será aberta automaticamente.

---

## 📋 Usando a Aplicação

### ✅ Aba: Usuários

#### Adicionar Novo Usuário
1. Preencha os campos:
   - **Nome**: Nome completo do usuário
   - **Email**: Email válido (deve conter @ e .)
   - **CPF**: 11 dígitos numéricos (sem pontuação)
   - **Telefone**: Número de telefone para contato

2. Clique no botão **"✅ Adicionar"**

3. Se houver erro, uma mensagem de alerta aparecerá
4. Se tudo estiver correto, uma confirmação será exibida
5. Os campos serão limpos automaticamente
6. A lista será atualizada com o novo usuário

**Exemplos de entrada válida:**
- Nome: João Silva
- Email: joao@gmail.com
- CPF: 12345678901
- Telefone: (11) 99999-9999

#### Remover Usuário
1. **Selecione um usuário** na lista abaixo (clique uma vez)
2. Clique no botão **"❌ Remover Selecionado"**
3. Uma confirmação pedirá aprovação
4. Após confirmar, o usuário será removido

#### Limpar os Campos
1. Clique no botão **"🗑️ Limpar Campos"**
2. Todos os campos de entrada serão resetados

---

### 📦 Aba: Produtos

#### Adicionar Novo Produto
1. Preencha os campos:
   - **Nome**: Nome do produto
   - **Preço (R$)**: Preço em reais (exemplo: 19.90 ou 19,90)
   - **Quantidade**: Quantidade em estoque (número inteiro)
   - **Descrição**: Descrição adicional do produto (opcional)

2. Clique no botão **"✅ Adicionar"**

3. Validações aplicadas:
   - Nome não pode estar vazio
   - Preço deve ser maior que 0
   - Quantidade não pode ser negativa
   - Não pode haver dois produtos com o mesmo nome

**Exemplos de entrada válida:**
- Nome: Notebook Dell
- Preço: 2500.00
- Quantidade: 5
- Descrição: Notebook I5 8GB RAM

#### Remover Produto
1. **Selecione um produto** na lista abaixo
2. Clique no botão **"❌ Remover Selecionado"**
3. Confirme a remoção
4. O produto será deletado da lista

#### Limpar os Campos
1. Clique no botão **"🗑️ Limpar Campos"**
2. Todos os campos serão resetados

---

### 📈 Aba: Estatísticas

Exibe informações resumidas do sistema:

- **Total de Usuários**: Quantidade total de usuários cadastrados
- **Total de Produtos**: Quantidade total de produtos cadastrados
- **Valor Total em Estoque**: Valor total de todos os produtos (preço × quantidade)

#### Atualizar Estatísticas
1. Clique no botão **"🔄 Atualizar Estatísticas"**
2. Os valores serão recalculados automaticamente
3. As estatísticas também se atualizam quando você adiciona ou remove usuários/produtos

---

## ⚠️ Validações e Regras

### Validações de Usuário

| Campo | Regra | Mensagem de Erro |
|-------|-------|-----------------|
| Nome | Não pode estar vazio | ❌ Todos os campos devem ser preenchidos! |
| Email | Não pode estar vazio | ❌ Todos os campos devem ser preenchidos! |
| Email | Deve conter @ e . | ❌ Email inválido! |
| CPF | Não pode estar vazio | ❌ Todos os campos devem ser preenchidos! |
| CPF | Deve ter 11 dígitos | ❌ CPF deve conter 11 dígitos! |
| CPF | Deve ser único | ❌ CPF já cadastrado! |
| Telefone | Não pode estar vazio | ❌ Todos os campos devem ser preenchidos! |

### Validações de Produto

| Campo | Regra | Mensagem de Erro |
|-------|-------|-----------------|
| Nome | Não pode estar vazio | ❌ Nome do produto não pode estar vazio! |
| Nome | Deve ser único | ❌ Produto já cadastrado! |
| Preço | Deve ser número | ❌ Preço deve ser um número válido! |
| Preço | Deve ser > 0 | ❌ Preço deve ser maior que zero! |
| Quantidade | Deve ser inteiro | ❌ Quantidade deve ser um número inteiro! |
| Quantidade | Não pode ser negativo | ❌ Quantidade não pode ser negativa! |

---

## 💾 Informações Importantes

### Dados em Memória
- Os dados estão armazenados **apenas em memória RAM**
- Ao fechar a aplicação, **todos os dados serão perdidos**
- Próximas versões podem incluir persistência em banco de dados

### Ordem de Exibição
- Os novos usuários/produtos aparecem **no topo da lista**
- A lista está sempre em ordem cronológica (mais novo primeiro)

### Interface Responsiva
- Você pode redimensionar a janela
- As listas aumentam/diminuem automaticamente
- Use a barra de rolagem se a lista ficar muito grande

---

## 🎓 Conceitos Implementados

### 1. Separação de Responsabilidades (MVC)
```
Você interage com a VIEW (interface)
    ▼
A VIEW chama o CONTROLLER (lógica)
    ▼
O CONTROLLER manipula o MODEL (dados)
    ▼
O VIEW se atualiza automaticamente
```

### 2. Validação de Dados
- Todos os dados são validados ANTES de serem armazenados
- O controlador retorna mensagens explicativas de erro
- A interface fornece feedback visual (✅ sucesso, ❌ erro)

### 3. Design Pattern DAO (Data Access Object)
- Os repositórios isolam a lógica de persistência
- O controlador não precisa saber como os dados são armazenados
- Fácil de mudar para banco de dados depois

### 4. Tratamento de Erros
- Nenhuma ação causa crash da aplicação
- Todos os erros são tratados e apresentados ao usuário
- Mensagens claras explicam o que deu errado

---

## 🔧 Troubleshooting (Resolvendo Problemas)

### ❌ "ModuleNotFoundError: No module named 'tkinter'"
**Solução:** Tkinter já vem com Python. Tente reinstalar Python marcando a opção Tkinter.

### ❌ "SyntaxError" ou "IndentationError"
**Solução:** Verifique se todos os arquivos estão na pasta `src` corretamente.

### ❌ A aplicação não inicia
**Solução:** Certifique-se de estar na pasta `src` ao executar:
```bash
cd ProjetoFinal/src
python main.py
```

### ❌ Dados desapareceram
**Solução:** Isso é normal! Os dados só existem enquanto o programa está aberto. Reabre para começar do zero.

---

## 📞 Suporte

Para dúvidas sobre o funcionamento:
1. Leia a documentação completa em `docs/DOCUMENTACAO.pdf`
2. Estude os diagramas em `docs/DIAGRAMAS.md`
3. Analise o código-fonte nos arquivos da pasta `src`

---

*Última atualização: 29 de abril de 2026*
