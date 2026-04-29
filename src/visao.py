import tkinter as tk
from tkinter import messagebox, ttk
from controlador import Controlador


class JanelaAplicacao(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controlador = Controlador()
        
        self.title("Sistema de Gerenciamento")
        self.geometry("900x600")
        
        self.criar_interface()
    
    def criar_interface(self):
        # Cabeçalho
        titulo = tk.Label(self, text="Gerenciamento de Usuários e Produtos", font=("Arial", 14, "bold"), pady=10)
        titulo.pack(fill="x")
        
        # Notebook com abas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Aba de Usuários
        self.frame_usuarios = tk.Frame(self.notebook)
        self.notebook.add(self.frame_usuarios, text="Usuários")
        self.criar_aba_usuarios()
        
        # Aba de Produtos
        self.frame_produtos = tk.Frame(self.notebook)
        self.notebook.add(self.frame_produtos, text="Produtos")
        self.criar_aba_produtos()
    
    def criar_aba_usuarios(self):
        # Formulário
        frame_form = tk.LabelFrame(self.frame_usuarios, text="Adicionar Usuário", padx=10, pady=10)
        frame_form.pack(fill="x", padx=10, pady=10)
        
        tk.Label(frame_form, text="Nome:").grid(row=0, column=0, sticky="w")
        self.entrada_nome = tk.Entry(frame_form, width=30)
        self.entrada_nome.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_form, text="Email:").grid(row=1, column=0, sticky="w")
        self.entrada_email = tk.Entry(frame_form, width=30)
        self.entrada_email.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(frame_form, text="CPF:").grid(row=2, column=0, sticky="w")
        self.entrada_cpf = tk.Entry(frame_form, width=30)
        self.entrada_cpf.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(frame_form, text="Telefone:").grid(row=3, column=0, sticky="w")
        self.entrada_telefone = tk.Entry(frame_form, width=30)
        self.entrada_telefone.grid(row=3, column=1, padx=5, pady=5)
        
        frame_botoes = tk.Frame(frame_form)
        frame_botoes.grid(row=4, column=0, columnspan=2, pady=10)
        
        tk.Button(frame_botoes, text="Adicionar", command=self.adicionar_usuario, bg="green", fg="white", width=15).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Limpar", command=self.limpar_usuarios, bg="orange", fg="white", width=15).pack(side="left", padx=5)
        
        # Lista de usuários
        frame_lista = tk.LabelFrame(self.frame_usuarios, text="Usuários", padx=10, pady=10)
        frame_lista.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.listbox_usuarios = tk.Listbox(frame_lista, height=12)
        self.listbox_usuarios.pack(fill="both", expand=True)
        
        tk.Button(self.frame_usuarios, text="Remover", command=self.remover_usuario, bg="red", fg="white").pack(pady=5)
        
        self.atualizar_listbox_usuarios()
    
    def criar_aba_produtos(self):
        # Formulário
        frame_form = tk.LabelFrame(self.frame_produtos, text="Adicionar Produto", padx=10, pady=10)
        frame_form.pack(fill="x", padx=10, pady=10)
        
        tk.Label(frame_form, text="Nome:").grid(row=0, column=0, sticky="w")
        self.entrada_prod_nome = tk.Entry(frame_form, width=30)
        self.entrada_prod_nome.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_form, text="Preço (R$):").grid(row=1, column=0, sticky="w")
        self.entrada_prod_preco = tk.Entry(frame_form, width=30)
        self.entrada_prod_preco.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(frame_form, text="Quantidade:").grid(row=2, column=0, sticky="w")
        self.entrada_prod_qtd = tk.Entry(frame_form, width=30)
        self.entrada_prod_qtd.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(frame_form, text="Descrição:").grid(row=3, column=0, sticky="w")
        self.entrada_prod_desc = tk.Entry(frame_form, width=30)
        self.entrada_prod_desc.grid(row=3, column=1, padx=5, pady=5)
        
        frame_botoes = tk.Frame(frame_form)
        frame_botoes.grid(row=4, column=0, columnspan=2, pady=10)
        
        tk.Button(frame_botoes, text="Adicionar", command=self.adicionar_produto, bg="green", fg="white", width=15).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Limpar", command=self.limpar_produtos, bg="orange", fg="white", width=15).pack(side="left", padx=5)
        
        # Lista de produtos
        frame_lista = tk.LabelFrame(self.frame_produtos, text="Produtos", padx=10, pady=10)
        frame_lista.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.listbox_produtos = tk.Listbox(frame_lista, height=12)
        self.listbox_produtos.pack(fill="both", expand=True)
        
        tk.Button(self.frame_produtos, text="Remover", command=self.remover_produto, bg="red", fg="white").pack(pady=5)
        
        self.atualizar_listbox_produtos()
    
    def adicionar_usuario(self):
        nome = self.entrada_nome.get()
        email = self.entrada_email.get()
        cpf = self.entrada_cpf.get()
        telefone = self.entrada_telefone.get()
        
        sucesso, mensagem = self.controlador.adicionar_usuario(nome, email, cpf, telefone)
        
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.limpar_usuarios()
            self.atualizar_listbox_usuarios()
        else:
            messagebox.showerror("Erro", mensagem)
    
    def remover_usuario(self):
        selecionado = self.listbox_usuarios.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um usuário!")
            return
        
        sucesso, mensagem = self.controlador.remover_usuario(selecionado[0])
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.atualizar_listbox_usuarios()
        else:
            messagebox.showerror("Erro", mensagem)
    
    def limpar_usuarios(self):
        self.entrada_nome.delete(0, tk.END)
        self.entrada_email.delete(0, tk.END)
        self.entrada_cpf.delete(0, tk.END)
        self.entrada_telefone.delete(0, tk.END)
    
    def atualizar_listbox_usuarios(self):
        self.listbox_usuarios.delete(0, tk.END)
        for usuario in self.controlador.obter_usuarios():
            self.listbox_usuarios.insert(tk.END, usuario)
    
    def adicionar_produto(self):
        nome = self.entrada_prod_nome.get()
        preco = self.entrada_prod_preco.get()
        quantidade = self.entrada_prod_qtd.get()
        descricao = self.entrada_prod_desc.get()
        
        sucesso, mensagem = self.controlador.adicionar_produto(nome, preco, quantidade, descricao)
        
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.limpar_produtos()
            self.atualizar_listbox_produtos()
        else:
            messagebox.showerror("Erro", mensagem)
    
    def remover_produto(self):
        selecionado = self.listbox_produtos.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um produto!")
            return
        
        sucesso, mensagem = self.controlador.remover_produto(selecionado[0])
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.atualizar_listbox_produtos()
        else:
            messagebox.showerror("Erro", mensagem)
    
    def limpar_produtos(self):
        self.entrada_prod_nome.delete(0, tk.END)
        self.entrada_prod_preco.delete(0, tk.END)
        self.entrada_prod_qtd.delete(0, tk.END)
        self.entrada_prod_desc.delete(0, tk.END)
    
    def atualizar_listbox_produtos(self):
        self.listbox_produtos.delete(0, tk.END)
        for produto in self.controlador.obter_produtos():
            self.listbox_produtos.insert(tk.END, produto)
