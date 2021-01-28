from tkinter import *
from datetime import datetime
from tkinter import messagebox

def popup():
    global data
    data = datetime.now().date()
    f = open("tarefa.txt", "r")   # abre o ficheiro em modo de Leitura
    for linha in f:
        campos = linha.split(";") 
        if data == campos[2]:
            messagebox.info("Notificação", "Tem uma tarefa com data limite hoje!")
        elif data < campos[2]:
            messagebox.info("Notificação", "Tem uma tarefa a chegar à data limite!")


ecra_popup=Tk()
ecra_popup.title("Notificações")
ecra_popup.geometry("200x200")
ecra_popup.resizable(1,0)
btn = Button(ecra_popup, text=0, command= popup)
ecra_popup.mainloop()