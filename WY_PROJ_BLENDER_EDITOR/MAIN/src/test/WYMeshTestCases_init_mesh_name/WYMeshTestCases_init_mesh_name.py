"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2017-12-21
Last update                         : 2017-12-21
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYMeshTestCases_init_mesh_name\WYMeshTestCases_init_mesh_name.py
Test case data file name            : ..\..\test\WYMeshTestCases_init_mesh_name\WYMeshTestCases_init_mesh_name.txt
Testing class file name             : ..\..\main\WYMesh\WYMesh.py
Testing class function name         : init_mesh_name()
Unit test case class name           : WYMeshTestCases_init_mesh_name
Unit test case description          : Unit test case for class WYMesh init_mesh_name() function
Unit test case result file name     : ..\..\test\WYMeshTestCases_init_mesh_name\WYMeshTestCaseResult_init_mesh_name.txt
"""

import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYMesh\\WYMesh.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYMeshTestCases_init_mesh_name(unittest.TestCase):
    """
    Unit test case for class WYMesh init_mesh_name() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :5
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYMeshTestCase_init_mesh_name_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_name function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object name member variable is initialized with "init_mesh_name" function which mesh_obj_name was initialized as "TestObject0001".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == "TestObject0001"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0001", bpy.data.meshes.new("TestMesh0001")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_name()
        self.assertTrue(wymesh.mesh_obj_name == "TestObject0001")
    def test_WYMeshTestCase_init_mesh_name_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_name function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object name member variable is initialized with "init_mesh_name" function which mesh_obj_name was initialized as "TestObject0002".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == "TestObject0002"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0002", bpy.data.meshes.new("TestMesh0002")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_name()
        self.assertTrue(wymesh.mesh_obj_name == "TestObject0002")
    def test_WYMeshTestCase_init_mesh_name_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_name function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object name member variable is initialized with "init_mesh_name" function which mesh_obj_name was initialized as "TestObject0003".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == "TestObject0003"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0003", bpy.data.meshes.new("TestMesh0003")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_name()
        self.assertTrue(wymesh.mesh_obj_name == "TestObject0003")
    def test_WYMeshTestCase_init_mesh_name_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_name function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object name member variable is initialized with "init_mesh_name" function which mesh_obj_name was initialized as "TestObject0004".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == "TestObject0004"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0004", bpy.data.meshes.new("TestMesh0004")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_name()
        self.assertTrue(wymesh.mesh_obj_name == "TestObject0004")
    def test_WYMeshTestCase_init_mesh_name_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_name function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object name member variable is initialized with "init_mesh_name" function which mesh_obj_name was initialized as "TestObject0005".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == "TestObject0005"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0005", bpy.data.meshes.new("TestMesh0005")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_name()
        self.assertTrue(wymesh.mesh_obj_name == "TestObject0005")

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYMeshTestCases_init_mesh_name))
