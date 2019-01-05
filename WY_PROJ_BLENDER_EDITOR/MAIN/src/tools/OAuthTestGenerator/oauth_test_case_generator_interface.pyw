#!/usr/bin/python3

import os
import re
import sys
import functools
import tkinter

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

#===============================================================================
# Interface Tkinter class panel
#===============================================================================
class OAuthTestCaseGeneratorInterface(Frame):
   # Create and pack the Checkboxes using the array passed into the allocation 
   # call.
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      # All options array.
      self.makefile_chosen_classes = picks

      # Checkbox is checked values array.
      self.vars = []

      # Checkbutton elements array to access them independently.
      self.checkbuttons = []

      # Create Checkbuttons and bind them to each var and checkbutton and store 
      # them to each independet arrays to access them.
      for pick in picks:
         var = IntVar()
         check_button = Checkbutton(self, text=pick, variable=var)
         check_button.pack(side=TOP, anchor=anchor, expand=YES)
         self.vars.append(var)
         self.checkbuttons.append(check_button)

   # Select all button click function.
   def select_all(self):
      for check_button in self.checkbuttons:
          check_button.select()

   # Deselect all button click function.
   def deselect_all(self):
      for check_button in self.checkbuttons:
          check_button.deselect()

   def state(self):
      return map((lambda var: var.get()), self.vars)

   def all_states(self): 
      print(list(self.state()))
      print(list(self.get_checkbutton_strings()))

   # Run button click function.
   def run(self):
      # Array to store the selected class names.
      testing_classes_selected_arr = []
      # Loop through the checkbutton values to check which options are selected.
      for i in range(0,len(self.vars)):
          # If selected ...
          if self.vars[i].get() == 1:
              # Store the selected class name into array to process them after.
              testing_classes_selected_arr.append(self.checkbuttons[i].cget("text"))

      # If no classes are chosen then return.
      if len(testing_classes_selected_arr) == 0:
          return

      # Create makefile using the selected class names.
      with open('makefile', 'w+') as file:
          # Start main Makfile.
          file.write("all: progress_bar makes\n")
          # Parallel process 1 - Progress bar.
          file.write("progress_bar:\n")
          for i in range(0, len(testing_classes_selected_arr)):
            file.write("	python oauth_test_case_generator_progressbar.py " + testing_classes_selected_arr[i] + "\n")
          # Parallel process 2 - Makefiles generate test cases for selected classes.
          file.write("makes:\n")
          for i in range(0, len(testing_classes_selected_arr)):
             file.write("	make -f make_" + testing_classes_selected_arr[i] + "\n")

      # Execute the makefile in parallel.
      os.system("make -j")
      



#===============================================================================
# Main
#===============================================================================
if __name__ == '__main__':
   # Retrieve classes indicated in data.config file read from main.bat.
   testing_classes_arr = []

   for arg in sys.argv[1:]:
        testing_classes_arr.append(arg)

        progress_bar_result_file_path = "data_generated_" + arg + ".txt" 
        progress_bar_terminate_file_path = "data_terminated_" + arg + ".txt"
        try:
            os.remove(progress_bar_result_file_path)
            os.remove(progress_bar_terminate_file_path)
        except OSError:
            pass

   num_testing_classes = len(testing_classes_arr)
   # Get Tkinter app window size using the number of elements passed into the 
   # main function.
   window_widht = 500
   window_height = num_testing_classes*30
   
   # Create TKinter app.
   root = Tk()
   root.geometry(str(window_widht) + "x" + str(window_height))

   # Create main window interface by passing the retrieved testing class array.
   main_window = OAuthTestCaseGeneratorInterface(root, testing_classes_arr)
   main_window.pack(side=TOP, fill=X)
   main_window.config(relief=GROOVE, bd=2)

   # Run button - Run the selected class makefile to genreate test cases.
   run_button = Button(root, text='Run', command=main_window.run, height=1, width=32)
   run_button.pack(side=RIGHT)
   run_button.place(x=250, y=70)



   # Quit button - Terminate the window.
   quit_button = Button(root, text='Quit', command=root.quit, height=1, width=32)
   quit_button.pack(side=RIGHT)
   quit_button.place(x=250, y=100)

   # Select all button - Select all the options provided as checkboxes.
   select_all_button = Button(root, text='Select All', command=main_window.select_all, height=1, width=32)
   select_all_button.pack(side=RIGHT)
   select_all_button.place(x=250, y=10)

   # Deselect all button - Deselect all the options provided as checkboxes.
   deselect_all_button = Button(root, text='Deselect All', command=main_window.deselect_all, height=1, width=32)
   deselect_all_button.pack(side=RIGHT)
   deselect_all_button.place(x=250, y=40)

   # Run app.
   root.mainloop()









