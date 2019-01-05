"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2017-11-03
Last update                         : 2017-11-28
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYUtilTestCases_triangulate_mesh\WYUtilTestCases_triangulate_mesh.py
Test case data file name            : ..\..\test\WYUtilTestCases_triangulate_mesh\WYUtilTestCases_triangulate_mesh.txt
Testing class file name             : ..\..\main\WYUtil\WYUtil.py
Testing class function name         : triangulate_mesh(main_mesh)
Unit test case class name           : WYUtilTestCases_triangulate_mesh
Unit test case description          : Unit test case for class WYUtil triangulate_mesh() function
Unit test case result file name     : ..\..\test\WYUtilTestCases_triangulate_mesh\WYUtilTestCaseResult_triangulate_mesh.txt
"""

import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYUtil\\WYUtil.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYUtilTestCases_triangulate_mesh(unittest.TestCase):
    """
    Unit test case for class WYUtil triangulate_mesh() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :506
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))" generates the default Blender cube on location (0,0,0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0001"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(1, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (1, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(1, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0002"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0.1, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (0.1, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0.1, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0003"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0.001, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (0.001, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0.001, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0004"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0.00001, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (0.00001, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0.00001, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0005"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(2, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (2, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(2, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0006"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(3, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (3, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(3, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0007"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(10, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (10, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(10, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0008"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(20, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (20, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(20, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0009"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(30, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (30, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(30, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0010"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0011(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0011

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(100, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (100, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(100, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0011"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0012(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0012

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(200, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (200, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(200, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0012"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0013(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0013

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(300, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (300, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(300, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0013"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0014(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0014

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(10000, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (10000, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(10000, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0014"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0015(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0015

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(20000, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (20000, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(20000, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0015"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0016(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0016

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(30000, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (30000, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(30000, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0016"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0017(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0017

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(1000000, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (1000000, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(1000000, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0017"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0018(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0018

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(2000000, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (2000000, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(2000000, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0018"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0019(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0019

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(3000000, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (3000000, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(3000000, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0019"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0020(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0020

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-1, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-1, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-1, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0020"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0021(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0021

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-0.1, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-0.1, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-0.1, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0021"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0022(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0022

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-0.001, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-0.001, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-0.001, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0022"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0023(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0023

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-0.00001, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-0.00001, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-0.00001, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0023"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0024(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0024

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-2, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-2, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-2, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0024"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0025(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0025

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-3, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-3, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-3, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0025"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0026(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0026

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-10, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-10, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-10, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0026"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0027(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0027

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-20, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-20, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-20, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0027"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0028(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0028

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-30, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-30, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-30, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0028"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0029(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0029

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-100, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-100, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-100, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0029"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0030(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0030

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-200, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-200, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-200, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0030"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0031(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0031

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-300, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-300, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-300, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0031"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0032(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0032

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-10000, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-10000, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-10000, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0032"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0033(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0033

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-20000, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-20000, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-20000, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0033"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0034(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0034

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-30000, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-30000, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-30000, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0034"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0035(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0035

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-1000000, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-1000000, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-1000000, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0035"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0036(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0036

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-2000000, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-2000000, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-2000000, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0036"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0037(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0037

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-3000000, 0, 0), rotation=(0,0,0))" generates the default Blender cube on location (-3000000, 0, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-3000000, 0, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0037"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0038(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0038

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 1, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 1, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 1, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0038"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0039(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0039

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0.1, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 0.1, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0.1, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0039"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0040(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0040

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0.001, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 0.001, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0.001, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0040"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0041(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0041

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0.00001, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 0.00001, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0.00001, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0041"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0042(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0042

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 2, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 2, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 2, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0042"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0043(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0043

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 3, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 3, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 3, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0043"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0044(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0044

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 10, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 10, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 10, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0044"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0045(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0045

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 20, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 20, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 20, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0045"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0046(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0046

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 30, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 30, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 30, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0046"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0047(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0047

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 100, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 100, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 100, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0047"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0048(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0048

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 200, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 200, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 200, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0048"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0049(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0049

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 300, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 300, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 300, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0049"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0050(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0050

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 10000, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 10000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 10000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0050"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0051(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0051

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 20000, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 20000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 20000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0051"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0052(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0052

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 30000, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 30000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 30000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0052"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0053(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0053

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 1000000, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 1000000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 1000000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0053"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0054(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0054

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 2000000, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 2000000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 2000000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0054"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0055(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0055

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 3000000, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, 3000000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 3000000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0055"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0056(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0056

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -1, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -1, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -1, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0056"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0057(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0057

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -0.1, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -0.1, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -0.1, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0057"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0058(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0058

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -0.001, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -0.001, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -0.001, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0058"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0059(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0059

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -0.00001, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -0.00001, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -0.00001, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0059"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0060(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0060

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -2, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -2, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -2, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0060"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0061(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0061

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -3, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -3, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -3, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0061"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0062(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0062

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -10, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -10, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -10, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0062"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0063(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0063

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -20, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -20, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -20, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0063"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0064(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0064

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -30, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -30, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -30, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0064"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0065(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0065

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -100, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -100, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -100, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0065"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0066(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0066

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -200, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -200, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -200, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0066"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0067(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0067

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -300, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -300, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -300, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0067"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0068(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0068

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -10000, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -10000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -10000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0068"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0069(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0069

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -20000, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -20000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -20000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0069"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0070(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0070

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -30000, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -30000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -30000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0070"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0071(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0071

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -1000000, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -1000000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -1000000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0071"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0072(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0072

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -2000000, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -2000000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -2000000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0072"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0073(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0073

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -3000000, 0), rotation=(0,0,0))" generates the default Blender cube on location (0, -3000000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -3000000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0073"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0074(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0074

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 1), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0074"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0075(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0075

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0.1), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 0.1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0.1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0075"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0076(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0076

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0.001), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 0.001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0.001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0076"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0077(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0077

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0.00001), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 0.00001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0.00001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0077"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0078(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0078

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 2), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 2) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 2), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0078"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0079(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0079

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 3), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 3) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 3), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0079"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0080(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0080

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 10), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 10) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 10), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0080"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0081(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0081

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 20), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 20) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 20), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0081"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0082(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0082

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 30), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 30) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 30), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0082"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0083(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0083

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 100), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 100) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 100), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0083"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0084(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0084

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 200), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 200) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 200), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0084"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0085(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0085

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 300), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 300) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 300), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0085"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0086(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0086

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 10000), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 10000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 10000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0086"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0087(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0087

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 20000), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 20000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 20000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0087"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0088(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0088

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 30000), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 30000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 30000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0088"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0089(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0089

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 1000000), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 1000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 1000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0089"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0090(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0090

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 2000000), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 2000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 2000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0090"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0091(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0091

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 3000000), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, 3000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 3000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0091"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0092(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0092

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -1), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0092"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0093(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0093

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -0.1), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -0.1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -0.1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0093"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0094(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0094

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -0.001), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -0.001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -0.001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0094"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0095(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0095

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -0.00001), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -0.00001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -0.00001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0095"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0096(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0096

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -2), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -2) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -2), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0096"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0097(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0097

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -3), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -3) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -3), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0097"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0098(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0098

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -10), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -10) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -10), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0098"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0099(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0099

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -20), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -20) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -20), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0099"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0100(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0100

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -30), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -30) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -30), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0100"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0101(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0101

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -100), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -100) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -100), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0101"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0102(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0102

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -200), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -200) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -200), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0102"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0103(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0103

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -300), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -300) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -300), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0103"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0104(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0104

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -10000), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -10000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -10000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0104"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0105(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0105

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -20000), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -20000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -20000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0105"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0106(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0106

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -30000), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -30000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -30000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0106"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0107(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0107

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -1000000), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -1000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -1000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0107"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0108(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0108

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -2000000), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -2000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -2000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0108"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0109(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0109

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0, -3000000), rotation=(0,0,0))" generates the default Blender cube on location (0, 0, -3000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -3000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0109"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0110(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0110

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(1, 1, 0), rotation=(0,0,0))" generates the default Blender cube on location (1, 1, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(1, 1, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0110"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0111(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0111

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0.1, 0.1, 0), rotation=(0,0,0))" generates the default Blender cube on location (0.1, 0.1, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0.1, 0.1, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0111"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0112(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0112

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0.001, 0.001, 0), rotation=(0,0,0))" generates the default Blender cube on location (0.001, 0.001, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0.001, 0.001, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0112"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0113(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0113

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0.00001, 0.00001, 0), rotation=(0,0,0))" generates the default Blender cube on location (0.00001, 0.00001, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0.00001, 0.00001, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0113"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0114(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0114

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(2, 2, 0), rotation=(0,0,0))" generates the default Blender cube on location (2, 2, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(2, 2, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0114"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0115(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0115

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(3, 3, 0), rotation=(0,0,0))" generates the default Blender cube on location (3, 3, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(3, 3, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0115"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0116(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0116

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(10, 10, 0), rotation=(0,0,0))" generates the default Blender cube on location (10, 10, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(10, 10, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0116"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0117(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0117

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(20, 20, 0), rotation=(0,0,0))" generates the default Blender cube on location (20, 20, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(20, 20, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0117"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0118(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0118

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(30, 30, 0), rotation=(0,0,0))" generates the default Blender cube on location (30, 30, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(30, 30, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0118"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0119(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0119

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(100, 100, 0), rotation=(0,0,0))" generates the default Blender cube on location (100, 100, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(100, 100, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0119"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0120(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0120

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(200, 200, 0), rotation=(0,0,0))" generates the default Blender cube on location (200, 200, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(200, 200, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0120"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0121(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0121

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(300, 300, 0), rotation=(0,0,0))" generates the default Blender cube on location (300, 300, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(300, 300, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0121"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0122(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0122

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(10000, 10000, 0), rotation=(0,0,0))" generates the default Blender cube on location (10000, 10000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(10000, 10000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0122"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0123(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0123

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(20000, 20000, 0), rotation=(0,0,0))" generates the default Blender cube on location (20000, 20000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(20000, 20000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0123"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0124(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0124

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(30000, 30000, 0), rotation=(0,0,0))" generates the default Blender cube on location (30000, 30000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(30000, 30000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0124"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0125(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0125

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(1000000, 1000000, 0), rotation=(0,0,0))" generates the default Blender cube on location (1000000, 1000000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(1000000, 1000000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0125"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0126(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0126

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(2000000, 2000000, 0), rotation=(0,0,0))" generates the default Blender cube on location (2000000, 2000000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(2000000, 2000000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0126"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0127(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0127

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(3000000, 3000000, 0), rotation=(0,0,0))" generates the default Blender cube on location (3000000, 3000000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(3000000, 3000000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0127"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0128(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0128

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-1, -1, 0), rotation=(0,0,0))" generates the default Blender cube on location (-1, -1, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-1, -1, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0128"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0129(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0129

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-0.1, -0.1, 0), rotation=(0,0,0))" generates the default Blender cube on location (-0.1, -0.1, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-0.1, -0.1, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0129"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0130(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0130

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-0.001, -0.001, 0), rotation=(0,0,0))" generates the default Blender cube on location (-0.001, -0.001, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-0.001, -0.001, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0130"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0131(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0131

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-0.00001, -0.00001, 0), rotation=(0,0,0))" generates the default Blender cube on location (-0.00001, -0.00001, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-0.00001, -0.00001, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0131"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0132(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0132

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-2, -2, 0), rotation=(0,0,0))" generates the default Blender cube on location (-2, -2, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-2, -2, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0132"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0133(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0133

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-3, -3, 0), rotation=(0,0,0))" generates the default Blender cube on location (-3, -3, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-3, -3, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0133"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0134(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0134

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-10, -10, 0), rotation=(0,0,0))" generates the default Blender cube on location (-10, -10, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-10, -10, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0134"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0135(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0135

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-20, -20, 0), rotation=(0,0,0))" generates the default Blender cube on location (-20, -20, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-20, -20, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0135"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0136(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0136

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-30, -30, 0), rotation=(0,0,0))" generates the default Blender cube on location (-30, -30, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-30, -30, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0136"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0137(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0137

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-100, -100, 0), rotation=(0,0,0))" generates the default Blender cube on location (-100, -100, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-100, -100, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0137"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0138(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0138

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-200, -200, 0), rotation=(0,0,0))" generates the default Blender cube on location (-200, -200, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-200, -200, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0138"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0139(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0139

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-300, -300, 0), rotation=(0,0,0))" generates the default Blender cube on location (-300, -300, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-300, -300, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0139"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0140(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0140

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-10000, -10000, 0), rotation=(0,0,0))" generates the default Blender cube on location (-10000, -10000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-10000, -10000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0140"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0141(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0141

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-20000, -20000, 0), rotation=(0,0,0))" generates the default Blender cube on location (-20000, -20000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-20000, -20000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0141"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0142(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0142

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-30000, -30000, 0), rotation=(0,0,0))" generates the default Blender cube on location (-30000, -30000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-30000, -30000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0142"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0143(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0143

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-1000000, -1000000, 0), rotation=(0,0,0))" generates the default Blender cube on location (-1000000, -1000000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-1000000, -1000000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0143"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0144(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0144

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-2000000, -2000000, 0), rotation=(0,0,0))" generates the default Blender cube on location (-2000000, -2000000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-2000000, -2000000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0144"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0145(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0145

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-3000000, -3000000, 0), rotation=(0,0,0))" generates the default Blender cube on location (-3000000, -3000000, 0) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-3000000, -3000000, 0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0145"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0146(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0146

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(1, 0, 1), rotation=(0,0,0))" generates the default Blender cube on location (1, 0, 1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(1, 0, 1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0146"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0147(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0147

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0.1, 0, 0.1), rotation=(0,0,0))" generates the default Blender cube on location (0.1, 0, 0.1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0.1, 0, 0.1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0147"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0148(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0148

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0.001, 0, 0.001), rotation=(0,0,0))" generates the default Blender cube on location (0.001, 0, 0.001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0.001, 0, 0.001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0148"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0149(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0149

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0.00001, 0, 0.00001), rotation=(0,0,0))" generates the default Blender cube on location (0.00001, 0, 0.00001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0.00001, 0, 0.00001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0149"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0150(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0150

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(2, 0, 2), rotation=(0,0,0))" generates the default Blender cube on location (2, 0, 2) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(2, 0, 2), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0150"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0151(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0151

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(3, 0, 3), rotation=(0,0,0))" generates the default Blender cube on location (3, 0, 3) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(3, 0, 3), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0151"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0152(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0152

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(10, 0, 10), rotation=(0,0,0))" generates the default Blender cube on location (10, 0, 10) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(10, 0, 10), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0152"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0153(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0153

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(20, 0, 20), rotation=(0,0,0))" generates the default Blender cube on location (20, 0, 20) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(20, 0, 20), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0153"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0154(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0154

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(30, 0, 30), rotation=(0,0,0))" generates the default Blender cube on location (30, 0, 30) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(30, 0, 30), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0154"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0155(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0155

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(100, 0, 100), rotation=(0,0,0))" generates the default Blender cube on location (100, 0, 100) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(100, 0, 100), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0155"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0156(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0156

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(200, 0, 200), rotation=(0,0,0))" generates the default Blender cube on location (200, 0, 200) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(200, 0, 200), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0156"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0157(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0157

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(300, 0, 300), rotation=(0,0,0))" generates the default Blender cube on location (300, 0, 300) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(300, 0, 300), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0157"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0158(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0158

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(10000, 0,  10000), rotation=(0,0,0))" generates the default Blender cube on location (10000, 0,  10000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(10000, 0,  10000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0158"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0159(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0159

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(20000, 0,  20000), rotation=(0,0,0))" generates the default Blender cube on location (20000, 0,  20000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(20000, 0,  20000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0159"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0160(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0160

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(30000, 0,  30000), rotation=(0,0,0))" generates the default Blender cube on location (30000, 0,  30000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(30000, 0,  30000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0160"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0161(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0161

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(1000000, 0,  1000000), rotation=(0,0,0))" generates the default Blender cube on location (1000000, 0,  1000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(1000000, 0,  1000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0161"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0162(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0162

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(2000000, 0,  2000000), rotation=(0,0,0))" generates the default Blender cube on location (2000000, 0,  2000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(2000000, 0,  2000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0162"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0163(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0163

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(3000000, 0,  3000000), rotation=(0,0,0))" generates the default Blender cube on location (3000000, 0,  3000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(3000000, 0,  3000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0163"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0164(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0164

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-1, 0, -1), rotation=(0,0,0))" generates the default Blender cube on location (-1, 0, -1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-1, 0, -1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0164"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0165(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0165

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-0.1, 0, -0.1), rotation=(0,0,0))" generates the default Blender cube on location (-0.1, 0, -0.1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-0.1, 0, -0.1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0165"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0166(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0166

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-0.001, 0, -0.001), rotation=(0,0,0))" generates the default Blender cube on location (-0.001, 0, -0.001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-0.001, 0, -0.001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0166"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0167(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0167

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-0.00001, 0, -0.00001), rotation=(0,0,0))" generates the default Blender cube on location (-0.00001, 0, -0.00001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-0.00001, 0, -0.00001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0167"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0168(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0168

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-2, 0, -2), rotation=(0,0,0))" generates the default Blender cube on location (-2, 0, -2) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-2, 0, -2), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0168"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0169(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0169

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-3, 0, -3), rotation=(0,0,0))" generates the default Blender cube on location (-3, 0, -3) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-3, 0, -3), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0169"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0170(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0170

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-10, 0, -10), rotation=(0,0,0))" generates the default Blender cube on location (-10, 0, -10) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-10, 0, -10), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0170"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0171(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0171

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-20, 0, -20), rotation=(0,0,0))" generates the default Blender cube on location (-20, 0, -20) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-20, 0, -20), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0171"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0172(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0172

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-30, 0, -30), rotation=(0,0,0))" generates the default Blender cube on location (-30, 0, -30) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-30, 0, -30), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0172"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0173(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0173

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-100, 0, -100), rotation=(0,0,0))" generates the default Blender cube on location (-100, 0, -100) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-100, 0, -100), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0173"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0174(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0174

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-200, 0, -200), rotation=(0,0,0))" generates the default Blender cube on location (-200, 0, -200) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-200, 0, -200), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0174"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0175(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0175

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-300, 0, -300), rotation=(0,0,0))" generates the default Blender cube on location (-300, 0, -300) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-300, 0, -300), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0175"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0176(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0176

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-10000, 0, -10000), rotation=(0,0,0))" generates the default Blender cube on location (-10000, 0, -10000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-10000, 0, -10000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0176"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0177(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0177

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-20000, 0, -20000), rotation=(0,0,0))" generates the default Blender cube on location (-20000, 0, -20000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-20000, 0, -20000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0177"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0178(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0178

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-30000, 0, -30000), rotation=(0,0,0))" generates the default Blender cube on location (-30000, 0, -30000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-30000, 0, -30000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0178"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0179(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0179

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-1000000, 0, -1000000), rotation=(0,0,0))" generates the default Blender cube on location (-1000000, 0, -1000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-1000000, 0, -1000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0179"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0180(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0180

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-2000000, 0, -2000000), rotation=(0,0,0))" generates the default Blender cube on location (-2000000, 0, -2000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-2000000, 0, -2000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0180"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0181(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0181

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-3000000, 0, -3000000), rotation=(0,0,0))" generates the default Blender cube on location (-3000000, 0, -3000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-3000000, 0, -3000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0181"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0182(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0182

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 1, 1), rotation=(0,0,0))" generates the default Blender cube on location (0, 1, 1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 1, 1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0182"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0183(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0183

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0.1, 0.1), rotation=(0,0,0))" generates the default Blender cube on location (0, 0.1, 0.1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0.1, 0.1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0183"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0184(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0184

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0.01, 0.001), rotation=(0,0,0))" generates the default Blender cube on location (0, 0.01, 0.001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0.01, 0.001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0184"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0185(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0185

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 0.00001, 0.00001), rotation=(0,0,0))" generates the default Blender cube on location (0, 0.00001, 0.00001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 0.00001, 0.00001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0185"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0186(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0186

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 2, 2), rotation=(0,0,0))" generates the default Blender cube on location (0, 2, 2) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 2, 2), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0186"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0187(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0187

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 3, 3), rotation=(0,0,0))" generates the default Blender cube on location (0, 3, 3) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 3, 3), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0187"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0188(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0188

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 10, 10), rotation=(0,0,0))" generates the default Blender cube on location (0, 10, 10) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 10, 10), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0188"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0189(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0189

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 20, 20), rotation=(0,0,0))" generates the default Blender cube on location (0, 20, 20) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 20, 20), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0189"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0190(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0190

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 30, 30), rotation=(0,0,0))" generates the default Blender cube on location (0, 30, 30) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 30, 30), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0190"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0191(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0191

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 100, 100), rotation=(0,0,0))" generates the default Blender cube on location (0, 100, 100) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 100, 100), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0191"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0192(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0192

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 200, 200), rotation=(0,0,0))" generates the default Blender cube on location (0, 200, 200) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 200, 200), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0192"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0193(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0193

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 300, 300), rotation=(0,0,0))" generates the default Blender cube on location (0, 300, 300) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 300, 300), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0193"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0194(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0194

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 10000, 10000), rotation=(0,0,0))" generates the default Blender cube on location (0, 10000, 10000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 10000, 10000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0194"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0195(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0195

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 20000, 20000), rotation=(0,0,0))" generates the default Blender cube on location (0, 20000, 20000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 20000, 20000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0195"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0196(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0196

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 30000, 30000), rotation=(0,0,0))" generates the default Blender cube on location (0, 30000, 30000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 30000, 30000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0196"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0197(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0197

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 1000000, 1000000), rotation=(0,0,0))" generates the default Blender cube on location (0, 1000000, 1000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 1000000, 1000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0197"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0198(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0198

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 2000000, 2000000), rotation=(0,0,0))" generates the default Blender cube on location (0, 2000000, 2000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 2000000, 2000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0198"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0199(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0199

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, 3000000, 3000000), rotation=(0,0,0))" generates the default Blender cube on location (0, 3000000, 3000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, 3000000, 3000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0199"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0200(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0200

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -1, -1), rotation=(0,0,0))" generates the default Blender cube on location (0, -1, -1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -1, -1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0200"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0201(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0201

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -0.1, -0.1), rotation=(0,0,0))" generates the default Blender cube on location (0, -0.1, -0.1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -0.1, -0.1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0201"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0202(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0202

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -0.001, -0.001), rotation=(0,0,0))" generates the default Blender cube on location (0, -0.001, -0.001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -0.001, -0.001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0202"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0203(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0203

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -0.00001, -0.00001), rotation=(0,0,0))" generates the default Blender cube on location (0, -0.00001, -0.00001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -0.00001, -0.00001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0203"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0204(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0204

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -2, -2), rotation=(0,0,0))" generates the default Blender cube on location (0, -2, -2) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -2, -2), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0204"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0205(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0205

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -3, -3), rotation=(0,0,0))" generates the default Blender cube on location (0, -3, -3) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -3, -3), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0205"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0206(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0206

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -10, -10), rotation=(0,0,0))" generates the default Blender cube on location (0, -10, -10) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -10, -10), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0206"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0207(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0207

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -20, -20), rotation=(0,0,0))" generates the default Blender cube on location (0, -20, -20) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -20, -20), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0207"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0208(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0208

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -30, -30), rotation=(0,0,0))" generates the default Blender cube on location (0, -30, -30) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -30, -30), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0208"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0209(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0209

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -100, -100), rotation=(0,0,0))" generates the default Blender cube on location (0, -100, -100) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -100, -100), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0209"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0210(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0210

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -200, -200), rotation=(0,0,0))" generates the default Blender cube on location (0, -200, -200) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -200, -200), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0210"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0211(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0211

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0, -300, -300), rotation=(0,0,0))" generates the default Blender cube on location (0, -300, -300) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0, -300, -300), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0211"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0212(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0212

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,  -10000,  -10000), rotation=(0,0,0))" generates the default Blender cube on location (0,  -10000,  -10000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,  -10000,  -10000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0212"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0213(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0213

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,  -20000,  -20000), rotation=(0,0,0))" generates the default Blender cube on location (0,  -20000,  -20000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,  -20000,  -20000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0213"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0214(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0214

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,  -30000,  -30000), rotation=(0,0,0))" generates the default Blender cube on location (0,  -30000,  -30000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,  -30000,  -30000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0214"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0215(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0215

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,  -1000000,  -1000000), rotation=(0,0,0))" generates the default Blender cube on location (0,  -1000000,  -1000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,  -1000000,  -1000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0215"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0216(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0216

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,  -2000000,  -2000000), rotation=(0,0,0))" generates the default Blender cube on location (0,  -2000000,  -2000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,  -2000000,  -2000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0216"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0217(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0217

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,  -3000000,  -3000000), rotation=(0,0,0))" generates the default Blender cube on location (0,  -3000000,  -3000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,  -3000000,  -3000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0217"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0218(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0218

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(1, 1, 1), rotation=(0,0,0))" generates the default Blender cube on location (1, 1, 1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(1, 1, 1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0218"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0219(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0219

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0.1, 0.1, 0.1), rotation=(0,0,0))" generates the default Blender cube on location (0.1, 0.1, 0.1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0.1, 0.1, 0.1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0219"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0220(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0220

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0.001, 0.01, 0.001), rotation=(0,0,0))" generates the default Blender cube on location (0.001, 0.01, 0.001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0.001, 0.01, 0.001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0220"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0221(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0221

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0.00001, 0.00001, 0.00001), rotation=(0,0,0))" generates the default Blender cube on location (0.00001, 0.00001, 0.00001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0.00001, 0.00001, 0.00001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0221"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0222(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0222

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(2, 2, 2), rotation=(0,0,0))" generates the default Blender cube on location (2, 2, 2) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(2, 2, 2), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0222"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0223(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0223

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(3, 3, 3), rotation=(0,0,0))" generates the default Blender cube on location (3, 3, 3) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(3, 3, 3), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0223"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0224(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0224

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(10, 10, 10), rotation=(0,0,0))" generates the default Blender cube on location (10, 10, 10) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(10, 10, 10), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0224"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0225(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0225

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(20, 20, 20), rotation=(0,0,0))" generates the default Blender cube on location (20, 20, 20) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(20, 20, 20), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0225"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0226(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0226

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(30, 30, 30), rotation=(0,0,0))" generates the default Blender cube on location (30, 30, 30) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(30, 30, 30), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0226"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0227(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0227

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(100, 100, 100), rotation=(0,0,0))" generates the default Blender cube on location (100, 100, 100) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(100, 100, 100), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0227"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0228(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0228

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(200, 200, 200), rotation=(0,0,0))" generates the default Blender cube on location (200, 200, 200) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(200, 200, 200), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0228"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0229(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0229

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(300, 300, 300), rotation=(0,0,0))" generates the default Blender cube on location (300, 300, 300) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(300, 300, 300), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0229"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0230(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0230

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(10000, 10000, 10000), rotation=(0,0,0))" generates the default Blender cube on location (10000, 10000, 10000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(10000, 10000, 10000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0230"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0231(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0231

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(20000, 20000, 20000), rotation=(0,0,0))" generates the default Blender cube on location (20000, 20000, 20000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(20000, 20000, 20000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0231"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0232(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0232

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(30000, 30000, 30000), rotation=(0,0,0))" generates the default Blender cube on location (30000, 30000, 30000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(30000, 30000, 30000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0232"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0233(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0233

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(1000000, 1000000, 1000000), rotation=(0,0,0))" generates the default Blender cube on location (1000000, 1000000, 1000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(1000000, 1000000, 1000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0233"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0234(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0234

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(2000000, 2000000, 2000000), rotation=(0,0,0))" generates the default Blender cube on location (2000000, 2000000, 2000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(2000000, 2000000, 2000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0234"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0235(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0235

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(3000000, 3000000, 3000000), rotation=(0,0,0))" generates the default Blender cube on location (3000000, 3000000, 3000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(3000000, 3000000, 3000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0235"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0236(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0236

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-1, -1, -1), rotation=(0,0,0))" generates the default Blender cube on location (-1, -1, -1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-1, -1, -1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0236"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0237(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0237

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-0.1, -0.1, -0.1), rotation=(0,0,0))" generates the default Blender cube on location (-0.1, -0.1, -0.1) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-0.1, -0.1, -0.1), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0237"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0238(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0238

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-0.001, -0.001, -0.001), rotation=(0,0,0))" generates the default Blender cube on location (-0.001, -0.001, -0.001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-0.001, -0.001, -0.001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0238"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0239(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0239

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-0.00001, -0.00001, -0.00001), rotation=(0,0,0))" generates the default Blender cube on location (-0.00001, -0.00001, -0.00001) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-0.00001, -0.00001, -0.00001), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0239"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0240(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0240

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-2, -2, -2), rotation=(0,0,0))" generates the default Blender cube on location (-2, -2, -2) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-2, -2, -2), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0240"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0241(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0241

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-3, -3, -3), rotation=(0,0,0))" generates the default Blender cube on location (-3, -3, -3) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-3, -3, -3), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0241"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0242(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0242

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-10, -10, -10), rotation=(0,0,0))" generates the default Blender cube on location (-10, -10, -10) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-10, -10, -10), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0242"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0243(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0243

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-20, -20, -20), rotation=(0,0,0))" generates the default Blender cube on location (-20, -20, -20) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-20, -20, -20), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0243"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0244(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0244

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-30, -30, -30), rotation=(0,0,0))" generates the default Blender cube on location (-30, -30, -30) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-30, -30, -30), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0244"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0245(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0245

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-100, -100, -100), rotation=(0,0,0))" generates the default Blender cube on location (-100, -100, -100) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-100, -100, -100), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0245"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0246(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0246

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-200, -200, -200), rotation=(0,0,0))" generates the default Blender cube on location (-200, -200, -200) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-200, -200, -200), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0246"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0247(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0247

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-300, -300, -300), rotation=(0,0,0))" generates the default Blender cube on location (-300, -300, -300) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-300, -300, -300), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0247"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0248(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0248

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-10000, -10000, -10000), rotation=(0,0,0))" generates the default Blender cube on location (-10000, -10000, -10000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-10000, -10000, -10000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0248"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0249(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0249

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-20000, -20000, -20000), rotation=(0,0,0))" generates the default Blender cube on location (-20000, -20000, -20000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-20000, -20000, -20000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0249"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0250(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0250

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-30000, -30000, -30000), rotation=(0,0,0))" generates the default Blender cube on location (-30000, -30000, -30000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-30000, -30000, -30000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0250"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0251(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0251

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-1000000, -1000000, -1000000), rotation=(0,0,0))" generates the default Blender cube on location (-1000000, -1000000, -1000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-1000000, -1000000, -1000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0251"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0252(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0252

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-2000000, -2000000, -2000000), rotation=(0,0,0))" generates the default Blender cube on location (-2000000, -2000000, -2000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-2000000, -2000000, -2000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0252"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0253(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0253

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(-3000000, -3000000, -3000000), rotation=(0,0,0))" generates the default Blender cube on location (-3000000, -3000000, -3000000) with rotation (0,0,0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(-3000000, -3000000, -3000000), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0253"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0254(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0254

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (1, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0254"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0255(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0255

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.1, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (0.1, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.1, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0255"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0256(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0256

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.001, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (0.001, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.001, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0256"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0257(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0257

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.00001, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (0.00001, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.00001, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0257"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0258(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0258

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (2, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0258"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0259(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0259

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (3, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0259"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0260(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0260

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (10, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0260"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0261(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0261

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (20, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0261"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0262(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0262

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (30, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0262"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0263(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0263

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(100, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (100, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(100, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0263"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0264(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0264

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(200, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (200, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(200, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0264"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0265(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0265

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(300, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (300, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(300, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0265"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0266(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0266

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10000, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (10000, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10000, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0266"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0267(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0267

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20000, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (20000, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20000, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0267"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0268(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0268

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30000, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (30000, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30000, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0268"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0269(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0269

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1000000, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (1000000, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1000000, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0269"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0270(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0270

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2000000, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (2000000, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2000000, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0270"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0271(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0271

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3000000, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (3000000, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3000000, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0271"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0272(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0272

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-1, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0272"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0273(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0273

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.1, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-0.1, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.1, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0273"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0274(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0274

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.001, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-0.001, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.001, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0274"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0275(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0275

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.00001, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-0.00001, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.00001, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0275"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0276(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0276

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-2, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0276"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0277(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0277

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-3, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0277"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0278(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0278

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-10, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0278"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0279(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0279

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-20, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0279"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0280(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0280

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-30, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0280"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0281(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0281

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-100, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-100, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-100, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0281"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0282(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0282

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-200, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-200, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-200, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0282"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0283(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0283

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-300, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-300, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-300, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0283"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0284(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0284

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10000, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-10000, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10000, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0284"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0285(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0285

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20000, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-20000, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20000, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0285"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0286(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0286

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30000, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-30000, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30000, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0286"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0287(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0287

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1000000, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-1000000, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1000000, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0287"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0288(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0288

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2000000, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-2000000, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2000000, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0288"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0289(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0289

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3000000, 0, 0))" generates the default Blender cube on location (0,0,0) with rotation (-3000000, 0, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3000000, 0, 0))
        cube = bpy.context.object
        cube.name = "TestCube0289"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0290(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0290

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 1, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 1, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 1, 0))
        cube = bpy.context.object
        cube.name = "TestCube0290"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0291(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0291

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0.1, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 0.1, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0.1, 0))
        cube = bpy.context.object
        cube.name = "TestCube0291"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0292(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0292

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0.001, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 0.001, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0.001, 0))
        cube = bpy.context.object
        cube.name = "TestCube0292"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0293(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0293

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0.00001, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 0.00001, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0.00001, 0))
        cube = bpy.context.object
        cube.name = "TestCube0293"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0294(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0294

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 2, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 2, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 2, 0))
        cube = bpy.context.object
        cube.name = "TestCube0294"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0295(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0295

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 3, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 3, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 3, 0))
        cube = bpy.context.object
        cube.name = "TestCube0295"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0296(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0296

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 10, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 10, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 10, 0))
        cube = bpy.context.object
        cube.name = "TestCube0296"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0297(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0297

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 20, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 20, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 20, 0))
        cube = bpy.context.object
        cube.name = "TestCube0297"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0298(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0298

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 30, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 30, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 30, 0))
        cube = bpy.context.object
        cube.name = "TestCube0298"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0299(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0299

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 100, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 100, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 100, 0))
        cube = bpy.context.object
        cube.name = "TestCube0299"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0300(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0300

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 200, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 200, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 200, 0))
        cube = bpy.context.object
        cube.name = "TestCube0300"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0301(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0301

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 300, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 300, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 300, 0))
        cube = bpy.context.object
        cube.name = "TestCube0301"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0302(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0302

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 10000, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 10000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 10000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0302"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0303(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0303

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 20000, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 20000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 20000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0303"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0304(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0304

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 30000, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 30000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 30000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0304"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0305(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0305

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 1000000, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 1000000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 1000000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0305"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0306(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0306

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 2000000, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 2000000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 2000000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0306"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0307(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0307

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 3000000, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, 3000000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 3000000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0307"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0308(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0308

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -1, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -1, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -1, 0))
        cube = bpy.context.object
        cube.name = "TestCube0308"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0309(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0309

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -0.1, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -0.1, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -0.1, 0))
        cube = bpy.context.object
        cube.name = "TestCube0309"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0310(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0310

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -0.001, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -0.001, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -0.001, 0))
        cube = bpy.context.object
        cube.name = "TestCube0310"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0311(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0311

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -0.00001, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -0.00001, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -0.00001, 0))
        cube = bpy.context.object
        cube.name = "TestCube0311"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0312(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0312

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -2, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -2, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -2, 0))
        cube = bpy.context.object
        cube.name = "TestCube0312"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0313(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0313

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -3, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -3, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -3, 0))
        cube = bpy.context.object
        cube.name = "TestCube0313"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0314(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0314

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -10, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -10, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -10, 0))
        cube = bpy.context.object
        cube.name = "TestCube0314"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0315(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0315

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -20, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -20, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -20, 0))
        cube = bpy.context.object
        cube.name = "TestCube0315"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0316(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0316

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -30, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -30, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -30, 0))
        cube = bpy.context.object
        cube.name = "TestCube0316"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0317(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0317

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -100, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -100, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -100, 0))
        cube = bpy.context.object
        cube.name = "TestCube0317"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0318(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0318

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -200, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -200, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -200, 0))
        cube = bpy.context.object
        cube.name = "TestCube0318"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0319(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0319

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -300, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -300, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -300, 0))
        cube = bpy.context.object
        cube.name = "TestCube0319"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0320(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0320

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -10000, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -10000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -10000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0320"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0321(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0321

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -20000, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -20000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -20000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0321"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0322(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0322

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -30000, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -30000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -30000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0322"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0323(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0323

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -1000000, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -1000000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -1000000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0323"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0324(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0324

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -2000000, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -2000000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -2000000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0324"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0325(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0325

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -3000000, 0))" generates the default Blender cube on location (0,0,0) with rotation (0, -3000000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -3000000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0325"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0326(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0326

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 1))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 1))
        cube = bpy.context.object
        cube.name = "TestCube0326"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0327(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0327

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 0.1))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 0.1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 0.1))
        cube = bpy.context.object
        cube.name = "TestCube0327"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0328(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0328

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 0.001))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 0.001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 0.001))
        cube = bpy.context.object
        cube.name = "TestCube0328"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0329(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0329

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 0.00001))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 0.00001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 0.00001))
        cube = bpy.context.object
        cube.name = "TestCube0329"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0330(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0330

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 2))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 2) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 2))
        cube = bpy.context.object
        cube.name = "TestCube0330"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0331(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0331

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 3))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 3) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 3))
        cube = bpy.context.object
        cube.name = "TestCube0331"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0332(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0332

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 10))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 10) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 10))
        cube = bpy.context.object
        cube.name = "TestCube0332"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0333(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0333

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 20))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 20) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 20))
        cube = bpy.context.object
        cube.name = "TestCube0333"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0334(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0334

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 30))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 30) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 30))
        cube = bpy.context.object
        cube.name = "TestCube0334"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0335(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0335

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 100))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 100) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 100))
        cube = bpy.context.object
        cube.name = "TestCube0335"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0336(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0336

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 200))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 200) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 200))
        cube = bpy.context.object
        cube.name = "TestCube0336"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0337(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0337

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 300))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 300) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 300))
        cube = bpy.context.object
        cube.name = "TestCube0337"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0338(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0338

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 10000))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 10000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 10000))
        cube = bpy.context.object
        cube.name = "TestCube0338"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0339(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0339

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 20000))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 20000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 20000))
        cube = bpy.context.object
        cube.name = "TestCube0339"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0340(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0340

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 30000))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 30000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 30000))
        cube = bpy.context.object
        cube.name = "TestCube0340"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0341(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0341

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 1000000))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 1000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 1000000))
        cube = bpy.context.object
        cube.name = "TestCube0341"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0342(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0342

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 2000000))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 2000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 2000000))
        cube = bpy.context.object
        cube.name = "TestCube0342"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0343(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0343

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 3000000))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, 3000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, 3000000))
        cube = bpy.context.object
        cube.name = "TestCube0343"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0344(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0344

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -1))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -1))
        cube = bpy.context.object
        cube.name = "TestCube0344"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0345(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0345

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -0.1))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -0.1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -0.1))
        cube = bpy.context.object
        cube.name = "TestCube0345"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0346(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0346

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -0.001))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -0.001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -0.001))
        cube = bpy.context.object
        cube.name = "TestCube0346"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0347(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0347

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -0.00001))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -0.00001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -0.00001))
        cube = bpy.context.object
        cube.name = "TestCube0347"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0348(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0348

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -2))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -2) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -2))
        cube = bpy.context.object
        cube.name = "TestCube0348"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0349(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0349

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -3))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -3) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -3))
        cube = bpy.context.object
        cube.name = "TestCube0349"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0350(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0350

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -10))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -10) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -10))
        cube = bpy.context.object
        cube.name = "TestCube0350"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0351(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0351

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -20))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -20) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -20))
        cube = bpy.context.object
        cube.name = "TestCube0351"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0352(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0352

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -30))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -30) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -30))
        cube = bpy.context.object
        cube.name = "TestCube0352"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0353(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0353

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -100))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -100) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -100))
        cube = bpy.context.object
        cube.name = "TestCube0353"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0354(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0354

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -200))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -200) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -200))
        cube = bpy.context.object
        cube.name = "TestCube0354"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0355(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0355

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -300))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -300) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -300))
        cube = bpy.context.object
        cube.name = "TestCube0355"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0356(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0356

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -10000))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -10000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -10000))
        cube = bpy.context.object
        cube.name = "TestCube0356"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0357(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0357

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -20000))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -20000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -20000))
        cube = bpy.context.object
        cube.name = "TestCube0357"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0358(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0358

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -30000))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -30000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -30000))
        cube = bpy.context.object
        cube.name = "TestCube0358"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0359(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0359

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -1000000))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -1000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -1000000))
        cube = bpy.context.object
        cube.name = "TestCube0359"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0360(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0360

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -2000000))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -2000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -2000000))
        cube = bpy.context.object
        cube.name = "TestCube0360"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0361(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0361

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -3000000))" generates the default Blender cube on location (0,0,0) with rotation (0, 0, -3000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0, -3000000))
        cube = bpy.context.object
        cube.name = "TestCube0361"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0362(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0362

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1, 1, 0))" generates the default Blender cube on location (0,0,0) with rotation (1, 1, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1, 1, 0))
        cube = bpy.context.object
        cube.name = "TestCube0362"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0363(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0363

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.1, 0.1, 0))" generates the default Blender cube on location (0,0,0) with rotation (0.1, 0.1, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.1, 0.1, 0))
        cube = bpy.context.object
        cube.name = "TestCube0363"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0364(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0364

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.001, 0.001, 0))" generates the default Blender cube on location (0,0,0) with rotation (0.001, 0.001, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.001, 0.001, 0))
        cube = bpy.context.object
        cube.name = "TestCube0364"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0365(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0365

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.00001, 0.00001, 0))" generates the default Blender cube on location (0,0,0) with rotation (0.00001, 0.00001, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.00001, 0.00001, 0))
        cube = bpy.context.object
        cube.name = "TestCube0365"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0366(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0366

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2, 2, 0))" generates the default Blender cube on location (0,0,0) with rotation (2, 2, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2, 2, 0))
        cube = bpy.context.object
        cube.name = "TestCube0366"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0367(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0367

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3, 3, 0))" generates the default Blender cube on location (0,0,0) with rotation (3, 3, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3, 3, 0))
        cube = bpy.context.object
        cube.name = "TestCube0367"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0368(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0368

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10, 10, 0))" generates the default Blender cube on location (0,0,0) with rotation (10, 10, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10, 10, 0))
        cube = bpy.context.object
        cube.name = "TestCube0368"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0369(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0369

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20, 20, 0))" generates the default Blender cube on location (0,0,0) with rotation (20, 20, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20, 20, 0))
        cube = bpy.context.object
        cube.name = "TestCube0369"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0370(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0370

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30, 30, 0))" generates the default Blender cube on location (0,0,0) with rotation (30, 30, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30, 30, 0))
        cube = bpy.context.object
        cube.name = "TestCube0370"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0371(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0371

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(100, 100, 0))" generates the default Blender cube on location (0,0,0) with rotation (100, 100, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(100, 100, 0))
        cube = bpy.context.object
        cube.name = "TestCube0371"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0372(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0372

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(200, 200, 0))" generates the default Blender cube on location (0,0,0) with rotation (200, 200, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(200, 200, 0))
        cube = bpy.context.object
        cube.name = "TestCube0372"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0373(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0373

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(300, 300, 0))" generates the default Blender cube on location (0,0,0) with rotation (300, 300, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(300, 300, 0))
        cube = bpy.context.object
        cube.name = "TestCube0373"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0374(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0374

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10000, 10000, 0))" generates the default Blender cube on location (0,0,0) with rotation (10000, 10000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10000, 10000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0374"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0375(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0375

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20000, 20000, 0))" generates the default Blender cube on location (0,0,0) with rotation (20000, 20000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20000, 20000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0375"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0376(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0376

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30000, 30000, 0))" generates the default Blender cube on location (0,0,0) with rotation (30000, 30000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30000, 30000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0376"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0377(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0377

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1000000, 1000000, 0))" generates the default Blender cube on location (0,0,0) with rotation (1000000, 1000000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1000000, 1000000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0377"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0378(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0378

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2000000, 2000000, 0))" generates the default Blender cube on location (0,0,0) with rotation (2000000, 2000000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2000000, 2000000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0378"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0379(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0379

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3000000, 3000000, 0))" generates the default Blender cube on location (0,0,0) with rotation (3000000, 3000000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3000000, 3000000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0379"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0380(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0380

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1, -1, 0))" generates the default Blender cube on location (0,0,0) with rotation (-1, -1, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1, -1, 0))
        cube = bpy.context.object
        cube.name = "TestCube0380"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0381(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0381

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.1, -0.1, 0))" generates the default Blender cube on location (0,0,0) with rotation (-0.1, -0.1, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.1, -0.1, 0))
        cube = bpy.context.object
        cube.name = "TestCube0381"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0382(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0382

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.001, -0.001, 0))" generates the default Blender cube on location (0,0,0) with rotation (-0.001, -0.001, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.001, -0.001, 0))
        cube = bpy.context.object
        cube.name = "TestCube0382"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0383(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0383

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.00001, -0.00001, 0))" generates the default Blender cube on location (0,0,0) with rotation (-0.00001, -0.00001, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.00001, -0.00001, 0))
        cube = bpy.context.object
        cube.name = "TestCube0383"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0384(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0384

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2, -2, 0))" generates the default Blender cube on location (0,0,0) with rotation (-2, -2, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2, -2, 0))
        cube = bpy.context.object
        cube.name = "TestCube0384"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0385(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0385

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3, -3, 0))" generates the default Blender cube on location (0,0,0) with rotation (-3, -3, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3, -3, 0))
        cube = bpy.context.object
        cube.name = "TestCube0385"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0386(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0386

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10, -10, 0))" generates the default Blender cube on location (0,0,0) with rotation (-10, -10, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10, -10, 0))
        cube = bpy.context.object
        cube.name = "TestCube0386"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0387(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0387

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20, -20, 0))" generates the default Blender cube on location (0,0,0) with rotation (-20, -20, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20, -20, 0))
        cube = bpy.context.object
        cube.name = "TestCube0387"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0388(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0388

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30, -30, 0))" generates the default Blender cube on location (0,0,0) with rotation (-30, -30, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30, -30, 0))
        cube = bpy.context.object
        cube.name = "TestCube0388"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0389(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0389

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-100, -100, 0))" generates the default Blender cube on location (0,0,0) with rotation (-100, -100, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-100, -100, 0))
        cube = bpy.context.object
        cube.name = "TestCube0389"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0390(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0390

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-200, -200, 0))" generates the default Blender cube on location (0,0,0) with rotation (-200, -200, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-200, -200, 0))
        cube = bpy.context.object
        cube.name = "TestCube0390"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0391(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0391

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-300, -300, 0))" generates the default Blender cube on location (0,0,0) with rotation (-300, -300, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-300, -300, 0))
        cube = bpy.context.object
        cube.name = "TestCube0391"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0392(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0392

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10000, -10000, 0))" generates the default Blender cube on location (0,0,0) with rotation (-10000, -10000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10000, -10000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0392"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0393(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0393

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20000, -20000, 0))" generates the default Blender cube on location (0,0,0) with rotation (-20000, -20000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20000, -20000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0393"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0394(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0394

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30000, -30000, 0))" generates the default Blender cube on location (0,0,0) with rotation (-30000, -30000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30000, -30000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0394"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0395(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0395

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1000000, -1000000, 0))" generates the default Blender cube on location (0,0,0) with rotation (-1000000, -1000000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1000000, -1000000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0395"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0396(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0396

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2000000, -2000000, 0))" generates the default Blender cube on location (0,0,0) with rotation (-2000000, -2000000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2000000, -2000000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0396"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0397(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0397

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3000000, -3000000, 0))" generates the default Blender cube on location (0,0,0) with rotation (-3000000, -3000000, 0) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3000000, -3000000, 0))
        cube = bpy.context.object
        cube.name = "TestCube0397"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0398(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0398

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1, 0, 1))" generates the default Blender cube on location (0,0,0) with rotation (1, 0, 1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1, 0, 1))
        cube = bpy.context.object
        cube.name = "TestCube0398"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0399(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0399

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.1, 0, 0.1))" generates the default Blender cube on location (0,0,0) with rotation (0.1, 0, 0.1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.1, 0, 0.1))
        cube = bpy.context.object
        cube.name = "TestCube0399"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0400(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0400

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.001, 0, 0.001))" generates the default Blender cube on location (0,0,0) with rotation (0.001, 0, 0.001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.001, 0, 0.001))
        cube = bpy.context.object
        cube.name = "TestCube0400"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0401(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0401

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.00001, 0, 0.00001))" generates the default Blender cube on location (0,0,0) with rotation (0.00001, 0, 0.00001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.00001, 0, 0.00001))
        cube = bpy.context.object
        cube.name = "TestCube0401"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0402(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0402

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2, 0, 2))" generates the default Blender cube on location (0,0,0) with rotation (2, 0, 2) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2, 0, 2))
        cube = bpy.context.object
        cube.name = "TestCube0402"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0403(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0403

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3, 0, 3))" generates the default Blender cube on location (0,0,0) with rotation (3, 0, 3) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3, 0, 3))
        cube = bpy.context.object
        cube.name = "TestCube0403"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0404(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0404

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10, 0, 10))" generates the default Blender cube on location (0,0,0) with rotation (10, 0, 10) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10, 0, 10))
        cube = bpy.context.object
        cube.name = "TestCube0404"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0405(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0405

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20, 0, 20))" generates the default Blender cube on location (0,0,0) with rotation (20, 0, 20) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20, 0, 20))
        cube = bpy.context.object
        cube.name = "TestCube0405"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0406(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0406

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30, 0, 30))" generates the default Blender cube on location (0,0,0) with rotation (30, 0, 30) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30, 0, 30))
        cube = bpy.context.object
        cube.name = "TestCube0406"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0407(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0407

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(100, 0, 100))" generates the default Blender cube on location (0,0,0) with rotation (100, 0, 100) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(100, 0, 100))
        cube = bpy.context.object
        cube.name = "TestCube0407"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0408(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0408

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(200, 0, 200))" generates the default Blender cube on location (0,0,0) with rotation (200, 0, 200) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(200, 0, 200))
        cube = bpy.context.object
        cube.name = "TestCube0408"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0409(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0409

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(300, 0, 300))" generates the default Blender cube on location (0,0,0) with rotation (300, 0, 300) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(300, 0, 300))
        cube = bpy.context.object
        cube.name = "TestCube0409"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0410(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0410

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10000, 0,  10000))" generates the default Blender cube on location (0,0,0) with rotation (10000, 0,  10000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10000, 0,  10000))
        cube = bpy.context.object
        cube.name = "TestCube0410"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0411(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0411

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20000, 0,  20000))" generates the default Blender cube on location (0,0,0) with rotation (20000, 0,  20000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20000, 0,  20000))
        cube = bpy.context.object
        cube.name = "TestCube0411"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0412(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0412

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30000, 0,  30000))" generates the default Blender cube on location (0,0,0) with rotation (30000, 0,  30000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30000, 0,  30000))
        cube = bpy.context.object
        cube.name = "TestCube0412"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0413(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0413

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1000000, 0,  1000000))" generates the default Blender cube on location (0,0,0) with rotation (1000000, 0,  1000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1000000, 0,  1000000))
        cube = bpy.context.object
        cube.name = "TestCube0413"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0414(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0414

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2000000, 0,  2000000))" generates the default Blender cube on location (0,0,0) with rotation (2000000, 0,  2000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2000000, 0,  2000000))
        cube = bpy.context.object
        cube.name = "TestCube0414"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0415(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0415

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3000000, 0,  3000000))" generates the default Blender cube on location (0,0,0) with rotation (3000000, 0,  3000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3000000, 0,  3000000))
        cube = bpy.context.object
        cube.name = "TestCube0415"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0416(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0416

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1, 0, -1))" generates the default Blender cube on location (0,0,0) with rotation (-1, 0, -1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1, 0, -1))
        cube = bpy.context.object
        cube.name = "TestCube0416"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0417(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0417

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.1, 0, -0.1))" generates the default Blender cube on location (0,0,0) with rotation (-0.1, 0, -0.1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.1, 0, -0.1))
        cube = bpy.context.object
        cube.name = "TestCube0417"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0418(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0418

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.001, 0, -0.001))" generates the default Blender cube on location (0,0,0) with rotation (-0.001, 0, -0.001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.001, 0, -0.001))
        cube = bpy.context.object
        cube.name = "TestCube0418"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0419(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0419

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.00001, 0, -0.00001))" generates the default Blender cube on location (0,0,0) with rotation (-0.00001, 0, -0.00001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.00001, 0, -0.00001))
        cube = bpy.context.object
        cube.name = "TestCube0419"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0420(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0420

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2, 0, -2))" generates the default Blender cube on location (0,0,0) with rotation (-2, 0, -2) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2, 0, -2))
        cube = bpy.context.object
        cube.name = "TestCube0420"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0421(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0421

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3, 0, -3))" generates the default Blender cube on location (0,0,0) with rotation (-3, 0, -3) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3, 0, -3))
        cube = bpy.context.object
        cube.name = "TestCube0421"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0422(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0422

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10, 0, -10))" generates the default Blender cube on location (0,0,0) with rotation (-10, 0, -10) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10, 0, -10))
        cube = bpy.context.object
        cube.name = "TestCube0422"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0423(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0423

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20, 0, -20))" generates the default Blender cube on location (0,0,0) with rotation (-20, 0, -20) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20, 0, -20))
        cube = bpy.context.object
        cube.name = "TestCube0423"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0424(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0424

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30, 0, -30))" generates the default Blender cube on location (0,0,0) with rotation (-30, 0, -30) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30, 0, -30))
        cube = bpy.context.object
        cube.name = "TestCube0424"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0425(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0425

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-100, 0, -100))" generates the default Blender cube on location (0,0,0) with rotation (-100, 0, -100) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-100, 0, -100))
        cube = bpy.context.object
        cube.name = "TestCube0425"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0426(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0426

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-200, 0, -200))" generates the default Blender cube on location (0,0,0) with rotation (-200, 0, -200) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-200, 0, -200))
        cube = bpy.context.object
        cube.name = "TestCube0426"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0427(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0427

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-300, 0, -300))" generates the default Blender cube on location (0,0,0) with rotation (-300, 0, -300) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-300, 0, -300))
        cube = bpy.context.object
        cube.name = "TestCube0427"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0428(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0428

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10000, 0, -10000))" generates the default Blender cube on location (0,0,0) with rotation (-10000, 0, -10000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10000, 0, -10000))
        cube = bpy.context.object
        cube.name = "TestCube0428"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0429(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0429

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20000, 0, -20000))" generates the default Blender cube on location (0,0,0) with rotation (-20000, 0, -20000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20000, 0, -20000))
        cube = bpy.context.object
        cube.name = "TestCube0429"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0430(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0430

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30000, 0, -30000))" generates the default Blender cube on location (0,0,0) with rotation (-30000, 0, -30000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30000, 0, -30000))
        cube = bpy.context.object
        cube.name = "TestCube0430"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0431(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0431

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1000000, 0, -1000000))" generates the default Blender cube on location (0,0,0) with rotation (-1000000, 0, -1000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1000000, 0, -1000000))
        cube = bpy.context.object
        cube.name = "TestCube0431"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0432(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0432

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2000000, 0, -2000000))" generates the default Blender cube on location (0,0,0) with rotation (-2000000, 0, -2000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2000000, 0, -2000000))
        cube = bpy.context.object
        cube.name = "TestCube0432"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0433(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0433

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3000000, 0, -3000000))" generates the default Blender cube on location (0,0,0) with rotation (-3000000, 0, -3000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3000000, 0, -3000000))
        cube = bpy.context.object
        cube.name = "TestCube0433"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0434(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0434

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 1, 1))" generates the default Blender cube on location (0,0,0) with rotation (0, 1, 1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 1, 1))
        cube = bpy.context.object
        cube.name = "TestCube0434"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0435(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0435

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0.1, 0.1))" generates the default Blender cube on location (0,0,0) with rotation (0, 0.1, 0.1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0.1, 0.1))
        cube = bpy.context.object
        cube.name = "TestCube0435"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0436(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0436

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0.01, 0.001))" generates the default Blender cube on location (0,0,0) with rotation (0, 0.01, 0.001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0.01, 0.001))
        cube = bpy.context.object
        cube.name = "TestCube0436"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0437(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0437

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0.00001, 0.00001))" generates the default Blender cube on location (0,0,0) with rotation (0, 0.00001, 0.00001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 0.00001, 0.00001))
        cube = bpy.context.object
        cube.name = "TestCube0437"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0438(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0438

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 2, 2))" generates the default Blender cube on location (0,0,0) with rotation (0, 2, 2) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 2, 2))
        cube = bpy.context.object
        cube.name = "TestCube0438"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0439(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0439

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 3, 3))" generates the default Blender cube on location (0,0,0) with rotation (0, 3, 3) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 3, 3))
        cube = bpy.context.object
        cube.name = "TestCube0439"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0440(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0440

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 10, 10))" generates the default Blender cube on location (0,0,0) with rotation (0, 10, 10) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 10, 10))
        cube = bpy.context.object
        cube.name = "TestCube0440"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0441(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0441

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 20, 20))" generates the default Blender cube on location (0,0,0) with rotation (0, 20, 20) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 20, 20))
        cube = bpy.context.object
        cube.name = "TestCube0441"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0442(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0442

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 30, 30))" generates the default Blender cube on location (0,0,0) with rotation (0, 30, 30) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 30, 30))
        cube = bpy.context.object
        cube.name = "TestCube0442"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0443(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0443

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 100, 100))" generates the default Blender cube on location (0,0,0) with rotation (0, 100, 100) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 100, 100))
        cube = bpy.context.object
        cube.name = "TestCube0443"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0444(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0444

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 200, 200))" generates the default Blender cube on location (0,0,0) with rotation (0, 200, 200) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 200, 200))
        cube = bpy.context.object
        cube.name = "TestCube0444"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0445(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0445

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 300, 300))" generates the default Blender cube on location (0,0,0) with rotation (0, 300, 300) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 300, 300))
        cube = bpy.context.object
        cube.name = "TestCube0445"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0446(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0446

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 10000, 10000))" generates the default Blender cube on location (0,0,0) with rotation (0, 10000, 10000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 10000, 10000))
        cube = bpy.context.object
        cube.name = "TestCube0446"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0447(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0447

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 20000, 20000))" generates the default Blender cube on location (0,0,0) with rotation (0, 20000, 20000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 20000, 20000))
        cube = bpy.context.object
        cube.name = "TestCube0447"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0448(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0448

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 30000, 30000))" generates the default Blender cube on location (0,0,0) with rotation (0, 30000, 30000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 30000, 30000))
        cube = bpy.context.object
        cube.name = "TestCube0448"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0449(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0449

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 1000000, 1000000))" generates the default Blender cube on location (0,0,0) with rotation (0, 1000000, 1000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 1000000, 1000000))
        cube = bpy.context.object
        cube.name = "TestCube0449"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0450(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0450

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 2000000, 2000000))" generates the default Blender cube on location (0,0,0) with rotation (0, 2000000, 2000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 2000000, 2000000))
        cube = bpy.context.object
        cube.name = "TestCube0450"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0451(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0451

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 3000000, 3000000))" generates the default Blender cube on location (0,0,0) with rotation (0, 3000000, 3000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, 3000000, 3000000))
        cube = bpy.context.object
        cube.name = "TestCube0451"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0452(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0452

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -1, -1))" generates the default Blender cube on location (0,0,0) with rotation (0, -1, -1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -1, -1))
        cube = bpy.context.object
        cube.name = "TestCube0452"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0453(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0453

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -0.1, -0.1))" generates the default Blender cube on location (0,0,0) with rotation (0, -0.1, -0.1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -0.1, -0.1))
        cube = bpy.context.object
        cube.name = "TestCube0453"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0454(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0454

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -0.001, -0.001))" generates the default Blender cube on location (0,0,0) with rotation (0, -0.001, -0.001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -0.001, -0.001))
        cube = bpy.context.object
        cube.name = "TestCube0454"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0455(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0455

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -0.00001, -0.00001))" generates the default Blender cube on location (0,0,0) with rotation (0, -0.00001, -0.00001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -0.00001, -0.00001))
        cube = bpy.context.object
        cube.name = "TestCube0455"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0456(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0456

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -2, -2))" generates the default Blender cube on location (0,0,0) with rotation (0, -2, -2) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -2, -2))
        cube = bpy.context.object
        cube.name = "TestCube0456"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0457(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0457

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -3, -3))" generates the default Blender cube on location (0,0,0) with rotation (0, -3, -3) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -3, -3))
        cube = bpy.context.object
        cube.name = "TestCube0457"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0458(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0458

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -10, -10))" generates the default Blender cube on location (0,0,0) with rotation (0, -10, -10) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -10, -10))
        cube = bpy.context.object
        cube.name = "TestCube0458"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0459(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0459

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -20, -20))" generates the default Blender cube on location (0,0,0) with rotation (0, -20, -20) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -20, -20))
        cube = bpy.context.object
        cube.name = "TestCube0459"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0460(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0460

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -30, -30))" generates the default Blender cube on location (0,0,0) with rotation (0, -30, -30) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -30, -30))
        cube = bpy.context.object
        cube.name = "TestCube0460"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0461(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0461

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -100, -100))" generates the default Blender cube on location (0,0,0) with rotation (0, -100, -100) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -100, -100))
        cube = bpy.context.object
        cube.name = "TestCube0461"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0462(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0462

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -200, -200))" generates the default Blender cube on location (0,0,0) with rotation (0, -200, -200) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -200, -200))
        cube = bpy.context.object
        cube.name = "TestCube0462"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0463(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0463

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -300, -300))" generates the default Blender cube on location (0,0,0) with rotation (0, -300, -300) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0, -300, -300))
        cube = bpy.context.object
        cube.name = "TestCube0463"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0464(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0464

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,  -10000,  -10000))" generates the default Blender cube on location (0,0,0) with rotation (0,  -10000,  -10000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,  -10000,  -10000))
        cube = bpy.context.object
        cube.name = "TestCube0464"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0465(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0465

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,  -20000,  -20000))" generates the default Blender cube on location (0,0,0) with rotation (0,  -20000,  -20000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,  -20000,  -20000))
        cube = bpy.context.object
        cube.name = "TestCube0465"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0466(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0466

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,  -30000,  -30000))" generates the default Blender cube on location (0,0,0) with rotation (0,  -30000,  -30000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,  -30000,  -30000))
        cube = bpy.context.object
        cube.name = "TestCube0466"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0467(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0467

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,  -1000000,  -1000000))" generates the default Blender cube on location (0,0,0) with rotation (0,  -1000000,  -1000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,  -1000000,  -1000000))
        cube = bpy.context.object
        cube.name = "TestCube0467"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0468(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0468

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,  -2000000,  -2000000))" generates the default Blender cube on location (0,0,0) with rotation (0,  -2000000,  -2000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,  -2000000,  -2000000))
        cube = bpy.context.object
        cube.name = "TestCube0468"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0469(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0469

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,  -3000000,  -3000000))" generates the default Blender cube on location (0,0,0) with rotation (0,  -3000000,  -3000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,  -3000000,  -3000000))
        cube = bpy.context.object
        cube.name = "TestCube0469"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0470(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0470

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1, 1, 1))" generates the default Blender cube on location (0,0,0) with rotation (1, 1, 1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1, 1, 1))
        cube = bpy.context.object
        cube.name = "TestCube0470"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0471(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0471

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.1, 0.1, 0.1))" generates the default Blender cube on location (0,0,0) with rotation (0.1, 0.1, 0.1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.1, 0.1, 0.1))
        cube = bpy.context.object
        cube.name = "TestCube0471"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0472(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0472

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.001, 0.01, 0.001))" generates the default Blender cube on location (0,0,0) with rotation (0.001, 0.01, 0.001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.001, 0.01, 0.001))
        cube = bpy.context.object
        cube.name = "TestCube0472"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0473(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0473

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.00001, 0.00001, 0.00001))" generates the default Blender cube on location (0,0,0) with rotation (0.00001, 0.00001, 0.00001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0.00001, 0.00001, 0.00001))
        cube = bpy.context.object
        cube.name = "TestCube0473"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0474(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0474

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2, 2, 2))" generates the default Blender cube on location (0,0,0) with rotation (2, 2, 2) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2, 2, 2))
        cube = bpy.context.object
        cube.name = "TestCube0474"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0475(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0475

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3, 3, 3))" generates the default Blender cube on location (0,0,0) with rotation (3, 3, 3) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3, 3, 3))
        cube = bpy.context.object
        cube.name = "TestCube0475"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0476(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0476

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10, 10, 10))" generates the default Blender cube on location (0,0,0) with rotation (10, 10, 10) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10, 10, 10))
        cube = bpy.context.object
        cube.name = "TestCube0476"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0477(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0477

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20, 20, 20))" generates the default Blender cube on location (0,0,0) with rotation (20, 20, 20) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20, 20, 20))
        cube = bpy.context.object
        cube.name = "TestCube0477"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0478(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0478

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30, 30, 30))" generates the default Blender cube on location (0,0,0) with rotation (30, 30, 30) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30, 30, 30))
        cube = bpy.context.object
        cube.name = "TestCube0478"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0479(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0479

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(100, 100, 100))" generates the default Blender cube on location (0,0,0) with rotation (100, 100, 100) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(100, 100, 100))
        cube = bpy.context.object
        cube.name = "TestCube0479"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0480(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0480

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(200, 200, 200))" generates the default Blender cube on location (0,0,0) with rotation (200, 200, 200) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(200, 200, 200))
        cube = bpy.context.object
        cube.name = "TestCube0480"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0481(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0481

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(300, 300, 300))" generates the default Blender cube on location (0,0,0) with rotation (300, 300, 300) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(300, 300, 300))
        cube = bpy.context.object
        cube.name = "TestCube0481"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0482(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0482

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10000, 10000, 10000))" generates the default Blender cube on location (0,0,0) with rotation (10000, 10000, 10000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(10000, 10000, 10000))
        cube = bpy.context.object
        cube.name = "TestCube0482"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0483(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0483

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20000, 20000, 20000))" generates the default Blender cube on location (0,0,0) with rotation (20000, 20000, 20000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(20000, 20000, 20000))
        cube = bpy.context.object
        cube.name = "TestCube0483"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0484(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0484

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30000, 30000, 30000))" generates the default Blender cube on location (0,0,0) with rotation (30000, 30000, 30000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(30000, 30000, 30000))
        cube = bpy.context.object
        cube.name = "TestCube0484"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0485(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0485

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1000000, 1000000, 1000000))" generates the default Blender cube on location (0,0,0) with rotation (1000000, 1000000, 1000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(1000000, 1000000, 1000000))
        cube = bpy.context.object
        cube.name = "TestCube0485"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0486(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0486

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2000000, 2000000, 2000000))" generates the default Blender cube on location (0,0,0) with rotation (2000000, 2000000, 2000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(2000000, 2000000, 2000000))
        cube = bpy.context.object
        cube.name = "TestCube0486"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0487(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0487

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3000000, 3000000, 3000000))" generates the default Blender cube on location (0,0,0) with rotation (3000000, 3000000, 3000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(3000000, 3000000, 3000000))
        cube = bpy.context.object
        cube.name = "TestCube0487"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0488(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0488

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1, -1, -1))" generates the default Blender cube on location (0,0,0) with rotation (-1, -1, -1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1, -1, -1))
        cube = bpy.context.object
        cube.name = "TestCube0488"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0489(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0489

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.1, -0.1, -0.1))" generates the default Blender cube on location (0,0,0) with rotation (-0.1, -0.1, -0.1) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.1, -0.1, -0.1))
        cube = bpy.context.object
        cube.name = "TestCube0489"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0490(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0490

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.001, -0.001, -0.001))" generates the default Blender cube on location (0,0,0) with rotation (-0.001, -0.001, -0.001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.001, -0.001, -0.001))
        cube = bpy.context.object
        cube.name = "TestCube0490"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0491(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0491

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.00001, -0.00001, -0.00001))" generates the default Blender cube on location (0,0,0) with rotation (-0.00001, -0.00001, -0.00001) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-0.00001, -0.00001, -0.00001))
        cube = bpy.context.object
        cube.name = "TestCube0491"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0492(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0492

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2, -2, -2))" generates the default Blender cube on location (0,0,0) with rotation (-2, -2, -2) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2, -2, -2))
        cube = bpy.context.object
        cube.name = "TestCube0492"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0493(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0493

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3, -3, -3))" generates the default Blender cube on location (0,0,0) with rotation (-3, -3, -3) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3, -3, -3))
        cube = bpy.context.object
        cube.name = "TestCube0493"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0494(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0494

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10, -10, -10))" generates the default Blender cube on location (0,0,0) with rotation (-10, -10, -10) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10, -10, -10))
        cube = bpy.context.object
        cube.name = "TestCube0494"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0495(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0495

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20, -20, -20))" generates the default Blender cube on location (0,0,0) with rotation (-20, -20, -20) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20, -20, -20))
        cube = bpy.context.object
        cube.name = "TestCube0495"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0496(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0496

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30, -30, -30))" generates the default Blender cube on location (0,0,0) with rotation (-30, -30, -30) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30, -30, -30))
        cube = bpy.context.object
        cube.name = "TestCube0496"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0497(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0497

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-100, -100, -100))" generates the default Blender cube on location (0,0,0) with rotation (-100, -100, -100) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-100, -100, -100))
        cube = bpy.context.object
        cube.name = "TestCube0497"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0498(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0498

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-200, -200, -200))" generates the default Blender cube on location (0,0,0) with rotation (-200, -200, -200) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-200, -200, -200))
        cube = bpy.context.object
        cube.name = "TestCube0498"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0499(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0499

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-300, -300, -300))" generates the default Blender cube on location (0,0,0) with rotation (-300, -300, -300) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-300, -300, -300))
        cube = bpy.context.object
        cube.name = "TestCube0499"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0500(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0500

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10000, -10000, -10000))" generates the default Blender cube on location (0,0,0) with rotation (-10000, -10000, -10000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-10000, -10000, -10000))
        cube = bpy.context.object
        cube.name = "TestCube0500"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0501(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0501

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20000, -20000, -20000))" generates the default Blender cube on location (0,0,0) with rotation (-20000, -20000, -20000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-20000, -20000, -20000))
        cube = bpy.context.object
        cube.name = "TestCube0501"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0502(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0502

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30000, -30000, -30000))" generates the default Blender cube on location (0,0,0) with rotation (-30000, -30000, -30000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-30000, -30000, -30000))
        cube = bpy.context.object
        cube.name = "TestCube0502"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0503(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0503

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1000000, -1000000, -1000000))" generates the default Blender cube on location (0,0,0) with rotation (-1000000, -1000000, -1000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-1000000, -1000000, -1000000))
        cube = bpy.context.object
        cube.name = "TestCube0503"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0504(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0504

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2000000, -2000000, -2000000))" generates the default Blender cube on location (0,0,0) with rotation (-2000000, -2000000, -2000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-2000000, -2000000, -2000000))
        cube = bpy.context.object
        cube.name = "TestCube0504"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0505(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0505

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3000000, -3000000, -3000000))" generates the default Blender cube on location (0,0,0) with rotation (-3000000, -3000000, -3000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3000000, -3000000, -3000000))
        cube = bpy.context.object
        cube.name = "TestCube0505"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)
    def test_WYMeshTestCase_triangulate_mesh_TC_NC_0506(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYUtil triangulate_mesh function testing normal case 0506

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object is properly triangulated through "triangulate_mesh" function, which primitive is created with code "bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3000000, -3000000, -3000000))" generates the default Blender cube on location (0,0,0) with rotation (-3000000, -3000000, -3000000) resulting len(cube.data.polygons) == 12 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: len(cube.data.polygons) == 12
        :expect: len(cube.data.polygons) == 6
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(-3000000, -3000000, -3000000))
        cube = bpy.context.object
        cube.name = "TestCube0506"
        wyutil = WYUtil()
        self.assertTrue(len(cube.data.polygons) == 6)
        wyutil.triangulate_mesh(cube.data)
        self.assertTrue(len(cube.data.polygons) == 12)

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYUtilTestCases_triangulate_mesh))
