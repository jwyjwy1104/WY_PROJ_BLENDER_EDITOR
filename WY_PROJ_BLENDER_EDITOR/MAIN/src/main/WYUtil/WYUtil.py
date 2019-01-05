################################################################################
# Project Name          	: WY_PROJ_BLENDER_EDITOR
# File Name             	: WYUtl.py
# Project Headquarter   	: https://docs.google.com/document/d/1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit#
# Test Plan Headquarter 	: https://docs.google.com/document/d/1wlFujpygsVKtqiz596ZdD1sCeUPkpIgr1lNlE_GN-_w/edit#
# WYUtil test plan      	: https://docs.google.com/document/d/1aTrvRFVpHoXrVYB1lXC74zcPukhAxOZt2dG3kbqtuL8/edit#
# Lead Programmer       	: Samil Chai
# Junior Programmer     	: Nick Jang
# Time                  	: 
# Description           	: 
################################################################################

import bpy
import bmesh

class WYUtil:
    '''
    This class is the collection of utility helper functions.

    ----------------------------------------------------------------------------
    Member functions:
    ----------------------------------------------------------------------------
    # def __init__(self):
    # def __eq__(self, other):
    # def triangulate_mesh(self, main_mesh):
        Test: https://docs.google.com/spreadsheets/d/1D6UntR5w_7Kk7ZfW1n_YUs3IoMQvLIcwda-NLkKUYzs/edit#gid=0
    # def create_custom_mesh(self, obj_name, px, py, pz, vertex_array, vertex_index_array):
        Test: https://docs.google.com/spreadsheets/d/1UmnmHb2cJCfrA6ANeQAarFOruqyDoxTdIar3wNTgGpU/edit#gid=0 
    '''
    def __init__(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYUtil default constructor.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Default constructor to allocate the WYUtil object.

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return : Allocated and initialized WYUtil object.
        :rtype  : WYUtil.
        '''
        print("")

    #---------------------------------------------------------------------------
    # Overriden equal function.
    #---------------------------------------------------------------------------
    def __eq__(self, other):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYUtil overrided equal function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Compares the member variables with the memeber variables intialized 
        in "other" object return True if these 2 object has all the member 
        variables same values else return False.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  other: Second WYUtil object to compare with.
        :type   other: WYUtil
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Return the result of comparison between 2 objects.
        :rtype: boolean
        '''
        if other == None:
            return False
        return True

    #---------------------------------------------------------------------------
    # Triangulate Blender mesh object function.
    #---------------------------------------------------------------------------
    def triangulate_mesh(self, main_mesh):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYUtil member function utility function to triangulate the faces of the 
        Blender bmesh object from quadratic faces.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function triangulates the Blender bmesh object from quadratic 
        faces, this is needed because I am using this game editor to create the 
        game models and import it to my custom game engines.

        Then, to import the models created within Blender, any modelling engine
        creates the mesh with quaratic faces, but in order to import to gaming 
        engine, the model must be with triangulated faces.

        Create a duplication of the mesh provided, then triangulate the newly 
        created mesh with Blender bmesh::ops::triangulate() function and store
        the triangulated mesh back into original mesh object, so the original
        mesh didn't change but the faces are triangulated.
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param main_mesh: Blender bmesh object to triangulate faces with.
        :type  main_mesh: bmesh (bpy.data.object.data)
        '''
        bpy.ops.object.mode_set(mode='OBJECT') 
        bm = bmesh.new()
        bm.from_mesh(main_mesh)
        bmesh.ops.triangulate(bm, faces=bm.faces)
        bm.to_mesh(main_mesh)
        bm.free()
        del bm
        
    # --------------------------------------------------------------------------
    # Create custom mesh
    # --------------------------------------------------------------------------
    # Code brought from : http://community.cgcookie.com/t/create-custom-mesh-in-python-part-2-basic-mesh/2417
    # objname: Object name
    # pX: position X axis (Cursor position)
    # pY: position Y axis (Cursor position)
    # pZ: position Z axis (Cursor position)
    # --------------------------------------------------------------------------

    def create_custom_mesh(self, obj_name, px, py, pz, 
                           vertex_array, vertex_index_array):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYUtil member function utility function to create the Blender mesh 
        object with the vertex array, vertex index array and mehs name 
        and links the model to the Blender scene.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function creates the Blender mesh object with name passed into the
        function call, then creates the Blender model object with the mesh just
        created, then link the mode object to the Blender scene and sets the 
        model position with the x,y,z values also passed into the function call.
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param obj_name: Name of the model to create the Blender bpy.data.mesh 
                         object with.
        :type  obj_name: string
        :param px: Blender mesh object X position value
        :type  px: int
        :param py: Blender mesh object Y position value
        :type  py: int
        :param py: Blender mesh object Z position value
        :type  py: int
        :param vertex_array: Vertices collection of the mesh to create 
                             Blender mesh object with.
        :type  vertex_array: [(x,y,z), ...]
        :param vertex_index_array: Collection of vertex indices to create the 
                                   Blender mesh object with.
        :type  vertex_index_array: [int, int ...]

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Created Blender bpy.data.object object.
        :rtype: bpy.data.object

        '''
        # Create mesh data
        mymesh = bpy.data.meshes.new(obj_name)
        # Create object
        myobject = bpy.data.objects.new(obj_name, mymesh)
        # Link object to scene
        bpy.context.scene.objects.link(myobject)
    
        # Generate mesh data
        # Create mesh with vertices loaded from my OBJ file
        mymesh.from_pydata(vertex_array, [], vertex_index_array)
    
        # Calculate the edges
        mymesh.update(calc_edges=True)

        # Set Location
        myobject.location.x = px
        myobject.location.y = py
        myobject.location.z = pz

        return myobject    
    
    
    
    
    
