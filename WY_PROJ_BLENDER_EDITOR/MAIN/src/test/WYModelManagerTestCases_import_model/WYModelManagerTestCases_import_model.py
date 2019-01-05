"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2018-01-21
Last update                         : 2018-01-21
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_import_model\WYModelManagerTestCases_import_model.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_import_model\WYModelManagerTestCases_import_model.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : import_model(file_path)
Unit test case class name           : WYModelManagerTestCases_import_model
Unit test case description          : Unit test case for class WYModelManager import_model() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_import_model\WYModelManagerTestCaseResult_import_model.txt
"""
import bpy
import mathutils

# Pre-condition: WYModel is tested.
# Pre-condition: WYModelManager::export_model() is tested.
# Pre-condition: WYModelManager::import_wymesh() is tested.
# Pre-condition: WYModelManager::import_wymaterial() is tested.
# Pre-condition: WYMaterial::__str__() is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_import_model(unittest.TestCase):
    """
    Unit test case for class WYModelManager import_model() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_import_model_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_model function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh and Blender material object is imported properly through import_model function, returning the data values initialized onto a WYModel object resulting the returned WYModel object has WYMesh object value imported (testmesh.name == "TestObject0001") and (len(testmesh.polygons) == 12) and WYMaterial object value imported (testmaterial.main_material_obj.name == "TestMaterial0001") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None).
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the WYModel object from, where i can load WYMaterial and WYMesh object from file by appending extension to the file path.
        :type  file_path: string.
        :test  file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0001".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYModel
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0001") and (len(testmesh.polygons) == 12)
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0001") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0001 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0001" + ".wyo", 'w+') as content_file:
            content_file.write("o TestObject0001\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0001" + ".wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")

        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0001" + ".wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0001\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmodel = wymodelmanager0001.import_model(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0001")     
        testmesh = bpy.data.objects["TestObject0001"].data    
        testmaterial = testmodel.main_wymaterial
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0001") and (len(testmesh.polygons) == 12))
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0001") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_model_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_model function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh and Blender material object is imported properly through import_model function, returning the data values initialized onto a WYModel object resulting the returned WYModel object has WYMesh object value imported (testmesh.name == "TestObject0002") and (len(testmesh.polygons) == 12) and WYMaterial object value imported (testmaterial.main_material_obj.name == "TestMaterial0002") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None).
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the WYModel object from, where i can load WYMaterial and WYMesh object from file by appending extension to the file path.
        :type  file_path: string.
        :test  file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0002".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYModel
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0002") and (len(testmesh.polygons) == 12)
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0002") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0002 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0002" + ".wyo", 'w+') as content_file:
            content_file.write("o TestObject0002\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0002" + ".wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")

        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0002" + ".wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0002\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmodel = wymodelmanager0002.import_model(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0002")     
        testmesh = bpy.data.objects["TestObject0002"].data    
        testmaterial = testmodel.main_wymaterial
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0002") and (len(testmesh.polygons) == 12))
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0002") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_model_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_model function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh and Blender material object is imported properly through import_model function, returning the data values initialized onto a WYModel object resulting the returned WYModel object has WYMesh object value imported (testmesh.name == "TestObject0003") and (len(testmesh.polygons) == 12) and WYMaterial object value imported (testmaterial.main_material_obj.name == "TestMaterial0003") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None).
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the WYModel object from, where i can load WYMaterial and WYMesh object from file by appending extension to the file path.
        :type  file_path: string.
        :test  file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0003".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYModel
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0003") and (len(testmesh.polygons) == 12)
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0003") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0003 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0003" + ".wyo", 'w+') as content_file:
            content_file.write("o TestObject0003\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0003" + ".wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")

        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0003" + ".wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0003\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmodel = wymodelmanager0003.import_model(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0003")     
        testmesh = bpy.data.objects["TestObject0003"].data    
        testmaterial = testmodel.main_wymaterial
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0003") and (len(testmesh.polygons) == 12))
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0003") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_model_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_model function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh and Blender material object is imported properly through import_model function, returning the data values initialized onto a WYModel object resulting the returned WYModel object has WYMesh object value imported (testmesh.name == "TestObject0004") and (len(testmesh.polygons) == 12) and WYMaterial object value imported (testmaterial.main_material_obj.name == "TestMaterial0004") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None).
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the WYModel object from, where i can load WYMaterial and WYMesh object from file by appending extension to the file path.
        :type  file_path: string.
        :test  file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0004".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYModel
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0004") and (len(testmesh.polygons) == 12)
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0004") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0004 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0004" + ".wyo", 'w+') as content_file:
            content_file.write("o TestObject0004\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0004" + ".wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")

        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0004" + ".wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0004\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmodel = wymodelmanager0004.import_model(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0004")     
        testmesh = bpy.data.objects["TestObject0004"].data    
        testmaterial = testmodel.main_wymaterial
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0004") and (len(testmesh.polygons) == 12))
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0004") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_model_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_model function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh and Blender material object is imported properly through import_model function, returning the data values initialized onto a WYModel object resulting the returned WYModel object has WYMesh object value imported (testmesh.name == "TestObject0005") and (len(testmesh.polygons) == 12) and WYMaterial object value imported (testmaterial.main_material_obj.name == "TestMaterial0005") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None).
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the WYModel object from, where i can load WYMaterial and WYMesh object from file by appending extension to the file path.
        :type  file_path: string.
        :test  file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0005".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYModel
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0005") and (len(testmesh.polygons) == 12)
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0005") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0005 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0005" + ".wyo", 'w+') as content_file:
            content_file.write("o TestObject0005\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0005" + ".wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")

        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0005" + ".wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0005\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmodel = wymodelmanager0005.import_model(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0005")     
        testmesh = bpy.data.objects["TestObject0005"].data    
        testmaterial = testmodel.main_wymaterial
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0005") and (len(testmesh.polygons) == 12))
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0005") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_model_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_model function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh and Blender material object is imported properly through import_model function, returning the data values initialized onto a WYModel object resulting the returned WYModel object has WYMesh object value imported (testmesh.name == "TestObject0006") and (len(testmesh.polygons) == 12) and WYMaterial object value imported (testmaterial.main_material_obj.name == "TestMaterial0006") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None).
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the WYModel object from, where i can load WYMaterial and WYMesh object from file by appending extension to the file path.
        :type  file_path: string.
        :test  file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0006".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYModel
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0006") and (len(testmesh.polygons) == 12)
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0006") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0006 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0006" + ".wyo", 'w+') as content_file:
            content_file.write("o TestObject0006\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0006" + ".wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")

        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0006" + ".wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0006\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmodel = wymodelmanager0006.import_model(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0006")     
        testmesh = bpy.data.objects["TestObject0006"].data    
        testmaterial = testmodel.main_wymaterial
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0006") and (len(testmesh.polygons) == 12))
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0006") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_model_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_model function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh and Blender material object is imported properly through import_model function, returning the data values initialized onto a WYModel object resulting the returned WYModel object has WYMesh object value imported (testmesh.name == "TestObject0007") and (len(testmesh.polygons) == 12) and WYMaterial object value imported (testmaterial.main_material_obj.name == "TestMaterial0007") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None).
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the WYModel object from, where i can load WYMaterial and WYMesh object from file by appending extension to the file path.
        :type  file_path: string.
        :test  file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0007".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYModel
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0007") and (len(testmesh.polygons) == 12)
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0007") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0007 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0007" + ".wyo", 'w+') as content_file:
            content_file.write("o TestObject0007\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0007" + ".wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")

        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0007" + ".wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0007\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmodel = wymodelmanager0007.import_model(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0007")     
        testmesh = bpy.data.objects["TestObject0007"].data    
        testmaterial = testmodel.main_wymaterial
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0007") and (len(testmesh.polygons) == 12))
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0007") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_model_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_model function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh and Blender material object is imported properly through import_model function, returning the data values initialized onto a WYModel object resulting the returned WYModel object has WYMesh object value imported (testmesh.name == "TestObject0008") and (len(testmesh.polygons) == 12) and WYMaterial object value imported (testmaterial.main_material_obj.name == "TestMaterial0008") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None).
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the WYModel object from, where i can load WYMaterial and WYMesh object from file by appending extension to the file path.
        :type  file_path: string.
        :test  file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0008".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYModel
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0008") and (len(testmesh.polygons) == 12)
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0008") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0008 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0008" + ".wyo", 'w+') as content_file:
            content_file.write("o TestObject0008\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0008" + ".wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")

        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0008" + ".wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0008\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmodel = wymodelmanager0008.import_model(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0008")     
        testmesh = bpy.data.objects["TestObject0008"].data    
        testmaterial = testmodel.main_wymaterial
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0008") and (len(testmesh.polygons) == 12))
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0008") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_model_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_model function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh and Blender material object is imported properly through import_model function, returning the data values initialized onto a WYModel object resulting the returned WYModel object has WYMesh object value imported (testmesh.name == "TestObject0009") and (len(testmesh.polygons) == 12) and WYMaterial object value imported (testmaterial.main_material_obj.name == "TestMaterial0009") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None).
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the WYModel object from, where i can load WYMaterial and WYMesh object from file by appending extension to the file path.
        :type  file_path: string.
        :test  file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0009".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYModel
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0009") and (len(testmesh.polygons) == 12)
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0009") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0009 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0009" + ".wyo", 'w+') as content_file:
            content_file.write("o TestObject0009\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0009" + ".wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")

        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0009" + ".wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0009\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmodel = wymodelmanager0009.import_model(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0009")     
        testmesh = bpy.data.objects["TestObject0009"].data    
        testmaterial = testmodel.main_wymaterial
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0009") and (len(testmesh.polygons) == 12))
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0009") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_model_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_model function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh and Blender material object is imported properly through import_model function, returning the data values initialized onto a WYModel object resulting the returned WYModel object has WYMesh object value imported (testmesh.name == "TestObject0010") and (len(testmesh.polygons) == 12) and WYMaterial object value imported (testmaterial.main_material_obj.name == "TestMaterial0010") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None).
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the WYModel object from, where i can load WYMaterial and WYMesh object from file by appending extension to the file path.
        :type  file_path: string.
        :test  file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0010".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYModel
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0010") and (len(testmesh.polygons) == 12)
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0010") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0010 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0010" + ".wyo", 'w+') as content_file:
            content_file.write("o TestObject0010\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0010" + ".wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")

        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0010" + ".wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0010\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmodel = wymodelmanager0010.import_model(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_model\\Test0010")     
        testmesh = bpy.data.objects["TestObject0010"].data    
        testmaterial = testmodel.main_wymaterial
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0010") and (len(testmesh.polygons) == 12))
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0010") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_import_model))
