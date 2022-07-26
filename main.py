import shutil
import tkinter as tk
from datetime import datetime
from os import listdir
from os.path import isfile, join
from PIL import Image
#from ttkwidgets import AutocompleteEntry
import re
from tkinter import font
from tkinter import filedialog

def listald():
    path = 'livros dentro'
    ln=[]
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for livro in files:
        livro=livro[:-4]
        ln.append(livro+"\n")
        print(livro)
    newWindow = tk.Toplevel(app)
    #newWindow.geometry("900x100")
    labelExample = tk.Label(newWindow, text="lista de livros na escola\n")
    buttonExample = tk.Button(newWindow, text="fechar", command=newWindow.destroy)
    text = tk.Text(newWindow, height=10)
    text.grid(row=1, column=0, sticky=tk.EW)
    scrollbar = tk.Scrollbar(newWindow, orient='vertical', command=text.yview)
    scrollbar.grid(row=1, column=1, sticky=tk.NS)
    text['yscrollcommand'] = scrollbar.set
    #text.insert(f'{0}.0',str(''.join(ln)))
    position = f'{1}.0'
    text.insert(position,str(''.join(sorted (ln))))
    labelExample.grid(row=0, column=0)
    buttonExample.grid(row=2, column=0)
    pass
def lista_t(parametro):
    lista = []
    arquivo=open(parametro,"r")
    nomes = arquivo.readlines()
    for nome in nomes:
        lista.append(nome)
        print(nome)
    return lista
    pass
def atualiza_l(nome):
    print("entrou")
    listanova = []
    arquivo=open("lista_de_emprestimo.txt","r")
    nomes = arquivo.readlines()
    for nomen in nomes:
        if nome in nomen:
            print("");
        else:
            listanova.append(nomen);
    arquivo.close()
    arquivo = open("lista_de_emprestimo.txt", "w")
    arquivo.writelines(listanova)
    arquivo.close()
    listar()
    pass
def verifica( string1):
   print("alunos")
   lista = 'lista_de_alunos.txt'
   file1 = open(lista, "r")
   readfile = file1.read()
   if string1 in readfile:
      file1.close()
      print("achou")
      return 0
   else:
      file1.close()
      return 1
   pass
def erro(param):
   newWindow = tk.Toplevel(app)
   param="erro : "+param
   labelExample = tk.Label(newWindow, text=param)
   buttonExample = tk.Button(newWindow, text="ok", command=newWindow.destroy)
   labelExample.pack()
   buttonExample.pack()
   print(param)
   pass
def verifica_d(param):
   try:
      f = open('livros dentro/'+param+'.txt')
      f.close()
      return 1
   except:
      print("dddd")
      erro('livro nao encontrado '+param)
      return 0
   pass
def salva_emp(newWindow,a,b):
   if(b==""):
      erro("colocar nome do livro")
   elif (a==""):
      erro("colocar nome")
   elif(0==verifica_d((b))):
      erro("livro nao disponivel")
   elif(verifica(a)):
      erro("aluno nao encontrado")
   else:
      print("nome", a)
      print("autor", b)
      now = datetime.now()
      data = now.strftime("%m/%d/%Y, %H:%M:%S")
      source = 'livros dentro/' + b + '.txt'
      desti = 'livros fora/' + b + '.txt'
      shutil.move(source, desti)
      arquivo = open('livros fora/' + b + '.txt', 'a')
      arquivo.write(a + "\n")
      arquivo.close()
      arquivo = open('lista_de_emprestimo.txt', 'a')
      arquivo.write(a + " & " + b+ " "+data+"\n")
      arquivo.close()
      newWindow.destroy()
   pass
def salva_dev(a,b):
    if (b == ""):
        erro("colocar nome do livro")
    elif (a == ""):
        erro("colocar nome")
    elif (verifica_d((b))):
        erro("livro  esta na escola")
    elif (verifica(a)):
        erro("aluno nao encontrado")
    else:
       print("aluno",a)
       print("livro",b)
       arquivo = open('lista_de_emprestimo.txt', 'a')
       atualiza_l(a)
       desti = 'livros dentro/' + b + '.txt'
       source = 'livros fora/' + b + '.txt'
       #joao & arte 08/16/2022, 18:08:46
       shutil.move(source, desti)
       app.destroy();
    pass
def salva_alu(newWindowa,c,d,e):
   print("ctr",d)
   print("telefone", e)
   print("nome",c )
   if (0==(verifica(c))):
      erro("ja tem esse nome")
   else:
      arquivo = open('lista_de_alunos.txt', 'a')
      arquivo.write(c+" & "+d+" & "+e+"\n")
      arquivo.close()
      cadlivro(newWindowa)
   pass
def salva_liv(newWindow,new,a,b):
    if (b == ""):
        erro("colocar nome do livro")
    elif (a == ""):
        erro("colocar nome")
    else:
       print("nome",a)
       print("autor",b)
       arquivo = open('lista_de_livros.txt', 'a')
       arquivo.write(a+" & "+b+"\n")
       arquivo.close()
       arquivo = open('livros dentro/'+a+'.txt', 'a')
       arquivo.write("autor: " + b + "\n")
       arquivo.close()
       new.destroy()
       newWindow.destroy()
    pass
def listar():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text="listas")
    buttonExample1 = tk.Button(newWindow, text="lista livros totais", command=listarlivros)
    buttonExample2 = tk.Button(newWindow, text="lista empestimos em abreto", command=listaremp)
    buttonExample3 = tk.Button(newWindow, text="lista alunos cadastrados", command=listaralunos)
    buttonExample5 = tk.Button(newWindow, text="lista de livro disponiveis", command=listald)
    buttonExample4 = tk.Button(newWindow, text="fechar", command=newWindow.destroy)
    labelExample.pack()
    buttonExample1.pack()
    buttonExample2.pack()
    buttonExample3.pack()
    buttonExample5.pack()
    buttonExample4.pack()
    pass
def listarlivros():
    newWindow = tk.Toplevel(app)
    newWindow.geometry("675x300")
    newWindow.configure()
    labelExample = tk.Label(newWindow, text="lista de livros ao todo da escola\nnome do livro, autor")
    buttonExample = tk.Button(newWindow, text="fechar", command=newWindow.destroy)
    text = tk.Text(newWindow, height=10)
    text.grid(row=1, column=0, sticky=tk.EW)
    labelExample.grid(row=0, column=0, sticky='ns')
    scrollbar = tk.Scrollbar(newWindow, orient='vertical', command=text.yview)
    scrollbar.grid(row=1, column=1, sticky=tk.NS)
    text['yscrollcommand'] = scrollbar.set
    position = f'{1}.0'
    text.insert(f'{1}.0',str(''.join(sorted (lista_t("lista_de_livros.txt")))))
    buttonExample.grid(row=3, column=0)
    pass
def listaralunos():

    newWindow = tk.Toplevel(app)
    newWindow.geometry("650x700")
    newWindow.configure()
    labelExample = tk.Label(newWindow, text="lista de alunos da escola\nnome do aluno, ctr, telefone")
    labelExamp = tk.Label(newWindow, text=str(''.join(lista_t("lista_de_alunos.txt"))))
    buttonExample = tk.Button(newWindow, text="fechar", command=newWindow.destroy)
    text = tk.Text(newWindow, height=10)
    text.grid(row=1, column=0, sticky=tk.EW)
    scrollbar = tk.Scrollbar(newWindow, orient='vertical', command=text.yview)
    scrollbar.grid(row=1, column=1, sticky=tk.NS)
    text['yscrollcommand'] = scrollbar.set
    text.insert(f'{1}.0',str(''.join(sorted(lista_t("lista_de_alunos.txt")))));
    labelExample.grid(row=0, column=0)
    buttonExample.grid(row=3, column=0)
    pass
def listaremp():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text="lista de livros fora da escola\nnome do aluno, nome do livro,data e hora que pegou")
    labelExamp = tk.Label(newWindow, text=str(''.join(lista_t("lista_de_emprestimo.txt"))))
    buttonExample = tk.Button(newWindow, text="fechar", command=newWindow.destroy)
    text = tk.Text(newWindow, height=10)
    text.grid(row=1, column=0, sticky=tk.EW)
    scrollbar = tk.Scrollbar(newWindow, orient='vertical', command=text.yview)
    scrollbar.grid(row=1, column=1, sticky=tk.NS)
    text['yscrollcommand'] = scrollbar.set
    text.insert(f'{1}.0', str(''.join(sorted(lista_t("lista_de_emprestimo.txt")))));
    labelExample.grid(row=0, column=0)
    buttonExample.grid(row=3, column=0)
    pass
def cadlivro(newWindowa):
   newWindow = tk.Toplevel(app)
   labelExample = tk.Label(newWindow, text="Nome")
   labelExample.pack()
   entrada = tk.Entry(newWindow, font="arial 15 bold")
   entrada.pack()
   label = tk.Label(newWindow, text="n de exemplares")
   label.pack()
   entrad = tk.Entry(newWindow, font="arial 15 bold")
   entrad.pack()
   label = tk.Label(newWindow, text="autor")
   label.pack()
   entra = tk.Entry(newWindow, font="arial 15 bold")
   entra.pack()
   buttonExample = tk.Button(newWindow, text="proxima",command=lambda: salva_liv(newWindow,newWindowa,(entrada.get()+entrad.get()),(entra.get())))
   buttonExample.pack()
   buttonExample = tk.Button(newWindow, text="cancelar", command=newWindow.destroy)
   buttonExample.pack()
   pass
def emprestar():




        newWindow = tk.Toplevel(app)
        labelExample = tk.Label(newWindow, text="aluno")
        labelExample.grid(row=0,column=0, padx= 10, pady=10)
        entrada = tk.Entry(newWindow, font="arial 15 bold")
        entrada.grid(row=1,column=0)
        label = tk.Label(newWindow, text="livro")
        label.grid(row=2,column=0, padx= 10, pady=10)
        entrad = tk.Entry(newWindow, font="arial 15 bold")
        entrad.grid(row=3,column=0, padx= 10, pady=10)
        label = tk.Label(newWindow, text="n de exemplares")
        label.grid(row=4,column=0, padx= 10, pady=10)
        entra = tk.Entry(newWindow, font="arial 15 bold")
        entra.grid(row=5,column=0, padx= 10, pady=10)
        buttonExample = tk.Button(newWindow, text="concluir",command=lambda: salva_emp(newWindow,entrada.get(),(entrad.get()+entra.get())))
        buttonExample.grid(row=6,column=0, padx= 10, pady=10)
        buttonExample = tk.Button(newWindow, text="cancelar", command=newWindow.destroy)
        buttonExample.grid(row=6,column=1, padx= 10, pady=10)
def devolver():
   newWindow = tk.Toplevel(app)
   labelExample = tk.Label(newWindow, text="aluno")
   labelExample.pack()
   entrada = tk.Entry(newWindow, font="arial 15 bold")
   entrada.pack()
   label = tk.Label(newWindow, text="livro")
   label.pack()
   entrad = tk.Entry(newWindow, font="arial 15 bold")
   entrad.pack()
   label = tk.Label(newWindow, text="n de exemplares")
   label.pack()
   entra = tk.Entry(newWindow, font="arial 15 bold")
   entra.pack()
   buttonExample = tk.Button(newWindow, text="concluir",command=lambda: salva_dev(entrada.get(),(entrad.get()+entra.get())))
   buttonExample.pack()
   buttonExample = tk.Button(newWindow, text="cancelar", command=newWindow.destroy)
   buttonExample.pack()
   pass
def cadaluno():
   newWindow = tk.Toplevel(app)
   labelExample = tk.Label(newWindow, text="Nome")
   labelExample.pack()
   entrada = tk.Entry(newWindow, font="arial 15 bold")
   entrada.pack()
   label = tk.Label(newWindow, text="ctr")
   label.pack()
   entrad = tk.Entry(newWindow, font="arial 15 bold")
   entrad.pack()
   labele = tk.Label(newWindow, text="telefone")
   labele.pack()
   entra = tk.Entry(newWindow, font="arial 15 bold")
   entra.pack()
   buttonExample = tk.Button(newWindow, text="proxima", command=lambda :salva_alu(newWindow,entrada.get(),entrad.get(),entra.get()))
   buttonExample.pack()
   buttonExample = tk.Button(newWindow, text="cancelar", command=newWindow.destroy)
   buttonExample.pack()
   pass
def createNewWindow():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button",command=createNewWindow)
    labelExample.pack()
    buttonExample.pack()
    pass
app = tk.Tk()
app.geometry("300x700")
app.configure( )
newWindow = tk.Toplevel(app)
newWindow.destroy()
buttona = tk.Button(app,text="Cadastrar aluno",width=15,height=2, command=cadaluno ,fg="black")
buttonb = tk.Button(app, text="Cadastar o livro",width=15,height=2, command=lambda: cadlivro(newWindow))
buttonc = tk.Button(app,text="emprestar",width=15,height=2,command=emprestar)
buttond = tk.Button(app,text="devolver",width=15,height=2,command=devolver)
buttone = tk.Button(app,text="detalhes",width=30,height=2,command=listar)
buttona.grid(row=1,column=0, padx= 10, pady=10)
buttonb.grid(row=1,column=1, padx= 10, pady=10)
buttonc.grid(row=2,column=1, padx= 10, pady=10)
buttond.grid(row=2,column=0, padx= 10, pady=10)
buttone.grid(row=3,column=0, columnspan=2)
labele = tk.Label(app, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
labele.grid(row=4,column=0,columnspan=2)
photo = tk.PhotoImage(file ="icon.png").subsample(5, 5)
labelExample = tk.Label(app,image = photo)
labelExample.grid(row=5,column=0, columnspan=2)
app.mainloop()
