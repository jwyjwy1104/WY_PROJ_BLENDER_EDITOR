################################################################################
# Project Name          	: WY_PROJ_BLENDER_EDITOR
# File Name             	: WYAnimationBoneKeyframe.py
# Project Headquarter   	: https://docs.google.com/document/d/1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit#
# Test Plan Headquarter 	: https://docs.google.com/document/d/1wlFujpygsVKtqiz596ZdD1sCeUPkpIgr1lNlE_GN-_w/edit#
# WYAnimationBone test plan : https://docs.google.com/document/d/1iUkgLkjyxa52i-9jh0NDOs3TTxDT3LT5FCfbrvyOYX0/edit#
# Lead Programmer       	: Samil Chai
# Junior Programmer     	: Nick Jang
# Time                  	: 
# Description           	: 
################################################################################

import bpy
import math
from mathutils import Vector 
from mathutils import Quaternion

class WYAnimationBoneKeyframe:
    '''
    This class represents the animation bone keyframe data which contains the 
    data values to animate a Blender pose bone.
    
    WYAnimationBoneKeyframe contans all the animation bone keyframe related 
    data which can animate the Blender API Armature bone object through 
    keyframe animation using the data assigned to each WYArmatureBoneKeyframe 
    object, it holds data such as bone head, tail coordinate values and 
    animation bone location, rotation quaternion and scale values 
    as each keyframe data. 

    .. seealso:: ../WYAnimationBone/WYAnimationBone.py

    ----------------------------------------------------------------------------
    Member variables:
    ----------------------------------------------------------------------------
    :Memeber variable main_animation_bone_obj               : Blender armature pose bone object to retrieve data from.
    :Memeber variable main_armature_bone_obj                : Blender armature data bone object which current animation bone keyframe is mapped onto.
    :Memeber variable animation_bone_keyframe_index         : Animation keyframe index.
    :Memeber variable animation_bone_head                   : abh - Animation keyframe armature bone head coordinate value.
    :Memeber variable animation_bone_tail                   : abt - Animation keyframe armature bone tail coordinate value.
    :Memeber variable animation_bone_location               : loc - Animation keyframe armature bone location vector value. (eg. Vector(()))
    :Memeber variable animation_bone_rotation_quaternion    : rotq - Animation keyframe armature bone rotation quaternion value.  (eg. Quaternion(()))
    :Memeber variable animation_bone_scale                  : sca - Animation keyframe armature bone scale vector value. (eg. Vector(()))

    ----------------------------------------------------------------------------
    Member functions:
    ----------------------------------------------------------------------------
    # def __init__(self, main_animation_bone_obj=None, main_armature_bone_obj=None):
        Test: https://docs.google.com/spreadsheets/d/1lY88EJYqNgdzirkx9cfzeaysJ4ZWumaSIWE0E0e_BIs/edit#gid=0
    # def __eq__(self, other):
        Test: https://docs.google.com/spreadsheets/d/1tNZG78cmKOiKCQE-df0aCL8dNS6DBtX07BDDMJ2R9io/edit#gid=0 
    # def __str__(self):
        Test: https://docs.google.com/spreadsheets/d/1tNZG78cmKOiKCQE-df0aCL8dNS6DBtX07BDDMJ2R9io/edit#gid=0
    # def init_animation_bone_keyframe_data(self):
        Test: https://docs.google.com/spreadsheets/d/13FiUD2X_WNqwIJlq5f9P5-4vHosPTJUW8pG5o5ppbg0/edit#gid=0
    # def init_wyanimationbonekeyframe_elements(self):
        Test: https://docs.google.com/spreadsheets/d/1uhyj1rrssZ8etpuIlAMI_u-un_cgw2y_kB4q8Fq7xIM/edit#gid=0
    # def init_animation_bone_keyframe_head_data(self, head):
        Test: https://docs.google.com/spreadsheets/d/1FoJPlWFqnWv7L2-sxPdXfPKGEAiZFpP85tmhDWZDgG8/edit#gid=0
    # def init_animation_bone_keyframe_tail_data(self, tail):
        Test: https://docs.google.com/spreadsheets/d/1h3LS8Dghx-eUTjPC9saGU3I2eXAEkqk_eIMLYYOgJFU/edit#gid=0
    # def init_animation_bone_keyframe_location_data(self, location): 
        Test: https://docs.google.com/spreadsheets/d/1e1x9o9nYw0Ac41DDSR9yjOvBgXh5GBg23E438ejPA9Y/edit#gid=0
    # def init_animation_bone_keyframe_rotation_quaternion_data(self, rotation_quaternion):
        Test: https://docs.google.com/spreadsheets/d/1oyPPIkextjbhlZ52olWHGATza8kBWKk-aLK-ELLRGVk/edit#gid=0
    # def init_animation_bone_keyframe_scale_data(self, scale):
        Test: https://docs.google.com/spreadsheets/d/1D8DwWYo0ZPiycSDgobTne0YAeTC3Fkp_W7wAkFMXqYQ/edit#gid=0
    # def get_animation_bone_keyframe_abh_str(self):
        Test: https://docs.google.com/spreadsheets/d/1FsYYLSpOPcMn_jN7qhz76nvLHxKVcTfN_b5Sf8ih8Jg/edit#gid=0
    # def get_animation_bone_keyframe_abt_str(self):
        Test: https://docs.google.com/spreadsheets/d/1aiOzVXnFeQ8e06mTdIQlfp92xaboGUGsfytY5uEhC1s/edit#gid=0
    # def get_animation_bone_keyframe_loc_str(self):
        Test: https://docs.google.com/spreadsheets/d/1QD4-Ivs-x2rJ_GlhzRxHgdPk_IZI1SwBo9OvsW3t-PA/edit#gid=0
    # def get_animation_bone_keyframe_rotq_str(self):
        Test: https://docs.google.com/spreadsheets/d/1lBCv0yAI0xVP9c-2a4kPSNdKeglo1AWuj2NzeroWaks/edit#gid=0
    # def get_animation_bone_keyframe_sca_str(self):
        Test: https://docs.google.com/spreadsheets/d/1r-Pc7p09zhP2PpaZ4qLo_41DEbcKFmyrZaMOsnlf0_g/edit#gid=0


    '''
    def __init__(self, 
                 main_animation_bone_obj=None, 
                 main_armature_bone_obj=None):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe general constructor.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Initialize the member variables with passed in value and others with 
        default values to be initialized after allocation.
                :Memeber variable main_animation_bone_obj               : Blender armature pose bone object to retrieve data from.
                :Memeber variable main_armature_bone_obj                : Blender armature data bone object which current animation bone keyframe is mapped onto.

        Calling sub function: init_wyanimationbonekeyframe_elements()

        Sub function: init_wyanimationbonekeyframe_elements()
            This function initializes the member variable with default values 
            which will be holding the major information data values:
                :Memeber variable animation_bone_head                   : abh - Animation keyframe armature bone head coordinate value.
                :Memeber variable animation_bone_tail                   : abt - Animation keyframe armature bone tail coordinate value.
                :Memeber variable animation_bone_location               : loc - Animation keyframe armature bone location vector value. (eg. Vector(()))
                :Memeber variable animation_bone_rotation_quaternion    : rotq - Animation keyframe armature bone rotation quaternion value.  (eg. Quaternion(()))
                :Memeber variable animation_bone_scale                  : sca - Animation keyframe armature bone scale vector value. (eg. Vector(()))

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  main_animation_bone_obj: Blender armature pose bone object to retrieve data from.
        :type   main_animation_bone_obj: bpy.data.object.pose.bones.
        :param   main_armature_bone_obj: Blender armature data bone object which current animation bone keyframe is mapped onto.
        :type    main_armature_bone_obj: bpy.data.object.data.bones.

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return : Allocated and initialized WYAnimationBoneKeyframe object.
        :rtype  : WYAnimationBoneKeyframe.
        '''
        # Blender armature pose bone object to retrieve data from.
        self.main_animation_bone_obj = main_animation_bone_obj
        # Blender armature data bone object which current animation bone 
        # keyframe is mapped onto.
        self.main_armature_bone_obj = main_armature_bone_obj

        # Call sub function to intialize the main animation bone keyframe 
        # important elements with default values.
        self.init_wyanimationbonekeyframe_elements()

    def __eq__(self, other):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe overrided equal function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Compares the member variables with the memeber variables intialized 
        in "other" object return True if these 2 object has all the member 
        variables same values else return False.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  other: Second WYAnimationBoneKeyframe object to compare with.
        :type   other: WYAnimationBoneKeyframe
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Return the result of comparison between 2 objects.
        :rtype: boolean

        '''
        if other == None:
            return False
        return (self.animation_bone_head == other.animation_bone_head and \
                self.animation_bone_tail == other.animation_bone_tail and \
                self.animation_bone_location == \
                    other.animation_bone_location and \
                self.animation_bone_rotation_quaternion == \
                    other.animation_bone_rotation_quaternion  and \
                self.animation_bone_scale == other.animation_bone_scale)

    def __str__(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe toString function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Manipulate the string to represent the current WYAnimationBoneKeyframe
        object in the file using the values initialized onto the object.

        This function acts like toString function in Java so when I print the 
        WYAnimationBoneKeyframe object directly, so when 
        WYAnimationBoneKeyframe is exported WYAnimationBoneKeyframe wil be 
        printed directly through file stream and the information about this 
        WYAnimationBoneKeyframe object will be printed to file with following 
        sample format:
            --------------------------------------------------------------------
            abh 0.0 0.0 0.0
            abt 0.0 0.0 0.0
            loc 0.0 0.0 0.0
            rotq 0.0 0.0 0.0 0.0
            sca 0.0 0.0 0.0
            --------------------------------------------------------------------

        This string is manipulated with following member variables initialized 
        onto this WYAnimationBoneKeyframe object:
            :Memeber variable animation_bone_head                   : abh - Animation keyframe armature bone head coordinate value.
            :Memeber variable animation_bone_tail                   : abt - Animation keyframe armature bone tail coordinate value.
            :Memeber variable animation_bone_location               : loc - Animation keyframe armature bone location vector value. (eg. Vector(()))
            :Memeber variable animation_bone_rotation_quaternion    : rotq - Animation keyframe armature bone rotation quaternion value.  (eg. Quaternion(()))
            :Memeber variable animation_bone_scale                  : sca - Animation keyframe armature bone scale vector value. (eg. Vector(()))

        Calling sub function: get_animation_bone_keyframe_abh_str()
            Generate string: abh     0.0 0.0 0.0
        Calling sub function: get_animation_bone_keyframe_abt_str()
            Generate string: abt     0.0 0.0 0.0
        Calling sub function: get_animation_bone_keyframe_loc_str()
            Generate string: loc     0.0 0.0 0.0
        Calling sub function: get_animation_bone_keyframe_rotq_str()
            Generate string: rotq    0.0 0.0 0.0 0.0
        Calling sub function: get_animation_bone_keyframe_sca_str()
            Generate string: scae    0.0 0.0 0.0
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Final string representing this 
                           WYAnimationBoneKeyframe object to be 
                           exported to files.
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += self.get_animation_bone_keyframe_abh_str()
        final_str += self.get_animation_bone_keyframe_abt_str()
        final_str += self.get_animation_bone_keyframe_loc_str()
        final_str += self.get_animation_bone_keyframe_rotq_str()
        final_str += self.get_animation_bone_keyframe_sca_str()
        return final_str

    def init_animation_bone_keyframe_data(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe member function initializes the 
        Blender animation keyframe object data values into 
        WYAnimationBoneKeyframe member variables.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the following member variables with the actual
        Blender armature bone object data values by calling multiple 
        sub functions:
        Calling sub function: WYAnimationBoneKeyframe::init_animation_bone_keyframe_head_data()
            :Memeber variable animation_bone_head                   : abh - Animation keyframe armature bone head coordinate value.
        Calling sub function: WYAnimationBoneKeyframe::init_animation_bone_keyframe_tail_data()
            :Memeber variable animation_bone_tail                   : abt - Animation keyframe armature bone tail coordinate value.
        Calling sub function: WYAnimationBoneKeyframe::init_animation_bone_keyframe_location_data()
            :Memeber variable animation_bone_location               : loc - Animation keyframe armature bone location vector value. (eg. Vector(()))
        Calling sub function: WYAnimationBoneKeyframe::init_animation_bone_keyframe_rotatation_quaternion_data()
            :Memeber variable animation_bone_rotation_quaternion    : rotq - Animation keyframe armature bone rotation quaternion value.  (eg. Quaternion(()))
        Calling sub function: WYAnimationBoneKeyframe::init_animation_bone_keyframe_scale_data()
            :Memeber variable animation_bone_scale                  : sca - Animation keyframe armature bone scale vector value. (eg. Vector(()))
        '''
        # If mapped on armature bone object exist, then record its head and 
        # tail coordinate just in case we need it.
        if self.main_armature_bone_obj != None:
            # abh - Animation keyframe armature bone head coordinate value.
            self.init_animation_bone_keyframe_head_data(
                self.main_armature_bone_obj.head)
            # abt - Animation keyframe armature bone tail coordinate value.
            self.init_animation_bone_keyframe_tail_data(
                self.main_armature_bone_obj.tail)

        # If pose bone object exist, then record current keyframe animation 
        # data values.
        if self.main_animation_bone_obj != None:
            # loc - Animation keyframe armature bone location vector value. 
            # (eg. Vector(()))
            self.init_animation_bone_keyframe_location_data(
                self.main_animation_bone_obj.location)
            # rotq - Animation keyframe armature bone rotation quaternion value.  
            # (eg. Quaternion(()))
            self.init_animation_bone_keyframe_rotation_quaternion_data(
                self.main_animation_bone_obj.rotation_quaternion)
            # sca - Animation keyframe armature bone scale vector value. 
            # (eg. Vector(()))
            self.init_animation_bone_keyframe_scale_data(
                self.main_animation_bone_obj.scale)

    def init_wyanimationbonekeyframe_elements(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe member function initializes the member variables 
        with default values when allocated.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variables with default values
                :Memeber variable animation_bone_head                   : [0,0,0]
                :Memeber variable animation_bone_tail                   : [0,0,0]
                :Memeber variable animation_bone_location               : [0,0,0]
                :Memeber variable animation_bone_rotation_quaternion    : [0,0,0,0]
                :Memeber variable animation_bone_scale                  : [0,0,0]

        '''
        # abh - Animation keyframe armature bone head coordinate value.
        self.animation_bone_head = [0,0,0]
        # abt - Animation keyframe armature bone tail coordinate value.
        self.animation_bone_tail = [0,0,0]
        # loc - Animation keyframe armature bone location vector value. (eg. Vector(()))
        self.animation_bone_location = [0,0,0]
        # rotq - Animation keyframe armature bone rotation quaternion value.  (eg. Quaternion(()))
        self.animation_bone_rotation_quaternion = [0,0,0,0]
        # sca - Animation keyframe armature bone scale vector value. (eg. Vector(()))
        self.animation_bone_scale = [0,0,0]

        # Animation keyframe index.
        self.animation_bone_keyframe_index = 0

    def init_animation_bone_keyframe_head_data(self, head):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe sub member function initializes the 
        member variable "animation_bone_head" with the animation keyframe  
        armature bone head coordinate value passed into the function.

        :Post-condition: 
            Member variable "animation_bone_head" is initialized with the
            head coordinate value passed into the function.

            :Memeber variable animation_bone_head                   : abh - Animation keyframe armature bone head coordinate value.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function is the setter of the member variable 
        "animation_bone_head".

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  head: Head coordinate to set with.
        :type   head: Vector((0,0,0)).

        '''
        # abh - Animation keyframe armature bone head coordinate value.
        self.animation_bone_head = head

    def init_animation_bone_keyframe_tail_data(self, tail):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe sub member function initializes the 
        member variable "animation_bone_tail" with the animation keyframe  
        armature bone tail coordinate value passed into the function.

        :Post-condition: 
            Member variable "animation_bone_tail" is initialized with the
            tail coordinate value passed into the function.

            :Memeber variable animation_bone_tail                   : abt - Animation keyframe armature bone tail coordinate value.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function is the setter of the member variable 
        "animation_bone_tail".

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  tail: Tail coordinate to set with.
        :type   tail: Vector((0,0,0)).

        '''
        # abt - Animation keyframe armature bone tail coordinate value.
        self.animation_bone_tail = tail

    def init_animation_bone_keyframe_location_data(self, location): 
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe sub member function initializes the 
        member variable "animation_bone_location" with the animation keyframe  
        armature bone location vector value passed into the function.

        :Post-condition: 
            Member variable "animation_bone_location" is initialized with the
            location vector value passed into the function.

            :Memeber variable animation_bone_location               : loc - Animation keyframe armature bone location vector value. (eg. Vector(()))
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function is the setter of the member variable 
        "animation_bone_location".

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  location: Location vector to set with.
        :type   location: Vector((0,0,0)).

        '''
        # loc - Animation keyframe armature bone location vector value. (eg. Vector(()))
        self.animation_bone_location = Vector((location[0],location[1],location[2]))

    def init_animation_bone_keyframe_rotation_quaternion_data(
        self, rotation_quaternion):

        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe sub member function initializes the 
        member variable "animation_bone_rotation_quaternion" with the 
        animation keyframe armature bone rotation quaternion value passed 
        into function.

        :Post-condition: 
            Member variable "animation_bone_rotation_quaternion" is initialized 
            with the rotation quaternion value passed into the function.

            :Memeber variable animation_bone_rotation_quaternion    : rotq - Animation keyframe armature bone rotation quaternion value.  (eg. Quaternion(()))
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function is the setter of the member variable 
        "animation_bone_rotation_quaternion".

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  rotation_quaternion: Roatation quaternion value to set with.
        :type   rotation_quaternion: Quaternion((0,0,0,0)).

        '''
        # rotq - Animation keyframe armature bone rotation quaternion value.  (eg. Quaternion(()))
        self.animation_bone_rotation_quaternion = Quaternion((rotation_quaternion[0],rotation_quaternion[1],rotation_quaternion[2],rotation_quaternion[3]))

    def init_animation_bone_keyframe_scale_data(self, scale):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe sub member function initializes the 
        member variable "animation_bone_scale" with the animation keyframe 
        armature bone scale vector value passed into the function.

        :Post-condition: 
            Member variable "animation_bone_scale" is initialized 
            with the scale vector value passed into the function.

            :Memeber variable animation_bone_scale                  : sca - Animation keyframe armature bone scale vector value. (eg. Vector(()))
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function is the setter of the member variable 
        "animation_bone_scale".

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  scale: Scale vector value to set with.
        :type   scale: Vector((0,0,0)).

        '''
        # sca - Animation keyframe armature bone scale vector value. (eg. Vector(()))
        self.animation_bone_scale = Vector((scale[0],scale[1],scale[2]))

    def get_animation_bone_keyframe_abh_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe sub member function generates the string to
        export the animation keyframe armature bone head coordinate value to 
        file.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the animation keyframe 
        armature bone head coordinate value
            :Memeber variable animation_bone_head                   : abh - Animation keyframe armature bone head coordinate value.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the head coordinate value 
                           in format "abh [head coordinate value]\\n".
                           Example:  "abh 0.0 0.0 0.0\\n".
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "abh "
        final_str += str(eval(format(self.animation_bone_head[0], '.6f'))) + \
                        " " + \
                        str(eval(format(self.animation_bone_head[1], '.6f'))) + \
                        " " + \
                        str(eval(format(self.animation_bone_head[2], '.6f'))) + "\n"  
        return final_str

    def get_animation_bone_keyframe_abt_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe sub member function generates the string to
        export the animation keyframe armature bone tail coordinate value to 
        file.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the animation keyframe 
        armature bone tail coordinate value
            :Memeber variable animation_bone_tail                   : abt - Animation keyframe armature bone tail coordinate value.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the tail coordinate value 
                           in format "abt [tail coordinate value]\\n".
                           Example:  "abt 0.0 0.0 0.0\\n".
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "abt "
        final_str += str(eval(format(self.animation_bone_tail[0], '.6f'))) \
                         + " " + \
                         str(eval(format(self.animation_bone_tail[1], '.6f'))) \
                         + " " + \
                         str(eval(format(self.animation_bone_tail[2], '.6f'))) \
                         + "\n"  
        return final_str

    def get_animation_bone_keyframe_loc_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe sub member function generates the string to
        export the animation keyframe armature bone location vector value to 
        file.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the animation keyframe 
        armature bone location vector value
            :Memeber variable animation_bone_location               : loc - Animation keyframe armature bone location vector value. (eg. Vector(()))
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the location vector value 
                           in format "loc [location vector value]\\n".
                           Example:  "loc 0.0 0.0 0.0\\n".
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "loc "
        final_str += str(eval(format(self.animation_bone_location[0], '.6f'))) \
                         + " " + \
                         str(eval(format(
                             self.animation_bone_location[1], '.6f'))) \
                         + " " + \
                         str(eval(format(
                             self.animation_bone_location[2], '.6f'))) + "\n"  
        return final_str

    def get_animation_bone_keyframe_rotq_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe sub member function generates the string to
        export the animation keyframe armature bone rotation quaternion value to 
        file.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the animation keyframe 
        armature bone rotation quaternion value
            :Memeber variable animation_bone_rotation_quaternion    : rotq - Animation keyframe armature bone rotation quaternion value.  (eg. Quaternion(()))
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the rotation quaternion 
                           value in format 
                           "rot1 [rotation quaternion value]\\n".
                           Example: "rptq 0.0 0.0 0.0 0.0\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "rotq "
        final_str += str(eval(format(
                            self.animation_bone_rotation_quaternion[0],
                            '.6f'))) + \
                         " " + \
                         str(eval(format(
                             self.animation_bone_rotation_quaternion[1],
                             '.6f'))) + \
                         " " + \
                         str(eval(format(
                             self.animation_bone_rotation_quaternion[2], 
                             '.6f'))) + \
                         " " + \
                         str(eval(format(
                             self.animation_bone_rotation_quaternion[3], 
                             '.6f'))) + "\n"  
        return final_str

    def get_animation_bone_keyframe_sca_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYAnimationBoneKeyframe sub member function generates the string to
        export the animation keyframe armature bone scale vector value to 
        file.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the animation keyframe 
        armature bone scale vector value
            :Memeber variable animation_bone_scale                  : sca - Animation keyframe armature bone scale vector value. (eg. Vector(()))
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the location vector value 
                           in format "sca [scale vector value]\\n".
                           Example:  "sca 0.0 0.0 0.0\\n".
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "sca "
        final_str += str(eval(format(
                            self.animation_bone_scale[0], '.6f'))) + \
                         " " + \
                         str(eval(format(
                             self.animation_bone_scale[1], '.6f'))) + \
                         " " + \
                         str(eval(format(
                             self.animation_bone_scale[2], '.6f'))) + "\n"  
        return final_str