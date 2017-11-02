
''' *****************************************
Laboratoire #4
Team: No Problem
Auteurs:Mathieu Blackburn (BLAM03049208)
		Alban Fourfooz (FOUA29089701)	
********************************************* '''

import looping
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
from timeit import default_timer as timer
from threading import Thread
 



''' *** Python Loop *** '''
def PLoop(NLoop):
    i = 0
    while i < NLoop :
        i=i+1

def PNoT(NLoop) :
    start = timer()
    PLoop(NLoop)
    end = timer()
    return (end - start)


def PYesT(NLoop):
        start = timer()
        n = NLoop/4
        T1 = LoopThread(n)
        T2 = LoopThread(n)
        T3 = LoopThread(n)
        T4 = LoopThread(n)

        T1.start()
        T2.start()
        T3.start()
        T4.start()

        T1.join()
        T2.join()
        T3.join()
        T4.join()

        end = timer()
        return (end - start)

class LoopThread(Thread):
    def __init__(self, NLoopT):
        Thread.__init__(self)
        self.NLoopT = NLoopT
    def run(self):
        PLoop(self.NLoopT)

''' *** END Python Loop *** '''    



class Interface(Frame):
    def __init__(self, master):

        Frame.__init__(self)
        self.master = master
        self.createWidgets()

        master.title("NP - Loop Calculator")

    #Creation de nos Labels, Entries et Buttons
    def createWidgets(self):
        
        row = Frame(root)
        Label(row, text="Bievenue dans notre programme!").pack()
        row.pack(side=TOP, fill=X, padx=2, pady=2)

        #Python Sans Thread
        row = Frame(root)
        Label(row, text="1. Python Sans Thread:  ").pack(side=LEFT)
        self.ent1 = Entry(row)
        self.ent1.pack(side=LEFT, expand=YES, fill=X)
        Button(row, text='Calculer', command=self.pNoThread).pack(side=RIGHT, padx=8, pady=5)
        row.pack(side=TOP, fill=X, padx=5, pady=2)

        row = Frame(root)
        self.lab1 = Label(row)
        self.lab1.pack(side = TOP)
        row.pack(side=TOP, fill=X, padx=5, pady=3)

        #C++ Sans Thread
        row = Frame(root)
        Label(row, text="2. C++ Sans Thread:      ").pack(side=LEFT)
        self.ent2 = Entry(row)
        self.ent2.pack(side=LEFT, expand=YES, fill=X)
        Button(row, text='Calculer', command=self.cNoThread).pack(side=RIGHT, padx=8, pady=5)
        row.pack(side=TOP, fill=X, padx=5, pady=5)

        row = Frame(root)
        self.lab2 = Label(row)
        self.lab2.pack(side = TOP)
        row.pack(side=TOP, fill=X, padx=5, pady=3)

       #Python Avec Thread
        row = Frame(root)
        Label(row, text="3. Python Avec Thread:").pack(side=LEFT)
        self.ent3 = Entry(row)
        self.ent3.pack(side=LEFT, expand=YES, fill=X)
        Button(row, text='Calculer', command=self.pThread).pack(side=RIGHT, padx=8, pady=5)
        row.pack(side=TOP, fill=X, padx=5, pady=5)

        row = Frame(root)
        self.lab3 = Label(row)
        self.lab3.pack(side = TOP)
        row.pack(side=TOP, fill=X, padx=5, pady=3)

        #C++ Avec Thread
        row = Frame(root)
        Label(row, text="4. C++ Avec Thread:     ").pack(side=LEFT)
        self.ent4 = Entry(row)
        self.ent4.pack(side=LEFT, expand=YES, fill=X)
        Button(row, text='Calculer', command=self.cThread).pack(side=RIGHT, padx=8, pady=5)
        row.pack(side=TOP, fill=X, padx=5, pady=5)

        row = Frame(root)
        self.lab4 = Label(row)
        self.lab4.pack(side = TOP)
        row.pack(side=TOP, fill=X, padx=5, pady=3)
        
        #Tous
        row = Frame(root)
        Label(row, text="5. Les 4 d'un coup :       ").pack(side=LEFT)
        self.ent5 = Entry(row)
        self.ent5.pack(side=LEFT, expand=YES, fill=X)
        Button(row, text='Calculer', command=self.AllTypes).pack(side=RIGHT, padx=8, pady=5)
        row.pack(side=TOP, fill=X, padx=5, pady=5)

    def pNoThread(self):
        self.lab1.configure(text = "Temps: " + str((PNoT(int(self.ent1.get())))*1000) + " ms")

    def cNoThread(self):
        self.lab2.configure(text = "Temps: " + str(looping.noThread(int(self.ent2.get()))/1000) + " ms")

    def pThread(self):
        self.lab3.configure(text = "Temps: " + str((PYesT(int(self.ent3.get())))*1000) + " ms")

    def cThread(self):
        self.lab4.configure(text = "Temps: " + str(looping.yesThread(int(self.ent4.get()))/1000) + " ms")

    def AllTypes(self):
        self.lab1.configure(text = "Temps: " + str((PNoT(int(self.ent5.get())))*1000) + " ms")
        self.lab2.configure(text = "Temps: " + str(looping.noThread(int(self.ent5.get()))/1000) + " ms")
        self.lab3.configure(text = "Temps: " + str((PYesT(int(self.ent5.get())))*1000) + " ms")
        self.lab4.configure(text = "Temps: " + str(looping.yesThread(int(self.ent5.get()))/1000) + " ms")

# MAIN

root = Tk()

w = 350 # width for the Tk root
h = 400 # height for the Tk root

ws = root.winfo_screenwidth() # get screen width and height
hs = root.winfo_screenheight() 

x = (ws/2) - (w/2) # calculate x and y coordinates for the Tk root window
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y)) # set the dimensions of the screen and where it is placed

app = Interface(root)
root.mainloop()

exit()