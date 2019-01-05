"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2017-11-22
Last update                         : 2017-11-29
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_import_material\WYModelManagerTestCases_import_material.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_import_material\WYModelManagerTestCases_import_material.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : import_material(material_file_path)
Unit test case class name           : WYModelManagerTestCases_import_material
Unit test case description          : Unit test case for class WYModelManager import_material() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_import_material\WYModelManagerTestCaseResult_import_material.txt
"""
import bpy
import mathutils

# Pre-condition: WYModel is tested.
# Pre-condition: WYModelManager::export_model() is tested.
# Pre-condition: WYModelManager::import_wymaterial() is tested.
# Pre-condition: WYMaterial::__str__() is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_import_material(unittest.TestCase):
    """
    Unit test case for class WYModelManager import_material() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_import_material_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_material function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender material object is imported properly through import_material function, returning the data values initialized onto a Blender material object resulting the returned Blender material object "(testmaterial.main_material_obj.name == "TestMaterial0001") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param material_file_path: String of the file path to import the Blender material object from..
        :type  material_file_path: string.
        :test  material_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0001.wym".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0001") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0001 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0001.wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0001\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmaterial = wymodelmanager0001.import_material(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0001.wym")         
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0001") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_material_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_material function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender material object is imported properly through import_material function, returning the data values initialized onto a Blender material object resulting the returned Blender material object "(testmaterial.main_material_obj.name == "TestMaterial0002") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param material_file_path: String of the file path to import the Blender material object from..
        :type  material_file_path: string.
        :test  material_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0002.wym".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0002") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0002 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0002.wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0002\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmaterial = wymodelmanager0002.import_material(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0002.wym")         
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0002") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_material_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_material function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender material object is imported properly through import_material function, returning the data values initialized onto a Blender material object resulting the returned Blender material object "(testmaterial.main_material_obj.name == "TestMaterial0003") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param material_file_path: String of the file path to import the Blender material object from..
        :type  material_file_path: string.
        :test  material_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0003.wym".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0003") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0003 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0003.wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0003\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmaterial = wymodelmanager0003.import_material(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0003.wym")         
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0003") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_material_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_material function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender material object is imported properly through import_material function, returning the data values initialized onto a Blender material object resulting the returned Blender material object "(testmaterial.main_material_obj.name == "TestMaterial0004") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param material_file_path: String of the file path to import the Blender material object from..
        :type  material_file_path: string.
        :test  material_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0004.wym".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0004") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0004 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0004.wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0004\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmaterial = wymodelmanager0004.import_material(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0004.wym")         
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0004") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_material_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_material function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender material object is imported properly through import_material function, returning the data values initialized onto a Blender material object resulting the returned Blender material object "(testmaterial.main_material_obj.name == "TestMaterial0005") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param material_file_path: String of the file path to import the Blender material object from..
        :type  material_file_path: string.
        :test  material_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0005.wym".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0005") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0005 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0005.wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0005\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmaterial = wymodelmanager0005.import_material(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0005.wym")         
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0005") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_material_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_material function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender material object is imported properly through import_material function, returning the data values initialized onto a Blender material object resulting the returned Blender material object "(testmaterial.main_material_obj.name == "TestMaterial0006") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param material_file_path: String of the file path to import the Blender material object from..
        :type  material_file_path: string.
        :test  material_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0006.wym".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0006") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0006 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0006.wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0006\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmaterial = wymodelmanager0006.import_material(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0006.wym")         
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0006") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_material_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_material function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender material object is imported properly through import_material function, returning the data values initialized onto a Blender material object resulting the returned Blender material object "(testmaterial.main_material_obj.name == "TestMaterial0007") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param material_file_path: String of the file path to import the Blender material object from..
        :type  material_file_path: string.
        :test  material_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0007.wym".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0007") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0007 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0007.wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0007\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmaterial = wymodelmanager0007.import_material(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0007.wym")         
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0007") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_material_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_material function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender material object is imported properly through import_material function, returning the data values initialized onto a Blender material object resulting the returned Blender material object "(testmaterial.main_material_obj.name == "TestMaterial0008") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param material_file_path: String of the file path to import the Blender material object from..
        :type  material_file_path: string.
        :test  material_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0008.wym".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0008") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0008 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0008.wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0008\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmaterial = wymodelmanager0008.import_material(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0008.wym")         
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0008") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_material_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_material function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender material object is imported properly through import_material function, returning the data values initialized onto a Blender material object resulting the returned Blender material object "(testmaterial.main_material_obj.name == "TestMaterial0009") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param material_file_path: String of the file path to import the Blender material object from..
        :type  material_file_path: string.
        :test  material_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0009.wym".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0009") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0009 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0009.wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0009\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmaterial = wymodelmanager0009.import_material(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0009.wym")         
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0009") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))
    def test_WYModelManagerTestCase_import_material_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_material function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender material object is imported properly through import_material function, returning the data values initialized onto a Blender material object resulting the returned Blender material object "(testmaterial.main_material_obj.name == "TestMaterial0010") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param material_file_path: String of the file path to import the Blender material object from..
        :type  material_file_path: string.
        :test  material_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0010.wym".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmaterial.main_material_obj.name == "TestMaterial0010") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None)
        """
        
        wymodelmanager0010 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0010.wym", 'w+') as content_file:
            content_file.write("mtl_material_name TestMaterial0010\nmtl_mirror_color 0.0 0.0 0.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.0 0.0 0.0\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.0 0.0 0.0\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")
        testmaterial = wymodelmanager0010.import_material(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_material\\Test0010.wym")         
        self.assertTrue((testmaterial.main_material_obj.name == "TestMaterial0010") and (testmaterial.main_material_obj.mirror_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.ambient == 1.0) and (testmaterial.main_material_obj.diffuse_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.diffuse_intensity == 0.800000011920929) and (testmaterial.main_material_obj.specular_color == mathutils.Color((0,0,0))) and (testmaterial.main_material_obj.specular_intensity == 0.5) and (testmaterial.main_material_obj.specular_hardness ==  97) and (testmaterial.main_material_obj.emit == 0.0) and (testmaterial.main_material_obj.alpha  == 1.0) and (testmaterial.main_material_obj.raytrace_transparency.ior == 1.0) and (testmaterial.main_material_obj.texture_slots[0] == None))

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_import_material))
