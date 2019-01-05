"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2017-10-22
Last update                         : 2017-12-21
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYMeshTestCases_get_mesh_mtllib_str\WYMeshTestCases_get_mesh_mtllib_str.py
Test case data file name            : ..\..\test\WYMeshTestCases_get_mesh_mtllib_str\WYMeshTestCases_get_mesh_mtllib_str.txt
Testing class file name             : ..\..\main\WYMesh\WYMesh.py
Testing class function name         : get_mesh_mtllib_str()
Unit test case class name           : WYMeshTestCases_get_mesh_mtllib_str
Unit test case description          : Unit test case for class WYMesh get_mesh_mtllib_str() function
Unit test case result file name     : ..\..\test\WYMeshTestCases_get_mesh_mtllib_str\WYMeshTestCaseResult_get_mesh_mtllib_str.txt
"""
# Pre-condition: init_mesh_material_relfile_path(mesh_material_relfile_path) function is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYMesh\\WYMesh.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYMeshTestCases_get_mesh_mtllib_str(unittest.TestCase):
    """
    Unit test case for class WYMesh get_mesh_mtllib_str() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYMeshTestCase_get_mesh_mtllib_str_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the relative material file path export string is properly retrieved as mtllib TestMaterialFilePath0001.txt\n with "get_mesh_mtllib_str" function which "mesh_mat_relfile_path" was initialized as "TestMaterialFilePath0001.txt" through member function "init_mesh_material_relfile_path" function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0001.txt"
        :expect: self.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0001.txt\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0001", bpy.data.meshes.new("TestMesh0001")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0001.txt")

        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0001.txt")
        self.assertTrue(wymesh.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0001.txt\n")
    def test_WYMeshTestCase_get_mesh_mtllib_str_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the relative material file path export string is properly retrieved as mtllib TestMaterialFilePath0002.txt\n with "get_mesh_mtllib_str" function which "mesh_mat_relfile_path" was initialized as "TestMaterialFilePath0002.txt" through member function "init_mesh_material_relfile_path" function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0002.txt"
        :expect: self.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0002.txt\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0002", bpy.data.meshes.new("TestMesh0002")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0002.txt")

        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0002.txt")
        self.assertTrue(wymesh.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0002.txt\n")
    def test_WYMeshTestCase_get_mesh_mtllib_str_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the relative material file path export string is properly retrieved as mtllib TestMaterialFilePath0003.txt\n with "get_mesh_mtllib_str" function which "mesh_mat_relfile_path" was initialized as "TestMaterialFilePath0003.txt" through member function "init_mesh_material_relfile_path" function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0003.txt"
        :expect: self.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0003.txt\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0003", bpy.data.meshes.new("TestMesh0003")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0003.txt")

        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0003.txt")
        self.assertTrue(wymesh.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0003.txt\n")
    def test_WYMeshTestCase_get_mesh_mtllib_str_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the relative material file path export string is properly retrieved as mtllib TestMaterialFilePath0004.txt\n with "get_mesh_mtllib_str" function which "mesh_mat_relfile_path" was initialized as "TestMaterialFilePath0004.txt" through member function "init_mesh_material_relfile_path" function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0004.txt"
        :expect: self.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0004.txt\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0004", bpy.data.meshes.new("TestMesh0004")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0004.txt")

        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0004.txt")
        self.assertTrue(wymesh.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0004.txt\n")
    def test_WYMeshTestCase_get_mesh_mtllib_str_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the relative material file path export string is properly retrieved as mtllib TestMaterialFilePath0005.txt\n with "get_mesh_mtllib_str" function which "mesh_mat_relfile_path" was initialized as "TestMaterialFilePath0005.txt" through member function "init_mesh_material_relfile_path" function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0005.txt"
        :expect: self.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0005.txt\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0005", bpy.data.meshes.new("TestMesh0005")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0005.txt")

        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0005.txt")
        self.assertTrue(wymesh.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0005.txt\n")
    def test_WYMeshTestCase_get_mesh_mtllib_str_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the relative material file path export string is properly retrieved as mtllib TestMaterialFilePath0006.txt\n with "get_mesh_mtllib_str" function which "mesh_mat_relfile_path" was initialized as "TestMaterialFilePath0006.txt" through member function "init_mesh_material_relfile_path" function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0006.txt"
        :expect: self.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0006.txt\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0006", bpy.data.meshes.new("TestMesh0006")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0006.txt")

        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0006.txt")
        self.assertTrue(wymesh.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0006.txt\n")
    def test_WYMeshTestCase_get_mesh_mtllib_str_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the relative material file path export string is properly retrieved as mtllib TestMaterialFilePath0007.txt\n with "get_mesh_mtllib_str" function which "mesh_mat_relfile_path" was initialized as "TestMaterialFilePath0007.txt" through member function "init_mesh_material_relfile_path" function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0007.txt"
        :expect: self.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0007.txt\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0007", bpy.data.meshes.new("TestMesh0007")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0007.txt")

        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0007.txt")
        self.assertTrue(wymesh.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0007.txt\n")
    def test_WYMeshTestCase_get_mesh_mtllib_str_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the relative material file path export string is properly retrieved as mtllib TestMaterialFilePath0008.txt\n with "get_mesh_mtllib_str" function which "mesh_mat_relfile_path" was initialized as "TestMaterialFilePath0008.txt" through member function "init_mesh_material_relfile_path" function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0008.txt"
        :expect: self.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0008.txt\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0008", bpy.data.meshes.new("TestMesh0008")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0008.txt")

        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0008.txt")
        self.assertTrue(wymesh.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0008.txt\n")
    def test_WYMeshTestCase_get_mesh_mtllib_str_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the relative material file path export string is properly retrieved as mtllib TestMaterialFilePath0009.txt\n with "get_mesh_mtllib_str" function which "mesh_mat_relfile_path" was initialized as "TestMaterialFilePath0009.txt" through member function "init_mesh_material_relfile_path" function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0009.txt"
        :expect: self.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0009.txt\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0009", bpy.data.meshes.new("TestMesh0009")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0009.txt")

        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0009.txt")
        self.assertTrue(wymesh.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0009.txt\n")
    def test_WYMeshTestCase_get_mesh_mtllib_str_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the relative material file path export string is properly retrieved as mtllib TestMaterialFilePath0010.txt\n with "get_mesh_mtllib_str" function which "mesh_mat_relfile_path" was initialized as "TestMaterialFilePath0010.txt" through member function "init_mesh_material_relfile_path" function.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : string
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: self.mesh_material_relfile_path == "TestMaterialFilePath0010.txt"
        :expect: self.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0010.txt\\n"
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0010", bpy.data.meshes.new("TestMesh0010")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_material_relfile_path("TestMaterialFilePath0010.txt")

        self.assertTrue(wymesh.mesh_material_relfile_path == "TestMaterialFilePath0010.txt")
        self.assertTrue(wymesh.get_mesh_mtllib_str() == "mtllib TestMaterialFilePath0010.txt\n")

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYMeshTestCases_get_mesh_mtllib_str))
