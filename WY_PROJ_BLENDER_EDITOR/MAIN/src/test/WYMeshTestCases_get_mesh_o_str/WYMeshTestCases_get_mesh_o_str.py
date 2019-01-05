"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2017-10-22
Last update                         : 2017-10-22
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYMeshTestCases_get_mesh_o_str\WYMeshTestCases_get_mesh_o_str.py
Test case data file name            : ..\..\test\WYMeshTestCases_get_mesh_o_str\WYMeshTestCases_get_mesh_o_str.txt
Testing class file name             : ..\..\main\WYMesh\WYMesh.py
Testing class function name         : get_mesh_o_str()
Unit test case class name           : WYMeshTestCases_get_mesh_o_str
Unit test case description          : Unit test case for class WYMesh get_mesh_o_str() function
Unit test case result file name     : ..\..\test\WYMeshTestCases_get_mesh_o_str\WYMeshTestCaseResult_get_mesh_o_str.txt
"""
# Pre-condition: WYMesh::init_mesh_name() is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYMesh\\WYMesh.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYMeshTestCases_get_mesh_o_str(unittest.TestCase):
    """
    Unit test case for class WYMesh get_mesh_o_str() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :5
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYMeshTestCase_get_mesh_o_str_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh get_mesh_o_str function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object name export string is properly retrieved as "o TestObject0001\n" with "get_mesh_o_str" function which mesh_obj_name was initialized as "TestObject0001" through __init__ function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == "TestObject0001"
        :expect: wymesh.get_mesh_o_str() == "o TestObject0001\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0001", bpy.data.meshes.new("TestMesh0001")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_name()
        self.assertTrue(wymesh.mesh_obj_name == "TestObject0001")
        self.assertTrue(wymesh.get_mesh_o_str() == "o TestObject0001\n")
    def test_WYMeshTestCase_get_mesh_o_str_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh get_mesh_o_str function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object name export string is properly retrieved as "o TestObject0002\n" with "get_mesh_o_str" function which mesh_obj_name was initialized as "TestObject0002" through __init__ function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == "TestObject0002"
        :expect: wymesh.get_mesh_o_str() == "o TestObject0002\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0002", bpy.data.meshes.new("TestMesh0002")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_name()
        self.assertTrue(wymesh.mesh_obj_name == "TestObject0002")
        self.assertTrue(wymesh.get_mesh_o_str() == "o TestObject0002\n")
    def test_WYMeshTestCase_get_mesh_o_str_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh get_mesh_o_str function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object name export string is properly retrieved as "o TestObject0003\n" with "get_mesh_o_str" function which mesh_obj_name was initialized as "TestObject0003" through __init__ function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == "TestObject0003"
        :expect: wymesh.get_mesh_o_str() == "o TestObject0003\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0003", bpy.data.meshes.new("TestMesh0003")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_name()
        self.assertTrue(wymesh.mesh_obj_name == "TestObject0003")
        self.assertTrue(wymesh.get_mesh_o_str() == "o TestObject0003\n")
    def test_WYMeshTestCase_get_mesh_o_str_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh get_mesh_o_str function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object name export string is properly retrieved as "o TestObject0004\n" with "get_mesh_o_str" function which mesh_obj_name was initialized as "TestObject0004" through __init__ function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == "TestObject0004"
        :expect: wymesh.get_mesh_o_str() == "o TestObject0004\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0004", bpy.data.meshes.new("TestMesh0004")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_name()
        self.assertTrue(wymesh.mesh_obj_name == "TestObject0004")
        self.assertTrue(wymesh.get_mesh_o_str() == "o TestObject0004\n")
    def test_WYMeshTestCase_get_mesh_o_str_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh get_mesh_o_str function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the mesh object name export string is properly retrieved as "o TestObject0005\n" with "get_mesh_o_str" function which mesh_obj_name was initialized as "TestObject0005" through __init__ function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == "TestObject0005"
        :expect: wymesh.get_mesh_o_str() == "o TestObject0005\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0005", bpy.data.meshes.new("TestMesh0005")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_name()
        self.assertTrue(wymesh.mesh_obj_name == "TestObject0005")
        self.assertTrue(wymesh.get_mesh_o_str() == "o TestObject0005\n")

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYMeshTestCases_get_mesh_o_str))
