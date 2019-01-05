#!/usr/bin/python3

import os
import sys
import bpy

from tkinter import *
import tkinter

class MyApp():
    def __init__(self):
        #===============================================================================
        # Tkinter main root window init 
        #===============================================================================
        self.root = Tk()
        self.root.geometry("520x120")
        self.root.resizable(width=False, height=False)
        self.root.title('Create and save Blender file in current directory')

        #===============================================================================
        # Text box for user input 
        #===============================================================================
        large_font = ('Verdana',25)
        large_font2 = ('Verdana',12)        
        entry1Var = StringVar(value='')
        self.entry1 = Entry(self.root, textvariable=entry1Var,font=large_font)
        #e = Entry(self.root)
        self.entry1.pack(side='left')
        self.entry1.focus_set()
        self.entry1.place(x=5,y=55)

        #===============================================================================
        # Text label for user input description
        #===============================================================================
        labelText=StringVar()
        labelText.set("Enter file name to save Blender file:")
        label1=Label(self.root, textvariable=labelText, height=2,font=large_font2)
        label1.pack(side="left")
        label1.place(x=5,y=5)

        #===============================================================================
        # Text label for user input description
        #===============================================================================
        button1 = Button(self.root, text='Create',command=self.savefile, height = 2, width = 10)
        button1.pack(side='right')
        button1.place(x=435,y=55)

        self.root.bind('<Return>', self.keypress_enter)

    def keypress_enter(self, event):
        self.savefile()
        print(event.keysym)

    def savefile(self):
        file_name = self.entry1.get()
        if file_name != "":
            if file_name.find(".blend") == -1:
                file_path = os.getcwd() + "\\" + file_name + ".blend"
            else:
                file_path = os.getcwd() + "\\" + file_name
        
            bpy.ops.wm.save_as_mainfile(filepath=file_path)
            self.root.destroy()

app = MyApp()
app.root.mainloop()


