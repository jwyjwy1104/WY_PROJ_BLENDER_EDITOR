################################################################################
# Project Name          	: WY_PROJ_BLENDER_EDITOR
# File Name             	: WYArmature.py
# Project Headquarter   	: https://docs.google.com/document/d/1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit#
# Test Plan Headquarter 	: https://docs.google.com/document/d/1wlFujpygsVKtqiz596ZdD1sCeUPkpIgr1lNlE_GN-_w/edit#
# WYArmature test plan  	: https://docs.google.com/document/d/18sDPMZOZk7k_DTkvAK56wIlaXUK0hrXJUFer7ybM7w4/edit#
# Lead Programmer       	: Samil Chai
# Junior Programmer     	: Nick Jang
# Time                  	: 
# Description           	: 
################################################################################

import bpy
import bmesh
import os
import sys
import struct
import math
from bpy import context

filename = os.getcwd() + "\\..\\..\\main\\WYArmatureBone\\WYArmatureBone.py" 
exec(compile(open(filename).read(), filename, 'exec')) # Import WYArmatureBone.py

class WYArmature:
    '''
    This class represents the armature object which contains the 
    data values to export a Blender armature object to file.
    
    WYArmature contans all the armature related data which are kept 
    by the Blender API Armature object, it holds data such as array of 
    WYArmatureBone and corresponding mapped on WYMesh object. 

    .. seealso:: ../WYArmatureBone/WYArmatureBone.py
    .. seealso:: ../WYMesh/WYMesh.py        

    ----------------------------------------------------------------------------
    Member variables:
    ----------------------------------------------------------------------------
    :Memeber variable main_wymodel_obj              : WYModel object which contains the mesh object that is mapped onto the armature.
    :Memeber variable main_armature_obj             : Blender armature object to retrieve data from.
    :Memeber variable armature_model_relfile_path   : mdllib        - Relative custom model file path if model object exist inside current armature object to be export with.
    :Memeber variable armature_name                 : an            - Name of the Blender armature object initalized as member variable "main_armature_obj"
    :Memeber variable armature_bones_arr            : bn,bt,bh,vg   - Array of WYArmatureBone objects to represent the armature bone objects.
    :Memeber variable num_armature_bones            : bc            - Size of the WYArmatureBone array initialize as member variabel "armature_bones_arr".
    :Memeber variable wycoordsys                    : CU,CF         - WYCoordsys object for coordinate conversion.
            
    ----------------------------------------------------------------------------
    Member functions:
    ----------------------------------------------------------------------------
    # def __init__(self, main_armature_obj=None, main_wymodel_obj=None, wycoordsys=None):
        Test: https://docs.google.com/spreadsheets/d/1MiAcCRWtAKITO0tm7pKn6G4BK6NDzNiQii1iMd-hfx8/edit#gid=0
    # def __eq__(self, other):
        Test: https://docs.google.com/spreadsheets/d/1kAtOhmvu98mD7TiUrRy-w9pMIQ-Rt8TlN2PmWrWDOgo/edit#gid=0
    # def __str__(self):
        Test: https://docs.google.com/spreadsheets/d/174uX6l_fOWWv5soRMHriS8VOkojVRpnp6o9bw3Nkj48/edit#gid=0
    # def init_armature_data(self):
        Test: https://docs.google.com/spreadsheets/d/1DmSdjMtm3QyNMiQiuuhKM_7bLPigjxlSpAOJdcQ79as/edit#gid=0
    # def init_wyarmature_elements(self):
        Test: https://docs.google.com/spreadsheets/d/1N2vJ2eguUNoHJ_lZeFMSagqpznPxQxvK0dy3g_5IY0s/edit#gid=0
    # def init_armature_model_relfile_path(self, armature_model_relfile_path):
        Test: https://docs.google.com/spreadsheets/d/1SnJ5P0u3mfEWuFZi8-r1Sw9BSQbFD4pCbEB-dNXZ29I/edit#gid=0
    # def init_armature_name(self):
        Test: https://docs.google.com/spreadsheets/d/1j_0Bb6v08GwHndVXvH0H9hoCP_QVW8JAz23_9CF2JLQ/edit#gid=0
    # def init_num_armature_bones_data(self):
        Test: https://docs.google.com/spreadsheets/d/18ZIAqIe-XNVwOsrJamaUTLla_mcjqEsFJAAMdbPB-AU/edit#gid=0
    # def init_armature_bones_arr_data(self):
        Test: https://docs.google.com/spreadsheets/d/1jL3hlSc1ngeVvukDHE0F3q43Ms7QkuKrn2AxjO7BHXI/edit#gid=0
    # def get_armature_an_str(self):
        Test: https://docs.google.com/spreadsheets/d/1EL0eoTF1CsUc72wNqHdIXY4eP6uKQlUwkbPbxQVDFZM/edit#gid=0 
    # def get_armature_mdllib_str(self):
        Test: https://docs.google.com/spreadsheets/d/1XEkJjPkHlFYKQnajLX_rOnbBBOIp2YL2Wri-K7BLFXg/edit#gid=0
    # def get_armature_bc_str(self):
        Test: https://docs.google.com/spreadsheets/d/1Tjeg2R777EJQeLVBwQE6wwx2PeAKDhcv_mW05LEzO4o/edit#gid=0
    # def get_armature_bones_arr_str(self):
        Test: https://docs.google.com/spreadsheets/d/1Z0LKluFQm49hXg7yUn_3VfbN_qiAkkRjgembplmS64g/edit#gid=0

    '''
    def __init__(self, main_armature_obj=None, main_wymodel_obj=None, wycoordsys=None):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmature general constructor.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        General constructor to allocate the WYArmature object with data values
        passed into the constructor.

        Initializing member variables:
            :Memeber variable main_wymodel_obj              : WYModel object which contains the mesh object that is mapped onto the armature.
            :Memeber variable main_armature_obj             : Blender armature object to retrieve data from.
            :Memeber variable wycoordsys                    : CU,CF         - WYCoordsys object for coordinate conversion.

        Calling sub function: init_wyarmature_elements()
        Sub function: init_wyarmature_elements()
            This function initializes the data structure which holds the major
            information data values such as:

            :Memeber variable armature_name                 : an            - Name of the Blender armature object initalized as member variable "main_armature_obj"
            :Memeber variable armature_bones_arr            : bn,bt,bh,vg   - Array of WYArmatureBone objects to represent the armature bone objects.
            :Memeber variable num_armature_bones            : bc            - Size of the WYArmatureBone array initialize as member variabel "armature_bones_arr".
            :Memeber variable armature_model_relfile_path   : mdllib        - Relative custom model file path if model object exist inside current armature object to be export with.

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return : Allocated and initialized WYArmature object.
        :rtype  : WYArmature.
        '''

        # WYModel object that this armature is mapped onto.
        self.main_wymodel_obj = main_wymodel_obj

        # Current Blender armature object.
        if main_armature_obj != None: 
            if main_armature_obj.type == 'ARMATURE':
                self.main_armature_obj = main_armature_obj

        # CU - Chosen export option UP vector.
        # CF - Chosen export option FORWARD vector.
        if self.main_wymodel_obj != None:
            if self.main_wymodel_obj.main_wymesh != None:
                if self.main_wymodel_obj.main_wymesh.wycoordsys != None:
                    self.wycoordsys = self.main_wymodel_obj.main_wymesh.wycoordsys
                else:
                    self.wycoordsys = wycoordsys
            else:
                    self.wycoordsys = wycoordsys
        else:
            self.wycoordsys = wycoordsys

        # Call sub function to intialize the main armature elements with 
        # default values to hold the armature data with.

        self.init_wyarmature_elements()

    #---------------------------------------------------------------------------
    # Overriden equal function.
    #---------------------------------------------------------------------------
    def __eq__(self, other):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmature overrided equal function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Compares the member variables with the memeber variables intialized 
        in "other" object return True if these 2 object has all the member 
        variables same values else return False.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  other: Second WYArmature object to compare with.
        :type   other: WYArmature 
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Return the result of comparison between 2 objects.
        :rtype: boolean
        '''
        if other == None:
            return False
        '''
        print(self.main_wymodel_obj == other.main_wymodel_obj)
        print(self.main_armature_obj == other.main_armature_obj)
        print(self.wycoordsys == other.wycoordsys)
        print(self.armature_name == other.armature_name)
        print(self.armature_bones_arr == other.armature_bones_arr)
        print(self.num_armature_bones == other.num_armature_bones)
        '''
        return (self.main_wymodel_obj == other.main_wymodel_obj and \
                self.main_armature_obj == other.main_armature_obj and \
                self.wycoordsys == other.wycoordsys and \
                self.armature_name == other.armature_name and \
                self.armature_bones_arr == other.armature_bones_arr and \
                self.num_armature_bones == other.num_armature_bones)


    def __str__(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmature toString function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Manipulate the string to represent the current WYArmature object in the 
        file using the values initialized when allocated.

        This function acts like toString function in Java so when I print the 
        WYArmature object directly, so when WYArmature is exported WYArmature 
        directly through file stream and the information about this WYArmature 
        wil be printed object will be printed to file with following 
        sample format:
             -------------------------------------------------------------------
             an Armature
             cmn Cube
             bc 2
             CU Z
             CF Y
             bn ""
             bt 0.0 0.0 0.0
             bh 0.0 0.0 0.0
             vg {
             vi 0
             v 0.0 0.0 0.0
             vw 0.0000
             }
             bn ""
             pbn ""
             bt 0.0 0.0 0.0
             bh 0.0 0.0 0.0
             vg {
             vi 0
             v 0.0 0.0 0.0
             vw 0.0000
             }
             -------------------------------------------------------------------

        This string is manipulated with following member variables initialized 
        onto this WYArmature object:
            :Memeber variable main_wymodel_obj              : WYModel object which contains the mesh object that is mapped onto the armature.
            :Memeber variable main_armature_obj             : Blender armature object to retrieve data from.
            :Memeber variable armature_name                 : Name of the Blender armature object initalized as member variable "main_armature_obj"
            :Memeber variable armature_bones_arr            : Array of WYArmatureBone objects to represent the armature bone objects.
            :Memeber variable num_armature_bones            : Size of the WYArmatureBone array initialize as member variabel "armature_bones_arr".

        Calling sub function: get_armature_an_str()
            Generate string: an      ""
        Calling sub function: get_armature_mdllib_str()
            Generate string: mdllib     ""
        Calling sub function: get_armature_bc_str()
            Generate string: bc      0
        Calling sub function: get_armature_bones_arr_str()
            Generate string: 
                bn "" 
                pbn "" 
                bt 0 0 0
                bh 0 0 0
                vg {
                vi 0
                v 0 0 0
                vw 0
                }

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Final string representing this WYArmature object to 
                           be exported to files.
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += self.get_armature_an_str()
        final_str += self.get_armature_mdllib_str()
        final_str += self.get_armature_bc_str()
        if self.wycoordsys != None:
            final_str += str(self.wycoordsys)
        final_str += self.get_armature_bones_arr_str()
        
        return final_str
    
    def init_armature_data(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmature member function initializes the Blender armature 
        object data values into WYArmature member variables.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the following member variables with the actual
        Blender armature object data values by calling multiple sub functions:
        
        Calling sub function: WYArmature::init_armature_name()
            :Memeber variable armature_name                 : an            - Name of the Blender armature object initalized as member variable "main_armature_obj"
        Calling sub function: WYArmature::init_armature_bones_arr_data()
            :Memeber variable armature_bones_arr            : bn,bt,bh,vg   - Array of WYArmatureBone objects to represent the armature bone objects.
        Calling sub function: WYArmature::init_num_armature_bones_data()
            :Memeber variable num_armature_bones            : bc            - Size of the WYArmatureBone array initialize as member variabel "armature_bones_arr".

        '''
        # an - Armature name.
        self.init_armature_name()
        # bn, pbn, bt, bh, vg.
        self.init_armature_bones_arr_data()
        # bc - Number of armature bones. 
        # (Must be after init_armature_bones_arr_data())
        self.init_num_armature_bones_data()

    def init_wyarmature_elements(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmature general constructor.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        General constructor to allocate the WYArmature object with data values
        passed into the constructor.

        Initializing member variables:
            :Memeber variable armature_name                 : ""
            :Memeber variable armature_bones_arr            : []
            :Memeber variable num_armature_bones            : 0
            :Memeber variable armature_model_relfile_path   : ""

        '''
        self.armature_name = ""
        self.armature_bones_arr = []
        self.num_armature_bones = 0
        self.armature_model_relfile_path = ""

    def init_armature_name(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmature sub member function initializes the Blender armature object name 
        value into WYArmature member variable "armature_name".

        :Post-condition: 
            Member variable "armature_name" is initialized with the
            name value using the data inside mesh object 
            initialized as member variable "main_armature_obj".

        Called by function: init_armature_data()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "armature_name" with 
        the actual Blender Armature object name value by retrieveing the "name" 
        value inside member variable "main_armature_obj".
            :Memeber variable main_armature_obj             : Blender armature object to retrieve data from.
        '''
        # an - Armature name.
        self.armature_name = self.main_armature_obj.name

    def init_armature_model_relfile_path(self, armature_model_relfile_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmature member function setter for member variable 
        "armature_model_relfile_path".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function is to set the member variable 
        "armature_model_relfile_path" outside of class.
            :Memeber variable armature_model_relfile_path   : mdllib        - Relative custom model file path if model object exist inside current armature object to be export with.
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param armature_model_relfile_path: Relative custom model file path if 
            model object exist inside current armature object to be exported 
            with.
        :type  armature_model_relfile_path: string
        '''
        # mdllib - Mapped on model exported relative file path.
        self.armature_model_relfile_path = armature_model_relfile_path

    def init_num_armature_bones_data(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmature sub member function initializes the number of armature bones
        as WYArmature member variable "num_armature_bones".

        :Pre-condition:
            Member variable "armature_bones_arr" must be initialized with 
            values before calling this function.
            
        :Post-condition: 
            Member variable "num_armature_bones" is initialized with the
            size of the array initialized as member variable 
            "armature_bones_arr".

        Called by function: init_armature_data()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "num_armature_bones" with 
        the data structure initialied with actual Blender armature bones into 
        member variable "armature_bones_arr" and gets the number of armature
        bones using "len()" function.
            :Memeber variable armature_bones_arr            : bn,bt,bh,vg   - Array of WYArmatureBone objects to represent the armature bone objects.
        '''

        # Using len() to calculate the number of armature bones stored inside
        # member variable "armature_bones_arr" and store it to member variable
        # "num_armature_bones"
        if self.armature_bones_arr != []:
            self.num_armature_bones = len(self.armature_bones_arr)
        else:
            self.num_armature_bones = -1

    def init_armature_bones_arr_data(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmature sub member function initializes the armature bones with the 
        armature bones initiailzied inside Blender armature object into
        WYArmatureBone array data structure initialized as WYArmature member 
        variable "armature_bones_arr".

        :Pre-condition:
            Blender armature has armature bones initialized inside.
            
        :Post-condition: 
            Member variable "armature_bones_arr" is initialized with the
            WYArmatuerBone objects initialized with actual Blender armature bone
            object initialized in Blender armature object into array data 
            structure initialized as member variable "armature_bones_arr".

        Called by function: init_armature_data()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "armature_bones_arr" with 
        the actual Blender armature bone objects initialied inside Blender 
        armature object as "bones" value, loop through the armature object
        to create WYArmatureBone object with each armature bone object and 
        append the initialized WYArmatureBone object into the data structure
        member variable "armature_bones_arr".
            :Memeber variable main_armature_obj             : Blender armature object to retrieve data from.
            :Memeber variable armature_bones_arr            : bn,bt,bh,vg   - Array of WYArmatureBone objects to represent the armature bone objects.
        
        Each WYArmatureBone object is initialized with function 
        "WYArmatureBone::init_armature_bone_data()" with information initialized
        inside each Blender armature bone object passed into the constructor
        on each allocation call.

        .. seealso:: ../WYArmatureBone/WYArmatureBone.py        

        '''
        if self.main_armature_obj != None and \
           self.main_armature_obj.type == 'ARMATURE':
            # Get armature object to iterate through to access each bone 
            # objects.
            armature = self.main_armature_obj.data
            
            # Store the data into the global data structure.
            for bone in armature.bones:
                # Create WYArmatureBone object for each armature bones.
                wyarmaturebone = WYArmatureBone(bone, self.main_wymodel_obj)
                wyarmaturebone.init_armature_bone_data()

                # Append the created WYArmatureBone object to the member 
                # variable "armature_bones_arr".
                self.armature_bones_arr.append(wyarmaturebone)

    def get_armature_an_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmature sub member function generates the string to export the 
        armature name value.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the armature name value
        inside current WYArmature object initialied as member variable
        "armature_name".
            :Memeber variable armature_name                 : an            - Name of the Blender armature object initalized as member variable "main_armature_obj"
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the armature name value
            in format "an [Armature name]\\n"
            Example: "an Armature\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        if self.main_armature_obj != None:
            final_str += "an "
            final_str += self.armature_name + '\n'
        return final_str

    def get_armature_mdllib_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmature sub member function generates the string to export the 
        armature mapped on model file path value.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the armature mapped on 
        model export file path value inside current WYArmature object 
        initialied as member variable "armature_model_relfile_path".
            :Memeber variable armature_model_relfile_path   : mdllib        - Relative custom model file path if model object exist inside current armature object to be export with.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the armature mapped on 
            model export file path value in format "mdllib [Model file path]\\n"
            Example: "mdllib C:/Test/Model.txt\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        if self.armature_model_relfile_path != "":
            final_str += "mdllib "
            final_str += self.armature_model_relfile_path + '\n'
                #final_str += self.main_wymodel_obj.main_wymesh.main_mesh_obj.name + '\n'
        return final_str

    def get_armature_bc_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmature sub member function generates the string to export the 
        armature number of armature bones value.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the armature number of 
        armature bones value inside current WYArmature object 
        initialied as member variable "num_armature_bones".
            :Memeber variable num_armature_bones            : bc            - Size of the WYArmatureBone array initialize as member variabel "armature_bones_arr".

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the armature number of 
            armature bones value in format "bc [Armature number of armature bones]\\n"
            Example: "bc 0\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        if self.num_armature_bones > 0:
            final_str += "bc "
            final_str += str(self.num_armature_bones) + '\n'
        return final_str

    def get_armature_bones_arr_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmature sub member function generates the string to export the 
        armature bones data structure values.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the armature bones data 
        structure value inside current WYArmature object initialized as member 
        variable "armature_bones_arr".
            :Memeber variable armature_bones_arr            : bn,bt,bh,vg   - Array of WYArmatureBone objects to represent the armature bone objects.

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the armature bones data 
            structure values in format
            # bn - Armature bone name.
            # pbn - Armature bone parent name.
            # bh - Armature bone head vertex coordinate.
            # bt - Armature bone tail vertex coordinate.
            # vg {
            # v     - Vertex coordinate.
            # vi    - Vertex index.
            # vw    - Vertex weight.
            # }
        Example: "
            bn Bone.001
            pbn Bone
            bt 0.0 0.0 2.5
            bh 0.0 0.0 -0.0
            {
            vi 0
            v -0.5000 -0.5000 3.8000
            vw 1.0000
            vi 1
            v -0.5000 0.5000 3.8000
            vw 1.0000
            }
            "
        :rtype  final_str: string
        '''
        final_str = ""
        # Iterate through the member variable "armature_bones_arr" to generated
        # the export string for all the armature bones inside current armature
        # object.
        for wyarmaturebone in self.armature_bones_arr:
            final_str += str(wyarmaturebone)

        return final_str
    
    
