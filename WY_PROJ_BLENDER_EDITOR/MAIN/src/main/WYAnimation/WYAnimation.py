################################################################################
# Project Name          	: WY_PROJ_BLENDER_EDITOR
# File Name             	: WYArmature.py
# Project Headquarter   	: https://docs.google.com/document/d/1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit#
# Test Plan Headquarter 	: https://docs.google.com/document/d/1wlFujpygsVKtqiz596ZdD1sCeUPkpIgr1lNlE_GN-_w/edit#
# WYAnimation test plan  	: https://docs.google.com/document/d/10Y8hoiDUpM9jJQ7nlgSQ2WEqvQjbXo1-OG-PQjJ81us/edit# 
# Lead Programmer       	: Samil Chai
# Junior Programmer     	: Nick Jang
# Time                  	: 
# Description           	: 
################################################################################

import bpy
import os
import sys
import struct
import math
from bpy import context

filename = os.getcwd() + "\\..\\..\\main\\WYAnimationBone\\WYAnimationBone.py" 
exec(compile(open(filename).read(), filename, 'exec')) # Import WYAnimationBone.py

class WYAnimation:
    '''
    This class represents the animation object which contains the 
    data values to animate Blender armature object on scene.
    
    WYAnimation contans all the animation related data which can animate the 
    Blender API Armature object through keyframe animation, it holds data 
    such as array of WYAnimationBone and corresponding mapped on WYArmature 
    object to animate with. 

    .. seealso:: ../WYAnimationBone/WYAnimationBone.py

    ----------------------------------------------------------------------------
    Member variables:
    ----------------------------------------------------------------------------
    :Memeber variable main_wyarmature_obj               : WYArmature object which contains the armature object that current animation is mapped onto.
    :Memeber variable main_animation_obj                : Blender pose object to retrieve animation data from.
    :Memeber variable animation_armature_relfile_path   : mamlib                        - Relative custom armature exported file path which current animation is mapped onto.
    :Memeber variable animation_name                    : ann                           - Name of the Blender armature object initalized as member variable "main_animation_armature_obj"
    :Memeber variable animation_bones_arr               : abn,abt,abh,loc,rotq,sca      - Array of WYAnimationBone objects to represent the animation bone objects.
    :Memeber variable num_animation_bones               : abc                           - Size of the WYAnimationBone array initialize as member variabel "animation_bones_arr".
    :Memeber variable wycoordsys                        : CU,CF                         - WYCoordsys object for coordinate conversion.
            
    ----------------------------------------------------------------------------
    Member functions:
    ----------------------------------------------------------------------------
    # def __init__(self, main_animation_obj=None, main_wyarmature_obj=None, wycoordsys=None):
        Test: https://docs.google.com/spreadsheets/d/1ucEPzeCD3W4Iuko4ikmgiqG_YhFhEYPdYJhgRw8vtAE/edit#gid=0
    # def __eq__(self, other):
        Test: https://docs.google.com/spreadsheets/d/1aus-bNxwv1vxs25-CwER4dIPmb7_1ivSDQ4gIoCLzMQ/edit#gid=0
    # def __str__(self):
        Test: https://docs.google.com/spreadsheets/d/1lEBjUUyA14xH3vfjQuAFYZzJ3OANIdQbUm9z7vzCcKY/edit#gid=0
    # def init_animation_data(self, start_index, end_index):
        Test: https://docs.google.com/spreadsheets/d/1YKdgOroUv_YZSNqQn67uyqtAqw6vCljBAQ4nddllD4o/edit#gid=0
    # def init_wyanimation_elements(self):
        Test: https://docs.google.com/spreadsheets/d/1aaJqNd1kGnO04d08Exv6zbR5A-v-zcroNb8oB9iLfI4/edit#gid=0
    # def init_animation_armature_relfile_path(self, animation_armature_relfile_path):
        Test: https://docs.google.com/spreadsheets/d/1_3ZfOr9xlzhwAE6ldm8GIH_ui2YGKl4c8p2WArvkkpc/edit#gid=0
    # def init_animation_name(self):
        Test: https://docs.google.com/spreadsheets/d/1mY1a_i46G_byiVNMX07hhiogMXIySntuDefNm3d6lpo/edit#gid=0
    # def init_animation_bones_arr_data(self, start_index, end_index):
        Test: https://docs.google.com/spreadsheets/d/1AftHDjj2eoDmdTmY6Fq_u9-PAmFRV88D4xROnRywyAo/edit#gid=0
    # def init_num_animation_bones_data(self):
        Test: https://docs.google.com/spreadsheets/d/1wdnQWqa2Zj7sw2JMntuN6R__4TPcu0QKQtkF1BLu2c0/edit#gid=0
    # def get_animation_ann_str(self):
        Test: https://docs.google.com/spreadsheets/d/1owti1lzLvbYjw5I6YYGpX6myaX4c7XqlR95BhBAxPqM/edit#gid=0
    # def get_animation_mamlib_str(self):
        Test: https://docs.google.com/spreadsheets/d/12ClmLhRYAPXNBNe0stB9v2DtWrsXpi5cmc81mT6zqeU/edit#gid=0
    # def get_animation_abc_str(self):
        Test: https://docs.google.com/spreadsheets/d/1cSK0BZJvJA1T1f11SGAUuedIeSSlHGff3UkGKzKFGfA/edit#gid=0
    # def get_animation_bones_arr_str(self):
        Test: https://docs.google.com/spreadsheets/d/1tqHYZrYokh1HtrE7vp2tz2lZ-XoVyq5yGpazIeNLbgU/edit#gid=0

    '''
    def __init__(self, 
                 main_animation_obj=None, 
                 main_wyarmature_obj=None, 
                 wycoordsys=None):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimation general constructor.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        General constructor to allocate the WYAnimation object with data values
        passed into the constructor.

        Initializing member variables:
            :Memeber variable main_wyarmature_obj               : WYArmature object which contains the armature object that current animation is mapped onto.
            :Memeber variable main_animation_obj                : Blender pose object to retrieve animation data from.
            :Memeber variable wycoordsys                        : CU,CF                         - WYCoordsys object for coordinate conversion.

        Calling sub function: init_wyarmature_elements()
        Sub function: init_wyarmature_elements()
            This function initializes the data structure which holds the major
            information data values such as:

            :Memeber variable animation_armature_relfile_path   : mamlib                        - Relative custom armature exported file path which current animation is mapped onto.
            :Memeber variable animation_name                    : ann                           - Name of the Blender armature object initalized as member variable "main_animation_armature_obj"
            :Memeber variable animation_bones_arr               : abn,abt,abh,loc,rotq,sca      - Array of WYAnimationBone objects to represent the animation bone objects.
            :Memeber variable num_animation_bones               : abc                           - Size of the WYAnimationBone array initialize as member variabel "animation_bones_arr".

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return : Allocated and initialized WYAnimation object.
        :rtype  : WYAnimation.
        '''

        # WYArmature object which contains the armature object that current 
        # animation is mapped onto.
        self.main_wyarmature_obj = main_wyarmature_obj

        # Blender pose object to retrieve animation data from.
        self.main_animation_obj = main_animation_obj

        # CU - Chosen export option UP vector.
        # CF - Chosen export option FORWARD vector.
        if self.main_wyarmature_obj != None:
            if self.main_wyarmature_obj.wycoordsys != None:
                self.wycoordsys = self.main_wyarmature_obj.wycoordsys
            else:
                self.wycoordsys = wycoordsys
        else:
            self.wycoordsys = wycoordsys

        # Call sub function to intialize the main armature elements with 
        # default values to hold the armature data with.
        self.init_wyanimation_elements()

    def __eq__(self, other):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimation overrided equal function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Compares the member variables with the memeber variables intialized 
        in "other" object return True if these 2 object has all the member 
        variables same values else return False.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  other: Second WYAnimation object to compare with.
        :type   other: WYAnimation 
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Return the result of comparison between 2 objects.
        :rtype: boolean
        '''
        if other == None:
            return False

        print(self.main_wyarmature_obj == other.main_wyarmature_obj)
        print(self.main_animation_obj == other.main_animation_obj)
        print(self.animation_armature_relfile_path == \
                    other.animation_armature_relfile_path)
        print(self.animation_name == other.animation_name)
        print(self.animation_bones_arr == other.animation_bones_arr)
        print(self.num_animation_bones == other.num_animation_bones)
        print(self.wycoordsys == other.wycoordsys)

        return (self.main_wyarmature_obj == other.main_wyarmature_obj and \
                self.main_animation_obj == other.main_animation_obj and \
                self.animation_armature_relfile_path == \
                    other.animation_armature_relfile_path and \
                self.animation_name == other.animation_name and \
                self.animation_bones_arr == other.animation_bones_arr and \
                self.num_animation_bones == other.num_animation_bones and \
                self.wycoordsys == other.wycoordsys)

    def __str__(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimation toString function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Manipulate the string to represent the current WYAnimation object in the 
        file using the values initialized when allocated.

        This function acts like toString function in Java so when I print the 
        WYAnimation object directly, so when WYAnimation is exported WYAnimation 
        directly through file stream and the information about this WYAnimation 
        wil be printed object will be printed to file with following 
        sample format:
             -------------------------------------------------------------------
             ann Animation
             mamlib ""
             abc 2
             CU Z
             CF Y
             abn ""
             apbn ""
             kf 0 {
                 abh 0.0 0.0 0.0
                 abt 0.0 0.0 0.0
                 loc 0.0 0.0 0.0
                 rotq 0.0 0.0 0.0 0.0
                 sca 0.0 0.0 0.0
             }
             abn ""
             apbn ""
             kf 0 {
                 abh 0.0 0.0 0.0
                 abt 0.0 0.0 0.0
                 loc 0.0 0.0 0.0
                 rotq 0.0 0.0 0.0 0.0
                 sca 0.0 0.0 0.0
             }
             -------------------------------------------------------------------

        This string is manipulated with following member variables initialized 
        onto this WYAnimation object:
            :Memeber variable animation_armature_relfile_path   : mamlib                        - Relative custom armature exported file path which current animation is mapped onto.
            :Memeber variable animation_name                    : ann                           - Name of the Blender armature object initalized as member variable "main_animation_armature_obj"
            :Memeber variable animation_bones_arr               : abn,abt,abh,loc,rotq,sca      - Array of WYAnimationBone objects to represent the animation bone objects.
            :Memeber variable num_animation_bones               : abc                           - Size of the WYAnimationBone array initialize as member variabel "animation_bones_arr".
            :Memeber variable wycoordsys                        : CU,CF                         - WYCoordsys object for coordinate conversion.
               
        Calling sub function: get_animation_ann_str()
            Generate string: ann      ""
        Calling sub function: get_animation_mamlib_str()
            Generate string: mamlib   ""
        Calling sub function: get_animation_abc_str()
            Generate string: abc      0
        Calling sub function: get_animation_bones_arr_str()
            Generate string: 
                 abn ""
                 apbn ""
                 kf 0 {
                     abh 0.0 0.0 0.0
                     abt 0.0 0.0 0.0
                     loc 0.0 0.0 0.0
                     rotq 0.0 0.0 0.0 0.0
                     sca 0.0 0.0 0.0
                 }

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Final string representing this WYAnimation object to 
                           be exported to files.
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += self.get_animation_ann_str()
        final_str += self.get_animation_mamlib_str()
        final_str += self.get_animation_abc_str()
        if self.wycoordsys != None:
            final_str += str(self.wycoordsys)
        final_str += self.get_animation_bones_arr_str()
        return final_str
    
    def init_animation_data(self, start_index, end_index):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimation member function initializes the Blender pose 
        object data values into WYAnimation member variables.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  start_index: Start index of the keyframe animation.
        :type   start_index: int.
        :param  end_index: End index of the keyframe animation.
        :type   end_index: int.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the following member variables with the actual
        Blender armature object data values by calling multiple sub functions:
        
        Calling sub function: WYArmature::init_animation_name()
            :Memeber variable animation_name                    : ann                           - Name of the Blender armature object initalized as member variable "main_animation_armature_obj"
        Calling sub function: WYArmature::init_animation_bones_arr_data()
            :Memeber variable animation_bones_arr               : abn,abt,abh,loc,rotq,sca      - Array of WYAnimationBone objects to represent the animation bone objects.
        Calling sub function: WYArmature::init_num_animation_bones_data()
            :Memeber variable num_animation_bones               : abc                           - Size of the WYAnimationBone array initialize as member variabel "animation_bones_arr".

        '''
        # ann - Animation name.
        self.init_animation_name()
        # abn,abt,abh,loc,rotq,sca - Animation per bone data values.
        self.init_animation_bones_arr_data(start_index, end_index)
        # abc - Number of animation pose bones. 
        # (Must be after init_animation_bones_arr_data())
        self.init_num_animation_bones_data()

    def init_wyanimation_elements(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimation general constructor.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        General constructor to allocate the WYAnimation object with data values
        passed into the constructor.

        Initializing member variables:
            :Memeber variable animation_name                    : ""
            :Memeber variable animation_bones_arr               : []
            :Memeber variable num_animation_bones               : 0
            :Memeber variable animation_armature_relfile_path   : ""
        
        '''
        self.animation_name = ""
        self.animation_bones_arr = []
        self.num_animation_bones = 0
        self.animation_armature_relfile_path = ""

    def init_animation_name(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimation sub member function initializes the animation name 
        value into WYAnimation member variable "armature_name".

        :Post-condition: 
            Member variable "animation_name" is initialized with the
            name value using the data inside pose object 
            initialized as member variable "main_animation_obj".

        Called by function: init_animation_data()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "animation_name" with 
        the actual Blender pose object name value by retrieveing the "name" 
        value inside member variable "main_animation_obj".
            :Memeber variable animation_name                    : ann                           - Name of the Blender armature object initalized as member variable "main_animation_armature_obj"
            :Memeber variable main_animation_obj                : Blender pose object to retrieve animation data from.
        '''
        # ann - Animation name.
        # self.animation_name = self.main_animation_obj.name
        if self.main_wyarmature_obj != None:
            self.animation_name = self.main_wyarmature_obj.armature_name

    def init_animation_armature_relfile_path(self, animation_armature_relfile_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimation member function setter for member variable 
        "animation_armature_relfile_path".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function is to set the member variable 
        "animation_armature_relfile_path" outside of class.
            :Memeber variable animation_armature_relfile_path   : mamlib                        - Relative custom armature exported file path which current animation is mapped onto.
        
        Called by function: init_animation_data()
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param animation_armature_relfile_paths: Relative custom armature file 
            path if model object exist inside current armature object to be 
            exported with.
        :type  animation_armature_relfile_path: string
        '''
        # mamlib - Mapped on armature exported relative file path.
        self.animation_armature_relfile_path = animation_armature_relfile_path

    def init_num_animation_bones_data(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimation sub member function initializes the number of animation 
        bonesas WYAnimation member variable "num_animation_bones".

        :Pre-condition:
            Member variable "animation_bones_arr" must be initialized with 
            values before calling this function.
            
        :Post-condition: 
            Member variable "num_animation_bones" is initialized with the
            size of the array initialized as member variable 
            "animation_bones_arr".

        Called by function: init_animation_data()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "num_animation_bones" with 
        the data structure initialized with actual Blender pose bones into 
        member variable "animation_bones_arr" and gets the number of animation
        bones using "len()" function.
            :Memeber variable animation_bones_arr               : abn,abt,abh,loc,rotq,sca      - Array of WYAnimationBone objects to represent the animation bone objects.
            :Memeber variable num_animation_bones               : abc                           - Size of the WYAnimationBone array initialize as member variabel "animation_bones_arr".
        '''

        # Using len() to calculate the number of animation bones stored inside
        # member variable "animation_bones_arr" and store it to member variable
        # "num_animation_bones"
        if self.animation_bones_arr != []:
            self.num_animation_bones = len(self.animation_bones_arr)
        else:
            self.num_animation_bones = -1

    def init_animation_bones_arr_data(self, start_index, end_index):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimation sub member function initializes the animation bones with the 
        animation bones initiailzied inside Blender pose object into
        WYAnimationBone array data structure initialized as WYAnimation member 
        variable "animation_bones_arr".

        :Pre-condition:
            Blender pose object has pose bones initialized inside.
            
        :Post-condition: 
            Member variable "animation_bones_arr" is initialized with the
            WYAnimationBone objects initialized with actual Blender pose bone
            object initialized in Blender pose object into array data 
            structure initialized as member variable "animation_bones_arr".

        Called by function: init_animation_data()

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  start_index: Start index of the keyframe animation.
        :type   start_index: int.
        :param  end_index: End index of the keyframe animation.
        :type   end_index: int.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "animation_bones_arr" with 
        the actual Blender pose bone objects initialized inside Blender 
        pose object as "pose.bones" value, loop through the pose object
        to create WYAnimationBone object with each pose bone object and 
        append the initialized WYAnimationBone object into the data structure
        member variable "animation_bones_arr".
            :Memeber variable animation_bones_arr               : abn,abt,abh,loc,rotq,sca      - Array of WYAnimationBone objects to represent the animation bone objects.
            :Memeber variable main_wyarmature_obj               : WYArmature object which contains the armature object that current animation is mapped onto.
            :Memeber variable main_animation_obj                : Blender pose object to retrieve animation data from.

        Each WYAnimationBone object is initialized with function 
        "WYAnimationBone::init_animation_bone_data()" with information 
        initialized inside each Blender pose bone object passed into the 
        constructor on each allocation call.

        .. seealso:: ../WYAnimationBone/WYAnimationBone.py        

        '''
        if self.main_animation_obj != None and self.main_wyarmature_obj != None:
            if len(self.main_wyarmature_obj.main_armature_obj.data.bones) > 0:
                # Store the data into the global data structure.
                for index, pbone in enumerate(self.main_animation_obj.bones):
                    # Get armature bone.
                    bone = self.main_wyarmature_obj.main_armature_obj.data.bones[index]

                    # Create WYAnimationBone object for each pose bones.
                    wyanimationbone = WYAnimationBone(pbone, bone)
                    # Initialize data with provided start and end index.
                    wyanimationbone.init_animation_bone_data(start_index, end_index)

                    # Append the created WYAnimationBone object to the member 
                    # variable "animation_bones_arr".
                    self.animation_bones_arr.append(wyanimationbone)

    def get_animation_ann_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimation sub member function generates the string to export the 
        animation name value.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the animation name value
        inside current WYAnimation object initialized as member variable
        "animation_name".
            :Memeber variable animation_name                    : ann                           - Name of the Blender armature object initalized as member variable "main_animation_armature_obj"
            :Memeber variable main_animation_obj                : Blender pose object to retrieve animation data from.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the animation name value
            in format "ann [Animation name]\\n"
            Example: "ann Pose\\n"
        :rtype  final_str: string
        '''

        final_str = ""
        if self.animation_name != "":
            final_str += "ann "
            final_str += self.animation_name + '\n'
        return final_str

    def get_animation_mamlib_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimation sub member function generates the string to export the 
        animation mapped on armature file path value.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the animation mapped on 
        armature export file path value inside current WYAnimation object 
        initialized as member variable "animation_armature_relfile_path".
            :Memeber variable animation_armature_relfile_path   : mamlib                        - Relative custom armature exported file path which current animation is mapped onto.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the animation mapped on 
            armature export file path value in format 
            "mamlib [Armature file path]\\n"
            Example: "mamlib C:/Test/Armature.txt\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        if self.animation_armature_relfile_path != "":
            final_str += "mamlib "
            final_str += self.animation_armature_relfile_path + '\n'
                #final_str += self.main_wymodel_obj.main_wymesh.main_mesh_obj.name + '\n'
        return final_str

    def get_animation_abc_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimation sub member function generates the string to export the 
        number of animation bones value.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the number of 
        animation bones value inside current WYAnimation object 
        initialized as member variable "num_animation_bones".
            :Memeber variable num_animation_bones               : abc                           - Size of the WYAnimationBone array initialize as member variabel "animation_bones_arr".

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the number of 
            animation bones value in format 
            "abc [Animation number of animation bones]\\n"
            Example: "abc 0\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        if self.num_animation_bones > 0:
            final_str += "abc "
            final_str += str(self.num_animation_bones) + '\n'
        return final_str

    def get_animation_bones_arr_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimation sub member function generates the string to export the 
        animation bones data structure values.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the animation bones data 
        structure value inside current WYAnimation object initialized as member 
        variable "animation_bones_arr".
            :Memeber variable animation_bones_arr               : abn,abt,abh,loc,rotq,sca      - Array of WYAnimationBone objects to represent the animation bone objects.

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the animation bones data 
            structure values in format
            # abn - Animation bone name.
            # apbn - Animation bone parent name.
            # kf index {
            # abh     - Animation bone local head coordinate.
            # abt     - Animation bone local tail coordinate.
            # loc     - Animation bone animation keyframe location vector.
            # rotq    - Animation bone animation keyframe rotation quaternion.
            # sca     - Animation bone animation keyframe scale vector.
            # }
        Example: "
            abn ""
            apbn ""
            kf 0 {
                abh 0.0 0.0 0.0
                abt 0.0 0.0 0.0
                loc 0.0 0.0 0.0
                rotq 0.0 0.0 0.0 0.0
                sca 0.0 0.0 0.0
            }
            "
        :rtype  final_str: string
        '''
        final_str = ""
        # Iterate through the member variable "animation_bones_arr" to generate
        # the export string for all the animation bones inside current pose
        # object.
        for wyanimationbone in self.animation_bones_arr:
            final_str += str(wyanimationbone)
        return final_str
    
    
