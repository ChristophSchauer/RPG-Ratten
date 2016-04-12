# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:25:11 2016

@author: Schauer

[2016.04.01, CS]:   test different GUIs found on the internet and start with 
                    the programming;                
"""

from tkinter import *

import tkinter

def update_dictionary():

    fL = {}
    
    def commando(x, y):
        fL.update({x:int(y)})  # Please note that these x and y vars are private to this function.  They are not the x and y vars as defined below.
        print(fL)
    
    root = Tk()
    root.title("Spam Words")
    
    x = StringVar()  # Creating the variables that will get the user's input.
    y = StringVar()
    
    label_1 = Label(root, text="Say a word: ", bg="#333333", fg="white")
    label_2 = Label(root, text="Give it a value, 1-10:", bg="#333333", fg="white")
    entry_1 = Entry(root, textvariable=x)
    entry_2 = Entry(root, textvariable=y)
    
    label_1.grid(row=1)
    label_2.grid(row=3)
    
    entry_1.grid(row=2, column=0)
    entry_2.grid(row=4, column=0)
    
    but = Button(root, text="Execute", bg="#333333", fg="white", command=lambda :commando(x.get(), y.get()))  # Note the use of lambda and the x and y variables.
    but.grid(row=5, column=0)
    
    root.mainloop()
    
class Application(tkinter.Frame):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("600x400")

        tkinter.Frame.__init__(self, self.root)
        self.playerstatus = {
            "name"      : ['test'],
            "clever"    : [],
            "social"    : [],
            "strong"    : [],
            "fast"      : [],
            "life"      : [],
            "tricks"    : [],
            "talents"   : [],
            "pack"      : [],
            "pros"      : [],
            "cons"      : []
                             }
        self.create_widgets()

    def create_widgets(self):
        self.root.bind('<Return>', self.parse)
        self.grid()
               
        # status of the player
        # labels for names
        text = ['name', 'life', 'clever', 'fast', 'social', 'strong', 'pack', 'talents', 'tricks', 'pros', 'cons']          
        for index in range(len(text)):
            tkinter.Label(self, text=text[index], justify='left', width=30).grid(column=0,row=index,sticky='W')
            tkinter.Label(self, text=self.playerstatus[text[index]], width=30).grid(column=1,row=index,sticky='w')         
        index = 11
        
        # entry field
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=index,columnspan=2,sticky='EW')
        self.entryVariable.set(u"Enter command here.")
        index += 1        
        
        # label
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable,anchor="nw",fg="white",bg="black")
        label.grid(column=0,row=index,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Hello !")
        index += 1
        
        # button
        self.submit = tkinter.Button(self, text="Submit")
        self.submit.bind('<Button-1>', self.parse)
        self.submit.grid(row=index)

    def parse(self, event):
        self.labelVariable.set(self.entryVariable.get())
        data = self.entryVariable.get().split(sep=',')
        self.playerstatus[data[0]] = data[1]
        self.playerstatus.update()
        text = ['name', 'life', 'clever', 'fast', 'social', 'strong', 'pack', 'talents', 'tricks', 'pros', 'cons']          
        for index in range(len(text)):
            tkinter.Label(self, text=text[index], justify='left', width=30).grid(column=0,row=index,sticky='W')
            tkinter.Label(self, text=self.playerstatus[text[index]], width=30).grid(column=1,row=index,sticky='w')
        print("You clicked?")

    def start(self):
        self.root.mainloop()
        
Application().start()