################################################################################
# Project Name          	: WY_PROJ_BLENDER_EDITOR
# File Name             	: WYAnimationBone.py
# Project Headquarter   	: https://docs.google.com/document/d/1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit#
# Test Plan Headquarter 	: https://docs.google.com/document/d/1wlFujpygsVKtqiz596ZdD1sCeUPkpIgr1lNlE_GN-_w/edit#
# WYAnimationBone test plan : https://docs.google.com/document/d/1iUkgLkjyxa52i-9jh0NDOs3TTxDT3LT5FCfbrvyOYX0/edit#
# Lead Programmer       	: Samil Chai
# Junior Programmer     	: Nick Jang
# Time                  	: 
# Description           	: 
################################################################################

import bpy

filename = os.getcwd() + "\\..\\..\\main\\WYAnimationBoneKeyframe\\WYAnimationBoneKeyframe.py" 
exec(compile(open(filename).read(), filename, 'exec')) # Import WYAnimationBoneKeyframe.py

class WYAnimationBone:
    '''
    This class represents the animation bone object which contains the 
    data values to export a Blender pose bone object to file.
    
    WYAnimationBone contans all the animation bone related data which can 
    animate the Blender API Armature bone object through keyframe animation 
    using the data assigned WYAnimationBone object, it holds data 
    such as bone name, parent bone name and animation keyframes as array of 
    WYAnimationBoneKeyframe objects. 

    .. seealso:: ../WYAnimationBoneKeyframe/WYAnimationBoneKeyframe.py

    ----------------------------------------------------------------------------
    Member variables:
    ----------------------------------------------------------------------------
    :Memeber variable main_animation_bone_obj       : Blender armature pose bone object to retrieve data from.
    :Memeber variable main_armature_bone_obj        : Blender armature data bone object which current animation bone keyframe is mapped onto.
    :Memeber variable parent_armature_bone_obj     : Blender parent armature pose bone object.
    :Memeber variable animation_bone_name           : abn - Name of the Blender armature pose bone object initalized as member variable "main_animation_bone_obj"
    :Memeber variable animation_bone_parent_name    : apbn - Name of the Blender parent armature pose bone object initalized as member variable "parent_armature_bone_obj"
    :Memeber variable animation_bone_keyframe_arr   : kf - Array of WYAnimationBoneKeyframe objects to hold the animation keyframe data to animate the armature object.

    ----------------------------------------------------------------------------
    Member functions:
    ----------------------------------------------------------------------------
    # def __init__(self, main_animation_bone_obj=None, main_armature_bone_obj=None):
        Test: https://docs.google.com/spreadsheets/d/1Evr5szRkRrGS_CsO_QfVgdMvokKgk6EIs8Mpo-ZV7D4/edit#gid=0
    # def __eq__(self, other):
        Test: https://docs.google.com/spreadsheets/d/1tM5hJOL_N-idAqyFeGPV9TXJo4CicHV05ojmUxXIrNU/edit#gid=0
    # def __str__(self):
        Test: https://docs.google.com/spreadsheets/d/1nVYC0AHZQVhokETaYR9mhURDwV2uH8QRDQzmnDetxNY/edit#gid=0
    # def init_animation_bone_data(self, start_index, end_index):
        Test: https://docs.google.com/spreadsheets/d/19xo7frxkGlmwR9R3JatjE6TGCLgEd2Uy9ebB40Ssk0Y/edit#gid=0
    # def init_wyanimationbone_elements(self):
        Test: https://docs.google.com/spreadsheets/d/1Dn80q78w7BpQeD88HWKorpVMOUM3jFTgKaXrYWCLkhA/edit#gid=0
    # def init_animation_bone_name(self):
        Test: https://docs.google.com/spreadsheets/d/1zzW1SvoMP17Qj4WVPcbzbuAFUzHZzc5YhtMPV-MPaKk/edit#gid=0
    # def init_animation_bone_parent_name(self)
        Test: https://docs.google.com/spreadsheets/d/1oJZ336DowM3uESYjphdnihghrfDU4wYR6Af1t42x6Ps/edit#gid=0
    # def init_animation_bone_keyframe_arr_data(self, start_index, end_index):
        Test: https://docs.google.com/spreadsheets/d/19DqZR5CVFjswBro5Uf_365IcsAeGs9m24sYZxi5u1Qo/edit#gid=0
    # def get_animation_bone_abn_str(self):
        Test: https://docs.google.com/spreadsheets/d/1I65IT7mTVBcA2HQLfjlHpJ4c17Hi19yevhIfH-rppuU/edit#gid=0
    # def get_animation_bone_apbn_str(self):
        Test:https://docs.google.com/spreadsheets/d/1yoIDh7e3EfGAm1SNXcwIRaGjinLUP6X97QSDRqTncsY/edit#gid=0
    # def get_animation_bone_kf_str(self):
        Test: https://docs.google.com/spreadsheets/d/1KqJYRbGf7ICCDor9rsgLcvt7GaDRlMW_D6ZlFiKdtCg/edit#gid=0

    '''
    def __init__(self, 
                 main_animation_bone_obj=None, 
                 main_armature_bone_obj=None):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBone general constructor.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Initialize the member variables using the values passed into the 
        allocation call.

        Initializing member varibles:
            :Memeber variable main_animation_bone_obj       : Blender animation pose bone object to retrieve data from.
            :Memeber variable main_armature_bone_obj        : Blender armature data bone object which current animation bone keyframe is mapped onto.
            :Memeber variable parent_armature_bone_obj      : Blender parent armautre data bone object.

        Calling sub function: init_wyanimationbone_elements()

        Sub function: init_wyanimationbone_elements()
            This function initializes the member variable with default values 
            which will be holding the major information data values:
                :Memeber variable animation_bone_name           : abn - Name of the Blender animation pose bone object initalized as member variable "main_animation_bone_obj".
                :Memeber variable animation_bone_parent_name    : apbn - Name of the Blender parent armature pose bone object initalized as member variable "parent_armature_bone_obj".
                :Memeber variable animation_bone_keyframe_arr   : kf - Array of WYAnimationBoneKeyframe objects to hold the animation keyframe data to animate the armature object.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param main_armature_bone_obj: Referenced Blender Mesh object to retrieve the mesh data values from.
        :type  main_armature_bone_obj: bpy.ArmatureBone
        :param main_wymodel_obj: Referenced WYModel object to retrieve the mesh and material data values from.
        :type  main_wymodel_obj: WYModel
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return : Allocated and initialized WYMesh object.
        :rtype  : WYMesh.
        '''
        # Blender animation pose bone object to retrieve data from.
        self.main_animation_bone_obj = main_animation_bone_obj
        # Blender armature data bone object which current animation bone 
        # keyframe is mapped onto.
        self.main_armature_bone_obj = main_armature_bone_obj

        # Blender parent armautre data bone object.
        if self.main_armature_bone_obj != None:
            if self.main_armature_bone_obj.parent != None:
                self.parent_armature_bone_obj = \
                    self.main_armature_bone_obj.parent
            else:
                self.parent_armature_bone_obj = None
        else:
            self.parent_armature_bone_obj = None

        # Call sub function to intialize the main animation bone  
        # important elements with default values.
        self.init_wyanimationbone_elements()

    def __eq__(self, other):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBone overrided equal function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Compares the member variables with the memeber variables intialized 
        in "other" object return True if these 2 object has all the member 
        variables same values else return False.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  other: Second WYAnimationBone object to compare with.
        :type   other: WYAnimationBone
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Return the result of comparison between 2 objects.
        :rtype: boolean

        '''
        if other == None:
            return False
        return (self.main_animation_bone_obj ==
                    other.main_animation_bone_obj and \
                self.main_armature_bone_obj ==
                    other.main_armature_bone_obj and \
                self.animation_bone_name ==
                    other.animation_bone_name and \
                self.animation_bone_parent_name ==
                    other.animation_bone_parent_name  and \
                self.animation_bone_keyframe_arr ==
                    other.animation_bone_keyframe_arr)

    def __str__(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBone toString function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Manipulate the string to represent the current WYAnimationBone
        object in the file using the values initialized onto the object.

        This function acts like toString function in Java so when I print the 
        WYAnimationBone object directly, so when 
        WYAnimationBone is exported WYAnimationBone wil be 
        printed directly through file stream and the information about this 
        WYAnimationBone object will be printed to file with following 
        sample format:
            --------------------------------------------------------------------
            abn ""
            apbn ""
            kf 0 {
                abh 0.0 0.0 0.0
                abt 0.0 0.0 0.0
                loc 0.0 0.0 0.0
                rotq 0.0 0.0 0.0 0.0
                sca 0.0 0.0 0.0
            }
            --------------------------------------------------------------------

        This string is manipulated with following member variables initialized 
        onto this WYAnimationBone object:
                :Memeber variable animation_bone_name           : abn - Name of the Blender animation pose bone object initalized as member variable "main_animation_bone_obj".
                :Memeber variable animation_bone_parent_name    : apbn - Name of the Blender parent armautre data bone object initalized as member variable "parent_armature_bone_obj".
                :Memeber variable animation_bone_keyframe_arr   : kf - Array of WYAnimationBoneKeyframe objects to hold the animation keyframe data to animate the armature object.

        Calling sub function: get_animation_bone_abn_str()
            Generate string: abn     ""
        Calling sub function: get_animation_bone_apbn_str()
            Generate string: apbn    ""
        Calling sub function: get_animation_bone_kf_str()
            Generate string: kf 0 {}

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Final string representing this WYAnimationBone 
                           object to be exported to files.
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += self.get_animation_bone_abn_str()
        final_str += self.get_animation_bone_apbn_str()
        final_str += self.get_animation_bone_kf_str()
        return final_str

    def init_animation_bone_data(self, start_index, end_index):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBone member function initializes the Blender armature bone 
        object data values into WYAnimationBone member variables.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the following member variables with the actual
        Blender armature bone object data values by calling multiple 
        sub functions:
        Calling sub function: WYAnimationBone::init_animation_bone_name()
            :Memeber variable animation_bone_name           : abn - Name of the Blender armature pose bone object initalized as member variable "main_animation_bone_obj".
        Calling sub function: WYAnimationBone::init_animation_bone_parent_name()
            :Memeber variable animation_bone_parent_name    : apbn - Name of the Blender parent armature pose bone object initalized as member variable "parent_armature_bone_obj".
        Calling sub function: WYAnimationBone::init_animation_bone_keyframe_arr_data()
            :Memeber variable animation_bone_keyframe_arr   : kf - Array of WYAnimationBoneKeyframe objects to hold the animation keyframe data to animate the armature object.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  start_index: Start index of the keyframe animation.
        :type   start_index: int.
        :param  end_index: End index of the keyframe animation.
        :type   end_index: int.
        '''
        # abn - Name of the Blender armature pose bone object.
        self.init_animation_bone_name()
        # apbn - Name of the Blender parent armature pose bone object.
        self.init_animation_bone_parent_name()
        # kf - Array of WYAnimationBoneKeyframe objects to hold the animation
        # keyframe data to animate the armature object.
        self.init_animation_bone_keyframe_arr_data(start_index, end_index)

    def init_wyanimationbone_elements(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBone member function initializes the member variables 
        with default values when allocated.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variables with default values
                :Memeber variable animation_bone_name           : ""
                :Memeber variable animation_bone_parent_name    : ""
                :Memeber variable animation_bone_keyframe_arr   : []

        '''
        # abn - Name of the Blender armature pose bone object."
        self.animation_bone_name = ""
        # apbn - Name of the Blender armature parent pose bone object."
        self.animation_bone_parent_name = ""
        # kf - Array of WYAnimationBoneKeyframe objects to hold the animation 
        # keyframe data to animate the armature object.
        self.animation_bone_keyframe_arr = []

    def init_animation_bone_name(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBone sub member function initializes the Blender 
        animation pose bone object name value into WYAnimationBone 
        member variable "armature_bone_name".

        :Post-condition: 
            Member variable "animation_bone_name" is initialized with the
            name value using the data inside animation pose bone object 
            initialized as member variable "main_animation_bone_obj".
            
            :Memeber variable animation_bone_name           : abn - Name of the Blender animation pose bone object initalized as member variable "main_animation_bone_obj".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "animation_bone_name" with 
        the actual Blender animation pose bone object name value by 
        retreiving the "name" value initialized inside member variable 
        "main_animation_bone_obj".
            :Memeber variable main_animation_bone_obj       : Blender animation pose bone object to retrieve data from.
        '''
        # abn - Name of the Blender armature pose bone object.
        if self.main_animation_bone_obj != None:
            self.animation_bone_name = self.main_animation_bone_obj.name

    def init_animation_bone_parent_name(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBone sub member function initializes the Blender animation 
        pose bone object parent pose bone name value into WYAnimationBone member 
        variable "animation_bone_parent_name".

        :Post-condition: 
            Member variable "animation_bone_parent_name" is initialized with the
            parent pose bone name value using the data inside armature pose 
            bone object initialized as member variable 
            "parent_armature_bone_obj".
            
            :Memeber variable animation_bone_parent_name    : apbn - Name of the Blender parent armature pose bone object initalized as member variable "parent_armature_bone_obj".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable 
        "animation_bone_parent_name" with the actual Blender animation pose bone 
        object parent data bone name value by retreiving the "name" value 
        initialized inside member variable "parent_armature_bone_obj".
            :Memeber variable parent_armature_bone_obj     : Blender parent armautre data bone object.
        '''
        # pbn - Armature bone parent name.
        if self.parent_armature_bone_obj != None:
            self.animation_bone_parent_name = self.parent_armature_bone_obj.name

    def init_animation_bone_keyframe_arr_data(self, start_index, end_index):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBone sub member function initializes the Blender animation 
        pose bone object animation keyframe data value into WYAnimationBone 
        member variable "animation_bone_keyframe_arr" as array of 
        WYAnimationBoneKeyframe object.

        :Post-condition: 
            Member variable "armature_bone_head" is initialized with the
            head coordinate value using the data inside armature bone object 
            initialized as member variable "main_armature_bone_obj".

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable 
        "animation_bone_keyframe_arr" with the actual Blender animation pose 
        bone object's keyframe animation value by retreiving the "location", 
        "rotation_quaternion" and "scale" value initialized inside 
        member variable "main_animation_bone_obj" creates 
        WYAnimationBoneKeyframe objects for each keyframe data exists and store
        them into the member variable "animation_bone_keyframe_arr".
            :Memeber variable main_animation_bone_obj       : Blender animation pose bone object to retrieve data from.
            :Memeber variable animation_bone_keyframe_arr   : kf - Array of WYAnimationBoneKeyframe objects to hold the animation keyframe data to animate the armature object.
        
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  start_index: Start index of the keyframe animation.
        :type   start_index: int.
        :param  end_index: End index of the keyframe animation.
        :type   end_index: int.

        '''
        # bpy.context.scene.frame_start
        for i in range(start_index, end_index):
            # Update scene keyframe to get each keyframe data values.
            bpy.context.scene.frame_set(i)

            # Create WYAnimationBoneKeyframe object to append with.
            wyanimationbonekeyframe = WYAnimationBoneKeyframe(
                self.main_animation_bone_obj, self.main_armature_bone_obj)
            # Initialize WYAnimationBoneKeyframe data.
            wyanimationbonekeyframe.init_animation_bone_keyframe_data()
            # Append initialized WYAnimationBoneKeyframe data to member 
            # variable data structure.
            self.animation_bone_keyframe_arr.append(wyanimationbonekeyframe)

            #print(str(wyanimationbonekeyframe))

            # Refresh temp object.
            wyanimationbonekeyframe = None

    def get_animation_bone_abn_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBone sub member function generates the name of the animation 
        pose bone object into strings to be exported to file.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the name of the animation 
        pose bone object intialized in this WYAnimationBone object.
            :Memeber variable main_animation_bone_obj       : Blender animation pose bone object to retrieve data from.
            :Memeber variable animation_bone_name           : abn - Name of the Blender animation pose bone object initalized as member variable "main_animation_bone_obj".
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the name of the animation 
                           pose bone object onto file in format "abn [Name]\\n"
                           Example: "abn posebone\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        if self.animation_bone_name != "":
            final_str += "abn "
            final_str += self.animation_bone_name + '\n'
        return final_str

    def get_animation_bone_apbn_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBone sub member function generates the name of the animation 
        pose bone parent bone object into strings to be exported to file.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the name of the parent 
        animation pose bone object intialized in this WYAnimationBone object.
            :Memeber variable parent_armature_bone_obj     : Blender parent armautre data bone object.
            :Memeber variable animation_bone_parent_name    : apbn - Name of the Blender parent armature pose bone object initalized as member variable "parent_armature_bone_obj".
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the name of the parent 
                           animation pose bone object onto file in format 
                           "apbn [Name]\\n"
                           Example: "apbn poseboneparent\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        if self.parent_armature_bone_obj != None and \
           self.animation_bone_parent_name != "":
            final_str += "apbn "
            final_str += self.animation_bone_parent_name + '\n'
        return final_str

    def get_animation_bone_kf_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBone sub member function generates the keyframe animation  
        data values stored in the animation pose bone object into strings 
        to be exported to file.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the keyframe animation  
        data values stored in the animation pose bone object intialized in this 
        WYAnimationBone object.
            :Memeber variable main_animation_bone_obj       : Blender animation pose bone object to retrieve data from.
            :Memeber variable animation_bone_keyframe_arr   : kf - Array of WYAnimationBoneKeyframe objects to hold the animation keyframe data to animate the armature object.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the keyframe animation 
                           data values of the animation pose bone object onto 
                           file in WYAnimationBoneKeyframe format.
                           Example: "kf 0 {
                                     abh 0.0 0.0 0.0
                                     abt 0.0 0.0 0.0
                                     loc 0.0 0.0 0.0
                                     rotq 0.0 0.0 0.0 0.0
                                     sca 0.0 0.0 0.0
                                     ...
                                     }"
        :rtype  final_str: string
        '''
        final_str = ""
        if self.animation_bone_keyframe_arr != []:
            for i in range(0, len(self.animation_bone_keyframe_arr)):
                final_str += "kf " + str(i) + " {\n"
                final_str += str(self.animation_bone_keyframe_arr[i])
                final_str += "}\n"
        return final_str

    
    
    
