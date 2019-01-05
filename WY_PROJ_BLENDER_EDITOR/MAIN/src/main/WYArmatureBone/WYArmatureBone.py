################################################################################
# Project Name          	: WY_PROJ_BLENDER_EDITOR
# File Name             	: WYArmatureBone.py
# Project Headquarter   	: https://docs.google.com/document/d/1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit#
# Test Plan Headquarter 	: https://docs.google.com/document/d/1wlFujpygsVKtqiz596ZdD1sCeUPkpIgr1lNlE_GN-_w/edit#
# WYArmatureBone test plan  : https://docs.google.com/document/d/1ZQGmTFJd7uM8kiD-DpapyqVceUK8g_70mILnPidQ5hI/edit#
# Lead Programmer       	: Samil Chai
# Junior Programmer     	: Nick Jang
# Time                  	: 
# Description           	: 
################################################################################

import bpy
import bmesh

filename = os.getcwd() + "\\..\\..\\main\\WYModel\\WYModel.py" 
exec(compile(open(filename).read(), filename, 'exec')) # Import WYModel.py

class WYArmatureBone:
    '''
    This class represents the armature bone object which contains the 
    data values to export a Blender armature bone object to file.
    
    WYArmatureBone contans all the armature bone related data which are kept 
    by the Blender API ArmatureBone object, it holds data such as bone head, 
    tail coordinate values and mesh object vertex group information that 
    is mapped onto this armature bone object. 

    .. seealso:: ../WYArmature/WYArmature.py
    .. seealso:: ../WYUtil/WYUtil.py
    .. seealso:: ../WYCoordsys/WYCoordsys.py

    ----------------------------------------------------------------------------
    Member variables:
    ----------------------------------------------------------------------------
    :Memeber variable main_wymodel_obj              : WYModel object which contains the mesh object that is mapped onto the armature.
    :Memeber variable main_armature_bone_obj        : Blender armature bone object to retrieve data from.
    :Memeber variable parent_armature_bone_obj      : Blender parent armature bone object.
    :Memeber variable armature_bone_name            : Name of the Blender armature bone object initalized as member variable "main_armature_bone_obj"
    :Memeber variable armature_bone_parent_name     : Name of the Blender parent armature bone object initalized as member variable "parent_armature_bone_obj"
    :Memeber variable armature_bone_head            : Head vertex coordinate of the Blender armature bone object initalized as member variable "main_armature_bone_obj"
    :Memeber variable armature_bone_tail            : Tail vertex coordinate of the Blender armature bone object initalized as member variable "main_armature_bone_obj
    :Memeber variable armature_vertex_group_array   : Vertex group data collection of the Blender armature bone object initalized as member variable "main_armature_bone_obj

    ----------------------------------------------------------------------------
    Member functions:
    ----------------------------------------------------------------------------
    # def __init__(self, main_armature_bone_obj=None, main_wymodel_obj=None):
        Test: https://docs.google.com/spreadsheets/d/1MC218ko9UxX4YkKIOf1Agodppb4JzBpQ02oL4k5KdwI/edit#gid=0
    # def __eq__(self, other):
        Test: https://docs.google.com/spreadsheets/d/1_XasY5N2VQtWpjnLEsYRtC6z-3mKMXbssd0ZjZJa6_w/edit#gid=0 
    # def __str__(self):
        Test: https://docs.google.com/spreadsheets/d/1_OBC90d6hh9Q_dE5DRoFAK71cdgb7jTrUa9bqvL0Xmg/edit#gid=0 
    # def init_armature_bone_data(self):
        Test: https://docs.google.com/spreadsheets/d/1_TCXNSIltBXBYv-m0DuH0fwBO9fvn7wdeBVXDCeH9D8/edit#gid=0
    # def init_wyarmaturebone_elements(self):
        Test: https://docs.google.com/spreadsheets/d/1STTl0Kf8irazNBt_762BTvzPyrqIxnMigwCBzAkyh2E/edit#gid=0
    # def init_armature_bone_name(self):
        Test: https://docs.google.com/spreadsheets/d/1y2yIXis2isP5Vy62ZjSNg0gh0QdSqKCSol9sVj7PKvo/edit#gid=0
    # def init_armature_bone_parent_name(self):
        Test: https://docs.google.com/spreadsheets/d/1y2yIXis2isP5Vy62ZjSNg0gh0QdSqKCSol9sVj7PKvo/edit#gid=0 
    # def init_armature_bone_head(self):
        Test: https://docs.google.com/spreadsheets/d/1EagRk30QzBdVjAxZcYM_eYiPBKFHCpgq25WTON5wqIY/edit#gid=0 
    # def init_armature_bone_tail(self):
        Test: https://docs.google.com/spreadsheets/d/1uJHrNMEnRMnCJ_4PKtvts5r0RqE1N1Wi3IlfkHkXvZE/edit#gid=0
    # def init_armature_bone_vertex_group_data(self):
        Test: https://docs.google.com/spreadsheets/d/18XwcNsCIq3AK0-nUY0SaL_6iFaZZgIoJJsXYh_bXJJM/edit#gid=0 
    # def get_armature_bone_bn_str(self):
        Test: https://docs.google.com/spreadsheets/d/1Odqi_429IzUQqqibODZv1AvAuCaf4dBunUNYFhhHWzg/edit#gid=0
    # def get_armature_bone_pbn_str(self):
        Test: https://docs.google.com/spreadsheets/d/11Mc5Z-q6rUJqCemSxTEHMfIem35Bg_AOSGhxnB5rByM/edit#gid=0 
    # def get_armature_bone_bh_str(self):
        Test: https://docs.google.com/spreadsheets/d/13z1EKAMnQAbAnNwpWI4PCS1Oq-8_gl96ILvyYW3YSC8/edit#gid=0 
    # def get_armature_bone_bt_str(self):
        Test: https://docs.google.com/spreadsheets/d/1iMXFcS5lkwqICgFgGjH20msuw1lvfegkcNSR68zHLk8/edit#gid=0
    # def get_armature_bone_vg_str(self):
        Test: https://docs.google.com/spreadsheets/d/1a1xZYZyCnfdBPkdeLsNJgavulGUAVRegfNgFgvg4o0s/edit#gid=0

    '''
    def __init__(self, main_armature_bone_obj=None, main_wymodel_obj=None):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone general constructor.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Initialize the member variables using the values passed into the 
        allocation call.

        Initializing member varibles:
            :Memeber variable main_wymodel_obj              : WYModel object which contains the mesh object and coordinate export option WYCoordsys object that is mapped onto the armature.
            :Memeber variable main_armature_bone_obj        : Blender armature bone object to retrieve data from.
            :Memeber variable parent_armature_bone_obj      : Blender parent armature bone object.
            :Memeber variable armature_bone_name            : Name of the Blender armature bone object initalized as member variable "main_armature_bone_obj"
            :Memeber variable armature_bone_parent_name     : Name of the Blender parent armature bone object initalized as member variable "parent_armature_bone_obj"

        Calling sub function: init_wyarmaturebone_elements()
        Sub function: init_wyarmaturebone_elements()
            This function initializes the member variable with default values 
            which will be holding the major information data values:
                :Memeber variable armature_bone_head            : Head vertex coordinate of the Blender armature bone object initalized as member variable "main_armature_bone_obj"
                :Memeber variable armature_bone_tail            : Tail vertex coordinate of the Blender armature bone object initalized as member variable "main_armature_bone_obj
                :Memeber variable armature_vertex_group_array   : Vertex group data collection of the Blender armature bone object initalized as member variable "main_armature_bone_obj

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
        :return : Allocated and initialized WYArmatureBone object.
        :rtype  : WYArmatureBone.
        '''
        # WYModel object that this armature bone is mapped onto.
        self.main_wymodel_obj = main_wymodel_obj
        # Current Blender armature bone object.
        self.main_armature_bone_obj = main_armature_bone_obj
        # Parent Blender armature bone object.
        if main_armature_bone_obj != None:
            self.parent_armature_bone_obj = main_armature_bone_obj.parent
        else:
            self.parent_armature_bone_obj = None

        # Call sub function to intialize the main armature bone elements 
        # with default values to hold the armature bone data with.
        self.init_wyarmaturebone_elements()

    def __eq__(self, other):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone overrided equal function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Compares the member variables with the memeber variables intialized 
        in "other" object return True if these 2 object has all the member 
        variables same values else return False.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  other: Second WYArmatureBone object to compare with.
        :type   other: WYArmatureBone
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Return the result of comparison between 2 objects.
        :rtype: boolean

        '''
        if other == None:
            return False
        return (self.main_wymodel_obj == other.main_wymodel_obj and \
                self.main_armature_bone_obj == other.main_armature_bone_obj and \
                self.parent_armature_bone_obj == other.parent_armature_bone_obj and \
                self.armature_bone_name == other.armature_bone_name  and \
                self.armature_bone_parent_name == other.armature_bone_parent_name and \
                self.armature_bone_head == other.armature_bone_head and \
                self.armature_bone_tail == other.armature_bone_tail and \
                self.armature_vertex_group_array == \
                    other.armature_vertex_group_array)

    def __str__(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone toString function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Manipulate the string to represent the current WYArmatureBone object 
        in the file using the values initialized when allocated.

        This function acts like toString function in Java so when I print the 
        WYArmatureBone object directly, so when WYArmatureBone is exported 
        WYArmatureBone wil be printed directly through file stream and the 
        information about this WYArmatureBone object will be printed to file 
        with following sample format:
            --------------------------------------------------------------------
            bn Bone
            bt 0.0 0.0 -0.0
            bh -0.4515 0.0 -2.5605
            {
            vi 8
            v -0.5000 -0.6722 -0.6463
            vw 1.0000
            }
            --------------------------------------------------------------------

        This string is manipulated with following member variables initialized 
        onto this WYMesh object:
            :Memeber variable main_wymodel_obj              : WYModel object which contains the mesh object that is mapped onto the armature.
            :Memeber variable main_wymesh_obj               : WYMesh object that contains the data value of the mesh that is mapped onto the armature.
            :Memeber variable main_mesh_obj                 : Blender mesh object that is mapped onto the armature initialized inside WYMesh object inside WYModel object passed into the allocation call.
            :Memeber variable main_armature_bone_obj        : Blender armature bone object to retrieve data from.
            :Memeber variable parent_armature_bone_obj      : Blender parent armature bone object.
            :Memeber variable armature_bone_name            : bn - Name of the Blender armature bone object initalized as member variable "main_armature_bone_obj"
            :Memeber variable armature_bone_parent_name     : pbn - Name of the Blender parent armature bone object initalized as member variable "parent_armature_bone_obj"
            :Memeber variable armature_bone_head            : bh - Head vertex coordinate of the Blender armature bone object initalized as member variable "main_armature_bone_obj"
            :Memeber variable armature_bone_tail            : bt - Tail vertex coordinate of the Blender armature bone object initalized as member variable "main_armature_bone_obj
            :Memeber variable armature_vertex_group_array   : vg - Vertex group data collection of the Blender armature bone object initalized as member variable "main_armature_bone_obj

        Calling sub function: get_armature_bone_bn_str()
            Generate string: bn      ""
        Calling sub function: get_armature_bone_pbn_str()
            Generate string: pbn     ""
        Calling sub function: get_armature_bone_bh_str()
            Generate string: bh      0 0 0
        Calling sub function: get_armature_bone_bt_str()
            Generate string: bt      0 0 0
        Calling sub function: get_armature_bone_vg_str()
            Generate string: vg      {v,vi,vw}
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Final string representing this WYArmatureBone object
                           to be exported to files.
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += self.get_armature_bone_bn_str()
        final_str += self.get_armature_bone_pbn_str()
        if self.main_wymodel_obj != None:
            final_str += str(self.main_wymodel_obj.main_wymesh.wycoordsys)
        final_str += self.get_armature_bone_bh_str()
        final_str += self.get_armature_bone_bt_str()
        final_str += self.get_armature_bone_vg_str()
        return final_str

    def init_armature_bone_data(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone member function initializes the Blender armature bone 
        object data values into WYArmatureBone member variables.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the following member variables with the actual
        Blender armature bone object data values by calling multiple 
        sub functions:
        Calling sub function: WYArmatureBone::init_armature_bone_name()
            :Memeber variable armature_bone_name            : Name of the Blender armature bone object initalized as member variable "main_armature_bone_obj"
        Calling sub function: WYArmatureBone::init_armature_bone_parent_name()
            :Memeber variable armature_bone_parent_name     : Name of the Blender parent armature bone object initalized as member variable "parent_armature_bone_obj"
        Calling sub function: WYArmatureBone::init_armature_bone_head()
            :Memeber variable armature_bone_head            : bh - Head vertex coordinate of the Blender armature bone object initalized as member variable "main_armature_bone_obj"
        Calling sub function: WYArmatureBone::init_armature_bone_tail()
            :Memeber variable armature_bone_tail            : bt - Tail vertex coordinate of the Blender armature bone object initalized as member variable "main_armature_bone_obj
        Calling sub function: WYArmatureBone::init_armature_bone_vertex_group_data()
            :Memeber variable armature_vertex_group_array   : vg - Vertex group data collection of the Blender armature bone object initalized as member variable "main_armature_bone_obj
        '''
        # bn - Armature bone name.
        self.init_armature_bone_name()
        # pbn - Armature parent bone name.
        self.init_armature_bone_parent_name()
        # bh - Armature bone head vertex coordinate.
        self.init_armature_bone_head()
        # bt - Armature bone tail vertex coordinate.
        self.init_armature_bone_tail()
        # vg {v,vi,vw)
        self.init_armature_bone_vertex_group_data()

    def init_wyarmaturebone_elements(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone member function initializes the member variables 
        with default values when allocated.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variables with default values
            :Memeber variable armature_bone_name            : ""
            :Memeber variable armature_bone_parent_name     : ""
            :Memeber variable armature_bone_head            : [0,0,0]
            :Memeber variable armature_bone_tail            : [0,0,0]
            :Memeber variable armature_vertex_group_array   : Defautl value [] 

        '''
        # bn - Armature bone name.
        self.armature_bone_name = ""
        # pbn - Armature bone parent name.
        self.armature_bone_parent_name = ""

        # bh - Armature bone head vertex coordinate.
        self.armature_bone_head = [0,0,0]
        # bt - Armature bone tail vertex coordinate.
        self.armature_bone_tail = [0,0,0]

        # vg {
        # v     - Vertex coordinate.
        # vi    - Vertex index.
        # vw    - Vertex weight.
        # }
        self.armature_vertex_group_array = []

    def init_armature_bone_name(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone sub member function initializes the Blender armature bone
        object name value into WYArmatureBone member variable 
        "armature_bone_name".

        :Post-condition: 
            Member variable "armature_bone_name" is initialized with the
            name value using the data inside armature bone object 
            initialized as member variable "main_armature_bone_obj".
            
            :Memeber variable armature_bone_name            : Name of the Blender armature bone object initalized as member variable "main_armature_bone_obj"
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "armature_bone_name" with 
        the actual Blender armature bone object name value by 
        retreiving the "name" value initialized inside member variable 
        "main_armature_bone_obj".
            :Memeber variable main_armature_bone_obj        : Blender armature bone object to retrieve data from.
        '''
        # bn - Armature bone name.
        if self.main_armature_bone_obj != None:
            self.armature_bone_name = self.main_armature_bone_obj.name

    def init_armature_bone_parent_name(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone sub member function initializes the Blender armature bone
        object parent bone name value into WYArmatureBone member variable 
        "armature_bone_head".

        :Post-condition: 
            Member variable "armature_bone_head" is initialized with the
            parent bone name value using the data inside armature bone object 
            initialized as member variable "main_armature_bone_obj".
            
            :Memeber variable armature_bone_parent_name     : Name of the Blender parent armature bone object initalized as member variable "parent_armature_bone_obj"
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "armature_bone_head" with 
        the actual Blender armature bone object parent bone name value by 
        retreiving the "name" value initialized inside member variable 
        "parent_armature_bone_obj".
            :Memeber variable parent_armature_bone_obj      : Blender parent armature bone object.
        '''
        # pbn - Armature bone parent name.
        if self.parent_armature_bone_obj != None:
            self.armature_bone_parent_name = self.parent_armature_bone_obj.name

    def init_armature_bone_head(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone sub member function initializes the Blender armature bone
        object head coordinate value into WYArmatureBone member variable 
        "armature_bone_head".

        :Post-condition: 
            Member variable "armature_bone_head" is initialized with the
            head coordinate value using the data inside armature bone object 
            initialized as member variable "main_armature_bone_obj".

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "armature_bone_head" with 
        the actual Blender armature bone object head coordinate value by 
        retreiving the "head_local" value initialized inside member variable 
        "main_armature_bone_obj".
            :Memeber variable main_armature_bone_obj        : Blender armature bone object to retrieve data from.
        
        '''
        self.armature_bone_head = self.main_armature_bone_obj.head_local

    def init_armature_bone_tail(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone sub member function initializes the Blender armature bone
        object tail coordinate value into WYArmatureBone member variable 
        "armature_bone_tail".

        :Post-condition: 
            Member variable "armature_bone_tail" is initialized with the
            tail coordinate value using the data inside armature bone object 
            initialized as member variable "main_armature_bone_obj".

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "armature_bone_tail" with 
        the actual Blender armature bone object tail coordinate values by 
        retreiving the "tail_local" value initialized inside member variable 
        "main_armature_bone_obj".
            :Memeber variable armature_bone_tail            : Tail vertex coordinate of the Blender armature bone object initalized as member variable "main_armature_bone_obj
        '''
        self.armature_bone_tail = self.main_armature_bone_obj.tail_local

    def init_armature_bone_vertex_group_data(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone sub member function initializes the Blender armature bone
        object corresponding mesh object's vertex groups that is mapped onto 
        current armature bone into WYArmatureBone member variable array
        "armature_vertex_group_array".

        :Post-condition: 
            Member variable "armature_vertex_group_array" is initialized with 
            the vertex coordiante values that this armature bone is mapped onto, 
            using the data inside mesh object initialized as member 
            variable "main_wymodel_obj".

        Vertex group array element:
            Description: [Vertex index, Vertex coordinate, Vertex weight]
            Type:        [int,          Vector(()),        float]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable 
        "armature_vertex_group_array" with the actual Blender mesh object 
        vertex coordinate values which current armature bone is mapped onto,
        retreiving the "vertices" value initialized inside member variable 
        "main_wymodel_obj.data" and collects the vertices which have the vertex
        group index that this armature bone is referenced with to be hold by 
        current armature bone object.
            :Memeber variable armature_vertex_group_array   : Vertex group data collection of the Blender armature bone object initalized as member variable "main_armature_bone_obj
        '''
        # Check if mesh mapped onto current armature object is valid.
        if self.main_wymodel_obj != None:
            # Loop through vertices inside current mesh object that is mapped 
            # onto current armature bone object.
            for vert in self.main_wymodel_obj.main_wymesh.main_mesh_obj.\
                data.vertices:
                for v in vert.groups:
                    # Get the vertex group index of vertices mapped onto 
                    # current armature bone name.
                    vert_group_index = self.main_wymodel_obj.\
                        main_wymesh.main_mesh_obj.vertex_groups[ \
                        self.armature_bone_name].index
                    if v.group == vert_group_index:
                        # Convert vertex coordinate into export format.
                        resultVertex = self.main_wymodel_obj.\
                            main_wymesh.wycoordsys.export_coordconversion(
                                vert.co.x,vert.co.y,vert.co.z)    
                        # Vertex group vertex index.
                        vertexIndex = vert.index
                        # Vertex group vertex coordinate.
                        vertexCoord = resultVertex

                        # Vertex group vertex weight.
                        vertexWeight = eval(format(v.weight, '.4f'))

                        # Append vertex data to the vertex group array data 
                        # structure.
                        self.armature_vertex_group_array.append(
                            [vertexIndex, vertexCoord, vertexWeight])


    def get_armature_bone_bn_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone sub member function generates the name of the armature 
        bone object into strings to be exported to file.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the name of the armature 
        bone object intialized in this WYArmatureBone object.
            :Memeber variable armature_bone_name            : Name of the Blender armature bone object initalized as member variable "main_armature_bone_obj"
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the name of the armature 
            bone object onto file in format "bn [Name]\\n"
            Example: "bn bone\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        if self.main_armature_bone_obj != None:
            final_str += "bn "
            final_str += self.armature_bone_name + '\n'

        return final_str

    def get_armature_bone_pbn_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone sub member function generates the name of the parent 
        armature bone object into strings to be exported to file.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the name of the parent 
        armature bone object intialized in this WYArmatureBone object.
            :Memeber variable armature_bone_parent_name     : Name of the Blender parent armature bone object initalized as member variable "parent_armature_bone_obj"
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the name of the armature 
            bone object onto file in format "pbn [Name]\\n"
            Example: "pbn parent_bone\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        if self.main_armature_bone_obj != None and \
            self.armature_bone_parent_name != "":
            final_str += "pbn "
            final_str += self.armature_bone_parent_name + '\n'
        return final_str

    def get_armature_bone_bh_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone sub member function generates the head coordinate of the 
        armature bone object into strings to be exported to file.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the head coordinate of the
        armature bone object intialized in this WYArmatureBone object.
            :Memeber variable armature_bone_head            : Head vertex coordinate of the Blender armature bone object initalized as member variable "main_armature_bone_obj"
            :Memeber variable armature_bone_tail            : Tail vertex coordinate of the Blender armature bone object initalized as member variable "main_armature_bone_obj
                
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the head coordinate 
            of the armature bone object onto file in format "bh [Head]\\n"
            Example: "bh 0 0 0\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "bh "
        final_str += str(eval(format(self.armature_bone_head[0], '.4f'))) + " " + \
                str(eval(format(self.armature_bone_head[1], '.4f'))) + " " +  \
                str(eval(format(self.armature_bone_head[2], '.4f'))) + "\n"
        return final_str

    def get_armature_bone_bt_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone sub member function generates the tail coordinate of the 
        armature bone object into strings to be exported to file.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the tail coordinate of the
        armature bone object intialized in this WYArmatureBone object.
            :Memeber variable armature_bone_tail            : Tail vertex coordinate of the Blender armature bone object initalized as member variable "main_armature_bone_obj
                
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the tail coordinate 
            of the armature bone object onto file in format "bt [Tail]\\n"
            Example: "bt 0 0 0\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "bt "
        final_str += str(eval(format(self.armature_bone_tail[0], '.4f'))) + " " + \
                     str(eval(format(self.armature_bone_tail[1], '.4f'))) + " " +  \
                     str(eval(format(self.armature_bone_tail[2], '.4f'))) + "\n"
        return final_str

    def get_armature_bone_vg_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYArmatureBone sub member function generates the vertex group data 
        values of the mesh mapped onto this armature bone object into strings 
        to be exported to file.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the vertex group data 
        values of the mesh mapped onto this armature bone object 
        intialized in this WYArmatureBone object.
            :Memeber variable armature_vertex_group_array   : Vertex group data collection of the Blender armature bone object initalized as member variable "main_armature_bone_obj
                
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the vertex group data 
            values of the mesh mapped onto this armature bone object onto file 
            in format "vg {\\n vi 0\\n v 0 0 0\\n vw 0\\n}\\n"
            Example: "
                vg {
                vi 0
                v 0 0 0
                vw 0
                }"
        :rtype  final_str: string
        '''
        final_str = ""
        if len(self.armature_vertex_group_array) > 0:
            final_str += "vg {\n"
            for i in range(0, len(self.armature_vertex_group_array)):
                final_str += "vi " + str(self.armature_vertex_group_array[i][0]) \
                             + "\n"
                final_str += "v " + \
                             str(eval(format(self.armature_vertex_group_array[i][1][0], '.4f'))) + \
                             " " + \
                             str(eval(format(self.armature_vertex_group_array[i][1][1], '.4f')))  + \
                             " " + \
                             str(eval(format(self.armature_vertex_group_array[i][1][2], '.4f')))  + "\n"
                final_str += "vw " + str(self.armature_vertex_group_array[i][2]) \
                             + "\n"
            final_str += "}\n"
        return final_str

    
    
    
