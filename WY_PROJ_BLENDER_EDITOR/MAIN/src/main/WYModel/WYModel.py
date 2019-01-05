################################################################################
# Project Name          	: WY_PROJ_BLENDER_EDITOR
# File Name            	 	: WYModel.py
# Project Headquarter   	: https://docs.google.com/document/d/1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit#
# Test Plan Headquarter 	: https://docs.google.com/document/d/1wlFujpygsVKtqiz596ZdD1sCeUPkpIgr1lNlE_GN-_w/edit#
# WYModel test plan     	: https://docs.google.com/document/d/1gaYXdG1hQ6rHOKWyzQ3sJnO06rsvamHcDFOCZWibNAE/edit#
# Lead Programmer       	: Samil Chai
# Junior Programmer     	: Nick Jang
# Time                  	: 
# Description           	: 
#
################################################################################

import os 
filename = os.getcwd() + "\\..\\..\\main\\WYMesh\\WYMesh.py" 
exec(compile(open(filename).read(), filename, 'exec')) # Import WYMesh.py
filename = os.getcwd() + "\\..\\..\\main\\WYMaterial\\WYMaterial.py"
exec(compile(open(filename).read(), filename, 'exec')) # Import WYMaterial.py

class WYModel:  
    '''
    This class holds all the properties to represent a single model object
    which contains a singel WYMesh object and a single WYMaterial object and
    the functions to support exporting them to files through WYModelManager.

    .. seealso:: ../WYModelManager/WYModelManager.py
    .. seealso:: ../WYMesh/WYMesh.py
    .. seealso:: ../WYMaterial/WYMaterial.py

    ----------------------------------------------------------------------------
    Member variables:
    ----------------------------------------------------------------------------
    :Memeber variable main_wymesh       : Main WYmesh object to hold the mesh related data into one.
    :Memeber variable main_wymaterial   : Main WYMaterial object to hold the material related data into one.
    
    ----------------------------------------------------------------------------
    Member functions:
    ----------------------------------------------------------------------------
    # def __init__(self, main_wymesh=None, main_wymaterial=None):
        Test: https://docs.google.com/spreadsheets/d/1B6edfrxpzn_oXxhV3dAVun_cgMUPRsaBcX4dPffh8ac/edit#gid=0
    # def __eq__(self, other):
        Test: https://docs.google.com/spreadsheets/d/1SPQHJ1684O1vFP6XdlOILjU3xLN7tfs98bmQNvx6OAw/edit#gid=0
    # def get_mesh_export_str(self):
        Test: https://docs.google.com/spreadsheets/d/1FLxfsMeQ-rSrX1joaVQP0CAxsJuS7fnFm_56AdT3_HY/edit#gid=0
    # def get_material_export_str(self):
        Test: https://docs.google.com/spreadsheets/d/1EI-tCU7J9dH4O0BvOLQ9QWwv6cpEH8GHKugufk8defs/edit#gid=0

    '''
    #---------------------------------------------------------------------------
    # Default constructor.
    #---------------------------------------------------------------------------
    def __init__(self, main_wymesh=None, main_wymaterial=None):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModel general constructor.
            
        Initializes the memeber variable "main_wymesh" and "main_wymaterial"
        with the WYMesh object and WYMaterial object passed in as the 
        arguments.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  main_wymesh: Main WYmesh object to hold the mesh related data 
                             into one.
        :type   main_wymesh: WYMesh
        :param  main_wymaterial: Main WYMaterial object to hold the material 
                             related data into one.
        :type   main_wymaterial: WYMaterial

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Returns the initialized WYModel object.
        :rtype: WYModel

        '''
        #if main_wymesh == None:
        #   raise Exception("ERROR::WYModel::__init__::WYMesh object is None!!!")

        # Main WYMesh object where all the mesh information data are stored in.
        self.main_wymesh = main_wymesh
        # Main WYMaterial object where all the material information data are 
        # stored in.
        self.main_wymaterial = main_wymaterial

    #---------------------------------------------------------------------------
    # Overriden equal function.
    #---------------------------------------------------------------------------
    def __eq__(self, other):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModel overrided equal function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Compares the member variables with the memeber variables intialized 
        in "other" object return True if these 2 object has all the member 
        variables same values else return False.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  other: Second WYModel object to compare with.
        :type   other: WYModel
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Return the result of comparison between 2 objects.
        :rtype: boolean

        '''
        if other == None:
            return False
        return (self.main_wymesh == other.main_wymesh and \
                self.main_wymaterial == other.main_wymaterial)
    
    #---------------------------------------------------------------------------
    # Get mesh final export string function.
    #---------------------------------------------------------------------------
    def get_mesh_export_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModel member function to retrieve the final mesh export data string
        from initialized WYMesh object as member variable "main_wymesh"
            
        Called by funciton WYModelManager::export_model()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function returns the final mesh export string by calling the WYMesh
        object's toString function if exist, then exports the WYMesh object onto 
        files.

        Raise exception if the WYMesh object initialized on this WYModel object
        not exist.

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Returns the string of WYMesh object.
        :rtype: string

        '''
        # Return mesh string.
        if self.main_wymesh != None:
            return "" + str(self.main_wymesh)
        # Print error message.
        else:
            raise Exception("ERROR::WYModel::get_mesh_export_str::No mesh availiable!!!")

    #---------------------------------------------------------------------------
    # Get mesh final export string function.
    #---------------------------------------------------------------------------
    def get_material_export_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModel member function to retrieve the final material export data 
        string from initialized WYMaterial object as member variable 
        "main_wymaterialh"
            
        Called by funciton WYModelManager::export_model()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function returns the final material export string by calling the 
        WYMaterial object's toString function if exist, then exports the 
        WYMaterial object onto files.

        Raise exception if the WYMaterial object initialized on this WYModel 
        object not exist.

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Returns the string of WYMaterial object.
        :rtype: string

        '''
        # Return material string.
        if self.main_wymaterial != None:
            return "" + str(self.main_wymaterial)
        # Print error message.
        else:
            raise Exception("ERROR::WYModel::get_material_export_str::No material availiable!!!")



        
