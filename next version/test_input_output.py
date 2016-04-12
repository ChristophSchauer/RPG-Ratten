# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:30:06 2016

@author: Schauer
"""

import tkinter

import main_RPG
import functions_RPG
import parameter_RPG

def game_init():
    window = tkinter.Tk()
    
    window.grid() 
    window.geometry('600x400')
    
    def change():
        window.labelVariable.set('you said: '+ window.entryVariable.get())
         
    # entry field for name
    window.entryVariable = tkinter.StringVar()
    entry = tkinter.Entry(window, textvariable=window.entryVariable)
    entry.grid(row=0,sticky='EW')
    window.entryVariable.set("Enter name here.") 
    
    window.labelVariable = tkinter.StringVar()
    window.labelVariable.set("hello") 
    #self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
    #self.entry.grid(column=0,row=index+1,columnspan=2,sticky='EW')
    #self.entry.bind("<Return>", self.OnPressEnter)
    #self.entryVariable.set(u"Enter command here.")    

     

    #e_name = tkinter.Entry(window, text = 'the name')
    e_button = tkinter.Button(text='accept', command=change)
    e_button.grid(row=1,sticky='EW')
    
    lbl = tkinter.Label(window, textvariable=window.labelVariable,fg="white",bg="black", width=85)
    lbl.grid(row=2,sticky='EW')
        
    window.mainloop()



if __name__ == "__main__":   
    # start the player in room 1
    currentRoom = 11
    # an inventory, which is initially empty
    inventory = []
    # initialize the turns
    turn = 1
    
    playerstatus = game_init()