"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2018-01-21
Last update                         : 2018-01-15
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_export_wymodel\WYModelManagerTestCases_export_wymodel.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_export_wymodel\WYModelManagerTestCases_export_wymodel.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : export_wymodel(wymodel, wymodel_file_path)
Unit test case class name           : WYModelManagerTestCases_export_wymodel
Unit test case description          : Unit test case for class WYModelManager export_wymodel() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_export_wymodel\WYModelManagerTestCaseResult_export_wymodel.txt
"""
# Pre-condition: WYModel is tested.
# Pre-condition: WYModelManager::export_wymesh() is tested.
# Pre-condition: WYModelManager::export_wymaterial() is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_export_wymodel(unittest.TestCase):
    """
    Unit test case for class WYModelManager export_wymodel() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :11
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_export_wymodel_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymesh function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYModel object initialized WYMesh object and WYMaterial object where WYMesh object is initialzied with default Blender cube object and WYMaterial object is initialized with Blender default material object, is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0001" through "export_wymodel" function resulting the string read from the given file path with extension .wyo is equal to ""o TestCube0001\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0001.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"" and extension .wym is equal to ""o TestCube0003\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0003.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymodel: WYModel object which holds all the model information data.
        :type  wymodel: WYModel.
        :test  wymodel: WYModel(wymesh,wymaterial).

        :param file_path: String of the file path to export the model onto.
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymesh\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o TestCube0001\\nCU Z\\nCF Y\\nmtllib " + os.getcwd() + "\\\\..\\\\..\\\\test\\\\WYModelManagerTestCases_export_wymesh\\\\Test0001.wym\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nf 2/2 3/3 1/1\\nf 4/4 7/7 3/3\\nf 8/8 5/5 7/7\\nf 6/6 1/1 5/5\\nf 7/7 1/1 3/3\\nf 4/4 6/6 8/8\\nf 2/2 4/4 3/3\\nf 4/4 8/8 7/7\\nf 8/8 6/6 5/5\\nf 6/6 2/2 1/1\\nf 7/7 5/5 1/1\\nf 4/4 2/2 6/6\\n"
        :expect: "mtl_material_name TestMaterial0001\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0001"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh.init_mesh_data()
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0001"))
        wymaterial.init_material_data()
        wymodel = WYModel(wymesh, wymaterial)
        wymodelmanager0001 = WYModelManager() 
        wymodelmanager0001.export_wymodel(wymodel, "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0001")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0001.wyo', 'r') as wymesh_file:
            wymesh_file_str = wymesh_file.read()       
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0001.wym', 'r') as wymaterial_file:
            wymaterial_file_str = wymaterial_file.read()   
        print(wymesh_file_str)
        print(wymaterial_file_str)
        print(wymesh_file_str == "o TestCube0001\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0001.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n")
        print(wymaterial_file_str == "o TestCube0001\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0001.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n")
        self.assertTrue(wymesh_file_str == "o TestCube0001\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0001.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n")
        self.assertTrue(wymaterial_file_str == "mtl_material_name TestMaterial0001\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")

    def test_WYModelManagerTestCase_export_wymodel_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymesh function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYModel object initialized WYMesh object and WYMaterial object where WYMesh object is initialzied with default Blender cube object and WYMaterial object is initialized with Blender default material object, is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0002" through "export_wymodel" function resulting the string read from the given file path with extension .wyo is equal to ""o TestCube0002\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0002.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"" and extension .wym is equal to ""o TestCube0004\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0004.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymodel: WYModel object which holds all the model information data.
        :type  wymodel: WYModel.
        :test  wymodel: WYModel(wymesh,wymaterial).

        :param file_path: String of the file path to export the model onto.
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymesh\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o TestCube0002\\nCU Z\\nCF Y\\nmtllib " + os.getcwd() + "\\\\..\\\\..\\\\test\\\\WYModelManagerTestCases_export_wymesh\\\\Test0002.wym\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nf 2/2 3/3 1/1\\nf 4/4 7/7 3/3\\nf 8/8 5/5 7/7\\nf 6/6 1/1 5/5\\nf 7/7 1/1 3/3\\nf 4/4 6/6 8/8\\nf 2/2 4/4 3/3\\nf 4/4 8/8 7/7\\nf 8/8 6/6 5/5\\nf 6/6 2/2 1/1\\nf 7/7 5/5 1/1\\nf 4/4 2/2 6/6\\n"
        :expect: "mtl_material_name TestMaterial0002\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0002"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh.init_mesh_data()
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0002"))
        wymaterial.init_material_data()
        wymodel = WYModel(wymesh, wymaterial)
        wymodelmanager0002 = WYModelManager() 
        wymodelmanager0002.export_wymodel(wymodel, "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0002")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0002.wyo', 'r') as wymesh_file:
            wymesh_file_str = wymesh_file.read()       
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0002.wym', 'r') as wymaterial_file:
            wymaterial_file_str = wymaterial_file.read()   
        self.assertTrue(wymesh_file_str == "o TestCube0002\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0002.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n")
        self.assertTrue(wymaterial_file_str == "mtl_material_name TestMaterial0002\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")

    def test_WYModelManagerTestCase_export_wymodel_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymesh function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYModel object initialized WYMesh object and WYMaterial object where WYMesh object is initialzied with default Blender cube object and WYMaterial object is initialized with Blender default material object, is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0003" through "export_wymodel" function resulting the string read from the given file path with extension .wyo is equal to ""o TestCube0003\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0003.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"" and extension .wym is equal to ""o TestCube0005\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0005.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymodel: WYModel object which holds all the model information data.
        :type  wymodel: WYModel.
        :test  wymodel: WYModel(wymesh,wymaterial).

        :param file_path: String of the file path to export the model onto.
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymesh\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o TestCube0003\\nCU Z\\nCF Y\\nmtllib " + os.getcwd() + "\\\\..\\\\..\\\\test\\\\WYModelManagerTestCases_export_wymesh\\\\Test0003.wym\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nf 2/2 3/3 1/1\\nf 4/4 7/7 3/3\\nf 8/8 5/5 7/7\\nf 6/6 1/1 5/5\\nf 7/7 1/1 3/3\\nf 4/4 6/6 8/8\\nf 2/2 4/4 3/3\\nf 4/4 8/8 7/7\\nf 8/8 6/6 5/5\\nf 6/6 2/2 1/1\\nf 7/7 5/5 1/1\\nf 4/4 2/2 6/6\\n"
        :expect: "mtl_material_name TestMaterial0003\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0003"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh.init_mesh_data()
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0003"))
        wymaterial.init_material_data()
        wymodel = WYModel(wymesh, wymaterial)
        wymodelmanager0003 = WYModelManager() 
        wymodelmanager0003.export_wymodel(wymodel, "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0003")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0003.wyo', 'r') as wymesh_file:
            wymesh_file_str = wymesh_file.read()       
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0003.wym', 'r') as wymaterial_file:
            wymaterial_file_str = wymaterial_file.read()   
        self.assertTrue(wymesh_file_str == "o TestCube0003\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0003.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n")
        self.assertTrue(wymaterial_file_str == "mtl_material_name TestMaterial0003\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")

    def test_WYModelManagerTestCase_export_wymodel_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymesh function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYModel object initialized WYMesh object and WYMaterial object where WYMesh object is initialzied with default Blender cube object and WYMaterial object is initialized with Blender default material object, is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0004" through "export_wymodel" function resulting the string read from the given file path with extension .wyo is equal to ""o TestCube0004\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0004.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"" and extension .wym is equal to ""o TestCube0006\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0006.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymodel: WYModel object which holds all the model information data.
        :type  wymodel: WYModel.
        :test  wymodel: WYModel(wymesh,wymaterial).

        :param file_path: String of the file path to export the model onto.
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymesh\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o TestCube0004\\nCU Z\\nCF Y\\nmtllib " + os.getcwd() + "\\\\..\\\\..\\\\test\\\\WYModelManagerTestCases_export_wymesh\\\\Test0004.wym\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nf 2/2 3/3 1/1\\nf 4/4 7/7 3/3\\nf 8/8 5/5 7/7\\nf 6/6 1/1 5/5\\nf 7/7 1/1 3/3\\nf 4/4 6/6 8/8\\nf 2/2 4/4 3/3\\nf 4/4 8/8 7/7\\nf 8/8 6/6 5/5\\nf 6/6 2/2 1/1\\nf 7/7 5/5 1/1\\nf 4/4 2/2 6/6\\n"
        :expect: "mtl_material_name TestMaterial0004\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0004"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh.init_mesh_data()
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0004"))
        wymaterial.init_material_data()
        wymodel = WYModel(wymesh, wymaterial)
        wymodelmanager0004 = WYModelManager() 
        wymodelmanager0004.export_wymodel(wymodel, "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0004")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0004.wyo', 'r') as wymesh_file:
            wymesh_file_str = wymesh_file.read()       
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0004.wym', 'r') as wymaterial_file:
            wymaterial_file_str = wymaterial_file.read()   
        self.assertTrue(wymesh_file_str == "o TestCube0004\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0004.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n")
        self.assertTrue(wymaterial_file_str == "mtl_material_name TestMaterial0004\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")

    def test_WYModelManagerTestCase_export_wymodel_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymesh function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYModel object initialized WYMesh object and WYMaterial object where WYMesh object is initialzied with default Blender cube object and WYMaterial object is initialized with Blender default material object, is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0005" through "export_wymodel" function resulting the string read from the given file path with extension .wyo is equal to ""o TestCube0005\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0005.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"" and extension .wym is equal to ""o TestCube0007\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0007.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymodel: WYModel object which holds all the model information data.
        :type  wymodel: WYModel.
        :test  wymodel: WYModel(wymesh,wymaterial).

        :param file_path: String of the file path to export the model onto.
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymesh\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o TestCube0005\\nCU Z\\nCF Y\\nmtllib " + os.getcwd() + "\\\\..\\\\..\\\\test\\\\WYModelManagerTestCases_export_wymesh\\\\Test0005.wym\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nf 2/2 3/3 1/1\\nf 4/4 7/7 3/3\\nf 8/8 5/5 7/7\\nf 6/6 1/1 5/5\\nf 7/7 1/1 3/3\\nf 4/4 6/6 8/8\\nf 2/2 4/4 3/3\\nf 4/4 8/8 7/7\\nf 8/8 6/6 5/5\\nf 6/6 2/2 1/1\\nf 7/7 5/5 1/1\\nf 4/4 2/2 6/6\\n"
        :expect: "mtl_material_name TestMaterial0005\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0005"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh.init_mesh_data()
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0005"))
        wymaterial.init_material_data()
        wymodel = WYModel(wymesh, wymaterial)
        wymodelmanager0005 = WYModelManager() 
        wymodelmanager0005.export_wymodel(wymodel, "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0005")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0005.wyo', 'r') as wymesh_file:
            wymesh_file_str = wymesh_file.read()       
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0005.wym', 'r') as wymaterial_file:
            wymaterial_file_str = wymaterial_file.read()   
        self.assertTrue(wymesh_file_str == "o TestCube0005\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0005.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n")
        self.assertTrue(wymaterial_file_str == "mtl_material_name TestMaterial0005\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")

    def test_WYModelManagerTestCase_export_wymodel_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymesh function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYModel object initialized WYMesh object and WYMaterial object where WYMesh object is initialzied with default Blender cube object and WYMaterial object is initialized with Blender default material object, is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0006" through "export_wymodel" function resulting the string read from the given file path with extension .wyo is equal to ""o TestCube0006\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0006.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"" and extension .wym is equal to ""o TestCube0008\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0008.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymodel: WYModel object which holds all the model information data.
        :type  wymodel: WYModel.
        :test  wymodel: WYModel(wymesh,wymaterial).

        :param file_path: String of the file path to export the model onto.
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymesh\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o TestCube0006\\nCU Z\\nCF Y\\nmtllib " + os.getcwd() + "\\\\..\\\\..\\\\test\\\\WYModelManagerTestCases_export_wymesh\\\\Test0006.wym\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nf 2/2 3/3 1/1\\nf 4/4 7/7 3/3\\nf 8/8 5/5 7/7\\nf 6/6 1/1 5/5\\nf 7/7 1/1 3/3\\nf 4/4 6/6 8/8\\nf 2/2 4/4 3/3\\nf 4/4 8/8 7/7\\nf 8/8 6/6 5/5\\nf 6/6 2/2 1/1\\nf 7/7 5/5 1/1\\nf 4/4 2/2 6/6\\n"
        :expect: "mtl_material_name TestMaterial0006\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0006"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh.init_mesh_data()
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0006"))
        wymaterial.init_material_data()
        wymodel = WYModel(wymesh, wymaterial)
        wymodelmanager0006 = WYModelManager() 
        wymodelmanager0006.export_wymodel(wymodel, "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0006")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0006.wyo', 'r') as wymesh_file:
            wymesh_file_str = wymesh_file.read()       
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0006.wym', 'r') as wymaterial_file:
            wymaterial_file_str = wymaterial_file.read()   
        self.assertTrue(wymesh_file_str == "o TestCube0006\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0006.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n")
        self.assertTrue(wymaterial_file_str == "mtl_material_name TestMaterial0006\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")

    def test_WYModelManagerTestCase_export_wymodel_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymesh function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYModel object initialized WYMesh object and WYMaterial object where WYMesh object is initialzied with default Blender cube object and WYMaterial object is initialized with Blender default material object, is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0007" through "export_wymodel" function resulting the string read from the given file path with extension .wyo is equal to ""o TestCube0007\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0007.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"" and extension .wym is equal to ""o TestCube0009\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0009.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymodel: WYModel object which holds all the model information data.
        :type  wymodel: WYModel.
        :test  wymodel: WYModel(wymesh,wymaterial).

        :param file_path: String of the file path to export the model onto.
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymesh\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o TestCube0007\\nCU Z\\nCF Y\\nmtllib " + os.getcwd() + "\\\\..\\\\..\\\\test\\\\WYModelManagerTestCases_export_wymesh\\\\Test0007.wym\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nf 2/2 3/3 1/1\\nf 4/4 7/7 3/3\\nf 8/8 5/5 7/7\\nf 6/6 1/1 5/5\\nf 7/7 1/1 3/3\\nf 4/4 6/6 8/8\\nf 2/2 4/4 3/3\\nf 4/4 8/8 7/7\\nf 8/8 6/6 5/5\\nf 6/6 2/2 1/1\\nf 7/7 5/5 1/1\\nf 4/4 2/2 6/6\\n"
        :expect: "mtl_material_name TestMaterial0007\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0007"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh.init_mesh_data()
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0007"))
        wymaterial.init_material_data()
        wymodel = WYModel(wymesh, wymaterial)
        wymodelmanager0007 = WYModelManager() 
        wymodelmanager0007.export_wymodel(wymodel, "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0007")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0007.wyo', 'r') as wymesh_file:
            wymesh_file_str = wymesh_file.read()       
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0007.wym', 'r') as wymaterial_file:
            wymaterial_file_str = wymaterial_file.read()   
        self.assertTrue(wymesh_file_str == "o TestCube0007\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0007.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n")
        self.assertTrue(wymaterial_file_str == "mtl_material_name TestMaterial0007\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")

    def test_WYModelManagerTestCase_export_wymodel_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymesh function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYModel object initialized WYMesh object and WYMaterial object where WYMesh object is initialzied with default Blender cube object and WYMaterial object is initialized with Blender default material object, is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0008" through "export_wymodel" function resulting the string read from the given file path with extension .wyo is equal to ""o TestCube0008\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0008.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"" and extension .wym is equal to ""o TestCube0010\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0010.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymodel: WYModel object which holds all the model information data.
        :type  wymodel: WYModel.
        :test  wymodel: WYModel(wymesh,wymaterial).

        :param file_path: String of the file path to export the model onto.
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymesh\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o TestCube0008\\nCU Z\\nCF Y\\nmtllib " + os.getcwd() + "\\\\..\\\\..\\\\test\\\\WYModelManagerTestCases_export_wymesh\\\\Test0008.wym\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nf 2/2 3/3 1/1\\nf 4/4 7/7 3/3\\nf 8/8 5/5 7/7\\nf 6/6 1/1 5/5\\nf 7/7 1/1 3/3\\nf 4/4 6/6 8/8\\nf 2/2 4/4 3/3\\nf 4/4 8/8 7/7\\nf 8/8 6/6 5/5\\nf 6/6 2/2 1/1\\nf 7/7 5/5 1/1\\nf 4/4 2/2 6/6\\n"
        :expect: "mtl_material_name TestMaterial0008\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0008"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh.init_mesh_data()
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0008"))
        wymaterial.init_material_data()
        wymodel = WYModel(wymesh, wymaterial)
        wymodelmanager0008 = WYModelManager() 
        wymodelmanager0008.export_wymodel(wymodel, "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0008")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0008.wyo', 'r') as wymesh_file:
            wymesh_file_str = wymesh_file.read()       
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0008.wym', 'r') as wymaterial_file:
            wymaterial_file_str = wymaterial_file.read()   
        self.assertTrue(wymesh_file_str == "o TestCube0008\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0008.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n")
        self.assertTrue(wymaterial_file_str == "mtl_material_name TestMaterial0008\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")

    def test_WYModelManagerTestCase_export_wymodel_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymesh function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYModel object initialized WYMesh object and WYMaterial object where WYMesh object is initialzied with default Blender cube object and WYMaterial object is initialized with Blender default material object, is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0009" through "export_wymodel" function resulting the string read from the given file path with extension .wyo is equal to ""o TestCube0009\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0009.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"" and extension .wym is equal to ""o TestCube0011\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0011.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymodel: WYModel object which holds all the model information data.
        :type  wymodel: WYModel.
        :test  wymodel: WYModel(wymesh,wymaterial).

        :param file_path: String of the file path to export the model onto.
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymesh\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o TestCube0009\\nCU Z\\nCF Y\\nmtllib " + os.getcwd() + "\\\\..\\\\..\\\\test\\\\WYModelManagerTestCases_export_wymesh\\\\Test0009.wym\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nf 2/2 3/3 1/1\\nf 4/4 7/7 3/3\\nf 8/8 5/5 7/7\\nf 6/6 1/1 5/5\\nf 7/7 1/1 3/3\\nf 4/4 6/6 8/8\\nf 2/2 4/4 3/3\\nf 4/4 8/8 7/7\\nf 8/8 6/6 5/5\\nf 6/6 2/2 1/1\\nf 7/7 5/5 1/1\\nf 4/4 2/2 6/6\\n"
        :expect: "mtl_material_name TestMaterial0009\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0009"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh.init_mesh_data()
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0009"))
        wymaterial.init_material_data()
        wymodel = WYModel(wymesh, wymaterial)
        wymodelmanager0009 = WYModelManager() 
        wymodelmanager0009.export_wymodel(wymodel, "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0009")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0009.wyo', 'r') as wymesh_file:
            wymesh_file_str = wymesh_file.read()       
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0009.wym', 'r') as wymaterial_file:
            wymaterial_file_str = wymaterial_file.read()   
        self.assertTrue(wymesh_file_str == "o TestCube0009\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0009.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n")
        self.assertTrue(wymaterial_file_str == "mtl_material_name TestMaterial0009\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")

    def test_WYModelManagerTestCase_export_wymodel_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymesh function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYModel object initialized WYMesh object and WYMaterial object where WYMesh object is initialzied with default Blender cube object and WYMaterial object is initialized with Blender default material object, is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0010" through "export_wymodel" function resulting the string read from the given file path with extension .wyo is equal to ""o TestCube0010\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0010.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"" and extension .wym is equal to "".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymodel: WYModel object which holds all the model information data.
        :type  wymodel: WYModel.
        :test  wymodel: WYModel(wymesh,wymaterial).

        :param file_path: String of the file path to export the model onto.
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymesh\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o TestCube0010\\nCU Z\\nCF Y\\nmtllib " + os.getcwd() + "\\\\..\\\\..\\\\test\\\\WYModelManagerTestCases_export_wymesh\\\\Test0010.wym\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nf 2/2 3/3 1/1\\nf 4/4 7/7 3/3\\nf 8/8 5/5 7/7\\nf 6/6 1/1 5/5\\nf 7/7 1/1 3/3\\nf 4/4 6/6 8/8\\nf 2/2 4/4 3/3\\nf 4/4 8/8 7/7\\nf 8/8 6/6 5/5\\nf 6/6 2/2 1/1\\nf 7/7 5/5 1/1\\nf 4/4 2/2 6/6\\n"
        :expect: "mtl_material_name TestMaterial0010\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0010"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh.init_mesh_data()
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0010"))
        wymaterial.init_material_data()
        wymodel = WYModel(wymesh, wymaterial)
        wymodelmanager0010 = WYModelManager() 
        wymodelmanager0010.export_wymodel(wymodel, "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0010")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0010.wyo', 'r') as wymesh_file:
            wymesh_file_str = wymesh_file.read()       
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0010.wym', 'r') as wymaterial_file:
            wymaterial_file_str = wymaterial_file.read()   
        self.assertTrue(wymesh_file_str == "o TestCube0010\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0010.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n")
        self.assertTrue(wymaterial_file_str == "mtl_material_name TestMaterial0010\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")

    def test_WYModelManagerTestCase_export_wymodel_TC_NC_0011(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wymesh function testing normal case 0011

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYModel object initialized WYMesh object and WYMaterial object where WYMesh object is initialzied with default Blender cube object and WYMaterial object is initialized with Blender default material object, is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0011" through "export_wymodel" function resulting the string read from the given file path with extension .wyo is equal to ""o TestCube0011\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0011.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n"" and extension .wym is equal to "".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymodel: WYModel object which holds all the model information data.
        :type  wymodel: WYModel.
        :test  wymodel: WYModel(wymesh,wymaterial).

        :param file_path: String of the file path to export the model onto.
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_wymesh\\WYModel(wymesh,wymaterial).

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o TestCube0011\\nCU Z\\nCF Y\\nmtllib " + os.getcwd() + "\\\\..\\\\..\\\\test\\\\WYModelManagerTestCases_export_wymesh\\\\Test0011.wym\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nf 2/2 3/3 1/1\\nf 4/4 7/7 3/3\\nf 8/8 5/5 7/7\\nf 6/6 1/1 5/5\\nf 7/7 1/1 3/3\\nf 4/4 6/6 8/8\\nf 2/2 4/4 3/3\\nf 4/4 8/8 7/7\\nf 8/8 6/6 5/5\\nf 6/6 2/2 1/1\\nf 7/7 5/5 1/1\\nf 4/4 2/2 6/6\\n"
        :expect: "mtl_material_name TestMaterial0011\\nmtl_mirror_color 1.0 1.0 1.0\\nmtl_ambient 1.0\\nmtl_diffuse_color 0.64 0.64 0.64\\nmtl_diffuse_intensity 0.8\\nmtl_specular_color 0.5 0.5 0.5\\nmtl_specular_intensity 0.5\\nmtl_specular_hardness 97.847358\\nmtl_emit 0.0\\nmtl_alpha 1.0\\nmtl_raytrace_transparency_ior 1.0\\nmtl_texture_map_image_path NULL\\n"
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0011"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh.init_mesh_data()
        wymaterial = WYMaterial(cube, bpy.data.materials.new(name="TestMaterial0011"))
        wymaterial.init_material_data()
        wymodel = WYModel(wymesh, wymaterial)
        wymodelmanager0011 = WYModelManager() 
        wymodelmanager0011.export_wymodel(wymodel, "..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0011")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0011.wyo', 'r') as wymesh_file:
            wymesh_file_str = wymesh_file.read()       
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0011.wym', 'r') as wymaterial_file:
            wymaterial_file_str = wymaterial_file.read()   
        self.assertTrue(wymesh_file_str == "o TestCube0011\nCU Z\nCF Y\nmtllib " + os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_export_wymesh\\Test0011.wym\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nf 2/2 3/3 1/1\nf 4/4 7/7 3/3\nf 8/8 5/5 7/7\nf 6/6 1/1 5/5\nf 7/7 1/1 3/3\nf 4/4 6/6 8/8\nf 2/2 4/4 3/3\nf 4/4 8/8 7/7\nf 8/8 6/6 5/5\nf 6/6 2/2 1/1\nf 7/7 5/5 1/1\nf 4/4 2/2 6/6\n")
        self.assertTrue(wymaterial_file_str == "mtl_material_name TestMaterial0011\nmtl_mirror_color 1.0 1.0 1.0\nmtl_ambient 1.0\nmtl_diffuse_color 0.64 0.64 0.64\nmtl_diffuse_intensity 0.8\nmtl_specular_color 0.5 0.5 0.5\nmtl_specular_intensity 0.5\nmtl_specular_hardness 97.847358\nmtl_emit 0.0\nmtl_alpha 1.0\nmtl_raytrace_transparency_ior 1.0\nmtl_texture_map_image_path NULL\n")


if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_export_wymodel))
