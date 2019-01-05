"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2018-01-21
Last update                         : 2018-01-21
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_export_wymaterial\WYModelManagerTestCases_export_wymaterial.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_export_wymaterial\WYModelManagerTestCases_export_wymaterial.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : export_wymaterial(wymaterial, wymaterial_file_path)
Unit test case class name           : WYModelManagerTestCases_export_wymaterial
Unit test case description          : Unit test case for class WYModelManager export_wymaterial() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_export_wymaterial\WYModelManagerTestCaseResult_export_wymaterial.txt
"""
# Pre-condition: WYModel is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_export_wymaterial(unittest.TestCase):
    """
    Unit test case for class WYModelManager export_wymaterial() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_export_wymaterial_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymaterial function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the default Blender material object is exported onto the given relative path "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0001" through "export_wymaterial" function resulting the string read from the given file path is equal to ""mtl_material_name TestMaterial0001\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymaterial: WYMaterial object to export with..
        :type  wymaterial: WYMaterial.
        :test  wymaterial: WYModel(wymesh,wymaterial).

        :param wymaterial_file_path: String of the file path to export the WYMaterial object onto.
        :type  wymaterial_file_path: string.
        :test  wymaterial_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "mtl_material_name TestMaterial0001\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0001"
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0001"))
        wymaterial.init_material_data()
        wymodelmanager0001 = WYModelManager() 
        wymodelmanager0001.export_wymaterial(wymaterial, "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0001.wym")

        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0001.wym', 'r') as content_file:
            content = content_file.read()       
        self.assertTrue(content == "mtl_material_name TestMaterial0001\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")


    def test_WYModelManagerTestCase_export_wymaterial_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymaterial function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the default Blender material object is exported onto the given relative path "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0002" through "export_wymaterial" function resulting the string read from the given file path is equal to ""mtl_material_name TestMaterial0002\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymaterial: WYMaterial object to export with..
        :type  wymaterial: WYMaterial.
        :test  wymaterial: WYModel(wymesh,wymaterial).

        :param wymaterial_file_path: String of the file path to export the WYMaterial object onto.
        :type  wymaterial_file_path: string.
        :test  wymaterial_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "mtl_material_name TestMaterial0002\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0002"
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0002"))
        wymaterial.init_material_data()
        wymodelmanager0002 = WYModelManager() 
        wymodelmanager0002.export_wymaterial(wymaterial, "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0002.wym")

        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0002.wym', 'r') as content_file:
            content = content_file.read()       
        self.assertTrue(content == "mtl_material_name TestMaterial0002\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")


    def test_WYModelManagerTestCase_export_wymaterial_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymaterial function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the default Blender material object is exported onto the given relative path "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0003" through "export_wymaterial" function resulting the string read from the given file path is equal to ""mtl_material_name TestMaterial0003\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymaterial: WYMaterial object to export with..
        :type  wymaterial: WYMaterial.
        :test  wymaterial: WYModel(wymesh,wymaterial).

        :param wymaterial_file_path: String of the file path to export the WYMaterial object onto.
        :type  wymaterial_file_path: string.
        :test  wymaterial_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "mtl_material_name TestMaterial0003\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0003"
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0003"))
        wymaterial.init_material_data()
        wymodelmanager0003 = WYModelManager() 
        wymodelmanager0003.export_wymaterial(wymaterial, "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0003.wym")

        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0003.wym', 'r') as content_file:
            content = content_file.read()       
        self.assertTrue(content == "mtl_material_name TestMaterial0003\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")


    def test_WYModelManagerTestCase_export_wymaterial_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymaterial function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the default Blender material object is exported onto the given relative path "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0004" through "export_wymaterial" function resulting the string read from the given file path is equal to ""mtl_material_name TestMaterial0004\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymaterial: WYMaterial object to export with..
        :type  wymaterial: WYMaterial.
        :test  wymaterial: WYModel(wymesh,wymaterial).

        :param wymaterial_file_path: String of the file path to export the WYMaterial object onto.
        :type  wymaterial_file_path: string.
        :test  wymaterial_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "mtl_material_name TestMaterial0004\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0004"
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0004"))
        wymaterial.init_material_data()
        wymodelmanager0004 = WYModelManager() 
        wymodelmanager0004.export_wymaterial(wymaterial, "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0004.wym")

        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0004.wym', 'r') as content_file:
            content = content_file.read()       
        self.assertTrue(content == "mtl_material_name TestMaterial0004\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")


    def test_WYModelManagerTestCase_export_wymaterial_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymaterial function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the default Blender material object is exported onto the given relative path "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0005" through "export_wymaterial" function resulting the string read from the given file path is equal to ""mtl_material_name TestMaterial0005\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymaterial: WYMaterial object to export with..
        :type  wymaterial: WYMaterial.
        :test  wymaterial: WYModel(wymesh,wymaterial).

        :param wymaterial_file_path: String of the file path to export the WYMaterial object onto.
        :type  wymaterial_file_path: string.
        :test  wymaterial_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "mtl_material_name TestMaterial0005\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0005"
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0005"))
        wymaterial.init_material_data()
        wymodelmanager0005 = WYModelManager() 
        wymodelmanager0005.export_wymaterial(wymaterial, "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0005.wym")

        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0005.wym', 'r') as content_file:
            content = content_file.read()       
        self.assertTrue(content == "mtl_material_name TestMaterial0005\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")


    def test_WYModelManagerTestCase_export_wymaterial_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymaterial function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the default Blender material object is exported onto the given relative path "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0006" through "export_wymaterial" function resulting the string read from the given file path is equal to ""mtl_material_name TestMaterial0006\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymaterial: WYMaterial object to export with..
        :type  wymaterial: WYMaterial.
        :test  wymaterial: WYModel(wymesh,wymaterial).

        :param wymaterial_file_path: String of the file path to export the WYMaterial object onto.
        :type  wymaterial_file_path: string.
        :test  wymaterial_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "mtl_material_name TestMaterial0006\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0006"
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0006"))
        wymaterial.init_material_data()
        wymodelmanager0006 = WYModelManager() 
        wymodelmanager0006.export_wymaterial(wymaterial, "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0006.wym")

        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0006.wym', 'r') as content_file:
            content = content_file.read()       
        self.assertTrue(content == "mtl_material_name TestMaterial0006\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")


    def test_WYModelManagerTestCase_export_wymaterial_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymaterial function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the default Blender material object is exported onto the given relative path "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0007" through "export_wymaterial" function resulting the string read from the given file path is equal to ""mtl_material_name TestMaterial0007\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymaterial: WYMaterial object to export with..
        :type  wymaterial: WYMaterial.
        :test  wymaterial: WYModel(wymesh,wymaterial).

        :param wymaterial_file_path: String of the file path to export the WYMaterial object onto.
        :type  wymaterial_file_path: string.
        :test  wymaterial_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "mtl_material_name TestMaterial0007\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0007"
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0007"))
        wymaterial.init_material_data()
        wymodelmanager0007 = WYModelManager() 
        wymodelmanager0007.export_wymaterial(wymaterial, "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0007.wym")

        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0007.wym', 'r') as content_file:
            content = content_file.read()       
        self.assertTrue(content == "mtl_material_name TestMaterial0007\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")


    def test_WYModelManagerTestCase_export_wymaterial_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymaterial function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the default Blender material object is exported onto the given relative path "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0008" through "export_wymaterial" function resulting the string read from the given file path is equal to ""mtl_material_name TestMaterial0008\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymaterial: WYMaterial object to export with..
        :type  wymaterial: WYMaterial.
        :test  wymaterial: WYModel(wymesh,wymaterial).

        :param wymaterial_file_path: String of the file path to export the WYMaterial object onto.
        :type  wymaterial_file_path: string.
        :test  wymaterial_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "mtl_material_name TestMaterial0008\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0008"
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0008"))
        wymaterial.init_material_data()
        wymodelmanager0008 = WYModelManager() 
        wymodelmanager0008.export_wymaterial(wymaterial, "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0008.wym")

        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0008.wym', 'r') as content_file:
            content = content_file.read()       
        self.assertTrue(content == "mtl_material_name TestMaterial0008\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")


    def test_WYModelManagerTestCase_export_wymaterial_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymaterial function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the default Blender material object is exported onto the given relative path "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0009" through "export_wymaterial" function resulting the string read from the given file path is equal to ""mtl_material_name TestMaterial0009\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymaterial: WYMaterial object to export with..
        :type  wymaterial: WYMaterial.
        :test  wymaterial: WYModel(wymesh,wymaterial).

        :param wymaterial_file_path: String of the file path to export the WYMaterial object onto.
        :type  wymaterial_file_path: string.
        :test  wymaterial_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "mtl_material_name TestMaterial0009\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0009"
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0009"))
        wymaterial.init_material_data()
        wymodelmanager0009 = WYModelManager() 
        wymodelmanager0009.export_wymaterial(wymaterial, "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0009.wym")

        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0009.wym', 'r') as content_file:
            content = content_file.read()       
        self.assertTrue(content == "mtl_material_name TestMaterial0009\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")


    def test_WYModelManagerTestCase_export_wymaterial_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymaterial function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the default Blender material object is exported onto the given relative path "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0010" through "export_wymaterial" function resulting the string read from the given file path is equal to ""mtl_material_name TestMaterial0010\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymaterial: WYMaterial object to export with..
        :type  wymaterial: WYMaterial.
        :test  wymaterial: WYModel(wymesh,wymaterial).

        :param wymaterial_file_path: String of the file path to export the WYMaterial object onto.
        :type  wymaterial_file_path: string.
        :test  wymaterial_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "mtl_material_name TestMaterial0010\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0010"
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0010"))
        wymaterial.init_material_data()
        wymodelmanager0010 = WYModelManager() 
        wymodelmanager0010.export_wymaterial(wymaterial, "..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0010.wym")

        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymaterial\\Test0010.wym', 'r') as content_file:
            content = content_file.read()       
        self.assertTrue(content == "mtl_material_name TestMaterial0010\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")



if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_export_wymaterial))
