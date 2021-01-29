from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
import random
import datetime

def tarefas_num_estado():
    desen = 0
    atra = 0
    panel2.place_forget()
    panel3.place_forget()
    panel1.place(x= 220, y=20)

    f = open("ficheiros\\tarefas.txt", "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    for lin in linhas:
        campos = lin.split(";")
        esta = campos[4]
        if esta == "Em Desenvolvimento":
            desen+=1
            tree.insert("","end",values=(campos[4],desen))
        elif esta == "Em atraso":
            atra +=1
            tree.insert("","end",values=(campos[4],atra))


def tarefas_num_categorias():
    pro = 0
    pes = 0
    aul = 0
    est = 0
    reu = 0
    inv = 0
    tes = 0
    proj = 0
    panel1.place_forget()
    panel3.place_forget()
    panel2.place(x = 220, y = 20)
    f = open("ficheiros\\tarefas.txt", "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    for lin in linhas:
        campos = lin.split(";")
        cat = campos[3]
        if cat == "Profissonais":
            pro+=1
            tree2.insert("","end",values=(campos[3],pro))
        elif cat == "Pessoais":
            pes +=1
            tree2.insert("","end",values=(campos[3],pes))
        elif cat == "Projetos":
            proj +=1
            tree2.insert("","end",values=(campos[3],proj))
        elif cat == "Testes":
            tes +=1
            tree2.insert("","end",values=(campos[3],tes))
        elif cat == "Investigações":
            inv +=1
            tree2.insert("","end",values=(campos[3],inv))
        elif cat == "Reuniões":
            reu +=1
            tree2.insert("","end",values=(campos[3],reu))
        elif cat == "Estudos":
            est +=1
            tree2.insert("","end",values=(campos[3],est))
        elif cat == "Aulas":
            aul +=1
            tree2.insert("","end",values=(campos[3],aul))


    
def tarefas_num_criadas():
    tar = 0
    panel1.place_forget()
    panel2.place_forget()
    panel3.place(x = 220, y = 20)
    f = open("ficheiros\\tarefas.txt", "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    for lin in linhas:
        campos = lin.split(";")
        tarefas = campos[0]
        tar+=1
    tree3.insert("","end",values=("tarefas",tar))



window= Tk()
window.title("Produtividade")
window.geometry("800x600")


btn_estado= Button(window, text="Nº tarefas por estado", width=18,height=3, font=("Helvetica", "10"), command = tarefas_num_estado)
btn_estado.place(x=20, y=120)

btn_categoria= Button(window, text="Nº tarefas por categoria", width=18,height=3, font=("Helvetica", "10"), command = tarefas_num_categorias)
btn_categoria.place(x=20, y=190)

btn_semana= Button(window, text="Nº tarefas criadas", width=18,height=3, font=("Helvetica", "10"), command = tarefas_num_criadas)
btn_semana.place(x=20, y=260)


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

tree2 = ttk.Treeview(panel2, columns = ("Categoria", "Nº tarefas"), show = "headings", height = 5, selectmode = "browse")
tree2.column("Categoria", width = 200, anchor = "c")
tree2.column("Nº tarefas", width = 200, anchor = "c")
tree2.heading("Categoria", text = "Categoria")
tree2.heading("Nº tarefas", text = "Nº de tarefas")
tree2.place(x=60, y=140)

#panel para nº/criadas
panel3 = PanedWindow(window, width=540, height=400, bd="3", relief="sunken")
panel3.place(x= 220, y=20)

num_criadas= Label(panel3, text="Nº de tarefas criadas", font=("Helvetica", "15"))
num_criadas.place(x=150, y=40)

tree3 = ttk.Treeview(panel3, columns = ("Criadas", "Nº tarefas"), show = "headings", height = 5, selectmode = "browse")
tree3.column("Criadas", width = 200, anchor = "c")
tree3.column("Nº tarefas", width = 200, anchor = "c")
tree3.heading("Criadas", text = "Criadas")
tree3.heading("Nº tarefas", text = "Nº de tarefas")
tree3.place(x=60, y=140)



window.mainloop()