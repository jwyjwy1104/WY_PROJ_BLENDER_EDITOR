################################################################################
# Project Name          	: WY_PROJ_BLENDER_EDITOR
# File Name             	: WYMesh.py
# Project Headquarter   	: https://docs.google.com/document/d/1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit#
# Test Plan Headquarter 	: https://docs.google.com/document/d/1wlFujpygsVKtqiz596ZdD1sCeUPkpIgr1lNlE_GN-_w/edit#
# WYMesh Test Plan      	: https://docs.google.com/document/d/1_orI3u_VWgKNfvp87C2YVKqGJhUbi6D9fN3SbKi5flE/edit#
# Lead Programmer       	: Samil Chai
# Junior Programmer     	: Nick Jang
# Time                  	: 
# Description           	: 
#
################################################################################

import bpy
import os
import bmesh
from mathutils import Vector, geometry

filename = os.getcwd() + "\\..\\..\\main\\WYCoordsys\\WYCoordsys.py" 
exec(compile(open(filename).read(), filename, 'exec')) # Import WYCoordsys.py
filename = os.getcwd() + "\\..\\..\\main\\WYUtil\\WYUtil.py"
exec(compile(open(filename).read(), filename, 'exec')) # Import WYUtil.py

class WYMesh:
    '''
    This class represents the mesh object which contains the data values to
    export a Blender mesh object to file.
    
    WYModel contains a WYMesh and a WYMaterial object to manage all the model  
    data collection in a single class object.
        
    WYMesh contans all the mesh related data which are kept by the Blender 
    API Mesh object, it holds data such as vertices, texture coordinates and   
    indices values and most importantly the mesh indices must be exported  
    with triangulated faces.

    .. seealso:: ../WYCoordsys/WYCoordsys.py
    .. seealso:: ../WYUtil/WYUtil.py

    ----------------------------------------------------------------------------
    Member variables:
    ----------------------------------------------------------------------------
    :Memeber variable main_mesh_obj                    : Blender model object.
    :Memeber variable main_mesh                        : Blender model's mesh object.
    :Memeber variable wycoordsys                       : WYCoordsys object for coordinate conversion.
    :Memeber variable wyutil                           : WYUtil object for utility functions.
    :Memeber variable mesh_obj_name                    : o             - Name of the mesh object to export with.
    :Memeber variable mesh_material_relfile_path       : mtllib        - Relative custom material file path if material object exist inside current mesh object to be export with.
    :Memeber variable mesh_vertex_array                : v             - Main data structure collection of vertices of current mesh object to be exported.
    :Memeber variable mesh_vertex_index_array          : f v/t/n - v   - Main data structure collection of the vertex indices of current mesh object to be exported. 
    :Memeber variable mesh_normal_array                : vn            - Main data structure collection of vertex normal vector of current mesh object to be exported.
    :Memeber variable mesh_normal_index_array          : f v/t/n - n   - Main data structure collection of the normal vector indices of current mesh object to be exported. 
    :Memeber variable mesh_texture_coord_array         : vt            - Main data structure collection of vertex coordinate of current mesh object's texture map to be exported.
    :Memeber variable mesh_texture_coord_index_array   : f v/t/n - t   - Main data structure collection of the vertex texture coordinate indices of current mesh object to be exported. 
    
    ----------------------------------------------------------------------------
    Member functions:
    ----------------------------------------------------------------------------
    # def __init__(self, main_mesh_obj=None, wycoordsys=None):
        Test: https://docs.google.com/spreadsheets/d/1hq10i_mtqwZQsoqUgK1NYzdj2447grfivi_oaOZWLXo/edit#gid=0 
    # def __eq__(self, other):
        Test: https://docs.google.com/spreadsheets/d/1goZLBWG4XIw8sAZmRV9y41Miebkf9zU3nwrai_XLyaQ/edit#gid=0
    # def __str__(self):
        Test: https://docs.google.com/spreadsheets/d/1o0NTG6H9DaJpikY6uzyjq4t_Qv7FOP0-lZJHp8nHtR0/edit#gid=0
    # def init_mesh_data(self):
        Test: https://docs.google.com/spreadsheets/d/12RJ1WW92QgIlxbhpn1XMNu7iqYqhunoE3lyDOJChtUI/edit#gid=0
    # def init_wymesh_elements(self):
        Test: https://docs.google.com/spreadsheets/d/1dAcs8SJvTzelbKzet7VFUihPEb8lTcV3W3JS2bTOKDM/edit#gid=0
    # def init_mesh_name(self):
        Test: https://docs.google.com/spreadsheets/d/1oCeJO4F-MoOnR7N14w9sqDNat1qK3_V-glas1mDKI_Q/edit#gid=0
    # def init_mesh_material_relfile_path(self, mesh_material_relfile_path):
        Test: https://docs.google.com/spreadsheets/d/10jRws5zA5c0qGz5lCvJp3amJGd1IcLWYbTsaLk0zSyk/edit#gid=0
    # def init_mesh_vertex_data(self):
        Test: https://docs.google.com/spreadsheets/d/1ty06_yMi41ax_ZL-RDoAwIf6-SJm2uOjvf5CTrPz0NQ/edit#gid=0
    # def init_mesh_vertex_index_data(self):
        Test: https://docs.google.com/spreadsheets/d/1k927e60fAU8XmKSd8-c6yv0b6kWoQ3XLCZIsZaBAHmY/edit#gid=0
    # def init_mesh_normal_data(self):
        Test: https://docs.google.com/spreadsheets/d/1OunqIDzvFqU_jY1O_js9R2qpv0bR8PN7PALmqs2LYVA/edit#gid=0
    # def init_mesh_normal_index_data(self): 
        Test: https://docs.google.com/spreadsheets/d/1MhQEt5Xg6VsyqrJum-SqgvDt7rzta4eB40HXt3uLVbo/edit#gid=0
    # def init_mesh_texcoord_data(self):
        Test: https://docs.google.com/spreadsheets/d/1fTNNYw7XjkxygkiMRd-o61FxPxtHXWPlEug6WJk-5R8/edit#gid=0
    # def init_mesh_texcoord_index_data(self):
        Test: https://docs.google.com/spreadsheets/d/1xiwysnD825hkfG2F9kHFZ2c45qYpCNT1SmI1IaK0m3U/edit#gid=0
    # def get_mesh_o_str(self):
        Test: https://docs.google.com/spreadsheets/d/1Odqi_429IzUQqqibODZv1AvAuCaf4dBunUNYFhhHWzg/edit#gid=0
    # def get_mesh_mtllib_str(self):
        Test: https://docs.google.com/spreadsheets/d/1KeJcEioO8W5wxYTNzwLVwy-YWFgT2SzbKZy05n7NqKc/edit#gid=0
    # def get_mesh_v_str(self):
        Test: https://docs.google.com/spreadsheets/d/1yHvCQYfWXn104OOkvHCYFzGGPquWeIACfXNBKgsboyE/edit#gid=
    # def get_mesh_vn_str(self):
        Test: https://docs.google.com/spreadsheets/d/1Mfa8ymWoQMN9ZBNBCUvlO4eF3vVmfPfTXLsRfBfDd3k/edit#gid=0
    # def get_mesh_vt_str(self):
        Test: https://docs.google.com/spreadsheets/d/1-tq4hcq3GERZnnFulX7--_ReoTqmczlvuCrK2i0LeP0/edit#gid=0 
    # def get_mesh_f_str(self):
        Test: https://docs.google.com/spreadsheets/d/1lTk_AoxCqi6omMa7ymKflaX5-3SMcLQcz_1RCEL4Zc4/edit#gid=0
    '''
    
    def __init__(self, main_mesh_obj=None, wycoordsys=None):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh general constructor.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Initialize the member variables using the values passed into the 
        allocation call.

        Initializing member varibles:
        :Memeber variable main_mesh_obj: Blender model object.
        :Memeber variable main_mesh    : Blender model's mesh object.
        :Memeber variable wycoordsys   : WYCoordsys object for coordinate conversion.
        :Memeber variable wyutil       : WYUtil object for utility functions.
            Allocate a WYUtil object for utility function calls. (eg. Triangulate Blender mesh object)

        Calling sub function: init_wymesh_elements()
        Sub function: init_wymesh_elements()
            This function initializes the member variable with default values 
            which will be holding the major information data values:
            :Memeber variable mesh_obj_name                    : o             - Name of the mesh object to export with.
            :Memeber variable mesh_material_relfile_path            : mtllib        - Relative custom material file path if material object exist inside current mesh object to be export with.
            :Memeber variable mesh_vertex_array                : v             - Main data structure collection of vertices of current mesh object to be exported.
            :Memeber variable mesh_vertex_index_array          : f v/t/n - v   - Main data structure collection of the vertex indices of current mesh object to be exported. 
            :Memeber variable mesh_normal_array                : vn            - Main data structure collection of vertex normal vector of current mesh object to be exported.
            :Memeber variable mesh_normal_index_array          : f v/t/n - n   - Main data structure collection of the normal vector indices of current mesh object to be exported. 
            :Memeber variable mesh_texture_coord_array         : vt            - Main data structure collection of vertex coordinate of current mesh object's texture map to be exported.
            :Memeber variable mesh_texture_coord_index_array   : f v/t/n - t   - Main data structure collection of the vertex texture coordinate indices of current mesh object to be exported. 

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param main_mesh_obj: Referenced Blender Mesh object to retrieve the mesh data values from.
        :type  main_mesh_obj: bmesh
        :param wycoordsys: WYCoordsys object which contains the user defined coordinate system export options to convert current WYMesh object's vertex corodinate values with when exported.
        :type  wycoordsys: WYCoordsys
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return : Allocated and initialized WYMesh object.
        :rtype  : WYMesh.
        '''
        #raise Exception("ERROR::WYMesh::__init__::Blender mesh object is none!!!")
        # Main Blender Mesh object to be converted to WYMesh with.
        self.main_mesh_obj = main_mesh_obj
        
        # WYUtil object to triangulate the mesh with.
        self.wyutil = WYUtil()

        # Main Blender Mesh to be used to triangulate the mesh object.
        if main_mesh_obj != None:
            self.main_mesh = main_mesh_obj.data
            
        # CU - Chosen export option UP vector.
        # CF - Chosen export option FORWARD vector.
        self.wycoordsys = wycoordsys
        
        # Call sub function to intialize the main mesh elements with 
        # default values to hold the mesh data with.
        self.init_wymesh_elements()

    #---------------------------------------------------------------------------
    # Overriden equal function.
    #---------------------------------------------------------------------------
    def __eq__(self, other):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh overrided equal function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Compares the member variables with the memeber variables intialized 
        in "other" object return True if these 2 object has all the member 
        variables same values else return False.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  other: Second WYMesh object to compare with.
        :type   other: WYMesh
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Return the result of comparison between 2 objects.
        :rtype: boolean

        '''
        if other == None:
            return False
        #self.main_mesh_obj == other.main_mesh_obj and \
        #self.main_mesh == other.main_mesh and \
         
        '''
        print(self.wycoordsys == other.wycoordsys)
        print(self.wyutil == other.wyutil)
        print(self.mesh_obj_name == other.mesh_obj_name)
        print(self.mesh_material_relfile_path == other.mesh_material_relfile_path)
        print(self.mesh_vertex_array == other.mesh_vertex_array)
        print(self.mesh_vertex_index_array == other.mesh_vertex_index_array)
        print(self.mesh_normal_array == other.mesh_normal_array)
        print(self.mesh_normal_index_array == other.mesh_normal_index_array)
        print(self.mesh_texture_coord_array == other.mesh_texture_coord_array)
        print(self.mesh_texture_coord_index_array == other.mesh_texture_coord_index_array)
        '''

        return (self.wycoordsys == other.wycoordsys and \
                self.wyutil == other.wyutil and \
                self.mesh_obj_name == other.mesh_obj_name  and \
                self.mesh_material_relfile_path == other.mesh_material_relfile_path and \
                self.mesh_vertex_array == other.mesh_vertex_array and \
                self.mesh_vertex_index_array == \
                    other.mesh_vertex_index_array and \
                self.mesh_normal_array == other.mesh_normal_array and \
                self.mesh_normal_index_array == \
                    other.mesh_normal_index_array and \
                self.mesh_texture_coord_array == \
                    other.mesh_texture_coord_array and \
                self.mesh_texture_coord_index_array == \
                    other.mesh_texture_coord_index_array)

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
             o      ""
             mtllib ""
             v      0/0/0
             v      0/0/0
             v      0/0/0
             vt     0/0
             vt     0/0
             vt     0/0
             vt     0/0
             vn     0/0/0
             vn     0/0/0
             vn     0/0/0
             vn     0/0/0
             f      v1/t1/n1 v2/t2/n2 v3/t3/n3
             f      v1/t1/n1 v2/t2/n2 v3/t3/n3
             f      v1/t1/n1 v2/t2/n2 v3/t3/n3
             -------------------------------------------------------------------

        This string is manipulated with following member variables initialized 
        onto this WYMesh object:
            :Memeber variable main_mesh_obj: Blender model object.
            :Memeber variable main_mesh    : Blender model's mesh object.
            :Memeber variable wycoordsys   : WYCoordsys object for coordinate conversion.
            :Memeber variable wyutil       : WYUtil object for utility functions.
            :Memeber variable mesh_obj_name                    : o             - Name of the mesh object to export with.
            :Memeber variable mesh_material_relfile_path            : mtllib        - Relative custom material file path if material object exist inside current mesh object to be exported with.
            :Memeber variable mesh_vertex_array                : v             - Main data structure collection of vertices of current mesh object to be exported.
            :Memeber variable mesh_vertex_index_array          : f v/t/n - v   - Main data structure collection of the vertex indices of current mesh object to be exported. 
            :Memeber variable mesh_normal_array                : vn            - Main data structure collection of vertex normal vector of current mesh object to be exported.
            :Memeber variable mesh_normal_index_array          : f v/t/n - n   - Main data structure collection of the normal vector indices of current mesh object to be exported. 
            :Memeber variable mesh_texture_coord_array         : vt            - Main data structure collection of vertex coordinate of current mesh object's texture map to be exported.
            :Memeber variable mesh_texture_coord_index_array   : f v/t/n - t   - Main data structure collection of the vertex texture coordinate indices of current mesh object to be exported. 

        Calling sub function: get_mesh_o_str()
            Generate string: o      ""
        Calling sub function: get_mesh_mtllib_str()
            Generate string: mtllib ""
        Calling sub function: get_mesh_v_str()
            Generate string: v      0/0/0
        Calling sub function: get_mesh_vn_str()
            Generate string: vt     0/0
        Calling sub function: get_mesh_vt_str()
            Generate string: vn     0/0/0
        Calling sub function: get_mesh_f_str()
            Generate string: f      v1/t1/n1 v2/t2/n2 v3/t3/n3
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Final string representing this WYMesh object to be exported to files.
        :rtype  final_str: string
        '''

        final_str = ""
        final_str += self.get_mesh_o_str()
        final_str += str(self.wycoordsys)
        final_str += self.get_mesh_mtllib_str()
        final_str += self.get_mesh_v_str()
        final_str += self.get_mesh_vn_str()
        final_str += self.get_mesh_vt_str()
        final_str += self.get_mesh_f_str()
        
        return final_str

    def init_mesh_data(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh member function initializes the Blender mesh object data values 
        into WYMesh member variables.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the following member variables with the actual
        Blender mesh object data values by calling multiple sub functions:
        Calling sub function: WYUtil::triangulate_mesh()
            Triangulate Blender mesh object through Blender to conver the modelling engine quadratic faces into gaming engine triangle faces.
        Calling sub function: init_mesh_name()
            :Memeber variable mesh_obj_name                    : o             - Name of the mesh object to export with.
        Calling sub function: init_mesh_vertex_data()
            :Memeber variable mesh_vertex_array                : v             - Main data structure collection of vertices of current mesh object to be exported.
        Calling sub function: init_mesh_normal_data()
            :Memeber variable mesh_normal_array                : vn            - Main data structure collection of vertex normal vector of current mesh object to be exported.
        Calling sub function: init_mesh_texcoord_data()
            :Memeber variable mesh_texture_coord_array         : vt            - Main data structure collection of vertex coordinate of current mesh object's texture map to be exported.
        Calling sub function: init_mesh_vertex_index_data()
            :Memeber variable mesh_vertex_index_array          : f v/t/n - v   - Main data structure collection of the vertex indices of current mesh object to be exported. 
        Calling sub function: init_mesh_normal_index_data()
            :Memeber variable mesh_normal_index_array          : f v/t/n - n   - Main data structure collection of the normal vector indices of current mesh object to be exported. 
        Calling sub function: init_mesh_texcorrd_index_data()
            :Memeber variable mesh_texture_coord_index_array   : f v/t/n - t   - Main data structure collection of the vertex texture coordinate indices of current mesh object to be exported. 
        '''
        # Main Blender Mesh to be used to triangulate the mesh object.
        if self.main_mesh_obj != None:
            # Triangulate the mesh object before accessing the data to export
            # using utlity funciton in WYUtil class.
            self.wyutil.triangulate_mesh(self.main_mesh)

        # o - Name of the mesh object to export with.
        self.init_mesh_name()

        # v - Vertex
        self.init_mesh_vertex_data()
        # vn - Vertex normal
        self.init_mesh_normal_data()
        # vt - Texture coordinate
        self.init_mesh_texcoord_data()
        
        # f - v/n/t
        # face - v index/vn index/vt index
        self.init_mesh_vertex_index_data()
        self.init_mesh_normal_index_data()
        self.init_mesh_texcoord_index_data()
    
    # --------------------------------------------------------------------------
    # Initialize main data structure with default values.
    # --------------------------------------------------------------------------
    def init_wymesh_elements(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh member function initializes the member variables with default
        values when allocated.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variables with default values
            :Memeber variable mesh_obj_name                    : ""
            :Memeber variable mesh_material_relfile_path            : ""
            :Memeber variable mesh_vertex_array                : Default value []
            :Memeber variable mesh_vertex_array                : Default value []
            :Memeber variable mesh_normal_array                : Default value []
            :Memeber variable mesh_texture_coord_array         : Default value []
            :Memeber variable mesh_vertex_index_array          : Default value []
            :Memeber variable mesh_normal_index_array          : Default value []
            :Memeber variable mesh_texture_coord_index_array   : Default value []

        Called by function: WYMesh::__init__()
        '''

        # o - Name of the mesh object to export with.
        self.mesh_obj_name = ""
        
        # mtllib - Relative custom material file path if material 
        #          object exist inside current mesh object to be export with.
        self.mesh_material_relfile_path = ""
        
        # v - Main data structure collection of vertices of current 
        #     mesh object to be exported.
        self.mesh_vertex_array = []
        # f v/t/n - v - Main data structure collection of the vertex 
        #               indices of current mesh object to be exported. 
        self.mesh_vertex_index_array = []
        
        # vn - Main data structure collection of vertex normal 
        #      vector of current mesh object to be exported.
        self.mesh_normal_array = []
        # f v/t/n - n - Main data structure collection of the vertex
        #               normal vector indices of current mesh object 
        #               to be exported. 
        self.mesh_normal_index_array = []
        
        # vt - Main data structure collection of vertex texture
        #      coordinate of current mesh object's texture map 
        #      to be exported.
        self.mesh_texture_coord_array = []
        # f v/t/n - t - Main data structure collection of the
        #               vertex texture coordinate indices of 
        #               current mesh object to be exported. 
        self.mesh_texture_coord_index_array = []

    def init_mesh_name(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh sub member function initializes the Blender mesh object name 
        value into WYMesh member variable "mesh_obj_name".

        :Post-condition: 
            Member variable "mesh_obj_name" is initialized with the
            name value using the data inside mesh object 
            initialized as member variable "main_mesh_obj".

        Called by function: init_mesh_data()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "mesh_obj_name" with 
        the actual Blender Mesh object name value by retrieveing the "name" 
        value inside member variable "main_mesh_obj".
            :Memeber variable main_mesh_obj             : Blender model object.
        '''
        # o - Name of the mesh object to export with.
        self.mesh_obj_name = self.main_mesh_obj.name
        
    #---------------------------------------------------------------------------
    # Set material relative file path to where current WYMesh mesh is exported 
    # to.            
    #---------------------------------------------------------------------------
    def init_mesh_material_relfile_path(self, mesh_material_relfile_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh member function setter for member variable 
        "mesh_material_relfile_path".
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function is to set the member variable "mesh_material_relfile_path" 
        outside of class.
            :Memeber variable mesh_material_relfile_path            : mtllib        - Relative custom material file path if material object exist inside current mesh object to be export with.
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param mesh_material_relfile_path: Relative custom material file path if 
            material object exist inside current mesh object to be exported with.
        :type  mesh_material_relfile_path: string
        '''
        self.mesh_material_relfile_path = mesh_material_relfile_path

    def init_mesh_vertex_data(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh sub member function initializes the Blender mesh object vertex 
        array data values into WYMesh member variable "mesh_vertex_array".

        :Pre-condition: 
            At least one vertex exist inside the mesh object initialized as 
            member variable "main_mesh".
        :Post-condition: 
            Member variable "mesh_normal_array" is initialized with the
            vertex coordinate values using the data inside mesh object 
            initialized as member variable "main_mesh".

        Called by function: init_mesh_data()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "mesh_vertex_array" with 
        the actual Blender Mesh object vertex data values by iterating through 
        Blender Mesh::vertices array and convert it into world coordinates 
        and store it inside member variable "mesh_vertex_array".
            :Memeber variable mesh_vertex_array                : v             - Main data structure collection of vertices of current mesh object to be exported.
        '''

        for v in self.main_mesh.vertices:
            vertexCoordsX = eval(str(format(v.co.x, '.4f')))
            vertexCoordsY = eval(str(format(v.co.y, '.4f')))
            vertexCoordsZ = eval(str(format(v.co.z, '.4f')))
            # Convert vertex coordinate values with the coordinate 
            # system export options.
            resultVertex = self.wycoordsys.export_coordconversion( \
                                    vertexCoordsX, \
                                    vertexCoordsY, \
                                    vertexCoordsZ)
            self.mesh_vertex_array.append(Vector(resultVertex))

    def init_mesh_vertex_index_data(self): 
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh sub member function initializes the Blender mesh object vertex 
        array indices data values into WYMesh member variable 
        "mesh_vertex_index_array".

        :Pre-condition: 
            At least one vertex exist inside the mesh object initialized as 
            member variable "main_mesh".
        :Post-condition: 
            Member variable "mesh_vertex_index_array" is initialized with the
            indices representing the index of the vertex coordinate value for  
            the vertex which forms the face of the mesh polygon.

        Called by function: init_mesh_data()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "mesh_vertex_index_array" 
        with  the actual Blender Mesh object faces indices data values by 
        iterating through Blender Mesh::polygons array and store it inside 
        member variable "mesh_vertex_index_array".
            :Memeber variable mesh_vertex_index_array          : f v/t/n - v   - Main data structure collection of the vertex indices of current mesh object to be exported. 
        
        Initialize the main data structure which holds the index value of the 
        vertices to form a single "f" element calculated using the 
        data retrieved from the main Blender mesh object.  
        '''
        # ----------------------------------------------------------------------
        # f - Index from mesh polygon faces (eg. f v/t/n)
        # ----------------------------------------------------------------------
        for faceElem in self.main_mesh.polygons:
            # ------------------------------------------------------------------
            # Vertex index (eg. f v/0/0) 
            # --> Append to "obj_vertex_index_array" as [v1, v2, v2 ... ]
            # ------------------------------------------------------------------
            self.mesh_vertex_index_array.append(faceElem.vertices[0])
            self.mesh_vertex_index_array.append(faceElem.vertices[1])
            self.mesh_vertex_index_array.append(faceElem.vertices[2])
            
    def init_mesh_normal_data(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh sub member function initializes the Blender mesh object vertex 
        normal vector array data values into WYMesh member variable 
        "mesh_normal_array".

        :Pre-condition: 
            At least one vertex exist inside the mesh object initialized as 
            member variable "main_mesh".
        :Post-condition: 
            Member variable "mesh_normal_array" is initialized with the
            vertex normal values using the data inside mesh object 
            initialized as member variable "main_mesh".

        Called by function: init_mesh_data()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "mesh_normal_array" with 
        the actual Blender Mesh object vertex normal vector data values by 
        iterating through Blender Mesh::vertices array and store it inside 
        member variable "mesh_normal_array".
            :Memeber variable mesh_normal_array                : vn            - Main data structure collection of vertex normal vector of current mesh object to be exported.
        '''
        # ----------------------------------------------------------------------
        # f - Index from mesh polygon faces (eg. f v/t/n)
        # ----------------------------------------------------------------------
        #for faceElem in self.main_mesh.polygons:
            # ------------------------------------------------------------------
            # vn - Normal vector 
            # --> Append to obj_normal_array [<Vector(0,0,0)>, ... ]
            # Normal index (eg. f 0/0/n) 
            # --> Append to obj_normal_index_array [n1, n1, n1, n2, n2, n2 ... ]
            # ------------------------------------------------------------------
            # vn - Normal vector
            #normalVector = faceElem.normal
             
        for v in self.main_mesh.vertices:
            normalVectorX = eval(str(format(v.normal[0], '.4f')))
            normalVectorY = eval(str(format(v.normal[1], '.4f')))
            normalVectorZ = eval(str(format(v.normal[2], '.4f')))
            normalVector = Vector((normalVectorX, normalVectorY, normalVectorZ))

            self.mesh_normal_array.append(normalVector)
            
    def init_mesh_normal_index_data(self): 
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh sub member function initializes the Blender mesh object vertex 
        normal vector indices data values into WYMesh member variable 
        "mesh_normal_index_array".

        :Pre-condition: 
            At least one vertex exist inside the mesh object initialized as 
            member variable "main_mesh".
        :Post-condition: 
            Member variable "mesh_normal_index_array" is initialized with the
            indices representing the index of the vertex normal value for the 
            vertex which forms the face of the mesh polygon.

        Called by function: init_mesh_data()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "mesh_normal_index_array" 
        with  the actual Blender Mesh object faces indices data values by 
        iterating through Blender Mesh::polygons array and store it inside 
        member variable "mesh_normal_index_array".
            :Memeber variable mesh_normal_index_array          : f v/t/n - n   - Main data structure collection of the normal vector indices of current mesh object to be exported. 
        
        Initialize the main data structure which holds the index value of the 
        vertex normals to form a single "f" element calculated using the 
        data retrieved from the main Blender mesh object.    
        '''
        # ----------------------------------------------------------------------
        # f - Index from mesh polygon faces (eg. f v/t/n)
        # ----------------------------------------------------------------------
        for faceElem in self.main_mesh.polygons:
            # ------------------------------------------------------------------
            # vn - Normal vector 
            # --> Append to obj_normal_array [<Vector(0,0,0)>, ... ]
            # Normal index (eg. f 0/0/n) 
            # --> Append to obj_normal_index_array [n1, n1, n1, n2, n2, n2 ... ]
            # ------------------------------------------------------------------
            # Because each vertex will have its own normal vector, the normal
            # indices would be the same as the vertex indices.
            self.mesh_normal_index_array.append(faceElem.vertices[0])
            self.mesh_normal_index_array.append(faceElem.vertices[1])
            self.mesh_normal_index_array.append(faceElem.vertices[2])
            
    def init_mesh_texcoord_data(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh sub member function initializes the Blender mesh object vertex 
        texture coordinate array data values into WYMesh member variable 
        "mesh_texture_coord_array".

        :Pre-condition: 
            At least one texture is mapped onto current mesh object initialized 
            as member variable "main_mesh".
        :Post-condition: 
            Member variable "mesh_texture_coord_array" is initialized with the
            texture coordinate values mapped onto the texture using the data 
            inside mesh object initialized as member variable "main_mesh".

        Called by function: init_mesh_data()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "mesh_texture_coord_array"  
        with the actual Blender Mesh object vertex texture coordinate data 
        values by iterating through Blender Mesh::data::uv_layers array and 
        store it inside member variable "mesh_texture_coord_array".
            :Memeber variable mesh_texture_coord_array         : vt            - Main data structure collection of vertex coordinate of current mesh object's texture map to be exported.
        '''
        if len(self.main_mesh.uv_layers) > 0:
            # -----------------------------------------------------------------
            # vt - Texture coordinates --> Append to [<Vector(0,0)>, ... ]
            # ------------------------------------------------------------------

            for uvLayer in self.main_mesh.uv_layers:
                for i in range(len(uvLayer.data)):
                    texcoordElem = uvLayer.data[i].uv
                    
                    # Append texture coordinate if not exist in the array.
                    if texcoordElem not in self.mesh_texture_coord_array:
                        self.mesh_texture_coord_array.append(texcoordElem)           
        
    def init_mesh_texcoord_index_data(self): 
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh sub member function initializes the Blender mesh object vertex 
        texture coordiante indices data values into WYMesh member variable 
        "mesh_texture_coord_array".

        :Pre-condition: 
            WYMesh::init_mesh_texcoord_data() is called, 
            Mmeber variable "mesh_texture_coord_array" is not empty.
        :Post-condition: 
            Member variable "mesh_texture_coord_index_array" is initialized 
            with the indices representing the index of the vertex texture  
            coordinate value for the vertex which forms the face of the mesh
            using the texture coordinate initialized inside 
            "mesh_texture_coord_array" after WYMesh::init_mesh_texcoord_data()
            is called. If duplicated texture coordinates are found then append
            the existing index.

        Called by function: init_mesh_data()
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function initializes the member variable "mesh_texture_coord_array" 
        with the actual Blender Mesh object faces indices data values by 
        iterating through Blender Mesh::data::uv_layers array and store it  
        inside member variable "mesh_texture_coord_array".
            :Memeber variable mesh_texture_coord_index_array   : f v/t/n - t   - Main data structure collection of the vertex texture coordinate indices of current mesh object to be exported. 

        Initialize the main data structure which holds the index value of the 
        texture coordinate to form a single "f" element calculated using the 
        data retrieved from the main Blender mesh object.     
        '''
        # Final texture coordinate index value init.
        texcoordIndex = 0
        if len(self.main_mesh.uv_layers) > 0:
            # ------------------------------------------------------------------
            # vt - Texture coordinates --> Append to [<Vector(0,0)>, ... ]
            # ------------------------------------------------------------------
            for uvLayer in self.main_mesh.uv_layers:
                for i in range(len(uvLayer.data)):
                    texcoordElem = uvLayer.data[i].uv
                    # ----------------------------------------------------------
                    # Texture coordinate index (eg. f 0/t/0) 
                    # --> Append to obj_texture_coord_index_array [t1, t2, ... ]
                    # ----------------------------------------------------------
                    
                    # if texture coordinate already exist in the array, 
                    # then save its index
                    if texcoordElem in self.mesh_texture_coord_array:
                        texcoordIndex = \
                            self.mesh_texture_coord_array.index(texcoordElem)
                        #print("texcoordIndex: " + str(texcoordIndex))
                    
                    # Texcoord index
                    self.mesh_texture_coord_index_array.append(texcoordIndex)
        
    def get_mesh_o_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh sub member function generates the name of the mesh object into 
        strings to be exported to file.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the name of the mesh object
        intialized in this WYMesh object.
            :Memeber variable mesh_obj_name                        : Name of the Blender mesh object initalized as member variable "main_mesh_obj"
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the name of the mesh 
            object onto file in format "o [Name]\\n"
            Example: "o Mesh1\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        final_str += "o "
        final_str += self.mesh_obj_name + '\n'
        return final_str

    def get_mesh_mtllib_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh sub member function generates the string to export the relative 
        file path of corresponding material file.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the relative file path of 
        WYMaterial object file which contains the material data values which 
        belongs to current WYMesh object.
            :Memeber variable mesh_material_relfile_path            : Relative custom material file path if material object exist inside current mesh object to be export with.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the relative file path of
            corresponding material file in format "mtllib [relative path]\\n"
            Example: "mtllib ./dir/WYMaterial.txt\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        if self.mesh_material_relfile_path != "":
            final_str += "mtllib "
            final_str += self.mesh_material_relfile_path + '\n'
        return final_str
    
    def get_mesh_v_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh sub member function generates the string to export the vertices 
        data values.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the vertices data values 
        inside current WYMesh object by iterating through the main data 
        structure and append the string to existing one to represent all the 
        vertices values.
            :Memeber variable mesh_vertex_array                : v             - Main data structure collection of vertices of current mesh object to be exported.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the vertices data values
            to file in format "v [vertex values]\\n"
            Example: "v 0 0 0\\n 
                      v 0 0 0\\n 
                      v 0 0 0\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        for i in range(0, len(self.mesh_vertex_array)):
            final_str += "v "
            final_str += str(self.mesh_vertex_array[i][0]) + \
                         " " + \
                         str(self.mesh_vertex_array[i][1]) + \
                         " " + \
                         str(self.mesh_vertex_array[i][2]) + "\n"
        return final_str

    def get_mesh_vn_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh sub member function generates the string to export the vertex 
        normal vector values.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the vertex normal vector 
        values inside current WYMesh object by iterating through the main data 
        structure and append the string to existing one to represent all the 
        vertex normal vector values.
            :Memeber variable mesh_normal_array                : vn            - Main data structure collection of vertex normal vector of current mesh object to be exported.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the vertex normal vector 
            values in format "vn [vertex normal vector values]\\n"
            Example: "vn 0 0 0\\n
                      vn 0 0 0\\n
                      vn 0 0 0\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        for i in range(0, len(self.mesh_normal_array)):
            final_str += "vn "
            final_str += str(format(self.mesh_normal_array[i][0], '.4f')) + \
                         " " + \
                         str(format(self.mesh_normal_array[i][1], '.4f')) + \
                         " " + \
                         str(format(self.mesh_normal_array[i][2], '.4f')) + "\n"  
        return final_str
       
    def get_mesh_vt_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh sub member function generates the string to export the vertex 
        texture coordinate values.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the vertex texture coordinate 
        values inside current WYMesh object by iterating through the main data 
        structure and append the string to existing one to represent all the 
        vertex texture coordinate values.
            :Memeber variable mesh_texture_coord_array         : vt            - Main data structure collection of vertex coordinate of current mesh object's texture map to be exported.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the vertex texture 
            coordinate values in format 
            "vt [vertex texture coordinate values]\\n"
            Example: "vt 0 0\\n
                      vt 0 0\\n
                      vt 0 0\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        for i in range(0, len(self.mesh_texture_coord_array)):
            final_str += "vt "
            final_str += str(format(self.mesh_texture_coord_array[i][0], '.4f')) \
                         + " " + \
                         str(format(self.mesh_texture_coord_array[i][1], '.4f')) \
                         + "\n"
        return final_str

    # --------------------------------------------------------------------------
    # f - Index from mesh polygon faces (eg. f v/t/n)
    # --------------------------------------------------------------------------
    def get_mesh_f_str(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYMesh sub member function generates the string to export the vertex 
        indices value which repsents a triangle, half of the face of the mesh
        object.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function generates the string to export the faces vertex indices
        values inside current WYMesh object by iterating through the main data 
        structure and append the string to existing one to represent all the 
        faces vertex indices values.
            :Memeber variable mesh_vertex_index_array          : f v/t/n - v   - Main data structure collection of the vertex indices of current mesh object to be exported. 
            :Memeber variable mesh_normal_index_array          : f v/t/n - n   - Main data structure collection of the normal vector indices of current mesh object to be exported. 
            :Memeber variable mesh_texture_coord_index_array   : f v/t/n - t   - Main data structure collection of the vertex texture coordinate indices of current mesh object to be exported. 
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return final_str: Generated string to export the faces vertex indices 
            values in format "f [face 1] [face 2] [face 3]\\n"
            Example: "f v1/t1/n1 v2/t2/n2 v3/t3/n3\\n
                      f v1/t1/n1 v2/t2/n2 v3/t3/n3\\n
                      f v1/t1/n1 v2/t2/n2 v3/t3/n3\\n"
        :rtype  final_str: string
        '''
        final_str = ""
        # ----------------------------------------------------------------------
        # Check data structure to be exported is valid
        # ----------------------------------------------------------------------
        # Boolean value to check the data structure is valid
        vertexIndexArrayInvalid = False
        texturecoordIndexArrayInvalid = False
        normalIndexArrayInvalid = False
        if len(self.mesh_vertex_index_array) <= 0:
            vertexIndexArrayInvalid = True
            #print("ERROR::Vertex coordinate index array size == 0!!!")
        if len(self.mesh_texture_coord_index_array) <= 0:
            texturecoordIndexArrayInvalid = True
            #print("ERROR::Texture coordinate index array size == 0!!!")
        if len(self.mesh_normal_index_array) <= 0:
            normalIndexArrayInvalid = True
            #print("ERROR::Normal coordinate index array size == 0!!!")
       
        #print("Num index : " + str(len(mainMesh.polygons)*3))
        
        # ----------------------------------------------------------------------
        # f - Index from mesh polygon faces (eg. f v/t/n)
        # ----------------------------------------------------------------------

        # If corresponding Blender mesh object is not initialized and if
        # the vertex index array is initialized then return the face index array 
        # string looping the vertex index array as iterator to generate the 
        # face index array string.
        # self.main_mesh == None and 
        if self.main_mesh == None and len(self.mesh_vertex_index_array) > 0:
            myiter = iter(range(0, len(self.mesh_vertex_index_array)))
        elif self.main_mesh != None:
            myiter = iter(range(0, len(self.main_mesh.polygons)*3))

        for i in myiter: 
            #print("i : %d" % i)
            final_str += "f "
            final_str += str(int(self.mesh_vertex_index_array[i]) + 1) + "/"
            if texturecoordIndexArrayInvalid == False:
                final_str += str(int(self.mesh_texture_coord_index_array[i]) + 1) \
                    + "/"
            final_str += str(int(self.mesh_normal_index_array[i]) + 1)
            final_str += " "
            
            i += 1
            next(myiter, None)
            final_str += str(int(self.mesh_vertex_index_array[i]) + 1) + "/"
            if texturecoordIndexArrayInvalid == False:
                final_str += str(int(self.mesh_texture_coord_index_array[i]) + 1) \
                    + "/"
            final_str += str(int(self.mesh_normal_index_array[i]) + 1)
            final_str += " "
            
            i += 1
            next(myiter, None)
            final_str += str(int(self.mesh_vertex_index_array[i]) + 1) + "/"
            if texturecoordIndexArrayInvalid == False:
                final_str += str(int(self.mesh_texture_coord_index_array[i]) + 1) \
                    + "/"
            final_str += str(int(self.mesh_normal_index_array[i]) + 1)
            final_str += "\n"

        return final_str
    