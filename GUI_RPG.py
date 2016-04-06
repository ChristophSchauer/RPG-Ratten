# -*- coding: utf-8 -*-
"""
Header

@author: Christoph
Version : 0.1

History:
[2016.03.31, CS]:   start with the basic layout of the GUI; insert the status, insert the 
                    commands, insert a input field, insert a button, insert a label field;
                    ERROR#8: make a history of commands given to the program by the 
                    player;
                    scrollbar postponed to 'GUI - version 2': ERROR#8 deferred;
[2016.04.04, CS]:   add the second window with the loplevel update of var_name doesn't 
                    work;
[2016.04.05, CS]:   update of var_name when the char_gen window is clicked a second time 
                    -> too late; should be automatically when the toplevel window is 
                    closed;
                    
Sources:
    http://sebsauvage.net/python/gui/#add_text_entry
    http://effbot.org/tkinterbook/scrollbar.htm
    http://effbot.org/tkinterbook/listbox.htm
    
    http://www.tutorialspoint.com/python/python_gui_programming.htm
    http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
"""



import tkinter

import functions_RPG

def simpleapp_tk(playerstatus):
    playerstatus = functions_RPG.generate_char()
    
    root = tkinter.Tk()
    root.grid()
    
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
        global playerstatus_global
        self.var_name = tkinter.StringVar()
        
        self.name_lbl = tkinter.Label(self.frame, textvariable = self.var_name)
        #self.name_lbl = tkinter.Label(self.frame, text = playerstatus_global['name'])
        self.button1 = tkinter.Button(self.frame, text='click me' , width = 25, command = self.new_window)
        # pack: This geometry manager organizes widgets in blocks before placing
        self.name_lbl.pack()
        self.button1.pack()
        self.frame.pack()
                         
    def new_window(self):
        self.newWindow = tkinter.Toplevel(self.master)
        self.var_name.set(playerstatus_global['name'])
        self.app = char_gen(self.newWindow)

class char_gen:

    def __init__(self, master):
        self.master = master
        
        # The Frame widget is used as a container widget to organize other widgets.
        self.frame = tkinter.Frame(self.master)
        global playerstatus_global
        # The Label widget is used to provide a single-line caption for other widgets. It 
        # can also contain images.
        # text: To display one or more lines of text in a label widget, Internal newlines 
        # ("\n") will force a line break.
        # bd: The size of the border around the indicator. Default is 2 pixels.
        # wraplength: limit the number of characters in each line by setting this option 
        # to the desired number
        var = tkinter.StringVar()
        var.set("used for the char gen!\nname hero:")
        self.lbl = tkinter.Label(self.frame, textvariable=var, bd=5, wraplength=200)
        # Entry: widget is used to display a single-line text field for accepting values 
        # from a user.
        self.name_entry = tkinter.Entry(self.frame)
        self.quitButton = tkinter.Button(self.frame, text = 'set name', width = 25, command = self.close_windows)
        # pack: This geometry manager organizes widgets in blocks before placing        
        self.lbl.pack()
        self.name_entry.pack(side=tkinter.LEFT)
        self.quitButton.pack()
        self.frame.pack()
        
    def close_windows(self):
        playerstatus_global['name'] = self.name_entry.get()
        self.protocol("WM_DELETE_WINDOW", callback)
        self.master.destroy()  
        
    def callback(self):
        self.var_name.set(playerstatus_global['name'])
   
def main():
    root = tkinter.Tk()
    # title of the main window
    root.title('GUI: Ratten!')
    # set the window size to 600px x 400px 
    root.geometry("600x400")
    # set the window icon, must be in the same folder as the script
    root.wm_iconbitmap('logo_black.ico')
    
    app = main_window(root)
    # grid: This geometry manager organizes widgets in a table-like structure 
    # in the parent widget. 
    # them in the parent widget
    #root.grid()
    
    root.mainloop()

if __name__ == "__main__":      
    main()
    #simpleapp_tk(playerstatus)
    
