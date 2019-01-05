import os
import subprocess
import re
import tkinter

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class OneBrowseFolderOneChooseWindow():
    def __init__(self, main_title_str="", \
        main_description_str="", \
        size_str="", \
        operation_onbuttonclick=None):
        # eg. size_str = "520x120"
        self.tk_main_title = main_title_str
        self.tk_main_description = main_description_str
        self.size_str = size_str
        self.operation_onbuttonclick = operation_onbuttonclick

    def draw_window(self):
        # Tkinter main root window init 
        self.root = Tk()
        #self.root.withdraw()  # hide window
        self.root.geometry(self.size_str)
        self.root.resizable(width=False, height=False)
        self.root.title(self.tk_main_title)

        # Text box for user input 
        large_font = ('Verdana',12)
        large_font2 = ('Verdana',12)        
        self.entry1Text = StringVar(value='')
        self.entry1 = Entry(self.root,textvariable=self.entry1Text,\
                            font=large_font)
        #e = Entry(self.root)
        self.entry1.pack(side='left')
        #self.entry1.focus_set()
        self.entry1.place(x=5,y=55, height=50, width=425)

        # Text label for user input description
        self.labelText=StringVar()
        self.labelText.set(self.tk_main_description)
        self.label1=Label(self.root, textvariable=self.labelText,\
                          height=2,font=large_font2)
        self.label1.pack(side="left")
        self.label1.place(x=5,y=5)
 
        # Button for submission
        button1 = Button(self.root, text='Browse',command=self.browsefolder,
                         height=1, width=7)
        button1.pack(side='right')
        button1.place(x=435,y=55)

        button2 = Button(self.root, text='Choose',command=self.choosefolder,
                         height=1, width=7)
        button2.pack(side='right')
        button2.place(x=435,y=80)

        # Keypress enter event
        self.root.bind('<Return>', self.keypress_enter)

    def browsefolder(self):
        # "Browse" button is clicked ...
        browsed_folder_path = filedialog.askdirectory()
        self.entry1Text.set(browsed_folder_path)
        print(browsed_folder_path)

    def keypress_enter(self, event):
        # "Enter" key pressed ...
        chosen_folder_path = self.entry1Text.get()
        self.choosefolder()

    def choosefolder(self):
        # "Choose" button clicked ...
        chosen_folder_path = self.entry1Text.get()

        # Proceed if folder exist ... 
        if os.path.isdir(chosen_folder_path):
            self.root.destroy()

            # Execute the operation passed into the allocation call
            self.operation_onbuttonclick(chosen_folder_path)
        else:
            messagebox.showinfo("Error Message", "Given folder path does not exist!!!")

# Main operation function to be executed when the button is clicked 
# inside OneBrowseFolderOneChooseWindow panel.
def iterate_dir(dir_path):
    result_file_path = os.getcwd() + "\\pydoc_iterator_result.txt"
    if os.path.isdir(dir_path):
        for filename in os.listdir(dir_path):
            # Iterate using recursive
            iterate_dir(os.path.join(dir_path, filename))
            # If the file has ".py" extension
            # If the file is not a testing file
            if os.path.join(dir_path, filename)[-3:] == ".py" and \
               os.path.join(dir_path, filename).find("test") == -1:
                print(os.path.join(dir_path, filename))
                # Generate Pydoc command
                pydoc_command = "cd " + dir_path + " & python -m pydoc -w " + \
                                filename[0:-3]
                print(pydoc_command)
                # Execute Pydoc command
                stdoutdata = subprocess.getoutput(pydoc_command)
                stdoutdata = re.sub(r'\n+', '\n\n', stdoutdata).strip()
                print("["  + stdoutdata + "]")
                with open(result_file_path, 'a') as result_file:
                    result_file.write(stdoutdata)

# Main function
if __name__ == "__main__":
    result_file_path = os.getcwd() + "\\pydoc_iterator_result.txt"
    open(result_file_path, 'w').close()

    main_window = OneBrowseFolderOneChooseWindow(
        "WY folder iteratable Pydoc genreator",\
        "Choose the folder to iterate to generate Pydoc HTML pages!", \
        "520x120", \
        iterate_dir)
    main_window.draw_window()
    main_window.root.mainloop()