from tkinter import *
from tkinter import filedialog
calls = []
calls_counter = 0
def open_file():

   result =  filedialog.askopenfile(initialdir="/", title="wybierz plik", filetypes=(("text files", ".txt"), ("all files", "*.*")))
   print(result)
   safe_tab = [] #tablica która przechowuje poszczególne wyrazy z każdej linijki using
   for c in result:
        safe_tab = c.split()
        is_quotation = 0
        for i in safe_tab:
            if '"' in (i) and is_quotation == 0:
                is_quotation = 1
            elif '"' in (i) and is_quotation == 1:
                is_quotation = 0
            if is_quotation == 0:
                if i == "import" or i == "using" or i == "include" or i == "open":
                    global calls_counter
                    calls.append(c) #dodanie linijki w której jest dodawany plik to tablicy
                    calls_counter = calls_counter + 1
                if "#" in (i):
                    break
   for i in range (0, calls_counter):
       print("wywolanie numer ", i + 1, "zawiera: ", calls[i])

def exit() :
    sys.exit()
root = Tk()
button = Button(root, text="wczytaj plik", command=open_file)
button1= Button(root, text="koniec", command=exit)
button.pack()
button1.pack()
root.mainloop()