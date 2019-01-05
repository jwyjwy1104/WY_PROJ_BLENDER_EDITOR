
import os
import re
import sys
import functools
import tkinter
import tkinter as tk
from tkinter import ttk
from time import sleep
from tkinter import *
from tkinter import messagebox

if __name__ == '__main__':
    progress_bar_result_file_path = ""
    progress_bar_terminate_file_path = ""
    num_data_lines = 0
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            progress_bar_result_file_path = "data_generated_" + arg + ".txt" 
            progress_bar_terminate_file_path = "data_terminated_" + arg + ".txt"

            try:
                os.remove(progress_bar_result_file_path)
                os.remove(progress_bar_terminate_file_path)
            except OSError:
                pass
            with open(progress_bar_result_file_path, 'w+') as \
                progress_bar_result_file:
                progress_bar_result_file.write('')
        #=======================================================================
        # Read number of line 'data.config'
        #=======================================================================
        for line in open('data.config'):
            if line.find(arg + " ") != -1:
                num_data_lines += 1
    else:
        progress_bar_result_file_path = "data_generated.txt"
        progress_bar_terminate_file_path = "data_terminated.txt"
        try:
            os.remove(progress_bar_result_file_path)
            os.remove(progress_bar_terminate_file_path)
        except OSError:
            pass

        with open(progress_bar_result_file_path, 'w+') as \
            progress_bar_result_file:
            progress_bar_result_file.write('')

        #=======================================================================
        # Read number of line 'data.config'
        #=======================================================================
        for line in open('data.config'):
            if line.find("title") != -1:
                num_data_lines += 1
    # Range of progress bar
    bar = range(num_data_lines)

    # Decrement number of data line by one.
    num_data_lines -= 1

    #===========================================================================
    # Progress bar
    #===========================================================================
    # Main progrss bar Tkinter window
    popup = tk.Tk()
    popup.title("OAuthTestGenerator Progress Bar")
    popup.geometry("500x50")

    #===========================================================================
    # When terminated ... 
    #===========================================================================
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            popup.destroy()
            f = open(progress_bar_terminate_file_path,'w')
            f.write('Boom')
            f.close()
    
    #===========================================================================
    # Bind exit function to handle application termination.
    #===========================================================================
    popup.protocol("WM_DELETE_WINDOW", on_closing)
    popup.bind('<Escape>', lambda e: popup.destroy())

    #===========================================================================
    # Label text
    #===========================================================================
    plabletextstr = StringVar()
    plabletextstr.set("")
    tk.Label(popup, textvariable=plabletextstr).grid(row=0,column=0)

    #===========================================================================
    # Progress bar
    #===========================================================================
    progress = 0
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(popup, variable=progress_var, 
                                   length=490, maximum=100)
    progress_bar.grid(row=1, column=0)#.pack(fill=tk.X, expand=1, side=tk.BOTTOM)
    progress_bar.place(x=5,y=25)
    popup.pack_slaves()

    #===========================================================================
    # Read number of line 'data_generated.txt'
    #===========================================================================
    num_data_generated_lines = 0
    num_data_generated_lines = sum(1 for line in 
                                   open(progress_bar_result_file_path))

    #===========================================================================
    # Main progress bar loop updates progress bar with data read from
    # data_generated.txt which is generated through parallel makefile process
    #===========================================================================
    progress_step = float(100.0/len(bar))

    while num_data_generated_lines < len(bar):
        popup.update()
        sleep(1) # lauch task

        # Read number of line 'data_generated.txt'
        num_data_generated_lines = sum(1 for line in 
                                       open(progress_bar_result_file_path))
        #print(num_data_generated_lines)

        # Read from data_generated.txt for updating progress bar tick.
        data_generated = open(progress_bar_result_file_path,"r")
        lines = data_generated.readlines()
        if lines != []:
            on_progress_str = lines[len(lines)-1]

            # Update progress bar label text.
            if on_progress_str != "\n" and on_progress_str != " ":
                # Update progress bar label text.
                plabletextstr.set("[" + str(num_data_generated_lines) + "/" + 
                                  str(len(bar)) + "] Finished progress: " + 
                                  on_progress_str)
        else:
            # First tick label text update.
            plabletextstr.set("Waiting ...")

        # Increment progress bar tick
        progress = progress_step*num_data_generated_lines
        progress_var.set(progress)


    #============================================================================
    # Out of the main loop. 
    #===========================================================================
    # Final messages to notify the users for complete.
    if (num_data_generated_lines >= num_data_lines):
        messagebox.showinfo("Alert Message", "Unit test cases generated and executed!!!")
    else:
        error_msg = num_data_lines - num_data_generated_lines
        messagebox.showinfo("Error Message", "Unit test cases not generated properly!!!")






