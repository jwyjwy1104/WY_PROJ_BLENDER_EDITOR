"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2017-11-23
Last update                         : 2018-01-21
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_import_mesh\WYModelManagerTestCases_import_mesh.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_import_mesh\WYModelManagerTestCases_import_mesh.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : import_mesh(mesh_file_path)
Unit test case class name           : WYModelManagerTestCases_import_mesh
Unit test case description          : Unit test case for class WYModelManager import_mesh() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_import_mesh\WYModelManagerTestCaseResult_import_mesh.txt
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

class WYModelManagerTestCases_import_mesh(unittest.TestCase):
    """
    Unit test case for class WYModelManager import_mesh() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_import_mesh_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_mesh function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh object is imported properly through import_mesh function, returning the data values initialized onto a Blender mesh object resulting the returned Blender mesh object "(testmesh.name == "TestObject0001") and (len(testmesh.polygons) == 12)" also the vertex array element is equal to the expected array [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))].
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param mesh_file_path: String of the file path to import the Blender mesh object from..
        :type  mesh_file_path: string.
        :test  mesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0001.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0001") and (len(testmesh.polygons) == 12)
        """
        
        wymodelmanager0001 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0001.wyo", 'w+') as content_file:
            content_file.write("o TestObject0001\nCU Z\nCF Y\nmtllib \nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymodelmanager0001.import_mesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0001.wyo")   
        testmesh = bpy.data.objects["TestObject0001"].data    
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        print(len(testmesh.polygons))
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0001") and (len(testmesh.polygons) == 12))
    def test_WYModelManagerTestCase_import_mesh_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_mesh function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh object is imported properly through import_mesh function, returning the data values initialized onto a Blender mesh object resulting the returned Blender mesh object "(testmesh.name == "TestObject0002") and (len(testmesh.polygons) == 12)" also the vertex array element is equal to the expected array [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))].
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param mesh_file_path: String of the file path to import the Blender mesh object from..
        :type  mesh_file_path: string.
        :test  mesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0002.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0002") and (len(testmesh.polygons) == 12)
        """
        
        wymodelmanager0002 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0002.wyo", 'w+') as content_file:
            content_file.write("o TestObject0002\nCU Z\nCF Y\nmtllib \nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymodelmanager0002.import_mesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0002.wyo")   
        testmesh = bpy.data.objects["TestObject0002"].data    
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0002") and (len(testmesh.polygons) == 12))
    def test_WYModelManagerTestCase_import_mesh_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_mesh function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh object is imported properly through import_mesh function, returning the data values initialized onto a Blender mesh object resulting the returned Blender mesh object "(testmesh.name == "TestObject0003") and (len(testmesh.polygons) == 12)" also the vertex array element is equal to the expected array [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))].
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param mesh_file_path: String of the file path to import the Blender mesh object from..
        :type  mesh_file_path: string.
        :test  mesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0003.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0003") and (len(testmesh.polygons) == 12)
        """
        
        wymodelmanager0003 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0003.wyo", 'w+') as content_file:
            content_file.write("o TestObject0003\nCU Z\nCF Y\nmtllib \nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymodelmanager0003.import_mesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0003.wyo")   
        testmesh = bpy.data.objects["TestObject0003"].data    
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0003") and (len(testmesh.polygons) == 12))
    def test_WYModelManagerTestCase_import_mesh_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_mesh function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh object is imported properly through import_mesh function, returning the data values initialized onto a Blender mesh object resulting the returned Blender mesh object "(testmesh.name == "TestObject0004") and (len(testmesh.polygons) == 12)" also the vertex array element is equal to the expected array [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))].
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param mesh_file_path: String of the file path to import the Blender mesh object from..
        :type  mesh_file_path: string.
        :test  mesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0004.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0004") and (len(testmesh.polygons) == 12)
        """
        
        wymodelmanager0004 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0004.wyo", 'w+') as content_file:
            content_file.write("o TestObject0004\nCU Z\nCF Y\nmtllib \nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymodelmanager0004.import_mesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0004.wyo")   
        testmesh = bpy.data.objects["TestObject0004"].data    
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0004") and (len(testmesh.polygons) == 12))
    def test_WYModelManagerTestCase_import_mesh_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_mesh function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh object is imported properly through import_mesh function, returning the data values initialized onto a Blender mesh object resulting the returned Blender mesh object "(testmesh.name == "TestObject0005") and (len(testmesh.polygons) == 12)" also the vertex array element is equal to the expected array [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))].
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param mesh_file_path: String of the file path to import the Blender mesh object from..
        :type  mesh_file_path: string.
        :test  mesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0005.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0005") and (len(testmesh.polygons) == 12)
        """
        
        wymodelmanager0005 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0005.wyo", 'w+') as content_file:
            content_file.write("o TestObject0005\nCU Z\nCF Y\nmtllib \nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymodelmanager0005.import_mesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0005.wyo")   
        testmesh = bpy.data.objects["TestObject0005"].data    
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0005") and (len(testmesh.polygons) == 12))
    def test_WYModelManagerTestCase_import_mesh_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_mesh function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh object is imported properly through import_mesh function, returning the data values initialized onto a Blender mesh object resulting the returned Blender mesh object "(testmesh.name == "TestObject0006") and (len(testmesh.polygons) == 12)" also the vertex array element is equal to the expected array [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))].
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param mesh_file_path: String of the file path to import the Blender mesh object from..
        :type  mesh_file_path: string.
        :test  mesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0006.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0006") and (len(testmesh.polygons) == 12)
        """
        
        wymodelmanager0006 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0006.wyo", 'w+') as content_file:
            content_file.write("o TestObject0006\nCU Z\nCF Y\nmtllib \nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymodelmanager0006.import_mesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0006.wyo")   
        testmesh = bpy.data.objects["TestObject0006"].data    
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0006") and (len(testmesh.polygons) == 12))
    def test_WYModelManagerTestCase_import_mesh_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_mesh function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh object is imported properly through import_mesh function, returning the data values initialized onto a Blender mesh object resulting the returned Blender mesh object "(testmesh.name == "TestObject0007") and (len(testmesh.polygons) == 12)" also the vertex array element is equal to the expected array [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))].
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param mesh_file_path: String of the file path to import the Blender mesh object from..
        :type  mesh_file_path: string.
        :test  mesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0007.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0007") and (len(testmesh.polygons) == 12)
        """
        
        wymodelmanager0007 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0007.wyo", 'w+') as content_file:
            content_file.write("o TestObject0007\nCU Z\nCF Y\nmtllib \nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymodelmanager0007.import_mesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0007.wyo")   
        testmesh = bpy.data.objects["TestObject0007"].data    
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0007") and (len(testmesh.polygons) == 12))
    def test_WYModelManagerTestCase_import_mesh_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_mesh function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh object is imported properly through import_mesh function, returning the data values initialized onto a Blender mesh object resulting the returned Blender mesh object "(testmesh.name == "TestObject0008") and (len(testmesh.polygons) == 12)" also the vertex array element is equal to the expected array [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))].
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param mesh_file_path: String of the file path to import the Blender mesh object from..
        :type  mesh_file_path: string.
        :test  mesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0008.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0008") and (len(testmesh.polygons) == 12)
        """
        
        wymodelmanager0008 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0008.wyo", 'w+') as content_file:
            content_file.write("o TestObject0008\nCU Z\nCF Y\nmtllib \nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymodelmanager0008.import_mesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0008.wyo")   
        testmesh = bpy.data.objects["TestObject0008"].data    
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0008") and (len(testmesh.polygons) == 12))
    def test_WYModelManagerTestCase_import_mesh_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_mesh function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh object is imported properly through import_mesh function, returning the data values initialized onto a Blender mesh object resulting the returned Blender mesh object "(testmesh.name == "TestObject0009") and (len(testmesh.polygons) == 12)" also the vertex array element is equal to the expected array [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))].
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param mesh_file_path: String of the file path to import the Blender mesh object from..
        :type  mesh_file_path: string.
        :test  mesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0009.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0009") and (len(testmesh.polygons) == 12)
        """
        
        wymodelmanager0009 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0009.wyo", 'w+') as content_file:
            content_file.write("o TestObject0009\nCU Z\nCF Y\nmtllib \nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymodelmanager0009.import_mesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0009.wyo")   
        testmesh = bpy.data.objects["TestObject0009"].data    
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0009") and (len(testmesh.polygons) == 12))
    def test_WYModelManagerTestCase_import_mesh_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_mesh function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender mesh object is imported properly through import_mesh function, returning the data values initialized onto a Blender mesh object resulting the returned Blender mesh object "(testmesh.name == "TestObject0010") and (len(testmesh.polygons) == 12)" also the vertex array element is equal to the expected array [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))].
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param mesh_file_path: String of the file path to import the Blender mesh object from..
        :type  mesh_file_path: string.
        :test  mesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0010.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMaterial
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: (testmesh.name == "TestObject0010") and (len(testmesh.polygons) == 12)
        """
        
        wymodelmanager0010 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0010.wyo", 'w+') as content_file:
            content_file.write("o TestObject0010\nCU Z\nCF Y\nmtllib \nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymodelmanager0010.import_mesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_mesh\\Test0010.wyo")   
        testmesh = bpy.data.objects["TestObject0010"].data    
        expected_vertex_array = [Vector((-1.0000, -1.0000, -1.0000)),Vector((-1.0000, -1.0000, 1.0000)),Vector((-1.0000, 1.0000, -1.0000)),Vector((-1.0000, 1.0000, 1.0000)),Vector((1.0000, -1.0000, -1.0000)),Vector((1.0000, -1.0000, 1.0000)),Vector((1.0000, 1.0000, -1.0000)),Vector((1.0000, 1.0000, 1.0000))] 
        for i in range(0, len(testmesh.vertices)):   
            self.assertTrue(testmesh.vertices[i].co == expected_vertex_array[i]) 
        self.assertTrue((testmesh.name == "TestObject0010") and (len(testmesh.polygons) == 12))

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_import_mesh))
