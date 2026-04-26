#Importando dependências do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

#importando Pillow
from PIL import Image, ImageTk

#tk calendário
from tkcalendar import Calendar, DateEntry
from datetime import date

#IMPORTANDO O VIEW
from view import *

#imagens dos botões
caminho = r'C:\Projetos\cadastro_de_alunos\assets\logo.png'
botaoadd = r'C:\Projetos\cadastro_de_alunos\assets\botao1.png'
botaosave = r'C:\Projetos\cadastro_de_alunos\assets\save.png'

#cores
co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#e5e5e5"
co3 = "#00a095"
co4 = "#403d3d"
co6 = "#00BFFF"
co7 = "#ef5350"
co8 = "#263238"
co9 = "e9edf5"

# Criando janela
janela = Tk()
janela.title("")
janela.geometry('850x620')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

Style = Style(janela)
Style.theme_use("clam")

#Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

#Trabalhando no Frame Logo
app_lp = Image.open(caminho)
app_lp = app_lp.resize((50, 50))
app_lp = ImageTk.PhotoImage(app_lp)
app_logo = Label(frame_logo, image=app_lp, text="Cadastro de Alunos", width=850,
                 compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_logo.place(x=0, y=0)


# ─────────────────────────────────────────
# FUNÇÃO ALUNOS
# ─────────────────────────────────────────

def alunos():

    # Nome
    Label(frame_detalhes, text="Nome*", height=1, anchor=NW,
          font=('Ivy 10'), bg=co1, fg=co4).place(x=4, y=10)
    e_nome = Entry(frame_detalhes, width=45, justify='left', relief='solid')
    e_nome.place(x=7, y=40)

    # E-mail
    Label(frame_detalhes, text="E-mail*", height=1, anchor=NW,
          font=('Ivy 10'), bg=co1, fg=co4).place(x=4, y=70)
    e_email = Entry(frame_detalhes, width=45, justify='left', relief='solid')
    e_email.place(x=7, y=100)

    # Telefone
    Label(frame_detalhes, text="Telefone*", height=1, anchor=NW,
          font=('Ivy 10'), bg=co1, fg=co4).place(x=4, y=130)
    e_tel = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_tel.place(x=7, y=160)

    # Sexo
    Label(frame_detalhes, text="Sexo*", height=1, anchor=NW,
          font=('Ivy 10'), bg=co1, fg=co4).place(x=190, y=130)
    c_sexo = ttk.Combobox(frame_detalhes, width=12, font=('Ivy 8 bold'))
    c_sexo['values'] = ('Masculino', 'Feminino', 'Outro')
    c_sexo.place(x=190, y=160)

    # Data de Nascimento
    Label(frame_detalhes, text='Data de Nascimento*', height=1, anchor=NW,
          font=('Ivy 10'), bg=co1, fg=co4).place(x=446, y=10)
    data_nascimento = DateEntry(frame_detalhes, width=18, background='darkblue',
                                foreground='white', borderwidth=2, year=2024)
    data_nascimento.place(x=450, y=40)

    # CPF
    Label(frame_detalhes, text="CPF*", height=1, anchor=NW,
          font=('Ivy 10'), bg=co1, fg=co4).place(x=446, y=70)
    e_cpf = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_cpf.place(x=450, y=100)

    # Turma
    Label(frame_detalhes, text="Turma*", height=1, anchor=NW,
          font=('Ivy 10'), bg=co1, fg=co4).place(x=446, y=130)
    c_turma = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_turma['values'] = ('Turma 1', 'Turma 2')
    c_turma.place(x=450, y=160)

    # Foto
    global imagem, l_imagem

    def escolher_imagem():
        global imagem, l_imagem
        caminho_imagem = fd.askopenfilename()
        if caminho_imagem:
            imagem = Image.open(caminho_imagem)
            imagem = imagem.resize((130, 130))
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem = Label(frame_detalhes, image=imagem, bg=co1)
            l_imagem.place(x=300, y=10)
            botao_foto['text'] = 'Trocar Foto'

    botao_foto = Button(frame_detalhes, command=escolher_imagem,
                        text='Carregar Foto'.upper(), width=20,
                        font=('Ivy 7'), bg=co1, fg=co0)
    botao_foto.place(x=300, y=160)

    # Separador lateral
    Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100,
          anchor=NW, font=('Ivy 1'), bg=co2, fg=co0).place(x=610, y=10)

    # Procurar
    Label(frame_detalhes, text="Procurar Aluno [Digite o nome]", height=1,
          anchor=NW, font=('Ivy 10'), bg=co1, fg=co4).place(x=627, y=10)
    e_nome_procurar = Entry(frame_detalhes, width=17, justify='center',
                            relief='solid', font=('Ivy 10'))
    e_nome_procurar.place(x=630, y=35)

    # ── Tabela de alunos ──
    global tree_aluno

    Label(frame_tabela, text="Tabela de Estudantes", height=1, anchor=NW,
          font=('Ivy 10 bold'), bg=co1, fg=co4).grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

    list_header = ['id', 'Nome', 'Email', 'Telefone', 'Sexo', 'Imagem', 'Data', 'CPF', 'Turma']

    tree_aluno = ttk.Treeview(frame_tabela, selectmode="browse",
                               columns=list_header, show="headings")
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)
    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=1)

    hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
    h  = [40, 150, 150, 70, 70, 70, 80, 80, 100]

    for n, col in enumerate(list_header):
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        tree_aluno.column(col, width=h[n], anchor=hd[n])

    # ── Funções internas ──

    def limpar_campos():
        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_tel.delete(0, END)
        e_cpf.delete(0, END)
        c_sexo.set('')
        c_turma.set('')

    def atualizar_tabela(dados):
        for row in tree_aluno.get_children():
            tree_aluno.delete(row)
        for item in dados:
            tree_aluno.insert('', 'end', values=item)

    def ver_tabela():
        dados = ver_alunos()
        atualizar_tabela(dados)

    def procurar_aluno():
        nome = e_nome_procurar.get()
        if nome == "":
            # Se campo vazio, mostra todos
            ver_tabela()
            return
        dados = buscar_aluno(nome)
        atualizar_tabela(dados)

    def criar_aluno():
        nome  = e_nome.get()
        email = e_email.get()
        tel   = e_tel.get()
        sexo  = c_sexo.get()
        cpf   = e_cpf.get()
        turma = c_turma.get()
        data  = data_nascimento.get()
        img   = ''

        # Validação
        for campo in [nome, email, tel, sexo, cpf, turma]:
            if campo == "":
                messagebox.showerror('Erro', 'Preencha todos os campos obrigatórios!')
                return

        # Salva no banco
        criar_alunos([nome, email, tel, sexo, img, data, cpf, turma])
        messagebox.showinfo('Sucesso', 'Aluno cadastrado com sucesso!')
        limpar_campos()
        ver_tabela()

    def selecionar_aluno(event):
        # Ao clicar na tabela, preenche os campos com os dados do aluno selecionado
        try:
            tree_item = tree_aluno.focus()
            valores   = tree_aluno.item(tree_item)['values']
            if not valores:
                return

            limpar_campos()
            e_nome.insert(0,  valores[1])
            e_email.insert(0, valores[2])
            e_tel.insert(0,   valores[3])
            c_sexo.set(valores[4])
            e_cpf.insert(0,   valores[7])
            c_turma.set(valores[8])

        except Exception:
            pass

    def atualizar_aluno_tela():
        try:
            tree_item = tree_aluno.focus()
            valores   = tree_aluno.item(tree_item)['values']
            if not valores:
                messagebox.showerror('Erro', 'Selecione um aluno na tabela!')
                return

            valor_id = valores[0]
            nome     = e_nome.get()
            email    = e_email.get()
            tel      = e_tel.get()
            sexo     = c_sexo.get()
            cpf      = e_cpf.get()
            turma    = c_turma.get()
            data     = data_nascimento.get()
            img      = valores[5]  # mantém imagem antiga

            for campo in [nome, email, tel, sexo, cpf, turma]:
                if campo == "":
                    messagebox.showerror('Erro', 'Preencha todos os campos obrigatórios!')
                    return

            atualizar_aluno([nome, email, tel, sexo, img, data, cpf, turma, valor_id])
            messagebox.showinfo('Sucesso', 'Aluno atualizado com sucesso!')
            limpar_campos()
            ver_tabela()

        except Exception as e:
            messagebox.showerror('Erro', f'Selecione um aluno na tabela!\n{e}')

    def deletar_aluno_tela():
        try:
            tree_item = tree_aluno.focus()
            valores   = tree_aluno.item(tree_item)['values']
            if not valores:
                messagebox.showerror('Erro', 'Selecione um aluno na tabela!')
                return

            confirmar = messagebox.askyesno('Confirmar', f'Deseja deletar o aluno "{valores[1]}"?')
            if confirmar:
                deletar_aluno(valores[0])
                messagebox.showinfo('Sucesso', 'Aluno deletado com sucesso!')
                limpar_campos()
                ver_tabela()

        except Exception as e:
            messagebox.showerror('Erro', f'Selecione um aluno na tabela!\n{e}')

    # Ao clicar na linha da tabela, preenche os campos automaticamente
    tree_aluno.bind('<<TreeviewSelect>>', selecionar_aluno)

    # ── Botões ──
    Button(frame_detalhes, command=criar_aluno, anchor=CENTER, text='Criar'.upper(),
           width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1).place(x=627, y=110)

    Button(frame_detalhes, command=atualizar_aluno_tela, anchor=CENTER, text='Atualizar'.upper(),
           width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1).place(x=627, y=135)

    Button(frame_detalhes, command=deletar_aluno_tela, anchor=CENTER, text='Deletar'.upper(),
           width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1).place(x=627, y=160)

    Button(frame_detalhes, command=ver_tabela, anchor=CENTER, text='Ver'.upper(),
           width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0).place(x=727, y=160)

    Button(frame_detalhes, command=procurar_aluno, anchor=CENTER, text='Procurar',
           width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0).place(x=757, y=35)

    ver_tabela()


# ─────────────────────────────────────────
# FUNÇÃO ADICIONAR (Cursos e Turmas)
# ─────────────────────────────────────────

def adicionar():

    global frame_tabela_curso, frame_tabela_turma

    frame_tabela_curso = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_tabela_linha = Frame(frame_tabela, width=30, height=200, bg=co1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    separator = ttk.Separator(frame_tabela, orient=VERTICAL)
    separator.grid(row=0, column=1, pady=0, padx=0, sticky=NS)

    frame_tabela_turma = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

    # ── Campos Curso ──
    Label(frame_detalhes, text="Nome do Curso", height=1, anchor=NW,
          font=('Ivy 10'), bg=co1, fg=co4).place(x=4, y=10)
    e_nomecurso = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nomecurso.place(x=7, y=40)

    Label(frame_detalhes, text="Duração", height=1, anchor=NW,
          font=('Ivy 10'), bg=co1, fg=co4).place(x=4, y=70)
    e_duracao = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_duracao.place(x=7, y=100)

    Label(frame_detalhes, text="Preço", height=1, anchor=NW,
          font=('Ivy 10'), bg=co1, fg=co4).place(x=4, y=130)
    e_preco = Entry(frame_detalhes, width=10, justify='left', relief='solid')
    e_preco.place(x=7, y=160)

    # ── Funções Curso ──

    def limpar_curso():
        e_nomecurso.delete(0, END)
        e_duracao.delete(0, END)
        e_preco.delete(0, END)

    def novo_curso():
        nome    = e_nomecurso.get()
        duracao = e_duracao.get()
        preco   = e_preco.get()

        for campo in [nome, duracao, preco]:
            if campo == "":
                messagebox.showerror('Erro', 'Preencha todos os campos!')
                return

        criar_cursos([nome, duracao, preco])
        messagebox.showinfo('Sucesso', 'Curso inserido com sucesso!')
        limpar_curso()
        mostrar_cursos()

    def selecionar_curso(event):
        try:
            tree_item = tree_curso.focus()
            valores   = tree_curso.item(tree_item)['values']
            if not valores:
                return
            limpar_curso()
            e_nomecurso.insert(0, valores[1])
            e_duracao.insert(0,   valores[2])
            e_preco.insert(0,     valores[3])
        except Exception:
            pass

    def salvar_atualizacao_curso():
        try:
            tree_item = tree_curso.focus()
            valores   = tree_curso.item(tree_item)['values']
            if not valores:
                messagebox.showerror('Erro', 'Selecione um curso na tabela!')
                return

            valor_id = valores[0]
            nome     = e_nomecurso.get()
            duracao  = e_duracao.get()
            preco    = e_preco.get()

            for campo in [nome, duracao, preco]:
                if campo == "":
                    messagebox.showerror('Erro', 'Preencha todos os campos!')
                    return

            atualizar_curso([nome, duracao, preco, valor_id])
            messagebox.showinfo('Sucesso', 'Curso atualizado com sucesso!')
            limpar_curso()
            mostrar_cursos()

        except Exception as e:
            messagebox.showerror('Erro', f'Selecione um curso na tabela!\n{e}')

    def excluir_curso():
        try:
            tree_item = tree_curso.focus()
            valores   = tree_curso.item(tree_item)['values']
            if not valores:
                messagebox.showerror('Erro', 'Selecione um curso na tabela!')
                return

            confirmar = messagebox.askyesno('Confirmar', f'Deseja deletar o curso "{valores[1]}"?')
            if confirmar:
                deletar_curso(valores[0])
                messagebox.showinfo('Sucesso', 'Curso deletado com sucesso!')
                limpar_curso()
                mostrar_cursos()

        except Exception as e:
            messagebox.showerror('Erro', f'Selecione um curso na tabela!\n{e}')

    # ── Botões Curso ──
    Button(frame_detalhes, command=novo_curso, anchor=CENTER, text='Salvar'.upper(),
           width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1).place(x=107, y=160)

    Button(frame_detalhes, command=salvar_atualizacao_curso, anchor=CENTER, text='Atualizar'.upper(),
           width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1).place(x=187, y=160)

    Button(frame_detalhes, command=excluir_curso, anchor=CENTER, text='Deletar'.upper(),
           width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1).place(x=267, y=160)

    mostrar_cursos()


# ─────────────────────────────────────────
# FUNÇÃO MOSTRAR CURSOS
# ─────────────────────────────────────────

def mostrar_cursos():
    global tree_curso, frame_tabela_curso

    Label(frame_tabela_curso, text="Tabela de Cursos", height=1, anchor=NW,
          font=('Ivy 10 bold'), bg=co1, fg=co4).grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

    list_header = ['ID', 'Curso', 'Duração', 'Preço']
    df_list     = ver_cursos()

    tree_curso = ttk.Treeview(frame_tabela_curso, selectmode="browse",
                               columns=list_header, show="headings")
    vsb = ttk.Scrollbar(frame_tabela_curso, orient="vertical", command=tree_curso.yview)
    hsb = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=tree_curso.xview)
    tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_curso.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela_curso.grid_rowconfigure(0, weight=1)

    hd = ["nw", "nw", "e", "e"]
    h  = [30, 150, 80, 60]

    for n, col in enumerate(list_header):
        tree_curso.heading(col, text=col.title(), anchor=NW)
        tree_curso.column(col, width=h[n], anchor=hd[n])

    for item in df_list:
        tree_curso.insert('', 'end', values=item)

    # Separador
    ttk.Separator(frame_detalhes, orient=VERTICAL).place(x=382, y=10, relheight=0.9)

    # ── Campos Turma ──
    Label(frame_detalhes, text="Nome da Turma*", height=1, anchor=NW,
          font=('Ivy 10'), bg=co1, fg=co4).place(x=404, y=10)
    e_nometurma = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nometurma.place(x=407, y=40)

    Label(frame_detalhes, text="Turma", height=1, anchor=NW,
          font=('Ivy 10'), bg=co1, fg=co4).place(x=404, y=70)

    c_curso = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_curso['values'] = ('Curso 1', 'Curso 2')
    c_curso.place(x=407, y=100)

    Label(frame_detalhes, text='Data de Início*', height=1, anchor=NW,
          font=('Ivy 10'), bg=co1, fg=co4).place(x=406, y=130)
    data_inicio = DateEntry(frame_detalhes, width=10, background='darkblue',
                            foreground='white', borderwidth=2, year=2024)
    data_inicio.place(x=407, y=160)

    Button(frame_detalhes, anchor=CENTER, text='Criar'.upper(),
           width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1).place(x=507, y=160)

    Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(),
           width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1).place(x=587, y=160)

    Button(frame_detalhes, anchor=CENTER, text='Deletar'.upper(),
           width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1).place(x=667, y=160)

    # ── Tabela Turma ──
    global tree_turma

    Label(frame_tabela_turma, text="Tabela de Turmas", height=1, anchor=NW,
          font=('Ivy 10 bold'), bg=co1, fg=co4).grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

    list_header_turma = ['ID', 'Nome da Turma', 'Curso', 'Início']
    df_turma = ver_turmas()

    tree_turma = ttk.Treeview(frame_tabela_turma, selectmode="browse",
                               columns=list_header_turma, show="headings")
    vsb2 = ttk.Scrollbar(frame_tabela_turma, orient="vertical", command=tree_turma.yview)
    hsb2 = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=tree_turma.xview)
    tree_turma.configure(yscrollcommand=vsb2.set, xscrollcommand=hsb2.set)
    tree_turma.grid(column=0, row=1, sticky='nsew')
    vsb2.grid(column=1, row=1, sticky='ns')
    hsb2.grid(column=0, row=2, sticky='ew')
    frame_tabela_turma.grid_rowconfigure(0, weight=1)

    hd2 = ["nw", "nw", "e", "e"]
    h2  = [30, 200, 120, 80]

    for n, col in enumerate(list_header_turma):
        tree_turma.heading(col, text=col.title(), anchor=NW)
        tree_turma.column(col, width=h2[n], anchor=hd2[n])

    for item in df_turma:
        tree_turma.insert('', 'end', values=item)


# ─────────────────────────────────────────
# FUNÇÃO SALVAR
# ─────────────────────────────────────────

def salvar():
    print('Salvar')


# ─────────────────────────────────────────
# FUNÇÃO CONTROL
# ─────────────────────────────────────────

def Control(i):

    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        alunos()

    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        adicionar()

    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        salvar()


# ─────────────────────────────────────────
# CRIANDO BOTÕES DO MENU
# ─────────────────────────────────────────

app_img_cadastro = Image.open(botaoadd)
app_img_cadastro = app_img_cadastro.resize((18, 18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda: Control('cadastro'),
                      image=app_img_cadastro, text="Cadastro", width=100,
                      compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_cadastro.place(x=10, y=30)

app_img_adicionar = Image.open(botaoadd)
app_img_adicionar = app_img_adicionar.resize((18, 18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados, command=lambda: Control('adicionar'),
                       image=app_img_adicionar, text="Adicionar", width=100,
                       compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.place(x=123, y=30)

app_img_salvar = Image.open(botaosave)
app_img_salvar = app_img_salvar.resize((18, 18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda: Control('salvar'),
                    image=app_img_salvar, text="Salvar", width=100,
                    compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_salvar.place(x=236, y=30)


# ─────────────────────────────────────────
# INICIANDO A TELA
# ─────────────────────────────────────────

alunos()
janela.mainloop()