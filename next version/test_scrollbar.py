# -*- coding: utf-8 -*-
"""
Header

@author: Christoph
Version : 0.1

History:
[2016.03.31, CS]:   start with the basic layout of the GUI; insert the status, 
                    insert the commands, insert a input field, insert a button,
                    insert a label field;
                    ERROR#8: make a history of commands given to the program 
                    by the player;
                    scrollbar postponed to 'GUI - version 2';
[2016.04.01, CS]:   
                    
Sources:
    http://sebsauvage.net/python/gui/#add_text_entry
    http://effbot.org/tkinterbook/scrollbar.htm
    http://effbot.org/tkinterbook/listbox.htm
"""

#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import tkinter as Tkinter

import main_RPG
import functions_RPG
import parameter_RPG

class simpleapp_tk(Tkinter.Tk):        
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize(playerstatus)

    def initialize(self, playerstatus):
        self.grid()
        # set the window size to 600px x 400px 
        self.geometry("600x400")
        # set the window icon, must be in the same folder as the script
        self.wm_iconbitmap('logo_black.ico')
        


        # status of the player
        # labels for names
        text = ['name', 'life', 'clever', 'fast', 'social', 'strong', 'pack', 'talents', 'tricks', 'pros', 'cons']          
                
        for index in range(len(text)):
            Tkinter.Label(self, text=text[index], justify='left', width=30).grid(column=0,row=index,sticky='W')
            Tkinter.Label(self, text=playerstatus[text[index]], width=30).grid(column=1,row=index,sticky='w') 
        # variables
        self.e_v_life = Tkinter.IntVar()
        self.e_v_clever = Tkinter.IntVar()
        # entries
        #Tkinter.Entry(self,textvariable=self.e_v_life).grid(column=1,row=0,sticky='W')

        #self.e_clever = Tkinter.Entry(self,textvariable=self.e_v_life)
        #self.e_clever.grid(column=1,row=1,sticky='W')
        self.e_v_fast = Tkinter.IntVar()
        #self.e_fast = Tkinter.Entry(self,textvariable=self.e_v_life)
        #self.e_fast.grid(column=1,row=2,sticky='W')
        self.e_v_social = Tkinter.IntVar()
        #self.e_social = Tkinter.Entry(self,textvariable=self.e_v_life)
        #self.e_social.grid(column=1,row=3,sticky='W')
        self.e_v_strong = Tkinter.IntVar()
        #self.e_strong = Tkinter.Entry(self,textvariable=self.e_v_life)
        #self.e_strong.grid(column=1,row=4,sticky='W')
        self.e_v_talents = Tkinter.IntVar()
        #self.e_talents = Tkinter.Entry(self,textvariable=self.e_v_life)
        #self.e_talents.grid(column=1,row=5,sticky='W')
        self.e_v_tricks = Tkinter.IntVar()
        #self.e_tricks = Tkinter.Entry(self,textvariable=self.e_v_life)
        #self.e_tricks.grid(column=1,row=6,sticky='W')
        self.e_v_pros = Tkinter.IntVar()
        #self.e_pros = Tkinter.Entry(self,textvariable=self.e_v_life)
        #self.e_pros.grid(column=1,row=7,sticky='W')
        self.e_v_cons = Tkinter.IntVar()
        #self.e_cons = Tkinter.Entry(self,textvariable=self.e_v_life)
        #self.e_cons.grid(column=1,row=8,sticky='W')   
        

        
        # available commands
        label = Tkinter.Label(self, text="commands:\n'exit'\n'status'\n'mission'\n'go [north, east, south, west, up, down]'\n'get [item]'\n'fight [person]'\n'drop [item]'",justify='left', borderwidth=10)
        label.grid(column=3,row=0,rowspan=index,sticky='W')
       
        # entry field
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=index+1,columnspan=2,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter command here.")
        # button
        button = Tkinter.Button(self,text=u"Click me !",command=self.OnButtonClick)
        button.grid(column=3,row=index+1,sticky='EW')
        
        '''
        # third row
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="nw",fg="white",bg="black",height=10)
        label.grid(column=0,row=2,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Hello !")
        
        # Versuch der Scrollbar Anfang
        scrollbar = Tkinter.Scrollbar(label)
        scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
        # width = 100 ist genau die Labelbreite, wird vmtl in Prozent sein
        history = Tkinter.Listbox(label, yscrollcommand=scrollbar.set, width = 80)
        #for i in range(100):
        #    listbox.insert(Tkinter.END, str(i))
        history.insert(Tkinter.END, self.entryVariable.get())
        history.pack(side=Tkinter.RIGHT, fill=Tkinter.BOTH)
        scrollbar.config(command=history.yview)
        # Versuch der Scrollbar Ende
        '''
        self.grid_columnconfigure(0,weight=1)
        # first is x-axis, second y-axis
        self.resizable(False,False)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        self.OnPressEnter(self)

    def OnPressEnter(self, event):
        self.labelVariable.set(self.entryVariable.get()+" (You pressed ENTER)" )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":   
    # start the player in room 1
    currentRoom = 11
    # an inventory, which is initially empty
    inventory = []
    # initialize the turns
    turn = 1
    # generate rooms
    rooms = functions_RPG.fct_rooms()
    # generate char
    playerstatus = functions_RPG.generate_char()
    
    app = simpleapp_tk(None)
    app.title('GUI: Ratten!')
    app.mainloop()