from tkinter import *
from tkinter import filedialog
from funkcje import *
from graph_h2 import *
import numpy as np
from graph_h1 import *

calls = []
calls_counter = 0
functionsInFiles = {}
modulesRelations = {}
dane_graf_his2 = []
path = []

def open_file():
    global path
    path = filedialog.askopenfilenames(initialdir=".", title="wybierz plik")
    #print(path)
    for lines in path:
        file_path = lines
        result = open(file_path)
        file_postion1 = file_path.index(".py")
        file_postion2 = file_path.rindex("/")
        file_name = file_path[file_postion2+1 : file_postion1+3]
        for c in result:
            safe_tab = c.split()
            is_quotation = 0
            for i in safe_tab:
                if '"' in (i) and is_quotation == 0:
                    is_quotation = 1
                elif '"' in (i) and is_quotation == 1:
                    is_quotation = 0
                if is_quotation == 0:
                    if i == "import" or i == "import*":
                        global calls_counter
                        if "from" in c:
                            position1 = c.find(i)
                            position2 = c.find("from")
                            for file in path:
                                filePostion1 = file.index(".py")
                                filePostion2 = file.rindex("/")
                                fileName = file[filePostion2 + 1: filePostion1 + 3]
                                if fileName == c[position2 + len("from "):position1 - 1] + ".py":
                                    calls.append([file_name, c[position2 + len("from "):position1 - 1]])  # dodanie nazwy pliku to tablicy
                                    calls_counter = calls_counter + 1
                        else:
                            position1 = c.find(i)
                            position2 = len(c)
                            for file in path:
                                filePostion1 = file.index(".py")
                                filePostion2 = file.rindex("/")
                                fileName = file[filePostion2 + 1: filePostion1 + 3]
                                if fileName == c[position1 + len(i) + 1:position2 - 1] + ".py":
                                    calls.append(
                                        [file_name,
                                         c[position1 + len(i) + 1:position2 - 1]])  # dodanie nazwy pliku to tablicy
                                    calls_counter = calls_counter + 1
                    if i == "using" or i == "include" or i == "open" or "open(" in i:
                        # global calls_counter
                        position1 = c.find(i)
                        position2 = len(c)
                        for file in path:
                            filePostion1 = file.index(".py")
                            filePostion2 = file.rindex("/")
                            fileName = file[filePostion2 + 1: filePostion1 + 3]
                            if fileName == c[position1 + len(i) + 1:position2 - 1] + ".py":
                                calls.append([file_name, c[position1 + len(i) + 1:position2 - 1]])  # dodanie nazwy pliku to tablicy
                                calls_counter = calls_counter + 1
                    if "#" in (i):
                        break
        #for i in range(0, calls_counter):
        #    print("wywolanie numer ", i + 1, "zawiera: ", calls[i])      # dałem w komentarz bo troche zbugowane
        #    pass

def convert(calls):         #zamiana listy w tuple
    return tuple(calls)
def dep():              #wypisanie danych pod graf
    #print(convert(calls))
    rysuj_graf(convert(calls))
def Graph():
    data_to_graph=convert(calls)
def func():
    global path
    files = path
    for file in files:
        functionsInFiles[file] = findFunctions(file)
    return files
def data_container():
    func()
    #przeniesiona i zmieniona część do "def poprawnosc"
    modules_relations()
def wage_graph_h():
    #listatupli do testu
    global dane_graf_his2
    slownik= {}
    for wyrazy in dane_graf_his2:
        slownik[wyrazy] = slownik.get(wyrazy, 0) + 1

    listafunkcji=[]
    listawag=[]
    for x in slownik.keys():
        listafunkcji.append(x)
    for x in slownik.values():
        listawag.append(x)
    poprawność(listafunkcji,listawag)
    listafunkcjiwtuple=tuple(listafunkcji)
    wage_graph(listafunkcjiwtuple, listawag)
def modules_relations():
    global modulesRelations
    files = func()
    modulesRelations = findFunctionCalls(functionsInFiles, files)

    slownik= {}
    for wyrazy in modulesRelations:
        slownik[wyrazy] = slownik.get(wyrazy, 0) + 1

    listafunkcji=[]
    listawag=[]
    for x in slownik.keys():
        listafunkcji.append(x.split(':'))
    for x in slownik.values():
        listawag.append(x)
    poprawność(listafunkcji,listawag)
    listafunkcjiwtuple=tuple(listafunkcji)
    historyjka_3(listafunkcjiwtuple, listawag)
    
    #print(modulesRelations)
def dane_graph_2():
    global dane_graf_his2
    dane = []
    pliki = func()
    function_list = list(functionsInFiles.values())
    function_list = np.concatenate(function_list)
    for plik in pliki:
        tresc_pliku = open(plik)
        aktualna_funkcja = ""
        for linia in tresc_pliku:
            if linia.find("def") == 0:
                aktualna_funkcja = linia.replace("def ", "")
                aktualna_funkcja = aktualna_funkcja[:aktualna_funkcja.find("(")]
                continue
            for funkcja in function_list:
                pozycja = linia.find(funkcja + "(")
                if pozycja != -1 and (linia[pozycja-1] == "(" or linia[pozycja-1] == " "):
                    dane.append((aktualna_funkcja, funkcja))
    dane_graf_his2 = dane
    wage_graph_h()
def poprawność(listafunkcji1,listawag1):
    #wypisuje dane aby można było porównać czy zgadzaja sie wagi na grafie z wagami w listach
    sprawdzenie_poprawnosci=[]
    x=0
    for y in listawag1:
        sprawdzenie_poprawnosci.append([listafunkcji1[x],listawag1[x]])
        print(sprawdzenie_poprawnosci[x][0]," wystepuje ",sprawdzenie_poprawnosci[x][1] ," raz/y ")
        x+=1
def exit() :
    sys.exit()
root = Tk()
root.geometry("300x190")
root.title("Panel użytkownika")
button = Button(root, text="Wczytaj plik", command=open_file, bg="cyan",fg="blue",font=("Arial",16))
button1= Button(root,text="Rysuj graf 1",command=dep, bg="cyan",fg="magenta",font=("Calibri",13))
button2= Button(root,text="Rysuj graf 2",command=dane_graph_2, bg="cyan",fg="magenta",font=("Calibri",13))
button3= Button(root,text="Rysuj graf 3",command=data_container, bg="cyan",fg="magenta",font=("Calibri",13))
button4= Button(root, text="Koniec", command=exit, bg="cyan",fg="red",font=("Arial",16))
#button5= Button(root,text="szukaj funkcji",command=func)
#button6= Button(root,text="Graf his_2",command=wage_graph_h)
#button= Button(root,text="Relacje między modułami",command=modules_relations)
button.pack(fill=X)
button1.pack(fill=X)
button2.pack(fill=X)
button3.pack(fill=X)
button4.pack(fill=X)
#button5.pack()
#button6.pack()
#button7.pack()
root.mainloop()
