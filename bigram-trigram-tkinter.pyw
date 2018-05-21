import collections
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

print("This program needs Python version 3 and it may no run on other versions.")

#To download the needed libraries:
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')

from nltk.tokenize import sent_tokenize

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


with open('shakespeare.txt', 'r') as myfile:
    data_en=myfile.read().replace('\n', ' ').replace(',',' ').replace('.',' ')
txtfiltered = [w for w in word_tokenize(data_en)]

def about():
    messagebox.showinfo("About the Word Predictor:", "This program was made as a test for second evaluation of Artificial Intelligence course, using bigrams and trigrams to guess the most probable next word given a sequence of 2 or 3 words.")
def guess(*args):
    if(len(texto.get().split(" "))==2):
        n=bigrams(txtfiltered, texto.get().split(" "))
        if(len(n)==0):
            messagebox.showwarning("Error", "There are no suggestion within the database.")
        else:
            print()
            messagebox.showwarning("Success!!", "Suggestions for '"+texto.get()+"' are:\n\n"+', '.join(n))
    elif(len(texto.get().split(" "))==3):
        n=trigrams(txtfiltered, texto.get().split(" "))
        if(len(n)==0):
            messagebox.showwarning("Error", "There are no suggestion within the database.")
        else:
            print()
            messagebox.showwarning("Success!!", "Suggestions for '"+texto.get()+"' are:\n\n"+', '.join(n))
    else:
        messagebox.showerror("Error:", "Only texts with 2 or 3 words are accepted.")


def bigrams(base, words):
    
    bigrams = []
    suggestions = []

    for i in range(0, len(base)):
        if (i == len(base)-1):
            break
        else:
            if(base[i].lower()==words[1].lower() and base[i-1].lower()==words[0].lower()):
                bigrams.append(base[i+1])

    counter = collections.Counter(bigrams)
    
    for i in range(0,len(counter.most_common())):
        if(i>=3):
            break
        else:
            suggestions.append(counter.most_common()[i][0])
    
    return suggestions


def trigrams(base, words):

    trigrams = []
    suggestions = []

    for i in range(0, len(base)):
        if (i == len(base)-2):
            break
        else:
            if(base[i].lower()==words[2].lower()
               and base[i-1].lower()==words[1].lower()
               and base[i-2].lower()==words[0].lower()):
                
                trigrams.append(base[i+1])
 
    counter = collections.Counter(trigrams)
    
    for i in range(0,len(counter.most_common())):
        if(i>=3):
            break
        else:
            suggestions.append(counter.most_common()[i][0])
    
    return suggestions



root = Tk()
root.title("Word Predictor v0.3 - By Adriano Martins")
#root.wm_iconbitmap('Icon.ico')

menu = Menu(root)
root.config(menu=menu)

arquivo = Menu(menu)
menu.add_cascade(label="File", menu=arquivo)
arquivo.add_separator()
arquivo.add_command(label="Exit", command=quit)

ajuda = Menu(menu)
menu.add_cascade(label="Help", menu=ajuda)
#ajuda.add_separator()
ajuda.add_command(label="About this software...", command=about)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

texto = StringVar()



ntexto = ttk.Entry(mainframe, width=15, textvariable=texto)
ntexto.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Type something:\n(2 or 3 words)").grid(column=1, row=1, sticky=W)


ttk.Button(mainframe, text="Analyze", command=guess).grid(column=3, row=1, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

ntexto.focus()
root.bind('<Return>', guess)

root.mainloop()
