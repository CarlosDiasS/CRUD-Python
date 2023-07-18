import tkinter
from tkinter import Tk
from tkinter import ttk
import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Projetosemestre1',
    database = 'projetocrud'

)
cursor = conexao.cursor()

janela = tkinter.Tk()
janela.title('Controle de Estoque')
#READ
#treeview com a tabela do banco de dados

tree = ttk.Treeview(janela)
tree.grid(column=0, row = 2)
tree["columns"] = ("nome_produto", "valor", "quantidade")
tree.heading("#0", text = "ID")
tree.heading("nome_produto", text = "nome_produto")
tree.heading("valor", text = "valor")
tree.heading("quantidade", text = "quantidade")

cursor.execute("SELECT * FROM tabela_produtos")

for row in cursor.fetchall():
    tree.insert("","end", text=row[0], values=(row[1], row[2], row[3]))
tree.pack()

#botao para adicionar produto

def abrir_janela_add():
    janela_add = tkinter.Toplevel(janela)
    janela_add.title("Adicionar um produto ao estoque")
    label_informativo = tkinter.Label(janela_add, text = "Preencha os campos abaixo:")
    label_informativo.pack()

    #entry nome do produto

    nome_var = tkinter.StringVar()
    label_nome= tkinter.Label(janela_add, text="insira o nome do produto :")
    label_nome.pack()
    input_nome = tkinter.Entry(janela_add, textvariable= nome_var)
    input_nome.pack()

    #entry valor do produto

    valor_var = tkinter.StringVar()
    label_valor = tkinter.Label(janela_add, text = "insira o valor do produto :")
    label_valor.pack()
    input_valor = tkinter.Entry(janela_add, textvariable= valor_var)
    input_valor.pack()

    #entry da qntd do produto

    qntd_var = tkinter.StringVar()
    label_qntd = tkinter.Label(janela_add, text = "insira a quantidade do produto :")
    label_qntd.pack()
    input_qntd = tkinter.Entry(janela_add, textvariable=qntd_var)
    input_qntd.pack()

    #CREATE
    def criar_produto():
        nome = input_nome.get()
        valor = input_valor.get()
        qntd = input_qntd.get()
        comando_create = f'INSERT INTO tabela_produtos (nome_produto, valor, quantidade) VALUES ("{nome}" , "{valor}" ,' \
                         f"{qntd}"')'

        cursor.execute(comando_create)
        conexao.commit()  # edita o banco de dados
        janela_add.destroy()
    botao_ok = tkinter.Button(janela_add, text ="Ok", command=criar_produto)
    botao_ok.pack()

botao_add = tkinter.Button(janela, text = "Adicionar produto no estoque", command=abrir_janela_add)
botao_add.pack()

#botao para deletar produto

def abrir_janela_del():
    janela_del = tkinter.Toplevel(janela)
    janela_del.title("Remover um produto ao estoque")
    label_informativo = tkinter.Label(janela_del, text="Preencha os campos abaixo:")
    label_informativo.pack()

    # entry nome do produto

    nome_var = tkinter.StringVar()
    label_nome = tkinter.Label(janela_del, text="insira o nome do produto :")
    label_nome.pack()
    input_nome = tkinter.Entry(janela_del, textvariable=nome_var)
    input_nome.pack()

    # entry da qntd do produto

    qntd_var = tkinter.IntVar()
    label_qntd = tkinter.Label(janela_del, text="insira a quantidade que deseja remover :")
    label_qntd.pack()
    input_qntd = tkinter.Entry(janela_del, textvariable=qntd_var)
    input_qntd.pack()

    # DELETE
    def deletar_prod():

        produto_del = input_nome.get()
        quant_del = input_qntd.get()
        qntd_int = int(quant_del)

        for c in range(qntd_int):
            comando_delete = f'DELETE from tabela_produtos WHERE nome_produto = "{produto_del}" '
            cursor.execute(comando_delete)
            conexao.commit()
        janela_del.destroy()
    botao_ok = tkinter.Button(janela_del, text="Ok", command=deletar_prod)
    botao_ok.pack()

botao_del = tkinter.Button(janela, text = "Deletar produto no estoque", command=abrir_janela_del)
botao_del.pack()

#botao para atualizar item do estoque

def abrir_janela_update():
    janela_upt = tkinter.Toplevel(janela)
    janela_upt.title("Atualizar um produto do estoque")
    label_informativo = tkinter.Label(janela_upt, text="Preencha os campos abaixo:")
    label_informativo.pack()

    # entry nome do produto

    nome_var = tkinter.StringVar()
    label_nome = tkinter.Label(janela_upt, text="insira o nome do produto :")
    label_nome.pack()
    input_nome = tkinter.Entry(janela_upt, textvariable=nome_var)
    input_nome.pack()

    # entry valor do produto

    valor_var = tkinter.IntVar()
    label_valor = tkinter.Label(janela_upt, text="insira o novo valor do produto :")
    label_valor.pack()
    input_valor = tkinter.Entry(janela_upt, textvariable=valor_var)
    input_valor.pack()

    # entry da qntd do produto

    qntd_var = tkinter.IntVar()
    label_qntd = tkinter.Label(janela_upt, text="insira a nova quantidade do produto :")
    label_qntd.pack()
    input_qntd = tkinter.Entry(janela_upt, textvariable=qntd_var)
    input_qntd.pack()

    #UPDATE
    def update_produto():
        produto_alteracao = nome_var.get()
        novo_valor = valor_var.get()
        novo_valor_int = int(novo_valor)
        nova_qntd = qntd_var.get()
        nova_qntd_int = int(nova_qntd)

        comando_update = f'UPDATE tabela_produtos SET valor = {novo_valor_int}, quantidade = {nova_qntd_int} ' \
                         f'WHERE nome_produto = "{produto_alteracao}"'
        cursor.execute(comando_update)
        conexao.commit()
        janela_upt.destroy()
    botao_ok = tkinter.Button(janela_upt, text="Ok", command=update_produto)
    botao_ok.pack()

botao_att = tkinter.Button(janela, text = "Atualizar  produto no estoque", command=abrir_janela_update)
botao_att.pack()

janela.mainloop()
cursor.close()
conexao.close()

