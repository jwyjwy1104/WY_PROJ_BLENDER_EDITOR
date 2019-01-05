"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2017-10-22
Last update                         : 2017-11-21
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYMeshTestCases___init__\WYMeshTestCases___init__.py
Test case data file name            : ..\..\test\WYMeshTestCases___init__\WYMeshTestCases___init__.txt
Testing class file name             : ..\..\main\WYMesh\WYMesh.py
Testing class function name         : __init__(main_mesh_obj, wycoordsys)
Unit test case class name           : WYMeshTestCases___init__
Unit test case description          : Unit test case for class WYMesh __init__() function
Unit test case result file name     : ..\..\test\WYMeshTestCases___init__\WYMeshTestCaseResult___init__.txt
"""
# Pre-condition: WYUtil class is tested.
# Pre-condition: WYCoordsys class is tested.
# Pre-condition: WYMesh::init_wyelements() is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYMesh\\WYMesh.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYMeshTestCases___init__(unittest.TestCase):
    """
    Unit test case for class WYMesh __init__() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYMeshTestCase___init___TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __init__ function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if all the mesh data arrays are properly initialized through "init_mesh_data" function, which initializes the vertex coordinate arraym vertex normal vector array and texture coordinate array of the primitive where coordinate values are converted with the coordinate system export option initialized in the WYCoordsys object as member variable "wycoordsys" testing with the primitive which is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 0) with rotation (0,0,0) triangulated with WYUtil::triangulate_mesh(main_mesh) function and the start initializing the member variables by calling sub functions resulting the followings:
         mesh_vertex_array == []
         mesh_normal_array == []
         mesh_texture_coord_array == []
        
        ----------------------------------------------------------------------
        Class object allocation __init__ parameters:
        ----------------------------------------------------------------------
        :param main_mesh_obj: Referenced Blender Mesh object to retrieve the mesh data values from.
        :type  main_mesh_obj: bpy.data.object.
        :test  main_mesh_obj: bpy.ops.mesh.primitive_cube_add(location=(0,0,0),rotation=(0,0,0)).

        :param wycoordsys: WYCoordsys object which contains the user defined coordinate system export options to convert current WYMesh object's vertex corodinate values with when exported.
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: mesh_vertex_array == []
        :expect: mesh_normal_array == []
        :expect: mesh_texture_coord_array == []
        :expect: mesh_vertex_index_array == []
        :expect: mesh_normal_index_array == []
        :expect: mesh_texture_coord_index_array == []
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0001"
        wymesh = WYMesh(cube, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        self.assertTrue(wymesh.main_mesh_obj.name == "TestCube0001")
        self.assertTrue(len(wymesh.main_mesh.polygons) == 6) 

        self.assertTrue(wymesh.main_mesh_obj == cube)
        self.assertTrue(wymesh.main_mesh == cube.data)
        self.assertTrue(wymesh.wycoordsys.ZU == True)
        self.assertTrue(wymesh.wycoordsys.YF == True)
        self.assertTrue(wymesh.wyutil != None)
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])
    def test_WYMeshTestCase___init___TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __init__ function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if all the mesh data arrays are properly initialized through "init_mesh_data" function, which initializes the vertex coordinate arraym vertex normal vector array and texture coordinate array of the primitive where coordinate values are converted with the coordinate system export option initialized in the WYCoordsys object as member variable "wycoordsys" testing with the primitive which is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 0) with rotation (0,0,0) triangulated with WYUtil::triangulate_mesh(main_mesh) function and the start initializing the member variables by calling sub functions resulting the followings:
         mesh_vertex_array == []
         mesh_normal_array == []
         mesh_texture_coord_array == []
        
        ----------------------------------------------------------------------
        Class object allocation __init__ parameters:
        ----------------------------------------------------------------------
        :param main_mesh_obj: Referenced Blender Mesh object to retrieve the mesh data values from.
        :type  main_mesh_obj: bpy.data.object.
        :test  main_mesh_obj: bpy.ops.mesh.primitive_cube_add(location=(0,0,0),rotation=(0,0,0)).

        :param wycoordsys: WYCoordsys object which contains the user defined coordinate system export options to convert current WYMesh object's vertex corodinate values with when exported.
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: mesh_vertex_array == []
        :expect: mesh_normal_array == []
        :expect: mesh_texture_coord_array == []
        :expect: mesh_vertex_index_array == []
        :expect: mesh_normal_index_array == []
        :expect: mesh_texture_coord_index_array == []
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0002"
        wymesh = WYMesh(cube, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        self.assertTrue(wymesh.main_mesh_obj.name == "TestCube0002")
        self.assertTrue(len(wymesh.main_mesh.polygons) == 6) 

        self.assertTrue(wymesh.main_mesh_obj == cube)
        self.assertTrue(wymesh.main_mesh == cube.data)
        self.assertTrue(wymesh.wycoordsys.ZU == True)
        self.assertTrue(wymesh.wycoordsys.YF == True)
        self.assertTrue(wymesh.wyutil != None)
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])
    def test_WYMeshTestCase___init___TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __init__ function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if all the mesh data arrays are properly initialized through "init_mesh_data" function, which initializes the vertex coordinate arraym vertex normal vector array and texture coordinate array of the primitive where coordinate values are converted with the coordinate system export option initialized in the WYCoordsys object as member variable "wycoordsys" testing with the primitive which is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 0) with rotation (0,0,0) triangulated with WYUtil::triangulate_mesh(main_mesh) function and the start initializing the member variables by calling sub functions resulting the followings:
         mesh_vertex_array == []
         mesh_normal_array == []
         mesh_texture_coord_array == []
        
        ----------------------------------------------------------------------
        Class object allocation __init__ parameters:
        ----------------------------------------------------------------------
        :param main_mesh_obj: Referenced Blender Mesh object to retrieve the mesh data values from.
        :type  main_mesh_obj: bpy.data.object.
        :test  main_mesh_obj: bpy.ops.mesh.primitive_cube_add(location=(0,0,0),rotation=(0,0,0)).

        :param wycoordsys: WYCoordsys object which contains the user defined coordinate system export options to convert current WYMesh object's vertex corodinate values with when exported.
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: mesh_vertex_array == []
        :expect: mesh_normal_array == []
        :expect: mesh_texture_coord_array == []
        :expect: mesh_vertex_index_array == []
        :expect: mesh_normal_index_array == []
        :expect: mesh_texture_coord_index_array == []
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0003"
        wymesh = WYMesh(cube, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        self.assertTrue(wymesh.main_mesh_obj.name == "TestCube0003")
        self.assertTrue(len(wymesh.main_mesh.polygons) == 6) 

        self.assertTrue(wymesh.main_mesh_obj == cube)
        self.assertTrue(wymesh.main_mesh == cube.data)
        self.assertTrue(wymesh.wycoordsys.ZU == True)
        self.assertTrue(wymesh.wycoordsys.YF == True)
        self.assertTrue(wymesh.wyutil != None)
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])
    def test_WYMeshTestCase___init___TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __init__ function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if all the mesh data arrays are properly initialized through "init_mesh_data" function, which initializes the vertex coordinate arraym vertex normal vector array and texture coordinate array of the primitive where coordinate values are converted with the coordinate system export option initialized in the WYCoordsys object as member variable "wycoordsys" testing with the primitive which is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 0) with rotation (0,0,0) triangulated with WYUtil::triangulate_mesh(main_mesh) function and the start initializing the member variables by calling sub functions resulting the followings:
         mesh_vertex_array == []
         mesh_normal_array == []
         mesh_texture_coord_array == []
        
        ----------------------------------------------------------------------
        Class object allocation __init__ parameters:
        ----------------------------------------------------------------------
        :param main_mesh_obj: Referenced Blender Mesh object to retrieve the mesh data values from.
        :type  main_mesh_obj: bpy.data.object.
        :test  main_mesh_obj: bpy.ops.mesh.primitive_cube_add(location=(0,0,0),rotation=(0,0,0)).

        :param wycoordsys: WYCoordsys object which contains the user defined coordinate system export options to convert current WYMesh object's vertex corodinate values with when exported.
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: mesh_vertex_array == []
        :expect: mesh_normal_array == []
        :expect: mesh_texture_coord_array == []
        :expect: mesh_vertex_index_array == []
        :expect: mesh_normal_index_array == []
        :expect: mesh_texture_coord_index_array == []
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0004"
        wymesh = WYMesh(cube, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        self.assertTrue(wymesh.main_mesh_obj.name == "TestCube0004")
        self.assertTrue(len(wymesh.main_mesh.polygons) == 6) 

        self.assertTrue(wymesh.main_mesh_obj == cube)
        self.assertTrue(wymesh.main_mesh == cube.data)
        self.assertTrue(wymesh.wycoordsys.ZU == True)
        self.assertTrue(wymesh.wycoordsys.YF == True)
        self.assertTrue(wymesh.wyutil != None)
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])
    def test_WYMeshTestCase___init___TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __init__ function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if all the mesh data arrays are properly initialized through "init_mesh_data" function, which initializes the vertex coordinate arraym vertex normal vector array and texture coordinate array of the primitive where coordinate values are converted with the coordinate system export option initialized in the WYCoordsys object as member variable "wycoordsys" testing with the primitive which is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 0) with rotation (0,0,0) triangulated with WYUtil::triangulate_mesh(main_mesh) function and the start initializing the member variables by calling sub functions resulting the followings:
         mesh_vertex_array == []
         mesh_normal_array == []
         mesh_texture_coord_array == []
        
        ----------------------------------------------------------------------
        Class object allocation __init__ parameters:
        ----------------------------------------------------------------------
        :param main_mesh_obj: Referenced Blender Mesh object to retrieve the mesh data values from.
        :type  main_mesh_obj: bpy.data.object.
        :test  main_mesh_obj: bpy.ops.mesh.primitive_cube_add(location=(0,0,0),rotation=(0,0,0)).

        :param wycoordsys: WYCoordsys object which contains the user defined coordinate system export options to convert current WYMesh object's vertex corodinate values with when exported.
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: mesh_vertex_array == []
        :expect: mesh_normal_array == []
        :expect: mesh_texture_coord_array == []
        :expect: mesh_vertex_index_array == []
        :expect: mesh_normal_index_array == []
        :expect: mesh_texture_coord_index_array == []
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0005"
        wymesh = WYMesh(cube, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        self.assertTrue(wymesh.main_mesh_obj.name == "TestCube0005")
        self.assertTrue(len(wymesh.main_mesh.polygons) == 6) 

        self.assertTrue(wymesh.main_mesh_obj == cube)
        self.assertTrue(wymesh.main_mesh == cube.data)
        self.assertTrue(wymesh.wycoordsys.ZU == True)
        self.assertTrue(wymesh.wycoordsys.YF == True)
        self.assertTrue(wymesh.wyutil != None)
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])
    def test_WYMeshTestCase___init___TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __init__ function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if all the mesh data arrays are properly initialized through "init_mesh_data" function, which initializes the vertex coordinate arraym vertex normal vector array and texture coordinate array of the primitive where coordinate values are converted with the coordinate system export option initialized in the WYCoordsys object as member variable "wycoordsys" testing with the primitive which is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 0) with rotation (0,0,0) triangulated with WYUtil::triangulate_mesh(main_mesh) function and the start initializing the member variables by calling sub functions resulting the followings:
         mesh_vertex_array == []
         mesh_normal_array == []
         mesh_texture_coord_array == []
        
        ----------------------------------------------------------------------
        Class object allocation __init__ parameters:
        ----------------------------------------------------------------------
        :param main_mesh_obj: Referenced Blender Mesh object to retrieve the mesh data values from.
        :type  main_mesh_obj: bpy.data.object.
        :test  main_mesh_obj: bpy.ops.mesh.primitive_cube_add(location=(0,0,0),rotation=(0,0,0)).

        :param wycoordsys: WYCoordsys object which contains the user defined coordinate system export options to convert current WYMesh object's vertex corodinate values with when exported.
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: mesh_vertex_array == []
        :expect: mesh_normal_array == []
        :expect: mesh_texture_coord_array == []
        :expect: mesh_vertex_index_array == []
        :expect: mesh_normal_index_array == []
        :expect: mesh_texture_coord_index_array == []
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0006"
        wymesh = WYMesh(cube, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        self.assertTrue(wymesh.main_mesh_obj.name == "TestCube0006")
        self.assertTrue(len(wymesh.main_mesh.polygons) == 6) 

        self.assertTrue(wymesh.main_mesh_obj == cube)
        self.assertTrue(wymesh.main_mesh == cube.data)
        self.assertTrue(wymesh.wycoordsys.ZU == True)
        self.assertTrue(wymesh.wycoordsys.YF == True)
        self.assertTrue(wymesh.wyutil != None)
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])
    def test_WYMeshTestCase___init___TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __init__ function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if all the mesh data arrays are properly initialized through "init_mesh_data" function, which initializes the vertex coordinate arraym vertex normal vector array and texture coordinate array of the primitive where coordinate values are converted with the coordinate system export option initialized in the WYCoordsys object as member variable "wycoordsys" testing with the primitive which is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 0) with rotation (0,0,0) triangulated with WYUtil::triangulate_mesh(main_mesh) function and the start initializing the member variables by calling sub functions resulting the followings:
         mesh_vertex_array == []
         mesh_normal_array == []
         mesh_texture_coord_array == []
        
        ----------------------------------------------------------------------
        Class object allocation __init__ parameters:
        ----------------------------------------------------------------------
        :param main_mesh_obj: Referenced Blender Mesh object to retrieve the mesh data values from.
        :type  main_mesh_obj: bpy.data.object.
        :test  main_mesh_obj: bpy.ops.mesh.primitive_cube_add(location=(0,0,0),rotation=(0,0,0)).

        :param wycoordsys: WYCoordsys object which contains the user defined coordinate system export options to convert current WYMesh object's vertex corodinate values with when exported.
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: mesh_vertex_array == []
        :expect: mesh_normal_array == []
        :expect: mesh_texture_coord_array == []
        :expect: mesh_vertex_index_array == []
        :expect: mesh_normal_index_array == []
        :expect: mesh_texture_coord_index_array == []
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0007"
        wymesh = WYMesh(cube, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        self.assertTrue(wymesh.main_mesh_obj.name == "TestCube0007")
        self.assertTrue(len(wymesh.main_mesh.polygons) == 6) 

        self.assertTrue(wymesh.main_mesh_obj == cube)
        self.assertTrue(wymesh.main_mesh == cube.data)
        self.assertTrue(wymesh.wycoordsys.ZU == True)
        self.assertTrue(wymesh.wycoordsys.YF == True)
        self.assertTrue(wymesh.wyutil != None)
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])
    def test_WYMeshTestCase___init___TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __init__ function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if all the mesh data arrays are properly initialized through "init_mesh_data" function, which initializes the vertex coordinate arraym vertex normal vector array and texture coordinate array of the primitive where coordinate values are converted with the coordinate system export option initialized in the WYCoordsys object as member variable "wycoordsys" testing with the primitive which is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 0) with rotation (0,0,0) triangulated with WYUtil::triangulate_mesh(main_mesh) function and the start initializing the member variables by calling sub functions resulting the followings:
         mesh_vertex_array == []
         mesh_normal_array == []
         mesh_texture_coord_array == []
        
        ----------------------------------------------------------------------
        Class object allocation __init__ parameters:
        ----------------------------------------------------------------------
        :param main_mesh_obj: Referenced Blender Mesh object to retrieve the mesh data values from.
        :type  main_mesh_obj: bpy.data.object.
        :test  main_mesh_obj: bpy.ops.mesh.primitive_cube_add(location=(0,0,0),rotation=(0,0,0)).

        :param wycoordsys: WYCoordsys object which contains the user defined coordinate system export options to convert current WYMesh object's vertex corodinate values with when exported.
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: mesh_vertex_array == []
        :expect: mesh_normal_array == []
        :expect: mesh_texture_coord_array == []
        :expect: mesh_vertex_index_array == []
        :expect: mesh_normal_index_array == []
        :expect: mesh_texture_coord_index_array == []
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0008"
        wymesh = WYMesh(cube, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        self.assertTrue(wymesh.main_mesh_obj.name == "TestCube0008")
        self.assertTrue(len(wymesh.main_mesh.polygons) == 6) 

        self.assertTrue(wymesh.main_mesh_obj == cube)
        self.assertTrue(wymesh.main_mesh == cube.data)
        self.assertTrue(wymesh.wycoordsys.ZU == True)
        self.assertTrue(wymesh.wycoordsys.YF == True)
        self.assertTrue(wymesh.wyutil != None)
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])
    def test_WYMeshTestCase___init___TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __init__ function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if all the mesh data arrays are properly initialized through "init_mesh_data" function, which initializes the vertex coordinate arraym vertex normal vector array and texture coordinate array of the primitive where coordinate values are converted with the coordinate system export option initialized in the WYCoordsys object as member variable "wycoordsys" testing with the primitive which is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 0) with rotation (0,0,0) triangulated with WYUtil::triangulate_mesh(main_mesh) function and the start initializing the member variables by calling sub functions resulting the followings:
         mesh_vertex_array == []
         mesh_normal_array == []
         mesh_texture_coord_array == []
        
        ----------------------------------------------------------------------
        Class object allocation __init__ parameters:
        ----------------------------------------------------------------------
        :param main_mesh_obj: Referenced Blender Mesh object to retrieve the mesh data values from.
        :type  main_mesh_obj: bpy.data.object.
        :test  main_mesh_obj: bpy.ops.mesh.primitive_cube_add(location=(0,0,0),rotation=(0,0,0)).

        :param wycoordsys: WYCoordsys object which contains the user defined coordinate system export options to convert current WYMesh object's vertex corodinate values with when exported.
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: mesh_vertex_array == []
        :expect: mesh_normal_array == []
        :expect: mesh_texture_coord_array == []
        :expect: mesh_vertex_index_array == []
        :expect: mesh_normal_index_array == []
        :expect: mesh_texture_coord_index_array == []
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0009"
        wymesh = WYMesh(cube, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        self.assertTrue(wymesh.main_mesh_obj.name == "TestCube0009")
        self.assertTrue(len(wymesh.main_mesh.polygons) == 6) 

        self.assertTrue(wymesh.main_mesh_obj == cube)
        self.assertTrue(wymesh.main_mesh == cube.data)
        self.assertTrue(wymesh.wycoordsys.ZU == True)
        self.assertTrue(wymesh.wycoordsys.YF == True)
        self.assertTrue(wymesh.wyutil != None)
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])
    def test_WYMeshTestCase___init___TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __init__ function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if all the mesh data arrays are properly initialized through "init_mesh_data" function, which initializes the vertex coordinate arraym vertex normal vector array and texture coordinate array of the primitive where coordinate values are converted with the coordinate system export option initialized in the WYCoordsys object as member variable "wycoordsys" testing with the primitive which is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 0) with rotation (0,0,0) triangulated with WYUtil::triangulate_mesh(main_mesh) function and the start initializing the member variables by calling sub functions resulting the followings:
         mesh_vertex_array == []
         mesh_normal_array == []
         mesh_texture_coord_array == []
        
        ----------------------------------------------------------------------
        Class object allocation __init__ parameters:
        ----------------------------------------------------------------------
        :param main_mesh_obj: Referenced Blender Mesh object to retrieve the mesh data values from.
        :type  main_mesh_obj: bpy.data.object.
        :test  main_mesh_obj: bpy.ops.mesh.primitive_cube_add(location=(0,0,0),rotation=(0,0,0)).

        :param wycoordsys: WYCoordsys object which contains the user defined coordinate system export options to convert current WYMesh object's vertex corodinate values with when exported.
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: mesh_vertex_array == []
        :expect: mesh_normal_array == []
        :expect: mesh_texture_coord_array == []
        :expect: mesh_vertex_index_array == []
        :expect: mesh_normal_index_array == []
        :expect: mesh_texture_coord_index_array == []
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0010"
        wymesh = WYMesh(cube, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        self.assertTrue(wymesh.main_mesh_obj.name == "TestCube0010")
        self.assertTrue(len(wymesh.main_mesh.polygons) == 6) 

        self.assertTrue(wymesh.main_mesh_obj == cube)
        self.assertTrue(wymesh.main_mesh == cube.data)
        self.assertTrue(wymesh.wycoordsys.ZU == True)
        self.assertTrue(wymesh.wycoordsys.YF == True)
        self.assertTrue(wymesh.wyutil != None)
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYMeshTestCases___init__))
