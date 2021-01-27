from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
import random
import datetime

def tarefas_num_estado():
    panel2.place_forget()
    panel3.place_forget()
    panel4.place_forget()
    panel1.place(x= 220, y=20)
    global num_concluidas
    global num_criadas
    tarefas=[]
    conclui=[]
    desenv=[]
    late=[]

    f = open("ficheiros/tarefas.txt", "r", encoding= "utf-8")
    linhas = f.readlines()
    f.close()
    for lin in linhas:
        campos = lin.split(";")
        if "Concluídas" == campos[4]:
            tarefa= campos[0]
            tarefas+=1
            conclui+=1
            tree.insert("","end", values=(campos[4], conclui))
        elif "Em desenvolvimento" == campos[4]:
            tarefa = campos[0]
            tarefas+=1
            desenv+=1
            tree.insert("","end", values=(campos[4],desenv))
        else:
            tarefa = campos[0]
            tarefas+=1
            late+=1
            tree.insert("","end", values=(campos[4],late))

def tarefas_num_categorias():
    panel1.place_forget()
    panel3.place_forget()
    panel4.place_forget()
    panel2.place(x = 220, y = 20)
    global num_concluidas
    global num_criadas
    tarefas=[]

    f = open("ficheiros/tarefas.txt", "r", encoding= "utf-8")
    linhas = f.readlines()
    f.close()
    for lin in linhas:
        campos = lin.split(";")
        if "Importante" == campos[3]:
            tarefa= campos[0]
            tarefas+=1
        elif "Trabalho" == campos[3]:
            tarefa = campos[0]
            tarefas+=1
        elif "Pessoal" == campos[3]:
            tarefa = campos[0]
            tarefas+=1
        else:
            tarefa = campos[0]
            tarefas+=1

def tarefas_num_semana():
    panel1.place_forget()
    panel2.place_forget()
    panel4.place_forget()
    panel3.place(x = 220, y = 20)
    global num_concluidas
    global num_criadas
    tarefas=[]
    semana = datetime.date.week.now()
    f = open("ficheiros/tarefas.txt", "r", encoding= "utf-8")
    linhas = f.readlines()
    f.close()
    for lin in linhas:
        campos = lin.split(";") 
        semana = campos[2]

def tarefas_num_mes():
    panel1.place_forget()
    panel2.place_forget()
    panel3.place_forget()
    panel4.place(x = 220, y = 20)
    global num_concluidas
    global num_criadas
    tarefas=[]
    mes = datetime.date.month.now()

    f = open("ficheiros/tarefas.txt", "r", encoding= "utf-8")
    linhas = f.readlines()
    f.close()
    for lin in linhas:
        campos = lin.split(";")
        mes= campos[2]


window= Tk()
window.title("Produtividade")
window.geometry("800x600")

num_concluidas = IntVar()
num_criadas = IntVar()
concluias_lb= Label(window, text="Tarefas concluídas: ")
concluias_lb.place(x=20, y=20)
num_concluidas= Entry(window, textvariable = num_concluidas, state = "disabled", width = 5)
num_concluidas.place(x=130, y=20)
criadas_lb= Label(window, text="Tarefas criadas: ")
criadas_lb.place(x=20, y=55)
num_criadas= Entry(window, textvariable = num_criadas, state = "disabled", width = 5)
num_criadas.place(x=130, y=55)

btn_estado= Button(window, text="Nº tarefas por estado", width=18,height=3, font=("Helvetica", "10"), command = tarefas_num_estado)
btn_estado.place(x=20, y=120)

btn_categoria= Button(window, text="Nº tarefas por categoria", width=18,height=3, font=("Helvetica", "10"), command = tarefas_num_categorias)
btn_categoria.place(x=20, y=190)

btn_semana= Button(window, text="Nº tarefas por semana", width=18,height=3, font=("Helvetica", "10"), command = tarefas_num_semana)
btn_semana.place(x=20, y=260)

btn_mes= Button(window, text="Nº tarefas por mês", width=18,height=3, font=("Helvetica", "10"), command = tarefas_num_mes)
btn_mes.place(x=20, y=330)

#Panel para o nº por estados 
panel1 = PanedWindow(window, width=540, height=400, bd="3", relief="sunken")
panel1.place(x= 220, y=20)

num_estados= Label(panel1, text="Nº de tarefas por estado", font=("Helvetica", "15"))
num_estados.place(x=150, y=40)

tree = ttk.Treeview(panel1, columns = ("Estado", "Nº tarefas"), show = "headings", height = 5, selectmode = "browse")
tree.column("Estado", width = 200, anchor = "c")
tree.column("Nº tarefas", width = 200, anchor = "c")
tree.heading("Estado", text = "Estado")
tree.heading("Nº tarefas", text = "Nº de tarefas")
tree.place(x=60, y=140)

#panel para nº por categoria
panel2 = PanedWindow(window, width=540, height=400, bd="3", relief="sunken")
panel2.place(x= 220, y=20)

num_categorias= Label(panel2, text="Nº de tarefas por categoria", font=("Helvetica", "15"))
num_categorias.place(x=150, y=40)

tree = ttk.Treeview(panel2, columns = ("Categoria", "Nº tarefas"), show = "headings", height = 5, selectmode = "browse")
tree.column("Categoria", width = 200, anchor = "c")
tree.column("Nº tarefas", width = 200, anchor = "c")
tree.heading("Categoria", text = "Categoria")
tree.heading("Nº tarefas", text = "Nº de tarefas")
tree.place(x=60, y=140)

#panel para nº/semana
panel3 = PanedWindow(window, width=540, height=400, bd="3", relief="sunken")
panel3.place(x= 220, y=20)

num_semana= Label(panel3, text="Nº de tarefas por semana", font=("Helvetica", "15"))
num_semana.place(x=150, y=40)

tree = ttk.Treeview(panel3, columns = ("Semana", "Nº tarefas"), show = "headings", height = 5, selectmode = "browse")
tree.column("Semana", width = 200, anchor = "c")
tree.column("Nº tarefas", width = 200, anchor = "c")
tree.heading("Semana", text = "Semana")
tree.heading("Nº tarefas", text = "Nº de tarefas")
tree.place(x=60, y=140)

#panel para nº/mês
panel4 = PanedWindow(window, width=540, height=400, bd="3", relief="sunken")
panel4.place(x= 220, y=20)

num_mes= Label(panel4, text="Nº de tarefas por mês", font=("Helvetica", "15"))
num_mes.place(x=150, y=40)

tree = ttk.Treeview(panel4, columns = ("Mês", "Nº tarefas"), show = "headings", height = 5, selectmode = "browse")
tree.column("Mês", width = 200, anchor = "c")
tree.column("Nº tarefas", width = 200, anchor = "c")
tree.heading("Mês", text = "Mês")
tree.heading("Nº tarefas", text = "Nº de tarefas")
tree.place(x=60, y=140)



window.mainloop()