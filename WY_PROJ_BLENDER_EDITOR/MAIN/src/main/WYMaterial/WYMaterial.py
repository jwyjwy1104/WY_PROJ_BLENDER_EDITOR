################################################################################
# Project Name          	: WY_PROJ_BLENDER_EDITOR
# File Name             	: WYMaterial.py
# Project Headquarter   	: https://docs.google.com/document/d/1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit#
# Test Plan Headquarter 	: https://docs.google.com/document/d/1wlFujpygsVKtqiz596ZdD1sCeUPkpIgr1lNlE_GN-_w/edit#
# WYMaterial test plan  	: https://docs.google.com/document/d/1g8EEbVXKorZn7_jSUZ0STpsBOUX2wqhSBvRLXb2k420/edit#heading=h.nnly3zngpsdr
# Lead Programmer       	: Samil Chai
# Junior Programmer     	: Nick Jang
# Time                  	: 
# Description           	: 
################################################################################
import os 

class WYMaterial:
    '''
    WYModel contains a WYMesh and a WYMaterial object to manage all the model  
    data collection in a single class object.

    WYMaterial contans all the material related data which are kept by the 
    Blender API material object, it holds data such as ambient, diffuse and 
    specular light values and most importantly holds the texture image file 
    path to be rendered on the surface of corresponding mesh object.
    
    ----------------------------------------------------------------------------
    Member variables:
    ----------------------------------------------------------------------------
    :Memeber variable main_mesh_obj                 : Blender model object.
    :Memeber variable main_material_obj             : Blender material object.
    :Memeber variable mtl_material_name             : Name of the Blender material object.
    :Memeber variable mtl_mirror_color              : Ambient color of the Blender material object.
    :Memeber variable mtl_ambient                   : Ambient intensity of the Blender material object.
    :Memeber variable mtl_diffuse_color             : Diffuse color of the Blender material object.
    :Memeber variable mtl_diffuse_intensity         : Diffuse intensity of the Blender material object.
    :Memeber variable mtl_specular_color            : Specular color of the Blender material object.
    :Memeber variable mtl_specular_intensity        : Specular intensity of the Blender material object.
    :Memeber variable mtl_specular_hardness         : Specular hardness of the Blender material object.
    :Memeber variable mtl_emit                      : Emissive intensity of the Blender material object.
    :Memeber variable mtl_raytrace_transparency_ior : Refraction index of the Blender material object.
    :Memeber variable mtl_alpha                     : Alpha value of the Blender material object.
    :Memeber variable mtl_texture_map_image_path    : Texture image file path mapped onto the of the Blender mesh object.

    ----------------------------------------------------------------------------
    Member functions:
    ----------------------------------------------------------------------------
    # def __init__(self, main_mesh_obj=None, main_material_obj=None):
        Test: https://docs.google.com/spreadsheets/d/1b4wf7Bpjh4j4RmA0YPii7QcmcjmF3vzUKUee6sDGyYQ/edit#gid=0
    # def __eq__(self, other):
        Test: https://docs.google.com/spreadsheets/d/13doaZ2b6QitiIUgBu4eHXeUWwCVNGxitJNbx_Og_tLs/edit#gid=0 
    # def __str__(self):
        Test: https://docs.google.com/spreadsheets/d/1-c_8Lh4sFkJCpFEiuPo8rexv9vkrjwG3PN7_ICxmVCs/edit#gid=0
    # def init_material_data(self):
        Test: https://docs.google.com/spreadsheets/d/1bQrfijaN0pUaUe3CO7AQme0F4AJyvB5CtT1fmBlwqCc/edit#gid=0
    # def init_wymaterial_elements(self):
        Test: https://docs.google.com/spreadsheets/d/1Vy9YW79FP3NzQ63EeunDDJT_HNCzHGzWsdD-qkUCams/edit#gid=0
    # def init_material_name(self):
        Test: https://docs.google.com/spreadsheets/d/1pWbdlMtAEYohM5HQLUOKH221ZR-sT-zVxdplD1VMK7Q/edit#gid=0
    # def init_material_ambient(self):
        Test: https://docs.google.com/spreadsheets/d/1qCyL8rPgETZDqWEEqpGCdGHYmlGc6LQx80mfi9-Fmm4/edit#gid=0
    # def init_material_diffuse(self):
        Test: https://docs.google.com/spreadsheets/d/1Vr5-_gb1_xoC34JWm8QTC-WA4l0Vk4sRxMOTfY2-LKo/edit#gid=0
    # def init_material_specular(self):
        Test: https://docs.google.com/spreadsheets/d/1ldWQnD665ScmMam1RHXJcyLnEXibd1zuNpw3Yl1x5Vk/edit#gid=0
    # def init_material_emissive(self):
        Test: https://docs.google.com/spreadsheets/d/1Vp2UGkT8i6fh60-6zsNG40vYC2mMKSI4sT6jbqOvfB4/edit#gid=0 
    # def init_material_alpha(self):
        Test: https://docs.google.com/spreadsheets/d/1699mLoMJONU7O5vEIn4xZ_CK43IbPskiIKe5C5s4bmM/edit#gid=0
    # def init_material_refraction(self):
        Test: https://docs.google.com/spreadsheets/d/1eI78VGIWRM0ErYjhKSXrIzrOpKGCvlDDhfic-Tn78X8/edit#gid=0
    # def init_material_texture(self):
        Test: https://docs.google.com/spreadsheets/d/19rEKC7Mcvm5ctldWl7M5yx8uZNnqsYcK6TlWBc4U_B4/edit#gid=0 
    # def get_material_name_str(self):
        Test: https://docs.google.com/spreadsheets/d/1zY_AuLBpdqHf9ur4C0EhxJGgNPoxa3rn34OZA2HrX9c/edit#gid=0
    # def get_material_ambient_str(self):
        Test: https://docs.google.com/spreadsheets/d/1cO0EpPBcJFwJpBtGdF__dHmQBkXNM4HNWXbw0A1eBwo/edit#gid=0
    # def get_material_diffuse_str(self):
        Test: https://docs.google.com/spreadsheets/d/1L6sWg9uRNYPVXU_pB9x3rw6ANBtiHEZYwHuRye9XoX0/edit#gid=0
    # def get_material_specular_str(self):
        Test: https://docs.google.com/spreadsheets/d/11p0t1IfWH2F5DMSXc5ngnLX3GM-lBjAo6bEaXHIAOmY/edit#gid=0
    # def get_material_emissive_str(self):
        Test: https://docs.google.com/spreadsheets/d/1gCR81w3mobxnGNHDKsA18EYe_sS4QHrP2JFF8uTwOcM/edit#gid=0
    # def get_material_alpha_str(self):
        Test: https://docs.google.com/spreadsheets/d/1jUQtw2HH7THxro7hvP_LNE1wed283qofpzFLKOwkXQQ/edit#gid=0
    # def get_material_refraction_str(self):
        Test: https://docs.google.com/spreadsheets/d/1uOEhITpvVhV5of0FEqoMOOVXVcIGGYiPbezR1frui_E/edit#gid=0
    # def get_material_texture_str(self):
        Test: https://docs.google.com/spreadsheets/d/1PlyAbGJOqGUaIyfb-fOdjfqu_FYohpwU6KbJ294Np00/edit#gid=0

    '''
    #---------------------------------------------------------------------------
    # General constructor.
    #---------------------------------------------------------------------------
    def __init__(self, main_mesh_obj=None, main_material_obj=None):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial general constructor.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Initialize the member variables using the values passed into the 
        allocation call.

        Initializing member varibles:
        :Memeber variable main_mesh_obj     : Blender model object.
        :Memeber variable main_material_obj : Blender material object.

        Calling sub function: WYMaterial::init_wymaterial_elements()
        Sub function: init_wymaterial_elements()
            This function initializes the data structure which holds the major
            information data values such as:
                :Memeber variable mtl_material_name             : Name of the Blender material object.
                :Memeber variable mtl_mirror_color              : Ambient color of the Blender material object.
                :Memeber variable mtl_ambient                   : Ambient intensity of the Blender material object.
                :Memeber variable mtl_diffuse_color             : Diffuse color of the Blender material object.
                :Memeber variable mtl_diffuse_intensity         : Diffuse intensity of the Blender material object.
                :Memeber variable mtl_specular_color            : Specular color of the Blender material object.
                :Memeber variable mtl_specular_intensity        : Specular intensity of the Blender material object.
                :Memeber variable mtl_specular_hardness         : Specular hardness of the Blender material object.
                :Memeber variable mtl_emit                      : Emissive intensity of the Blender material object.
                :Memeber variable mtl_raytrace_transparency_ior : Refraction index of the Blender material object.
                :Memeber variable mtl_alpha                     : Alpha value of the Blender material object.
                :Memeber variable mtl_texture_map_image_path    : Texture image file path mapped onto the of the Blender mesh object.
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  main_mesh_obj: Referenced Blender mesh object.
        :type   main_mesh_obj: bpy.data.object
        :param  main_material_obj: Referenced Blender material object.
        :type   main_material_obj: bpy.data.material
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Initialized WYMaterial object.
        :rtype: WYMaterial

        '''
        #if main_mesh_obj == None:
        #    raise Exception("ERROR::WYMaterial::__init__::Blender mesh object is none!!!")
        #if main_material_obj == None:
        #    raise Exception("ERROR::WYMaterial::__init__::Blender material object is none!!!")
        self.main_mesh_obj = main_mesh_obj
        self.main_material_obj = main_material_obj

        # Call sub function to intialize the main material elements with 
        # default values to hold the material data with.
        self.init_wymaterial_elements()

    #---------------------------------------------------------------------------
    # Overriden equal function.
    #---------------------------------------------------------------------------
    def __eq__(self, other):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial overrided equal function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Compares the member variables with the memeber variables intialized 
        in "other" object return True if these 2 object has all the member 
        variables same values else return False.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  other: Second WYMaterial object to compare with.
        :type   other: WYMaterial
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Return the result of comparison between 2 objects.
        :rtype: boolean

        '''
        if other == None:
            return False
        return (self.main_mesh_obj == other.main_mesh_obj and \
                self.main_material_obj == other.main_material_obj and \
                self.mtl_material_name == other.mtl_material_name and \
                self.mtl_mirror_color == other.mtl_mirror_color and \
                self.mtl_ambient == other.mtl_ambient  and \
                self.mtl_diffuse_color == other.mtl_diffuse_color and \
                self.mtl_diffuse_intensity == other.mtl_diffuse_intensity and \
                self.mtl_specular_color == other.mtl_specular_color and \
                self.mtl_specular_intensity == other.mtl_specular_intensity and \
                self.mtl_specular_hardness == other.mtl_specular_hardness and \
                self.mtl_emit == other.mtl_emit and \
                self.mtl_raytrace_transparency_ior == other.mtl_raytrace_transparency_ior and \
                self.mtl_alpha == other.mtl_alpha and \
                self.mtl_texture_map_image_path == other.mtl_texture_map_image_path)
        
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    # Main toString function.
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    def __str__(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh toString function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Manipulate the string to represent the current WYMesh object in the 
        file using the values initialized when allocated.

        This function acts like toString function in Java so when I print the 
        WYMesh object directly, so when WYMesh is exported WYMesh wil be printed 
        directly through file stream and the information about this WYmesh 
        object will be printed to file with following sample format:
            -------------------------------------------------------------------
            mtl_material_name ""
            mtl_mirror_color 0.0 0.0 0.0
            mtl_ambient 0.0
            mtl_diffuse_color 0.0 0.0 0.0
            mtl_diffuse_intensity 0.0
            mtl_specular_color 0.0 0.0 0.0
            mtl_specular_intensity 0.0
            mtl_specular_hardness 0.0
            mtl_emit 0.0
            mtl_alpha 0.0
            mtl_raytrace_transparency_ior 0.0
            mtl_texture_map_image_path ""
            -------------------------------------------------------------------

        This string is manipulated with following member variables initialized 
        onto this WYMesh object:
            :Memeber variable main_mesh_obj     : Blender model object.
            :Memeber variable main_material_obj : Blender material object.
            :Memeber variable mtl_material_name : Name of the Blender material object.
            :Memeber variable mtl_mirror_color  : Ambient color of the Blender material object.
            :Memeber variable mtl_ambient       : Ambient intensity of the Blender material object.
            :Memeber variable mtl_diffuse_color             : Diffuse color of the Blender material object.
            :Memeber variable mtl_diffuse_intensity         : Diffuse intensity of the Blender material object.
            :Memeber variable mtl_specular_color            : Specular color of the Blender material object.
            :Memeber variable mtl_specular_intensity        : Specular intensity of the Blender material object.
            :Memeber variable mtl_specular_hardness         : Specular hardness of the Blender material object.
            :Memeber variable mtl_emit                      : Emissive intensity of the Blender material object.
            :Memeber variable mtl_raytrace_transparency_ior : Refraction index of the Blender material object.
            :Memeber variable mtl_alpha                     : Alpha value of the Blender material object.
            :Memeber variable mtl_texture_map_image_path    : Texture image file path mapped onto the of the Blender mesh object.

        Calling sub function: get_material_name_str()
        Calling sub function: get_material_ambient_str()
        Calling sub function: get_material_diffuse_str()
        Calling sub function: get_material_specular_str()
        Calling sub function: get_material_emissive_str()
        Calling sub function: get_material_alpha_str()
        Calling sub function: get_material_refraction_str()
        Calling sub function: get_material_texture_str()
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Final string representing this WYMesh object to be exported to files.
        :rtype  final_str: string
        '''

        final_str = ""
        final_str += self.get_material_name_str()
        final_str += self.get_material_ambient_str()
        final_str += self.get_material_diffuse_str()
        final_str += self.get_material_specular_str()
        final_str += self.get_material_emissive_str()
        final_str += self.get_material_alpha_str()
        final_str += self.get_material_refraction_str()
        final_str += self.get_material_texture_str()
        
        return final_str

    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    # Main init function - Initialize all the data converted from Blender 
    #                      Material object to WYMaterial object.          
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    def init_material_data(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function initializes the Blender material
        object data value into WYMaterial member variables.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the following member variables with the actual
        Blender material object data values by calling multiple sub functions:

        Calling sub function: init_material_name()
            :Memeber variable mtl_material_name : Name of the Blender material object.
        Calling sub function: init_material_ambient()
            :Memeber variable mtl_ambient       : Ambient intensity of the Blender material object.
            :Memeber variable mtl_mirror_color  : Ambient color of the Blender material object.
        Calling sub function: init_material_diffuse()
            :Memeber variable mtl_diffuse_color             : Diffuse color of the Blender material object.
            :Memeber variable mtl_diffuse_intensity         : Diffuse intensity of the Blender material object.
        Calling sub function: init_material_specular()
            :Memeber variable mtl_specular_color            : Specular color of the Blender material object.
            :Memeber variable mtl_specular_intensity        : Specular intensity of the Blender material object.
            :Memeber variable mtl_specular_hardness         : Specular hardness of the Blender material object.
        Calling sub function: init_material_emissive()
            :Memeber variable mtl_emit                      : Emissive intensity of the Blender material object.
        Calling sub function: init_material_alpha()
            :Memeber variable mtl_alpha                     : Alpha value of the Blender material object.
        Calling sub function: init_material_refraction()
            :Memeber variable mtl_raytrace_transparency_ior : Refraction index of the Blender material object.
        Calling sub function: init_material_texture()
            :Memeber variable mtl_texture_map_image_path    : Texture image file path mapped onto the of the Blender mesh object.
            
        '''
        # mtl_material_name
        self.init_material_name()
        # mtl_mirror_color, mtl_ambient
        self.init_material_ambient()
        # mtl_diffuse_color, mtl_diffuse_intensity
        self.init_material_diffuse()
        # mtl_specular_color, mtl_specular_intensity, mtl_specular_hardness
        self.init_material_specular()
        # mtl_emit
        self.init_material_emissive()
        # mtl_alpha
        self.init_material_alpha()
        # mtl_raytrace_transparency_ior
        self.init_material_refraction()
        # mtl_texture_map_image_path
        self.init_material_texture()
        
    def init_wymaterial_elements(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial member function initializes the member variables with default
        values when allocated.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variables with default values
            :Memeber variable mtl_material_name             : ""
            :Memeber variable mtl_mirror_color              : [0,0,0]
            :Memeber variable mtl_ambient                   : 0
            :Memeber variable mtl_diffuse_color             : [0,0,0]
            :Memeber variable mtl_diffuse_intensity         : 0
            :Memeber variable mtl_specular_color            : [0,0,0]
            :Memeber variable mtl_specular_intensity        : 0
            :Memeber variable mtl_specular_hardness         : 0
            :Memeber variable mtl_emit                      : 0
            :Memeber variable mtl_raytrace_transparency_ior : 0
            :Memeber variable mtl_alpha                     : 0
            :Memeber variable mtl_texture_map_image_path    : ""

        Called by function: WYMaterial::__init__()

        '''
        # Name of current exporting material object.
        self.mtl_material_name = ""
        # Ambient color.
        self.mtl_mirror_color = [0,0,0]
        # Ambient intensity.
        self.mtl_ambient = 0
        # Diffuse color.
        self.mtl_diffuse_color = [0,0,0]
        # Diffuse intensity.
        self.mtl_diffuse_intensity = 0
        # Specular color.
        self.mtl_specular_color = [0,0,0]
        # Specular intensity.
        self.mtl_specular_intensity = 0
        # Specular hardness, shinesss.
        self.mtl_specular_hardness = 0
        # Emissive light color.
        self.mtl_emit = 0
        # Refraction index.
        self.mtl_raytrace_transparency_ior = 0
        # Dissolve, alpha.
        self.mtl_alpha = 0
        # Relative texture image path mapped onto current material object.
        self.mtl_texture_map_image_path = ""

    #---------------------------------------------------------------------------
    # Material : newmtl = Material name
    #---------------------------------------------------------------------------
    def init_material_name(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function initializes the Blender material object 
        name value into WYMaterial member variable "mtl_material_name".

        :Post-condition: 
            Member variable "mtl_material_name" is initialized with the
            name of the material object initialized as member 
            variable "main_material_obj".

        Called by function: init_material_data()

        This component is commonly refer to "newmtl" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component as "mtl_material_name".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "mtl_material_name" with 
        the actual Blender Material object name value retrieved from "name" 
        value of the member variable "main_material_obj".
            :Memeber variable main_material_obj : Blender material object.
        '''
        self.mtl_material_name = self.main_material_obj.name
    
    # --------------------------------------------------------------------------
    # Material : Ka = Ambient color * Ambient 
    # --------------------------------------------------------------------------
    def init_material_ambient(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function initializes the Blender material object 
        ambient related data values into WYMaterial member variables
        "mtl_mirror_color" and "mtl_ambient"

        :Post-condition: 
            Member variable "mtl_mirror_color" is initialized with the
            ambient color "mirror_color" value of the material object 
            initialized as member variable "main_material_obj".

            Member variable "mtl_ambient" is initialized with the
            ambient intensity "ambient" value of the material object 
            initialized as member variable "main_material_obj".

        Called by function: init_material_data()

        This component is commonly refer to "Ka" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component into multiple component values: 
        "mtl_mirror_color", "mtl_ambient".

        Formula: Ka = mtl_mirror_color * mtl_ambient
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "mtl_mirror_color" 
        and "mtl_ambient" with the actual Blender Material object ambient color 
        and ambient intensity value retrieved from 
        "mirror_color" and "ambient" values of the member variable 
        "main_material_obj".
            :Memeber variable main_material_obj : Blender material object.
        '''
        self.mtl_mirror_color = self.main_material_obj.mirror_color
        self.mtl_ambient = self.main_material_obj.ambient
        self.mtl_ambient = eval(format(self.mtl_ambient, '.6f'))
        self.mtl_mirror_color[0] = self.mtl_mirror_color[0] * self.mtl_ambient
        self.mtl_mirror_color[1] = self.mtl_mirror_color[1] * self.mtl_ambient
        self.mtl_mirror_color[2] = self.mtl_mirror_color[2] * self.mtl_ambient

        self.mtl_mirror_color[0] = eval(format(self.mtl_mirror_color[0], '.6f'))
        self.mtl_mirror_color[1] = eval(format(self.mtl_mirror_color[1], '.6f'))
        self.mtl_mirror_color[2] = eval(format(self.mtl_mirror_color[2], '.6f'))
        
    # --------------------------------------------------------------------------
    # Material : Kd = Diffuse color * Diffuse intensity
    # --------------------------------------------------------------------------
    def init_material_diffuse(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function initializes the Blender material object 
        diffuse related data values into WYMaterial member variables
        "mtl_diffuse_color" and "mtl_diffuse_intensity"

        :Post-condition: 
            Member variable "mtl_diffuse_color" is initialized with the
            diffuse color "diffuse_color" value of the material object 
            initialized as member variable "main_material_obj".

            Member variable "mtl_diffuse_intensity" is initialized with the
            diffuse intensity "diffuse_intensity" value of the material object 
            initialized as member variable "main_material_obj".

        Called by function: init_material_data()

        This component is commonly refer to "Kd" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component into multiple component values: 
        "mtl_diffuse_color", "mtl_diffuse_intensity".

        Formula: Kd = mtl_diffuse_color * mtl_diffuse_intensity
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "mtl_diffuse_color" 
        and "diffuse_color" with the actual Blender Material object 
        diffuse color and diffuse intensity value retrieved from 
        "diffuse_color" and "diffuse_intensity" values of the member variable 
        "main_material_obj".
            :Memeber variable main_material_obj : Blender material object.
        '''
        self.mtl_diffuse_color = self.main_material_obj.diffuse_color
        self.mtl_diffuse_intensity = self.main_material_obj.diffuse_intensity
        self.mtl_diffuse_intensity = eval(format(
            self.mtl_diffuse_intensity, 
            '.6f'))
        self.mtl_diffuse_color[0] = \
            self.mtl_diffuse_color[0] * self.mtl_diffuse_intensity
        self.mtl_diffuse_color[1] = \
            self.mtl_diffuse_color[1] * self.mtl_diffuse_intensity
        self.mtl_diffuse_color[2] = \
            self.mtl_diffuse_color[2] * self.mtl_diffuse_intensity

        self.mtl_diffuse_color[0] = \
            eval(format(self.mtl_diffuse_color[0], '.6f'))
        self.mtl_diffuse_color[1] = \
            eval(format(self.mtl_diffuse_color[1], '.6f'))
        self.mtl_diffuse_color[2] = \
            eval(format(self.mtl_diffuse_color[2], '.6f'))
        
    # --------------------------------------------------------------------------
    # Material : Ks = Specular color (Min = (0,0,0)) * 
    #                 Specular intensity (Min = 0, Max = 1)
    # --------------------------------------------------------------------------
    def init_material_specular(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function initializes the Blender material object 
        specular related data values into WYMaterial member variables
        "mtl_specular_color", "mtl_specular_intensity" 
        and "mtl_specular_hardness"

        :Post-condition: 
            Member variable "mtl_specular_color" is initialized with the
            diffuse color "specular_color" value of the material object 
            initialized as member variable "main_material_obj".

            Member variable "mtl_specular_intensity" is initialized with the
            diffuse intensity "specular_intensity" value of the material object 
            initialized as member variable "main_material_obj".

            Member variable "mtl_specular_hardness" is initialized with the
            diffuse intensity "specular_hardness" value of the material object 
            initialized as member variable "main_material_obj" converted with 
            formula (/ 511 * 1000).

        Called by function: init_material_data()

        This component is commonly refer to "Ks" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component into multiple component values: 
        "mtl_specular_color" and "mtl_specular_intensity".
        
        This component is commonly refer to "Ns" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component into multiple component values: 
        "mtl_specular_hardness".


        Formula: Ks = Specular color (Min = (0,0,0)) * 
                      Specular intensity (Min = 0, Max = 1)
         
                 Ns = Shininess, Specular exponent (Larger = More focus), 
                     Specular hardness / 511 * 1000 --> Actual Obj Ns 
                     (Min = 1, Max = 511)
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "mtl_specular_color", 
        "mtl_specular_intensity" and "mtl_specular_hardness" with the actual 
        Blender Material object specular color, specular intensity and specular 
        hardness value retrieved from "specular_color", "specular_intensity" 
        and "specular_hardness" values of the member variable 
        "main_material_obj" where specular hardness value is converted with 
        formula manually (/ 511 * 1000) to match the format with standard MTL 
        Ns value. 
            :Memeber variable main_material_obj : Blender material object.
        '''
        self.mtl_specular_color = self.main_material_obj.specular_color
        self.mtl_specular_intensity = \
            eval(format(self.main_material_obj.specular_intensity, '.6f'))

        self.mtl_specular_color[0] = \
            self.mtl_specular_color[0] * self.mtl_specular_intensity
        self.mtl_specular_color[1] = \
            self.mtl_specular_color[1] * self.mtl_specular_intensity
        self.mtl_specular_color[2] = \
            self.mtl_specular_color[2] * self.mtl_specular_intensity

        self.mtl_specular_color[0] = \
            eval(format(self.mtl_specular_color[0], '.6f'))
        self.mtl_specular_color[1] = \
            eval(format(self.mtl_specular_color[1], '.6f'))
        self.mtl_specular_color[2] = \
            eval(format(self.mtl_specular_color[2], '.6f'))
        
        # ----------------------------------------------------------------------
        # Material : Ns = Shininess, Specular exponent (Larger = More focus), 
        #            Specular hardness / 511 * 1000 --> Actual Obj Ns 
        #            (Min = 1, Max = 511)
        # ----------------------------------------------------------------------
        self.mtl_specular_hardness = \
            self.main_material_obj.specular_hardness / 511 * 1000
        self.mtl_specular_hardness = \
            eval(format(self.mtl_specular_hardness, '.6f'))

    # --------------------------------------------------------------------------
    # Material : Ke = Emissive intensity value (Min = 0.0)
    # --------------------------------------------------------------------------
    def init_material_emissive(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function initializes the Blender material object 
        emissive intensity data value into WYMaterial member variables 
        "mtl_emit".

        :Post-condition: 
            Member variable "mtl_emit" is initialized with the
            diffuse color "emit" value of the material object 
            initialized as member variable "main_material_obj".

        Called by function: init_material_data()
        
        This component is commonly refer to "Ke" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component as "mtl_emit".

        Formula: Ke = Emissive intensity value (Min = 0.0)
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "mtl_emit" with the 
        actual Blender Material object emissive intensity value retrieved from 
        "emit" value of the member variable "main_material_obj".
            :Memeber variable main_material_obj : Blender material object.
        '''
        self.mtl_emit = self.main_material_obj.emit
        self.mtl_emit = eval(format(self.mtl_emit, '.6f'))
        
    # --------------------------------------------------------------------------
    # Material : d = Alpha (Dissolve) (Min = 0.0, Max = 1.0)
    # --------------------------------------------------------------------------
    def init_material_alpha(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function initializes the Blender material object 
        alpha data value into WYMaterial member variable
        "mtl_alpha".

        :Post-condition: 
            Member variable "mtl_emit" is initialized with the
            alpha "alpha" value of the material object 
            initialized as member variable "main_material_obj".

        Called by function: init_material_data()
        
        This component is commonly refer to "d" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component as "mtl_alpha".

        Formula: d = Alpha (Dissolve) (Min = 0.0, Max = 1.0)
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "mtl_alpha" with the 
        actual Blender Material object alpha value retrieved from 
        "alpha" value of the member variable "main_material_obj".
            :Memeber variable main_material_obj : Blender material object.
        '''
        self.mtl_alpha = self.main_material_obj.alpha
        self.mtl_alpha = eval(format(self.mtl_alpha, '.6f'))
        
    # --------------------------------------------------------------------------
    # Material : Ni = Refraction index (Min = 0.25, Max = 4.0)
    # --------------------------------------------------------------------------
    def init_material_refraction(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function initializes the Blender material object 
        refraction index data value into WYMaterial member variable
        "mtl_raytrace_transparency_ior".

        :Post-condition: 
            Member variable "mtl_raytrace_transparency_ior" is 
            initialized with the refraction index "raytrace_transparency.ior" 
            value of the material object initialized as member 
            variable "main_material_obj".

        Called by function: init_material_data()
        
        This component is commonly refer to "Ni" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component as "mtl_raytrace_transparency_ior".

        Formula: Ni = Refraction index (Min = 0.25, Max = 4.0)

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable 
        "mtl_raytrace_transparency_ior" with the actual Blender Material object 
        refraction index value retrieved from "raytrace_transparency.ior" 
        value of the member variable "main_material_obj".
            :Memeber variable main_material_obj : Blender material object.
        '''
        self.mtl_raytrace_transparency_ior = \
            self.main_material_obj.raytrace_transparency.ior
        self.mtl_raytrace_transparency_ior = \
            eval(format(self.mtl_raytrace_transparency_ior, '.6f'))

    # --------------------------------------------------------------------------
    # Material : map_K = Texture image map
    # --------------------------------------------------------------------------
    def init_material_texture(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function initializes the Blender material object 
        texture image file path string value into WYMaterial member variable
        "mtl_texture_map_image_path".

        :Post-condition: 
            Member variable "mtl_texture_map_image_path" is 
            initialized with the texture image file path 
            "uv_textures.active.data[0].image" value of the mesh object 
            initialized as member variable "main_mesh_obj".

        Called by function: init_material_data()
        
        This component is commonly refer to "map_Kd" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component as "mtl_texture_map_image_path".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable 
        "mtl_texture_map_image_path" with the actual Blender Mesh object 
        texture image file path string value retrieved from 
        "uv_textures.active.data[0].image" value of the member variable 
        "main_mesh_obj".
            :Memeber variable main_mesh_obj : Blender mesh object.
        '''
        if len(self.main_mesh_obj.data.uv_textures) <= 0:
            self.mtl_texture_map_image_path = "NULL"
        else:
            textureImg = \
                self.main_mesh_obj.data.uv_textures.active.data[0].image
            '''
            textureImgAbsolutePath = bpy.path.basename(textureImg.filepath)
            print(bpy.path.abspath(textureImg.filepath))
            '''
            #textureImgAbsolutePath = bpy.path.abspath(textureImg.filepath)
            textureImgAbsolutePath = bpy.path.relpath(textureImg.filepath)[2:]
            self.mtl_texture_map_image_path = textureImgAbsolutePath

    # --------------------------------------------------------------------------
    # mtl_material_name
    # --------------------------------------------------------------------------
    def get_material_name_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function generates the name of the material 
        object into strings to be exported to file.

        This component is commonly refer to "newmtl" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component as "mtl_material_name".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the name of the material 
        object intialized in this WYMaterial object.
            :Memeber variable mtl_material_name : Name of the Blender material object.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the name of the material 
            object onto file in format "mtl_material_name [Name]\\n"
            Example: "mtl_material_name Material1\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "mtl_material_name "
        final_str += self.mtl_material_name + '\n'
        return final_str
    
    # --------------------------------------------------------------------------
    # mtl_mirror_color, mtl_ambient
    # --------------------------------------------------------------------------
    def get_material_ambient_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function generates the ambient related data 
        values of the material object into strings to be exported to file.

        This component is commonly refer to "Ka" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component into multiple component values: 
        "mtl_mirror_color", "mtl_ambient".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the ambient related data 
        values of the material object intialized in this WYMaterial object.
            :Memeber variable mtl_ambient       : Ambient intensity of the Blender material object.
            :Memeber variable mtl_mirror_color  : Ambient color of the Blender material object.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the ambient related data 
            values of the material object onto file in format 
            "mtl_mirror_color 0 0 0\\nmtl_ambient 0\\n"
            Example: "mtl_mirror_color 0 0 0\\nmtl_ambient 0\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "mtl_mirror_color "
        final_str += str(eval(format(self.mtl_mirror_color[0], '.6f'))) \
                     + " " + \
                     str(eval(format(self.mtl_mirror_color[1], '.6f'))) \
                     + " " + \
                     str(eval(format(self.mtl_mirror_color[2], '.6f'))) + '\n'
        final_str += "mtl_ambient "
        final_str += str(self.mtl_ambient) + '\n'
        return final_str
    
    # --------------------------------------------------------------------------
    # mtl_diffuse_color, mtl_diffuse_intensity
    # --------------------------------------------------------------------------
    def get_material_diffuse_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function generates the diffuse related data 
        values of the material object into strings to be exported to file.

        This component is commonly refer to "Kd" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component into multiple component values: 
        "mtl_diffuse_color", "mtl_diffuse_intensity".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the diffuse related 
        data values of the material object intialized in this WYMaterial object.
            :Memeber variable mtl_diffuse_color             : Diffuse color of the Blender material object.
            :Memeber variable mtl_diffuse_intensity         : Diffuse intensity of the Blender material object.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the diffuse related 
            data values of the material object onto file in format 
            "mtl_diffuse_color 0 0 0\\nmtl_diffuse_intensity 0\\n"
            Example: "mtl_diffuse_color 0 0 0\\nmtl_diffuse_intensity 0\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "mtl_diffuse_color "
        final_str += str(eval(format(self.mtl_diffuse_color[0], '.6f'))) \
                     + " " + \
                     str(eval(format(self.mtl_diffuse_color[1], '.6f'))) \
                     + " " + \
                     str(eval(format(self.mtl_diffuse_color[2], '.6f'))) + '\n'
        final_str += "mtl_diffuse_intensity "
        final_str += str(self.mtl_diffuse_intensity) + '\n'
        return final_str
    # --------------------------------------------------------------------------
    # mtl_specular_color, mtl_specular_intensity, mtl_specular_hardness
    # --------------------------------------------------------------------------
    def get_material_specular_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function generates the specular related data 
        values of the material object into strings to be exported to file.

        This component is commonly refer to "Ks" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component into multiple component values: 
        "mtl_specular_color", "mtl_specular_intensity", "mtl_specular_hardness".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the specular related 
        data values of the material object intialized in this WYMaterial object.
            :Memeber variable mtl_specular_color            : Specular color of the Blender material object.
            :Memeber variable mtl_specular_intensity        : Specular intensity of the Blender material object.
            :Memeber variable mtl_specular_hardness         : Specular hardness of the Blender material object.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the specular related 
            data values of the material object onto file in format 
            "mtl_specular_color 0 0 0\\nmtl_specular_intensity 0\\nmtl_specular_hardness 0 \\n"
            Example: "mtl_specular_color 0 0 0\\nmtl_specular_intensity 0\\nmtl_specular_hardness 0 \\n"
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "mtl_specular_color "
        final_str += str(eval(format(self.mtl_specular_color[0], '.6f'))) \
                     + " " + \
                     str(eval(format(self.mtl_specular_color[1], '.6f'))) \
                     + " " + \
                     str(eval(format(self.mtl_specular_color[2], '.6f'))) + '\n'
        final_str += "mtl_specular_intensity "
        final_str += str(self.mtl_specular_intensity) + '\n'
        final_str += "mtl_specular_hardness "
        final_str += str(self.mtl_specular_hardness) + '\n'
        return final_str
    # --------------------------------------------------------------------------
    # mtl_emit
    # --------------------------------------------------------------------------
    def get_material_emissive_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function generates the emissive intensity
        value of the material object into strings to be exported to file.

        This component is commonly refer to "Ke" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component as "mtl_emit".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the emissive intensity
        value of the material object intialized in this WYMaterial object.
            :Memeber variable mtl_emit                      : Emissive intensity of the Blender material object.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the emissive intensity
            value of the material object onto file in format 
            "mtl_emit 0\\n"
            Example: "mtl_emit 0\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "mtl_emit "
        final_str += str(self.mtl_emit) + '\n'
        return final_str
    # --------------------------------------------------------------------------
    # mtl_alpha
    # --------------------------------------------------------------------------
    def get_material_alpha_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function generates the alpha
        value of the material object into strings to be exported to file.

        This component is commonly refer to "d" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component as "mtl_alpha".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the alpha
        value of the material object intialized in this WYMaterial object.
            :Memeber variable mtl_alpha                     : Alpha value of the Blender material object.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the alpha
            value of the material object onto file in format 
            "mtl_alpha 0\\n"
            Example: "mtl_alpha 0\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "mtl_alpha "
        final_str += str(self.mtl_alpha) + '\n'
        return final_str
    # --------------------------------------------------------------------------
    # mtl_raytrace_transparency_ior
    # --------------------------------------------------------------------------
    def get_material_refraction_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function generates the refraction index
        value of the material object into strings to be exported to file.

        This component is commonly refer to "Ni" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component as "mtl_raytrace_transparency_ior".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the refraction index
        value of the material object intialized in this WYMaterial object.
            :Memeber variable mtl_alpha                     : Alpha value of the Blender material object.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the refraction index
            value of the material object onto file in format 
            "mtl_raytrace_transparency_ior 0\\n"
            Example: "mtl_raytrace_transparency_ior 0\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "mtl_raytrace_transparency_ior "
        final_str += str(self.mtl_raytrace_transparency_ior) + '\n'
        return final_str
    # --------------------------------------------------------------------------
    # mtl_texture_map_image_path
    # --------------------------------------------------------------------------
    def get_material_texture_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMaterial sub member function generates the texture image file path 
        string value of the material object into strings to be exported to file.

        This component is commonly refer to "map_Kd" component in standard MTL 
        file, but for more accurate data transfer and clear naming conventions,
        I named the component as "mtl_texture_map_image_path".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the texture image file path 
        string value of the material object intialized in this WYMaterial object.
            :Memeber variable mtl_texture_map_image_path    : Texture image file path mapped onto the of the Blender mesh object.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the texture image file 
            path string value of the material object onto file in format 
            "mtl_texture_map_image_path ""\\n"
            Example: "mtl_texture_map_image_path "texture.png"\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "mtl_texture_map_image_path "
        final_str += str(self.mtl_texture_map_image_path) + '\n'
        return final_str
        