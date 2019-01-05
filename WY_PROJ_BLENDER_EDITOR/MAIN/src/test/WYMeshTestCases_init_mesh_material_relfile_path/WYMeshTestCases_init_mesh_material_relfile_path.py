"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2017-10-25
Last update                         : 2018-01-02
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYMeshTestCases_init_mesh_material_relfile_path\WYMeshTestCases_init_mesh_material_relfile_path.py
Test case data file name            : ..\..\test\WYMeshTestCases_init_mesh_material_relfile_path\WYMeshTestCases_init_mesh_material_relfile_path.txt
Testing class file name             : ..\..\main\WYMesh\WYMesh.py
Testing class function name         : init_mesh_material_relfile_path(mesh_material_relfile_path)
Unit test case class name           : WYMeshTestCases_init_mesh_material_relfile_path
Unit test case description          : Unit test case for class WYMesh init_mesh_material_relfile_path() function
Unit test case result file name     : ..\..\test\WYMeshTestCases_init_mesh_material_relfile_path\WYMeshTestCaseResult_init_mesh_material_relfile_path.txt
"""

import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYMesh\\WYMesh.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYMeshTestCases_init_mesh_material_relfile_path(unittest.TestCase):
    """
    Unit test case for class WYMesh init_mesh_material_relfile_path() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYMeshTestCase_init_mesh_material_relfile_path_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_material_relfile_path function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variable "mesh_mat_relfile_path" relative material file path is properly intialized with "TestMaterialFilePath0001.txt".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0001.txt"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0001", bpy.data.meshes.new("TestMesh0001")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0001.txt")
        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0001.txt")
    def test_WYMeshTestCase_init_mesh_material_relfile_path_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_material_relfile_path function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variable "mesh_mat_relfile_path" relative material file path is properly intialized with "TestMaterialFilePath0002.txt".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0002.txt"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0002", bpy.data.meshes.new("TestMesh0002")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0002.txt")
        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0002.txt")
    def test_WYMeshTestCase_init_mesh_material_relfile_path_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_material_relfile_path function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variable "mesh_mat_relfile_path" relative material file path is properly intialized with "TestMaterialFilePath0003.txt".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0003.txt"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0003", bpy.data.meshes.new("TestMesh0003")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0003.txt")
        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0003.txt")
    def test_WYMeshTestCase_init_mesh_material_relfile_path_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_material_relfile_path function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variable "mesh_mat_relfile_path" relative material file path is properly intialized with "TestMaterialFilePath0004.txt".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0004.txt"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0004", bpy.data.meshes.new("TestMesh0004")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0004.txt")
        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0004.txt")
    def test_WYMeshTestCase_init_mesh_material_relfile_path_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_material_relfile_path function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variable "mesh_mat_relfile_path" relative material file path is properly intialized with "TestMaterialFilePath0005.txt".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0005.txt"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0005", bpy.data.meshes.new("TestMesh0005")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0005.txt")
        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0005.txt")
    def test_WYMeshTestCase_init_mesh_material_relfile_path_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_material_relfile_path function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variable "mesh_mat_relfile_path" relative material file path is properly intialized with "TestMaterialFilePath0006.txt".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0006.txt"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0006", bpy.data.meshes.new("TestMesh0006")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0006.txt")
        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0006.txt")
    def test_WYMeshTestCase_init_mesh_material_relfile_path_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_material_relfile_path function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variable "mesh_mat_relfile_path" relative material file path is properly intialized with "TestMaterialFilePath0007.txt".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0007.txt"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0007", bpy.data.meshes.new("TestMesh0007")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0007.txt")
        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0007.txt")
    def test_WYMeshTestCase_init_mesh_material_relfile_path_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_material_relfile_path function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variable "mesh_mat_relfile_path" relative material file path is properly intialized with "TestMaterialFilePath0008.txt".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0008.txt"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0008", bpy.data.meshes.new("TestMesh0008")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0008.txt")
        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0008.txt")
    def test_WYMeshTestCase_init_mesh_material_relfile_path_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_material_relfile_path function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variable "mesh_mat_relfile_path" relative material file path is properly intialized with "TestMaterialFilePath0009.txt".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0009.txt"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0009", bpy.data.meshes.new("TestMesh0009")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0009.txt")
        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0009.txt")
    def test_WYMeshTestCase_init_mesh_material_relfile_path_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_mesh_material_relfile_path function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variable "mesh_mat_relfile_path" relative material file path is properly intialized with "TestMaterialFilePath0010.txt".
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0010.txt"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0010", bpy.data.meshes.new("TestMesh0010")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0010.txt")
        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0010.txt")

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYMeshTestCases_init_mesh_material_relfile_path))
