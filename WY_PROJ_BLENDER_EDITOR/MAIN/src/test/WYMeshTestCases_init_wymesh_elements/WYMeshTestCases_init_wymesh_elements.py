"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2017-10-22
Last update                         : 2017-12-21
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYMeshTestCases_init_wymesh_elements\WYMeshTestCases_init_wymesh_elements.py
Test case data file name            : ..\..\test\WYMeshTestCases_init_wymesh_elements\WYMeshTestCases_init_wymesh_elements.txt
Testing class file name             : ..\..\main\WYMesh\WYMesh.py
Testing class function name         : init_wymesh_elements()
Unit test case class name           : WYMeshTestCases_init_wymesh_elements
Unit test case description          : Unit test case for class WYMesh init_wymesh_elements() function
Unit test case result file name     : ..\..\test\WYMeshTestCases_init_wymesh_elements\WYMeshTestCaseResult_init_wymesh_elements.txt
"""

import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYMesh\\WYMesh.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYMeshTestCases_init_wymesh_elements(unittest.TestCase):
    """
    Unit test case for class WYMesh init_wymesh_elements() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :4
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYMeshTestCase_init_wymesh_elements_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variables mesh_name,mesh_material_relfile_path, mesh_vertex_array, mesh_vertex_index_array, mesh_normal_array, mesh_normal_index_array, mesh_texture_coord_array, and mesh_texture_coord_index_array are properly intialized with default values with the main initialization function "init_wymesh_elements" function call 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == ""
        :expect: wymesh.mesh_material_relfile_path == ""
        :expect: wymesh.mesh_vertex_array == []
        :expect: wymesh.mesh_vertex_index_array == []
        :expect: wymesh.mesh_normal_array == []
        :expect: wymesh.mesh_normal_index_array == []
        :expect: wymesh.mesh_texture_coord_array == []
        :expect: wymesh.mesh_texture_coord_index_array == []
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0001", bpy.data.meshes.new("TestMesh0001")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))

        self.assertTrue(wymesh.mesh_obj_name == "")
        self.assertTrue(wymesh.mesh_material_relfile_path == "")
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])
    def test_WYMeshTestCase_init_wymesh_elements_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variables mesh_name,mesh_material_relfile_path, mesh_vertex_array, mesh_vertex_index_array, mesh_normal_array, mesh_normal_index_array, mesh_texture_coord_array, and mesh_texture_coord_index_array are properly intialized with default values with the main initialization function "init_wymesh_elements" function call 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == ""
        :expect: wymesh.mesh_material_relfile_path == ""
        :expect: wymesh.mesh_vertex_array == []
        :expect: wymesh.mesh_vertex_index_array == []
        :expect: wymesh.mesh_normal_array == []
        :expect: wymesh.mesh_normal_index_array == []
        :expect: wymesh.mesh_texture_coord_array == []
        :expect: wymesh.mesh_texture_coord_index_array == []
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0002", bpy.data.meshes.new("TestMesh0002")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))

        self.assertTrue(wymesh.mesh_obj_name == "")
        self.assertTrue(wymesh.mesh_material_relfile_path == "")
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])
    def test_WYMeshTestCase_init_wymesh_elements_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variables mesh_name,mesh_material_relfile_path, mesh_vertex_array, mesh_vertex_index_array, mesh_normal_array, mesh_normal_index_array, mesh_texture_coord_array, and mesh_texture_coord_index_array are properly intialized with default values with the main initialization function "init_wymesh_elements" function call 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == ""
        :expect: wymesh.mesh_material_relfile_path == ""
        :expect: wymesh.mesh_vertex_array == []
        :expect: wymesh.mesh_vertex_index_array == []
        :expect: wymesh.mesh_normal_array == []
        :expect: wymesh.mesh_normal_index_array == []
        :expect: wymesh.mesh_texture_coord_array == []
        :expect: wymesh.mesh_texture_coord_index_array == []
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0003", bpy.data.meshes.new("TestMesh0003")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))

        self.assertTrue(wymesh.mesh_obj_name == "")
        self.assertTrue(wymesh.mesh_material_relfile_path == "")
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])
    def test_WYMeshTestCase_init_wymesh_elements_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh init_wymesh_elements function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the member variables mesh_name,mesh_material_relfile_path, mesh_vertex_array, mesh_vertex_index_array, mesh_normal_array, mesh_normal_index_array, mesh_texture_coord_array, and mesh_texture_coord_index_array are properly intialized with default values with the main initialization function "init_wymesh_elements" function call 
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wymesh.mesh_obj_name == ""
        :expect: wymesh.mesh_material_relfile_path == ""
        :expect: wymesh.mesh_vertex_array == []
        :expect: wymesh.mesh_vertex_index_array == []
        :expect: wymesh.mesh_normal_array == []
        :expect: wymesh.mesh_normal_index_array == []
        :expect: wymesh.mesh_texture_coord_array == []
        :expect: wymesh.mesh_texture_coord_index_array == []
        """
        wymesh = WYMesh(bpy.data.objects.new("TestObject0004", bpy.data.meshes.new("TestMesh0004")), WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))

        self.assertTrue(wymesh.mesh_obj_name == "")
        self.assertTrue(wymesh.mesh_material_relfile_path == "")
        self.assertTrue(wymesh.mesh_vertex_array == [])
        self.assertTrue(wymesh.mesh_vertex_index_array == [])
        self.assertTrue(wymesh.mesh_normal_array == [])
        self.assertTrue(wymesh.mesh_normal_index_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_array == [])
        self.assertTrue(wymesh.mesh_texture_coord_index_array == [])

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYMeshTestCases_init_wymesh_elements))
