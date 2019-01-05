"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2018-01-22
Last update                         : 2018-01-22
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_import_armature_model\WYModelManagerTestCases_import_armature_model.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_import_armature_model\WYModelManagerTestCases_import_armature_model.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : import_armature_model(file_path)
Unit test case class name           : WYModelManagerTestCases_import_armature_model
Unit test case description          : Unit test case for class WYModelManager import_armature_model() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_import_armature_model\WYModelManagerTestCaseResult_import_armature_model.txt
"""
# Pre-condition: WYArmature is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_import_armature_model(unittest.TestCase):
    """
    Unit test case for class WYModelManager import_armature_model() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :11
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_import_armature_model_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature_model function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is imported from the given path "..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0001" through "import_armature_model" function resulting the imported WYArmature object is equal to the manually created WYArmature object for export.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the Blender armature object from..
        :type  file_path: string.
        :test  file_path: myArmature=bpy.data.armatures.new("TestArmature0001")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0001",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0001")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature_exported.armature_name == wyarmature_imported.armature_name
        :expect: len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)
        :expect: wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail
        """
        myArmature = bpy.data.armatures.new("TestArmature0001")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0001", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0001")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0001 = WYModelManager()
        wyarmature_exported = wymodelmanager0001.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0001")
        wyarmature_imported = wymodelmanager0001.import_armature_model("..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0001")
        print(wyarmature_exported.main_armature_obj.name)
        print(wyarmature_imported.main_armature_obj.name)
        self.assertTrue(wyarmature_exported.armature_name == wyarmature_imported.armature_name) 
        self.assertTrue(len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)) 
        self.assertTrue(wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail)
    def test_WYModelManagerTestCase_import_armature_model_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature_model function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is imported from the given path "..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0002" through "import_armature_model" function resulting the imported WYArmature object is equal to the manually created WYArmature object for export.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the Blender armature object from..
        :type  file_path: string.
        :test  file_path: myArmature=bpy.data.armatures.new("TestArmature0002")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0002",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0002")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature_exported.armature_name == wyarmature_imported.armature_name
        :expect: len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)
        :expect: wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail
        """
        myArmature = bpy.data.armatures.new("TestArmature0002")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0002", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0002")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0002 = WYModelManager()
        wyarmature_exported = wymodelmanager0002.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0002")
        wyarmature_imported = wymodelmanager0002.import_armature_model("..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0002")
        print(wyarmature_exported.main_armature_obj.name)
        print(wyarmature_imported.main_armature_obj.name)
        self.assertTrue(wyarmature_exported.armature_name == wyarmature_imported.armature_name) 
        self.assertTrue(len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)) 
        self.assertTrue(wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail)
    def test_WYModelManagerTestCase_import_armature_model_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature_model function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is imported from the given path "..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0003" through "import_armature_model" function resulting the imported WYArmature object is equal to the manually created WYArmature object for export.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the Blender armature object from..
        :type  file_path: string.
        :test  file_path: myArmature=bpy.data.armatures.new("TestArmature0003")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0003",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0003")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature_exported.armature_name == wyarmature_imported.armature_name
        :expect: len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)
        :expect: wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail
        """
        myArmature = bpy.data.armatures.new("TestArmature0003")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0003", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0003")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0003 = WYModelManager()
        wyarmature_exported = wymodelmanager0003.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0003")
        wyarmature_imported = wymodelmanager0003.import_armature_model("..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0003")
        print(wyarmature_exported.main_armature_obj.name)
        print(wyarmature_imported.main_armature_obj.name)
        self.assertTrue(wyarmature_exported.armature_name == wyarmature_imported.armature_name) 
        self.assertTrue(len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)) 
        self.assertTrue(wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail)
    def test_WYModelManagerTestCase_import_armature_model_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature_model function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is imported from the given path "..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0004" through "import_armature_model" function resulting the imported WYArmature object is equal to the manually created WYArmature object for export.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the Blender armature object from..
        :type  file_path: string.
        :test  file_path: myArmature=bpy.data.armatures.new("TestArmature0004")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0004",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0004")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature_exported.armature_name == wyarmature_imported.armature_name
        :expect: len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)
        :expect: wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail
        """
        myArmature = bpy.data.armatures.new("TestArmature0004")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0004", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0004")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0004 = WYModelManager()
        wyarmature_exported = wymodelmanager0004.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0004")
        wyarmature_imported = wymodelmanager0004.import_armature_model("..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0004")
        print(wyarmature_exported.main_armature_obj.name)
        print(wyarmature_imported.main_armature_obj.name)
        self.assertTrue(wyarmature_exported.armature_name == wyarmature_imported.armature_name) 
        self.assertTrue(len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)) 
        self.assertTrue(wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail)
    def test_WYModelManagerTestCase_import_armature_model_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature_model function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is imported from the given path "..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0005" through "import_armature_model" function resulting the imported WYArmature object is equal to the manually created WYArmature object for export.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the Blender armature object from..
        :type  file_path: string.
        :test  file_path: myArmature=bpy.data.armatures.new("TestArmature0005")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0005",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0005")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature_exported.armature_name == wyarmature_imported.armature_name
        :expect: len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)
        :expect: wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail
        """
        myArmature = bpy.data.armatures.new("TestArmature0005")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0005", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0005")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0005 = WYModelManager()
        wyarmature_exported = wymodelmanager0005.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0005")
        wyarmature_imported = wymodelmanager0005.import_armature_model("..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0005")
        print(wyarmature_exported.main_armature_obj.name)
        print(wyarmature_imported.main_armature_obj.name)
        self.assertTrue(wyarmature_exported.armature_name == wyarmature_imported.armature_name) 
        self.assertTrue(len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)) 
        self.assertTrue(wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail)
    def test_WYModelManagerTestCase_import_armature_model_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature_model function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is imported from the given path "..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0006" through "import_armature_model" function resulting the imported WYArmature object is equal to the manually created WYArmature object for export.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the Blender armature object from..
        :type  file_path: string.
        :test  file_path: myArmature=bpy.data.armatures.new("TestArmature0006")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0006",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0006")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature_exported.armature_name == wyarmature_imported.armature_name
        :expect: len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)
        :expect: wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail
        """
        myArmature = bpy.data.armatures.new("TestArmature0006")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0006", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0006")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0006 = WYModelManager()
        wyarmature_exported = wymodelmanager0006.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0006")
        wyarmature_imported = wymodelmanager0006.import_armature_model("..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0006")
        print(wyarmature_exported.main_armature_obj.name)
        print(wyarmature_imported.main_armature_obj.name)
        self.assertTrue(wyarmature_exported.armature_name == wyarmature_imported.armature_name) 
        self.assertTrue(len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)) 
        self.assertTrue(wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail)
    def test_WYModelManagerTestCase_import_armature_model_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature_model function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is imported from the given path "..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0007" through "import_armature_model" function resulting the imported WYArmature object is equal to the manually created WYArmature object for export.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the Blender armature object from..
        :type  file_path: string.
        :test  file_path: myArmature=bpy.data.armatures.new("TestArmature0007")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0007",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0007")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature_exported.armature_name == wyarmature_imported.armature_name
        :expect: len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)
        :expect: wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail
        """
        myArmature = bpy.data.armatures.new("TestArmature0007")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0007", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0007")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0007 = WYModelManager()
        wyarmature_exported = wymodelmanager0007.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0007")
        wyarmature_imported = wymodelmanager0007.import_armature_model("..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0007")
        print(wyarmature_exported.main_armature_obj.name)
        print(wyarmature_imported.main_armature_obj.name)
        self.assertTrue(wyarmature_exported.armature_name == wyarmature_imported.armature_name) 
        self.assertTrue(len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)) 
        self.assertTrue(wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail)
    def test_WYModelManagerTestCase_import_armature_model_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature_model function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is imported from the given path "..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0008" through "import_armature_model" function resulting the imported WYArmature object is equal to the manually created WYArmature object for export.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the Blender armature object from..
        :type  file_path: string.
        :test  file_path: myArmature=bpy.data.armatures.new("TestArmature0008")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0008",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0008")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature_exported.armature_name == wyarmature_imported.armature_name
        :expect: len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)
        :expect: wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail
        """
        myArmature = bpy.data.armatures.new("TestArmature0008")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0008", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0008")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0008 = WYModelManager()
        wyarmature_exported = wymodelmanager0008.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0008")
        wyarmature_imported = wymodelmanager0008.import_armature_model("..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0008")
        print(wyarmature_exported.main_armature_obj.name)
        print(wyarmature_imported.main_armature_obj.name)
        self.assertTrue(wyarmature_exported.armature_name == wyarmature_imported.armature_name) 
        self.assertTrue(len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)) 
        self.assertTrue(wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail)
    def test_WYModelManagerTestCase_import_armature_model_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature_model function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is imported from the given path "..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0009" through "import_armature_model" function resulting the imported WYArmature object is equal to the manually created WYArmature object for export.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the Blender armature object from..
        :type  file_path: string.
        :test  file_path: myArmature=bpy.data.armatures.new("TestArmature0009")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0009",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0009")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature_exported.armature_name == wyarmature_imported.armature_name
        :expect: len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)
        :expect: wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail
        """
        myArmature = bpy.data.armatures.new("TestArmature0009")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0009", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0009")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0009 = WYModelManager()
        wyarmature_exported = wymodelmanager0009.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0009")
        wyarmature_imported = wymodelmanager0009.import_armature_model("..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0009")
        print(wyarmature_exported.main_armature_obj.name)
        print(wyarmature_imported.main_armature_obj.name)
        self.assertTrue(wyarmature_exported.armature_name == wyarmature_imported.armature_name) 
        self.assertTrue(len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)) 
        self.assertTrue(wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail)
    def test_WYModelManagerTestCase_import_armature_model_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature_model function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is imported from the given path "..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0010" through "import_armature_model" function resulting the imported WYArmature object is equal to the manually created WYArmature object for export.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the Blender armature object from..
        :type  file_path: string.
        :test  file_path: myArmature=bpy.data.armatures.new("TestArmature0010")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0010",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0010")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature_exported.armature_name == wyarmature_imported.armature_name
        :expect: len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)
        :expect: wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail
        """
        myArmature = bpy.data.armatures.new("TestArmature0010")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0010", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0010")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0010 = WYModelManager()
        wyarmature_exported = wymodelmanager0010.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0010")
        wyarmature_imported = wymodelmanager0010.import_armature_model("..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0010")
        print(wyarmature_exported.main_armature_obj.name)
        print(wyarmature_imported.main_armature_obj.name)
        self.assertTrue(wyarmature_exported.armature_name == wyarmature_imported.armature_name) 
        self.assertTrue(len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)) 
        self.assertTrue(wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail)
    def test_WYModelManagerTestCase_import_armature_model_TC_NC_0011(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature_model function testing normal case 0011

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is imported from the given path "..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0011" through "import_armature_model" function resulting the imported WYArmature object is equal to the manually created WYArmature object for export.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param file_path: String of the file path to import the Blender armature object from..
        :type  file_path: string.
        :test  file_path: myArmature=bpy.data.armatures.new("TestArmature0011")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0011",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0011")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature_exported.armature_name == wyarmature_imported.armature_name
        :expect: len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)
        :expect: wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail
        """
        myArmature = bpy.data.armatures.new("TestArmature0011")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0011", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0011")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0011 = WYModelManager()
        wyarmature_exported = wymodelmanager0011.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0011")
        wyarmature_imported = wymodelmanager0011.import_armature_model("..\\..\\test\\WYModelManagerTestCases_import_armature_model\\TestFile0011")
        print(wyarmature_exported.main_armature_obj.name)
        print(wyarmature_imported.main_armature_obj.name)
        self.assertTrue(wyarmature_exported.armature_name == wyarmature_imported.armature_name) 
        self.assertTrue(len(wyarmature_exported.main_armature_obj.data.bones) == len(wyarmature_imported.main_armature_obj.data.bones)) 
        self.assertTrue(wyarmature_exported.main_armature_obj.data.bones[0].name == wyarmature_imported.main_armature_obj.data.bones[0].name and wyarmature_exported.main_armature_obj.data.bones[0].head == wyarmature_imported.main_armature_obj.data.bones[0].head and wyarmature_exported.main_armature_obj.data.bones[0].tail == wyarmature_imported.main_armature_obj.data.bones[0].tail)

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_import_armature_model))
