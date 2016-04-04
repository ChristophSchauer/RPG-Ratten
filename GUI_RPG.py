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
[2016.04.04, CS]:   add the second window with the loplevel;
                    update der name variable funzt nicht;
                    
Sources:
    http://sebsauvage.net/python/gui/#add_text_entry
    http://effbot.org/tkinterbook/scrollbar.htm
    http://effbot.org/tkinterbook/listbox.htm
    
    http://www.tutorialspoint.com/python/python_gui_programming.htm
    http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
"""



import tkinter

import main_RPG
import functions_RPG
import parameter_RPG

def game_init():
    window = tkinter.Tk()
    
    root.grid()    
    
    tkinter.Label(window, text='Name your Hero please:').grid(sticky='EW')   
    
    print("Name your Hero please:")
    playerstatus_dummy["name"] = input(">")

    value = 0
    while (value != 8):
        value = 0
        print_lines("you can distribute 8 points onto the following 4 attributes:\n", 
                    "clever, social, strong, fast", 
                    "seperate them by comma (eg:2,2,3,1)",
                    "no atttribute should have more than 3 points")
        data = input(">").split(sep= ",")
        for index in range(4):
            # check if the values from the user are between 0 and 3
            if int(data[index]) <= 3 and int(data[index]) >= 0:
                 value = value + int(data[index])
        if value != 8:
            print("you distributed the values false")
        else:
            playerstatus_dummy["clever"] = int(data[0])
            playerstatus_dummy["social"] = int(data[1])
            playerstatus_dummy["strong"] = int(data[2])
            playerstatus_dummy["fast"] = int(data[3])
            playerstatus_dummy["life"] = int(data[2])*3
    print("your char was created, now the game can begin")
    return(playerstatus_dummy)

def simpleapp_tk(playerstatus):
    playerstatus = functions_RPG.generate_char()
    
    root = tkinter.Tk()
    root.grid()
    root.title('GUI: Ratten!')
    # set the window size to 600px x 400px 
    root.geometry("600x400")
    # set the window icon, must be in the same folder as the script
    root.wm_iconbitmap('logo_black.ico')
    
    # status of the player
    # labels for names
    text = ['name', 'life', 'clever', 'fast', 'social', 'strong', 'pack', 'talents', 'tricks', 'pros', 'cons']          
        
    for index in range(len(text)):
        tkinter.Label(root, text=text[index], anchor='e',width=10, fg="white",bg="black").grid(column=0,row=index,sticky='EW')
        tkinter.Label(root, text=playerstatus[text[index]],anchor='w', width=60).grid(column=1,row=index,sticky='w') 
        
    root.mainloop()
 
'''
new start
'''
   
global playerstatus 
playerstatus_global = {
        "name"      : 'global',
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
    
class main_window:
    def __init__(self, master):
        self.master = master
        # The Frame widget is used as a container widget to organize other widgets.
        self.frame = tkinter.Frame(self.master)
        var = tkinter.StringVar()
        var.set(playerstatus_global['name'])
        self.name_lbl = tkinter.Label(self.frame, textvariable = var)
        self.button1 = tkinter.Button(self.frame, text='click me' , width = 25, command = self.new_window)
        # pack: This geometry manager organizes widgets in blocks before placing
        self.name_lbl.pack()
        self.button1.pack()
        self.frame.pack()
        #self.name_lbl.config(textvariable = var)
                         
    def new_window(self):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = char_gen(self.newWindow)

class char_gen:

    def __init__(self, master):
        self.master = master
        
        # The Frame widget is used as a container widget to organize other widgets.
        self.frame = tkinter.Frame(self.master)
        #The Label widget is used to provide a single-line caption for other widgets. It can also contain images.
        # text: To display one or more lines of text in a label widget, Internal newlines ("\n") will force a line break.
        # bd: The size of the border around the indicator. Default is 2 pixels.
        # wraplength: limit the number of characters in each line by setting this option to the desired number
        var = tkinter.StringVar()
        var.set("used for the char gen!\nname hero:")
        self.lbl = tkinter.Label(self.frame, textvariable=var, bd=5, wraplength=200)
        # Entry: widget is used to display a single-line text field for accepting values from a user.
        self.name_entry = tkinter.Entry(self.frame)
        self.quitButton = tkinter.Button(self.frame, text = 'set name', width = 25, command = self.close_windows)
        # pack: This geometry manager organizes widgets in blocks before placing        
        self.lbl.pack()
        self.name_entry.pack(side=tkinter.LEFT)
        self.quitButton.pack()
        self.frame.pack()
        self.lbl.update_idletasks()
        
    def close_windows(self):
        playerstatus_global['name'] = self.name_entry.get()
        self.master.destroy()
    
def main():
    # start the player in room 1
    currentRoom = 11
    # an inventory, which is initially empty
    inventory = []
    # initialize the turns
    turn = 1
    root = tkinter.Tk()
    app = main_window(root)
    # grid: This geometry manager organizes widgets in a table-like structure 
    # in the parent widget. 
    # them in the parent widget
    #root.grid()
    

    root.mainloop()

if __name__ == "__main__":   
    #playerstatus = game_init()
    
    main()
    #simpleapp_tk(playerstatus)
    
