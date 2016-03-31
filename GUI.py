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
                    
Sources:
    http://sebsauvage.net/python/gui/#add_text_entry
    http://effbot.org/tkinterbook/scrollbar.htm
    http://effbot.org/tkinterbook/listbox.htm
"""

#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import tkinter as Tkinter

class simpleapp_tk(Tkinter.Tk):        
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        # set the window size to 600px x 400px 
        self.geometry("600x400")
        # set the window icon, must be in the same folder as the script
        self.wm_iconbitmap('logo_black.ico')

        
        # status of the player
        label = Tkinter.Label(self, text="here would be the player status")
        label.grid(column=0,row=0)
        
        # available commands
        label = Tkinter.Label(self, text="commands:\n'exit'\n'status'\n'mission'\n'go [north, east, south, west, up, down]'\n'get [item]'\n'fight [person]'\n'drop [item]'",justify='left')
        label.grid(column=1,row=0)

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=1,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter command here.")

        button = Tkinter.Button(self,text=u"Click me !",
                                command=self.OnButtonClick)
        button.grid(column=1,row=1,sticky='EW')
        
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="nw",fg="white",bg="blue",height=50)
        label.grid(column=0,row=2,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Hello !")
        
        # Versuch der Scrollbar Anfang
        scrollbar = Tkinter.Scrollbar(label)
        scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
        history = Tkinter.Listbox(label, yscrollcommand=scrollbar.set)
        #for i in range(100):
        #    listbox.insert(Tkinter.END, str(i))
        history.insert(Tkinter.END, self.entryVariable.get())
        history.pack(side=Tkinter.RIGHT, fill=Tkinter.BOTH)
        scrollbar.config(command=history.yview)
        # Versuch der Scrollbar Ende
        
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
    app = simpleapp_tk(None)
    app.title('GUI: Ratten!')
    app.mainloop()