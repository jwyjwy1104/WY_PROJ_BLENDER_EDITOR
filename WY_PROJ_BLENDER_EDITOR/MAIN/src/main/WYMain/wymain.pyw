# Main window --> Export --> Blender file browse --> Model choose --> Export
#             --> Import --> Custom WYMesh file browse 
#                        --> Import to Blender browse --> Import

#!/usr/bin/python3

import bpy
import os
import re
import sys
import functools
import tkinter

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

filename = os.getcwd() + "\\..\\..\\main\\WYModel\\WYModel.py" 
exec(compile(open(filename).read(), filename, 'exec'))
filename = os.getcwd() + "\\..\\..\\main\\WYModelManager\\WYModelManager.py" 
exec(compile(open(filename).read(), filename, 'exec'))
filename = os.getcwd() + "\\..\\..\\main\\WYMesh\\WYMesh.py" 
exec(compile(open(filename).read(), filename, 'exec'))
filename = os.getcwd() + "\\..\\..\\main\\WYMaterial\\WYMaterial.py" 
exec(compile(open(filename).read(), filename, 'exec'))
filename = os.getcwd() + "\\..\\..\\main\\WYUtil\\WYUtil.py" 
exec(compile(open(filename).read(), filename, 'exec'))
filename = os.getcwd() + "\\..\\..\\main\\WYCoordsys\\WYCoordsys.py" 
exec(compile(open(filename).read(), filename, 'exec'))

################################################################################
################################################################################
################################################################################
# Main Blender WY custom exporter panel
################################################################################
################################################################################
################################################################################
class WYBlenderExporter():
    def __init__(self, main_title_str="", options_arr=[], size_str="", 
                 button_label_str="", operation_onbuttonclick=None):
        # eg. size_str = "520x120"
        self.tk_main_title = main_title_str
        self.options_arr = options_arr
        self.size_str = size_str
        self.button_label_str = button_label_str
        self.operation_onbuttonclick = operation_onbuttonclick

    def draw_window(self):
        #=======================================================================
        # Tkinter main root window init 
        #=======================================================================
        self.root = Tk()
        #self.root.withdraw()  # hide window
        self.root.geometry(self.size_str)
        self.root.resizable(width=False, height=False)
        self.root.title(self.tk_main_title)

        large_font = ('Verdana',8)

        #=======================================================================
        # Option menu: Models
        #=======================================================================
        # Text label for user input description
        self.labelText=StringVar()
        self.labelText.set("Choose model to export:")
        self.labelModels=Label(self.root, textvariable=self.labelText, 
                               height=2,font=large_font)
        self.labelModels.pack(side="left")
        self.labelModels.place(x=5,y=5)

        # Option menu
        optionmenu_models_default_value = self.options_arr[0]
        self.chosen_option_model_name = self.options_arr[0]
        variable = StringVar(value='')
        # Default value
        variable.set(optionmenu_models_default_value) 
        self.chosen_models_option_value = optionmenu_models_default_value
        self.optionmenu_models = OptionMenu(self.root, variable, 
                                    *self.options_arr, 
                                    command=self.process_optionmenu_model_name)
        self.optionmenu_models.configure(width=78, height=5)
        self.optionmenu_models.pack()
        self.optionmenu_models.place(x=5, y=35)

        #=======================================================================
        # Option menu: Coordinate system export axis UP vector
        #=======================================================================
        # Text label description
        self.labelText=StringVar()
        self.labelText.set("Choose coordinate system UP axis to export:")
        self.labelCoordUp=Label(self.root, textvariable=self.labelText, 
                                height=2,font=large_font)
        self.labelCoordUp.pack(side="left")
        self.labelCoordUp.place(x=5, y=125)

        # Option menu
        self.coord_up_arr = ["X", "-X", "Y", "-Y"]
        optionmenu_coord_up_default_value = "Z"
        self.chosen_option_coord_up_value = optionmenu_coord_up_default_value
        self.optionmenu_coord_up_text = StringVar(value='')
        # Default value
        self.optionmenu_coord_up_text.set(optionmenu_coord_up_default_value) 
        self.chosen_coord_up_option_value = optionmenu_coord_up_default_value
        self.optionmenu_coord_up = OptionMenu(self.root, 
                                    self.optionmenu_coord_up_text, 
                                    *self.coord_up_arr, 
                                    command=self.process_optionmenu_coord_up)
        self.optionmenu_coord_up.configure(width=78, height=1)
        self.optionmenu_coord_up.pack()
        self.optionmenu_coord_up.place(x=5, y=155)

        #=======================================================================
        # Option menu: Coordinate system export axis FORWARD vector
        #=======================================================================
        # Text label description
        self.labelText=StringVar()
        self.labelText.set("Choose coordinate system FORWARD axis to export:")
        self.labelCoordUp=Label(self.root, textvariable=self.labelText, 
                                height=2,font=large_font)
        self.labelCoordUp.pack(side="left")
        self.labelCoordUp.place(x=5,y=185)

        # Option menu
        self.coord_forward_arr = ["X", "-X", "Z", "-Z"]
        optionmenu_coord_forward_default_value = "Y"
        self.chosen_option_coord_forward_value = \
            optionmenu_coord_forward_default_value
        self.optionmenu_coord_forward_text = StringVar(value='')
        # Default value
        self.optionmenu_coord_forward_text.set( \
            optionmenu_coord_forward_default_value)
        self.chosen_coord_forward_option_value = \
            optionmenu_coord_forward_default_value
        self.optionmenu_coord_forward = OptionMenu(self.root, 
                                self.optionmenu_coord_forward_text, 
                                *self.coord_forward_arr, 
                                command=self.process_optionmenu_coord_forward)
        self.optionmenu_coord_forward.configure(width=78, height=1)
        self.optionmenu_coord_forward.pack()
        self.optionmenu_coord_forward.place(x=5, y=215)

        #=======================================================================
        # Export to browse entry
        #=======================================================================
        # Text label description
        self.labelText=StringVar()
        self.labelText.set("Export to:")
        self.labelCoordUp=Label(self.root, textvariable=self.labelText, 
                                height=2,font=large_font)
        self.labelCoordUp.pack(side="left")
        self.labelCoordUp.place(x=5,y=245)

        # Entry browse folder 
        self.entry_export_folder_text = StringVar(value='')
        self.entry_export_folder = Entry(self.root, 
                                textvariable=self.entry_export_folder_text,
                                font=large_font)
        self.entry_export_folder.pack(side='left')
        self.entry_export_folder.focus_set()
        self.entry_export_folder.place(x=5, y=270, height=50, width=425)

        button_browse_folder = Button(self.root, text='Browse',
                                      command=self.browse_folder,
                                      height=1, width=7)
        button_browse_folder.pack(side='right')
        button_browse_folder.place(x=435, y=270, width=80, height=50)

        #=======================================================================
        # File name entry
        #=======================================================================
        # Text label for user input description
        self.labelText=StringVar()
        self.labelText.set("Save as file name:")
        self.labelFileName=Label(self.root, textvariable=self.labelText,
                                 height=2,font=large_font)
        self.labelFileName.pack(side="left")
        self.labelFileName.place(x=5,y=325)

        # Entry file name
        self.entry_file_name_text = StringVar(value='')
        self.entry_file_name = Entry(self.root, 
                                     textvariable=self.entry_file_name_text,
                                     font=large_font)
        self.entry_file_name.pack(side='left')
        self.entry_file_name.focus_set()
        self.entry_file_name.place(x=5, y=350, height=50, width=510)

        #=======================================================================
        # Export button
        #=======================================================================
        # Need to use "functools" to pass the member variable values to the 
        # operation function initialized in current object.
        button_export = Button(self.root, text='Export', 
                               command=self.export_model, height=5, width=71)
        button_export.pack(side='right')
        button_export.place(x=7, y=425)

        #=======================================================================
        # Keypress enter event
        #=======================================================================
        self.root.bind('<Return>', self.keypress_enter)

    def keypress_enter(self, event):
        # "Enter" key pressed ...
        self.export_model()

    def process_optionmenu_model_name(self,value):
        # Selected model name value updated ...
        self.chosen_option_model_name = value
        #print(self.chosen_option_model_name)

    def process_optionmenu_coord_up(self,value):
        # Selected coordinate system UP axis value updated ...
        self.chosen_option_coord_up_value = value
        self.optionmenu_coord_up_text.set(self.chosen_option_coord_up_value)

        coord_forward_menu = self.optionmenu_coord_forward["menu"]
        coord_forward_text = self.optionmenu_coord_forward_text
        if self.chosen_option_coord_up_value == "X":
            coord_forward_menu.delete(0, 'end')
            # Insert list of new options (tk._setit hooks them up to var)
            new_options = ('Y', '-Y', 'Z', '-Z')
            for option_val in new_options:
                 self.optionmenu_coord_forward['menu'].add_command(
                     label=option_val, 
                     command=tkinter._setit(coord_forward_text, option_val))
            coord_forward_text.set(new_options[0])
        if self.chosen_option_coord_up_value == "-X":
            coord_forward_menu.delete(0, 'end')
            # Insert list of new options (tk._setit hooks them up to var)
            new_options = ('Y', '-Y', 'Z', '-Z')
            for option_val in new_options:
                 self.optionmenu_coord_forward['menu'].add_command(
                     label=option_val, 
                     command=tkinter._setit(coord_forward_text, option_val))
            coord_forward_text.set(new_options[0])
        if self.chosen_option_coord_up_value == "Y":
            coord_forward_menu.delete(0, 'end')
            # Insert list of new options (tk._setit hooks them up to var)
            new_options = ('X', '-X', 'Z', '-Z')
            for option_val in new_options:
                 self.optionmenu_coord_forward['menu'].add_command(
                     label=option_val, 
                     command=tkinter._setit(coord_forward_text, option_val))
            coord_forward_text.set(new_options[0])
        if self.chosen_option_coord_up_value == "-Y":
            coord_forward_menu.delete(0, 'end')
            # Insert list of new options (tk._setit hooks them up to var)
            new_options = ('X', '-X', 'Z', '-Z')
            for option_val in new_options:
                 self.optionmenu_coord_forward['menu'].add_command(
                     label=option_val, 
                     command=tkinter._setit(coord_forward_text, option_val))
            coord_forward_text.set(new_options[0])
        if self.chosen_option_coord_up_value == "Z":
            coord_forward_menu.delete(0, 'end')
            # Insert list of new options (tk._setit hooks them up to var)
            new_options = ('X', '-X', 'Y', '-Y')
            for option_val in new_options:
                 self.optionmenu_coord_forward['menu'].add_command(
                     label=option_val, 
                     command=tkinter._setit(coord_forward_text, option_val))
            coord_forward_text.set(new_options[0])
        if self.chosen_option_coord_up_value == "-Z":
            coord_forward_menu.delete(0, 'end')
            # Insert list of new options (tk._setit hooks them up to var)
            new_options = ('X', '-X', 'Y', '-Y')
            for option_val in new_options:
                 self.optionmenu_coord_forward['menu'].add_command(
                     label=option_val, 
                     command=tkinter._setit(coord_forward_text, option_val))
            coord_forward_text.set(new_options[0])

    def process_optionmenu_coord_forward(self,value):
        print(value)
        # Selected coordinate system FORWARD axis value updated ...
        self.chosen_option_coord_forward_value = value
        #print(self.chosen_option_coord_forward_value)
        self.optionmenu_coord_forward_text.set(\
            self.chosen_option_coord_forward_value)

    def browse_folder(self):
        self.entry_export_folder_text.set(filedialog.askdirectory())

    def export_model(self):
        # "Export" button clicked ...
        model_name = self.chosen_option_model_name
        coord_up_str = self.optionmenu_coord_up_text.get()
        coord_forward_str = self.optionmenu_coord_forward_text.get()
        export_dir_path = self.entry_export_folder_text.get()
        export_file_name = self.entry_file_name_text.get()

        print(model_name)
        print(coord_up_str)
        print(coord_forward_str)
        print(export_dir_path)
        print(export_file_name)

        # CU, CF - Coordinate exported options.
        XU,M_XU,YU,M_YU,ZU,M_ZU = (False,)* 6
        XF,M_XF,YF,M_YF,ZF,M_ZF = (False,)* 6

        if coord_up_str == "X": XU = True 
        if coord_up_str == "-X": XU = True 
        if coord_up_str == "Y": XU = True 
        if coord_up_str == "-Y": XU = True 
        if coord_up_str == "Z": XU = True 
        if coord_up_str == "-Z": XU = True 

        if coord_forward_str == "X": XU = True 
        if coord_forward_str == "-X": XU = True 
        if coord_forward_str == "Y": XU = True 
        if coord_forward_str == "-Y": XU = True 
        if coord_forward_str == "Z": XU = True 
        if coord_forward_str == "-Z": XU = True 

        if os.path.isdir(export_dir_path):
            if len(re.findall(r'[^A-Za-z0-9_\-\\]', export_file_name)) <= 0 \
               and export_file_name != "":
                print("Export!")
            
                # Create a WYModelManager object to export the selected model.
                wymodelmanager = WYModelManager()
                wycoordsys = WYCoordsys(XU, M_XU, YU, M_YU, ZU, M_ZU, XF, 
                                        M_XF, YF, M_YF, ZF, M_ZF)

                # Get the selected model object and set it active.
                bpy.context.scene.objects.active = bpy.data.objects[model_name]

                # Using the selected Blender model object to create WYMesh
                # object to export the model onto files.
                wymesh = WYMesh(bpy.data.objects[model_name], wycoordsys)
                # Initialize WYMesh object data before exporting.
                wymesh.init_mesh_data()

                # Create a WYMaterial object for the very first material 
                # object exists inside the exporting Blender mesh object.
                wymaterial = WYMaterial(
                    bpy.data.objects[model_name], 
                    bpy.data.objects[model_name].data.materials[0])
                # Initialize WYMaterial object data before exporting.
                wymaterial.init_material_data()

                # Create final WYModel object to pass onto the 
                # WYModelManager object to export with.
                wymodel = WYModel(wymesh, wymaterial)

                # Export the model using the initialized WYModel object and
                # the file path to export onto.
                wymodelmanager.export_model(
                    wymodel, 
                    export_dir_path + "\\" + export_file_name)

                # Alert message when export is done.
                export_model_alert_msg = "Model \"" + str(bpy.data.objects[model_name].name) + "\" is exported onto \"" + export_dir_path + "\" named \"" + export_file_name + "\"!!!"
                messagebox.showinfo("Export", export_model_alert_msg )
            else:
                messagebox.showinfo("Error Message", "Invalid file name format!!!")
        else:
            messagebox.showinfo("Error Message", "Export to folder does not exist!!!")

################################################################################
################################################################################
################################################################################
# Main Blender WY custom importer panel
################################################################################
################################################################################
################################################################################
class WYBlenderImporter():
    def __init__(self, main_title_str="", size_str="", 
                 button_label_str="", operation_onbuttonclick=None):
        # eg. size_str = "520x120"
        self.tk_main_title = main_title_str
        self.size_str = size_str
        self.button_label_str = button_label_str

        self.operation_onbuttonclick = operation_onbuttonclick
        
    def draw_window(self):
        #=======================================================================
        # Tkinter main root window init 
        #=======================================================================
        self.root = Tk()
        #self.root.withdraw()  # hide window
        self.root.geometry(self.size_str)
        self.root.resizable(width=False, height=False)
        self.root.title(self.tk_main_title)

        large_font = ('Verdana',8)

        #=======================================================================
        # Import from browse WYMesh file entry
        #=======================================================================     
        # Text label description
        self.labelText=StringVar()
        self.labelText.set("Import from WYMesh file:")
        self.labelCoordUp=Label(self.root, textvariable=self.labelText, 
                                height=2,font=large_font)
        self.labelCoordUp.pack(side="left")
        self.labelCoordUp.place(x=5,y=5)

        # Entry browse WYMesh file to import from
        self.entry_import_from_file_text = StringVar(value='')
        self.entry_import_from_wyo_file = Entry(self.root, 
                                textvariable=self.entry_import_from_file_text,
                                font=large_font)
        self.entry_import_from_wyo_file.pack(side='left')
        self.entry_import_from_wyo_file.focus_set()
        self.entry_import_from_wyo_file.place(x=5, y=30, height=50, width=425)

        button_browse_wyo_file = Button(self.root, text='Browse',
                                        command=self.browse_wyo_file, 
                                        height=1, width=7)
        button_browse_wyo_file.pack(side='right')
        button_browse_wyo_file.place(x=435, y=30, width=80, height=50)

        #=======================================================================
        # Import to browse Blender file entry
        #=======================================================================     
        # Text label description
        self.labelText=StringVar()
        self.labelText.set("Import to Blender file:")
        self.labelCoordUp=Label(self.root, textvariable=self.labelText, 
                                height=2,font=large_font)
        self.labelCoordUp.pack(side="left")
        self.labelCoordUp.place(x=5,y=85)

        # Entry browse Blender file to import onto
        self.entry_import_to_file_text = StringVar(value='')
        self.entry_import_to_blender_file = Entry(self.root, 
                                    textvariable=self.entry_import_to_file_text,
                                    font=large_font)
        self.entry_import_to_blender_file.pack(side='left')
        self.entry_import_to_blender_file.focus_set()
        self.entry_import_to_blender_file.place(x=5, y=110, height=50, width=425)

        button_browse_blender_file = Button(self.root, text='Browse',
                                            command=self.browse_blender_file, 
                                            height=1, width=7)
        button_browse_blender_file.pack(side='right')
        button_browse_blender_file.place(x=435, y=110, width=80, height=50)
        
        #=======================================================================
        # Import button
        #=======================================================================
        button_export = Button(self.root, text='Import', 
                               command=self.import_model, height=5, width=71)
        button_export.pack(side='right')
        button_export.place(x=7, y=175)

        #=======================================================================
        # Keypress enter event
        #=======================================================================
        self.root.bind('<Return>', self.keypress_enter)

    def keypress_enter(self, event):
        # "Enter" key pressed ...
        self.import_model()

    def browse_wyo_file(self):
        # "Browse" button is clicked ...
        browsed_file_path = filedialog.askopenfilename(
            initialdir = "C:/",
            title = "choose your file",
            filetypes = (("WYMesh file", "*.wyo"),("all files","*.*")))
        self.entry_import_from_file_text.set(browsed_file_path)

    def browse_blender_file(self):
        # "Browse" button is clicked ...
        browsed_file_path = filedialog.askopenfilename(
            initialdir = "C:/",
            title = "choose your file",
            filetypes = (("Blender file", "*.blend"),("all files","*.*")))
        self.entry_import_to_file_text.set(browsed_file_path)

    def import_model(self):
        # "Import" button clicked ...
        import_from_wyo_file_path = self.entry_import_from_file_text.get()
        import_to_blender_file_path = self.entry_import_to_file_text.get()

        # Alert message if WYMesh file not exist ... 
        if os.path.isfile(import_from_wyo_file_path) == False or \
            import_from_wyo_file_path == "":
            messagebox.showinfo("Error Message", "Invalid import from WYMesh file path!!!")  

        # Alert message if Blender file not exists ... 
        if os.path.isfile(import_to_blender_file_path) == False or \
            import_to_blender_file_path == "":
            messagebox.showinfo("Error Message", "Invalid import to Blender file path!!!")

        # Import the WYMesh file to Blender file if WYMesh file and Blender 
        # file both exists ...
        if os.path.isfile(import_from_wyo_file_path) and \
           import_from_wyo_file_path != "" and \
           os.path.isfile(import_to_blender_file_path) and \
           import_to_blender_file_path != "":
           # Execute the operation passed into the allocation call
           self.operation_onbuttonclick(import_from_wyo_file_path, import_to_blender_file_path)  

           # Alert message when export is done.
           import_model_alert_msg = "Model from \"" + import_from_wyo_file_path + "\" is imported onto \"" + import_to_blender_file_path + "\"!!!"
           messagebox.showinfo("Import", import_model_alert_msg)
        else:
            messagebox.showinfo("Error Message", "Error!!!")


#===============================================================================
#===============================================================================
#===============================================================================
# 2 Button window panel
#===============================================================================
#===============================================================================
#===============================================================================
class TwoButtonWindow():
    def __init__(self, main_title_str="", size_str="", 
                 first_window=None, first_button_label_str="", 
                 second_window=None, second_button_label_str=""):
        # eg. size_str = "520x120"
        self.tk_main_title = main_title_str
        self.size_str = size_str
        self.first_window = first_window
        self.second_window = second_window
        self.first_button_label_str = first_button_label_str
        self.second_button_label_str = second_button_label_str

    def draw_window(self):
        #=======================================================================
        # Tkinter main root window init 
        #=======================================================================
        self.root = Tk()
        self.root.geometry(self.size_str)
        self.root.resizable(width=False, height=False)
        self.root.title(self.tk_main_title)
 
        #=======================================================================
        # Button for submission
        #=======================================================================
        button1 = Button(self.root, text=self.first_button_label_str,
                         command=self.open_first_window, height=5, width=35)
        button1.pack(side='left')
        button1.place(x=5,y=20)

        button2 = Button(self.root, text=self.second_button_label_str,
                         command=self.open_second_window, height=5, width=35)
        button2.pack(side='right')
        button2.place(x=260,y=20)

    def open_first_window(self):
        self.root.destroy()

        self.first_window.draw_window()
        self.first_window.root.deiconify()
        self.first_window.root.mainloop()

    def open_second_window(self):
        self.root.destroy()

        self.second_window.draw_window()
        self.second_window.root.deiconify()
        self.second_window.root.mainloop()

#===============================================================================
#===============================================================================
#===============================================================================
# 1 Option menu and 1 button window panel
#===============================================================================
#===============================================================================
#===============================================================================
class OneOptionmenuOneButtonWindow():
    def __init__(self, main_title_str="", options_arr=[], size_str="", 
                 button_label_str="", operation_onbuttonclick=None):
        # eg. size_str = "520x120"
        self.tk_main_title = main_title_str
        self.options_arr = options_arr
        self.size_str = size_str
        self.button_label_str = button_label_str
        self.operation_onbuttonclick = operation_onbuttonclick

    def draw_window(self):
        #=======================================================================
        # Tkinter main root window init 
        #=======================================================================
        self.root = Tk()
        #self.root.withdraw()  # hide window
        self.root.geometry(self.size_str)
        self.root.resizable(width=False, height=False)
        self.root.title(self.tk_main_title)

        optionmenu_default_value = self.options_arr[0]
        variable = StringVar(value='')
        variable.set(optionmenu_default_value) # default value
        self.chosen_option_value = optionmenu_default_value

        self.optionmenu = OptionMenu(self.root, variable, *self.options_arr, 
                                     command=self.process_optionmenu)
        self.optionmenu.place(x=5,y=55, height=50, width=425)
        self.optionmenu.configure(width=60, height=40)
        self.optionmenu.pack(side="left")

        #=======================================================================
        # Button for submission
        #=======================================================================
        # Need to use "functools" to pass the member variable values to the operation
        # function initialized in current object.
        button1 = Button(self.root, text=self.button_label_str,
                         command=functools.partial(
                             self.operation_onbuttonclick, 
                             self.chosen_option_value), 
                         height=6, width=12)
        button1.pack(side='right')
        button1.place(x=410,y=10)

        #=======================================================================
        # Keypress enter event
        #=======================================================================
        self.root.bind('<Return>', self.keypress_enter)

    def keypress_enter(self, event):
        # "Enter" key pressed ...
        if self.chosen_option_value != "":
            if self.bpy_context_objects_arr[self.chosen_option_value] != None:
                self.savefile()
                print(event.keysym)
        else:
             messagebox.showinfo("Error Message", "Must choose one value!!!")

    def process_optionmenu(self,value):
        # Selected values updated ...
        self.chosen_option_value = value
        #print(self.chosen_option_value)

#===============================================================================
#===============================================================================
#===============================================================================
# 1 Text label, 1 input entry box, 1 Browse file button and 1 Choose button window panel
#===============================================================================
#===============================================================================
#===============================================================================
class OneBrowseFileOneChooseWindow():
    def __init__(self, main_title_str="", main_description_str="", size_str="",
                browse_file_extension_str="", 
                browse_file_extension_description_str="",
                operation_onbuttonclick=None):
        # eg. size_str = "520x120"
        self.tk_main_title = main_title_str
        self.tk_main_description = main_description_str
        self.size_str = size_str
        self.browse_file_extension_str = browse_file_extension_str
        self.browse_file_extension_description_str = \
            browse_file_extension_description_str

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
        self.entry1 = Entry(self.root, textvariable=self.entry1Text,
                            font=large_font)
        #e = Entry(self.root)
        self.entry1.pack(side='left')
        #self.entry1.focus_set()
        self.entry1.place(x=5,y=55, height=50, width=425)

        # Text label for user input description
        self.labelText=StringVar()
        self.labelText.set(self.tk_main_description)
        self.label1=Label(self.root, textvariable=self.labelText, 
                          height=2,font=large_font2)
        self.label1.pack(side="left")
        self.label1.place(x=5,y=5)
 
        # Button for submission
        button1 = Button(self.root, text='Browse',command=self.browsefile, 
                         height=1, width=7)
        button1.pack(side='right')
        button1.place(x=435,y=55)

        button2 = Button(self.root, text='Choose',command=self.choosefile, 
                         height=1, width=7)
        button2.pack(side='right')
        button2.place(x=435,y=80)

        # Keypress enter event
        self.root.bind('<Return>', self.keypress_enter)

    def browsefile(self):
        # "Browse" button is clicked ...
        browsed_file_path = filedialog.askopenfilename(
            initialdir = "C:/",
            title = "choose your file",
            filetypes = ((
                self.browse_file_extension_description_str, 
                self.browse_file_extension_str),("all files","*.*")))
        self.entry1Text.set(browsed_file_path)
        print(browsed_file_path)

    def keypress_enter(self, event):
        # "Enter" key pressed ...
        if os.path.isfile(self.entry1Text.get()):
            self.choosefile()
            print(event.keysym)
        else:
            messagebox.showinfo("Error Message", "Given Blender file path does not exist!!!")

    def choosefile(self):
        # "Choose" button clicked ...
        chosen_file_path = self.entry1Text.get()

        # Proceed if file exist ... 
        if os.path.isfile(chosen_file_path):
            self.root.destroy()

            # Execute the operation passed into the allocation call
            self.operation_onbuttonclick(
                chosen_file_path, 
                self.browse_file_extension_str)
        else:
            messagebox.showinfo("Error Message", "Given Blender file path does not exist!!!")



#===============================================================================
#===============================================================================
# Global function: Operation to be passed onto the WYBlenderImporter object
#                  to be exeucted when the import button is clicked.
#===============================================================================
#===============================================================================
def opertation_import(import_from_wyo_file_path="", 
                      import_to_blender_file_path=""):
    # Open Blender file.
    bpy.ops.wm.open_mainfile(filepath=import_to_blender_file_path)

    wymodelmanager = WYModelManager()
    wymodelmanager.import_model(import_from_wyo_file_path)

    # Update Blender file.
    bpy.ops.wm.save_mainfile(filepath=import_to_blender_file_path)

    print("Import Done!!!")

#===============================================================================
#===============================================================================
# Global function: Operation to be passed onto the OneBrowseOneChooseWindow object
#                  to be exeucted when the Blender file is chosen ready for export
#                  and the button is clicked.
#===============================================================================
#===============================================================================
def opertation_export(chosen_file_path="", browse_file_extension_str=""):
    # Handle *.blend files
    if browse_file_extension_str == "*.blend":
        # "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MESH_MAT_EXPORTER\\src\\main\\WYMain\\test.blend"

        #=======================================================================
        # Blender file opened
        #=======================================================================
        # Open Blender file.
        bpy.ops.wm.open_mainfile(filepath=chosen_file_path)
        bpy.ops.object.mode_set(mode='OBJECT')

        # Collect all the models inside Blender file which has mesh inside.
        bpy_context_objects_name_arr = []
        # Provide options for mesh objects only.
        for ob in bpy.context.scene.objects:
            if ob.type == 'MESH':
                print("object name:  ", ob.name)
                bpy_context_objects_name_arr.append(ob.name)
        
        # Open WYBlenderExporter to export the selected model.
        wyblenderexporter = WYBlenderExporter(
            "Choose model to export with!", 
            bpy_context_objects_name_arr, 
            "520x520", "Export", None)
        wyblenderexporter.draw_window()
        wyblenderexporter.root.mainloop()

        # Update Blender file.
        bpy.ops.wm.save_mainfile(filepath=chosen_file_path)
        #=======================================================================

# Main function
if __name__ == "__main__":
    #===========================================================================
    # Import window:
    #    Browse WYMesh file to import with
    #    Browse Blender file to import onto
    #    Click import button
    #    Import WYMesh file model onto the Blender file.
    #===========================================================================
    import_from_wyo_file_window = WYBlenderImporter(
        "WY custom Blender importer!", 
        "520x270", "Import", opertation_import)

    #===========================================================================
    # Export window:
    #    Browse Blender file to access model to export with
    #    Show lists of models to export
    #    Choose the model name to export with
    #    Choose the coordinate system options
    #    Browse the folder to export the model onto
    #    Provide the file name to export with
    #    Click export button
    #    Export WYMesh file model from the Blender file.
    #===========================================================================
    export_from_blend_file_window = OneBrowseFileOneChooseWindow(
        "WY custom Blender exporter", 
        "Choose Blender file to access to export with!", 
        "520x120", "*.blend", "Blender files", opertation_export)

    #===========================================================================
    # Main window:
    #    Double button window:
    #        Left - Import --> Import window
    #        Right - Export --> Export window
    #===========================================================================
    main_window = TwoButtonWindow(
        "WY_PROJ_BLENDER_EDITOR", 
        "520x120", 
        import_from_wyo_file_window, "Import", 
        export_from_blend_file_window, "Export")

    # Draw main window
    main_window.draw_window()
    # Execute main window loop for user input
    main_window.root.mainloop()







