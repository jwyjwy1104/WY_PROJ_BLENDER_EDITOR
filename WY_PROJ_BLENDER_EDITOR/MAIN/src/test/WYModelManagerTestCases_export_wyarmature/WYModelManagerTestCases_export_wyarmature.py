"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2018-01-22
Last update                         : 2018-01-22
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_export_wyarmature\WYModelManagerTestCases_export_wyarmature.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_export_wyarmature\WYModelManagerTestCases_export_wyarmature.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : export_wyarmature(wyarmature, wyarmature_file_path)
Unit test case class name           : WYModelManagerTestCases_export_wyarmature
Unit test case description          : Unit test case for class WYModelManager export_wyarmature() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_export_wyarmature\WYModelManagerTestCaseResult_export_wyarmature.txt
"""
# Pre-condition: WYArmature is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_export_wyarmature(unittest.TestCase):
    """
    Unit test case for class WYModelManager export_wyarmature() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_export_wyarmature_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyarmature function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmature object initialized with default Blender armature object is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0001" through "export_wyarmature" function resulting the string read from the given file path is equal to the object toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to export with..
        :type  wyarmature: WYArmature.
        :test  wyarmature: myArmature=bpy.data.armatures.new("TestArmature0001")
myObject=bpy.data.objects.new("TestArmatureObject0001",myArmature)
bpy.context.scene.objects.link(myObject)
bpy.context.scene.objects.active=myObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myObject.data.edit_bones.new("TestArmatureBoneName0001")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
wyarmature=WYArmature(myObject,None,None).

        :param wyarmature_file_path: String of the file path to export the WYArmature object onto.
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0001.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyarmature)
        """
        myArmature = bpy.data.armatures.new("TestArmature0001")
        myObject = bpy.data.objects.new("TestArmatureObject0001", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestArmatureBoneName0001")
        myArmatureBone.head = [1, 0, 0]
        myArmatureBone.tail = [0, 0, 0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wyarmature = WYArmature(myObject, None, None)
        wyarmature.init_armature_data()
        wymodelmanager0001 = WYModelManager()
        wymodelmanager0001.export_wyarmature(wyarmature, "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0001.wya")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0001.wya', 'r') as content_file:
            content = content_file.read()    
        print(content)   
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0001'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyarmature_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyarmature function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmature object initialized with default Blender armature object is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0002" through "export_wyarmature" function resulting the string read from the given file path is equal to the object toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to export with..
        :type  wyarmature: WYArmature.
        :test  wyarmature: myArmature=bpy.data.armatures.new("TestArmature0002")
myObject=bpy.data.objects.new("TestArmatureObject0002",myArmature)
bpy.context.scene.objects.link(myObject)
bpy.context.scene.objects.active=myObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myObject.data.edit_bones.new("TestArmatureBoneName0002")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
wyarmature=WYArmature(myObject,None,None).

        :param wyarmature_file_path: String of the file path to export the WYArmature object onto.
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0002.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyarmature)
        """
        myArmature = bpy.data.armatures.new("TestArmature0002")
        myObject = bpy.data.objects.new("TestArmatureObject0002", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestArmatureBoneName0002")
        myArmatureBone.head = [1, 0, 0]
        myArmatureBone.tail = [0, 0, 0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wyarmature = WYArmature(myObject, None, None)
        wyarmature.init_armature_data()
        wymodelmanager0002 = WYModelManager()
        wymodelmanager0002.export_wyarmature(wyarmature, "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0002.wya")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0002.wya', 'r') as content_file:
            content = content_file.read()    
        print(content)   
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0002'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyarmature_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyarmature function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmature object initialized with default Blender armature object is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0003" through "export_wyarmature" function resulting the string read from the given file path is equal to the object toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to export with..
        :type  wyarmature: WYArmature.
        :test  wyarmature: myArmature=bpy.data.armatures.new("TestArmature0003")
myObject=bpy.data.objects.new("TestArmatureObject0003",myArmature)
bpy.context.scene.objects.link(myObject)
bpy.context.scene.objects.active=myObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myObject.data.edit_bones.new("TestArmatureBoneName0003")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
wyarmature=WYArmature(myObject,None,None).

        :param wyarmature_file_path: String of the file path to export the WYArmature object onto.
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0003.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyarmature)
        """
        myArmature = bpy.data.armatures.new("TestArmature0003")
        myObject = bpy.data.objects.new("TestArmatureObject0003", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestArmatureBoneName0003")
        myArmatureBone.head = [1, 0, 0]
        myArmatureBone.tail = [0, 0, 0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wyarmature = WYArmature(myObject, None, None)
        wyarmature.init_armature_data()
        wymodelmanager0003 = WYModelManager()
        wymodelmanager0003.export_wyarmature(wyarmature, "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0003.wya")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0003.wya', 'r') as content_file:
            content = content_file.read()    
        print(content)   
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0003'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyarmature_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyarmature function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmature object initialized with default Blender armature object is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0004" through "export_wyarmature" function resulting the string read from the given file path is equal to the object toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to export with..
        :type  wyarmature: WYArmature.
        :test  wyarmature: myArmature=bpy.data.armatures.new("TestArmature0004")
myObject=bpy.data.objects.new("TestArmatureObject0004",myArmature)
bpy.context.scene.objects.link(myObject)
bpy.context.scene.objects.active=myObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myObject.data.edit_bones.new("TestArmatureBoneName0004")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
wyarmature=WYArmature(myObject,None,None).

        :param wyarmature_file_path: String of the file path to export the WYArmature object onto.
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0004.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyarmature)
        """
        myArmature = bpy.data.armatures.new("TestArmature0004")
        myObject = bpy.data.objects.new("TestArmatureObject0004", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestArmatureBoneName0004")
        myArmatureBone.head = [1, 0, 0]
        myArmatureBone.tail = [0, 0, 0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wyarmature = WYArmature(myObject, None, None)
        wyarmature.init_armature_data()
        wymodelmanager0004 = WYModelManager()
        wymodelmanager0004.export_wyarmature(wyarmature, "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0004.wya")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0004.wya', 'r') as content_file:
            content = content_file.read()    
        print(content)   
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0004'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyarmature_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyarmature function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmature object initialized with default Blender armature object is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0005" through "export_wyarmature" function resulting the string read from the given file path is equal to the object toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to export with..
        :type  wyarmature: WYArmature.
        :test  wyarmature: myArmature=bpy.data.armatures.new("TestArmature0005")
myObject=bpy.data.objects.new("TestArmatureObject0005",myArmature)
bpy.context.scene.objects.link(myObject)
bpy.context.scene.objects.active=myObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myObject.data.edit_bones.new("TestArmatureBoneName0005")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
wyarmature=WYArmature(myObject,None,None).

        :param wyarmature_file_path: String of the file path to export the WYArmature object onto.
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0005.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyarmature)
        """
        myArmature = bpy.data.armatures.new("TestArmature0005")
        myObject = bpy.data.objects.new("TestArmatureObject0005", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestArmatureBoneName0005")
        myArmatureBone.head = [1, 0, 0]
        myArmatureBone.tail = [0, 0, 0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wyarmature = WYArmature(myObject, None, None)
        wyarmature.init_armature_data()
        wymodelmanager0005 = WYModelManager()
        wymodelmanager0005.export_wyarmature(wyarmature, "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0005.wya")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0005.wya', 'r') as content_file:
            content = content_file.read()    
        print(content)   
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0005'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyarmature_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyarmature function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmature object initialized with default Blender armature object is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0006" through "export_wyarmature" function resulting the string read from the given file path is equal to the object toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to export with..
        :type  wyarmature: WYArmature.
        :test  wyarmature: myArmature=bpy.data.armatures.new("TestArmature0006")
myObject=bpy.data.objects.new("TestArmatureObject0006",myArmature)
bpy.context.scene.objects.link(myObject)
bpy.context.scene.objects.active=myObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myObject.data.edit_bones.new("TestArmatureBoneName0006")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
wyarmature=WYArmature(myObject,None,None).

        :param wyarmature_file_path: String of the file path to export the WYArmature object onto.
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0006.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyarmature)
        """
        myArmature = bpy.data.armatures.new("TestArmature0006")
        myObject = bpy.data.objects.new("TestArmatureObject0006", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestArmatureBoneName0006")
        myArmatureBone.head = [1, 0, 0]
        myArmatureBone.tail = [0, 0, 0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wyarmature = WYArmature(myObject, None, None)
        wyarmature.init_armature_data()
        wymodelmanager0006 = WYModelManager()
        wymodelmanager0006.export_wyarmature(wyarmature, "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0006.wya")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0006.wya', 'r') as content_file:
            content = content_file.read()    
        print(content)   
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0006'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyarmature_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyarmature function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmature object initialized with default Blender armature object is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0007" through "export_wyarmature" function resulting the string read from the given file path is equal to the object toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to export with..
        :type  wyarmature: WYArmature.
        :test  wyarmature: myArmature=bpy.data.armatures.new("TestArmature0007")
myObject=bpy.data.objects.new("TestArmatureObject0007",myArmature)
bpy.context.scene.objects.link(myObject)
bpy.context.scene.objects.active=myObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myObject.data.edit_bones.new("TestArmatureBoneName0007")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
wyarmature=WYArmature(myObject,None,None).

        :param wyarmature_file_path: String of the file path to export the WYArmature object onto.
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0007.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyarmature)
        """
        myArmature = bpy.data.armatures.new("TestArmature0007")
        myObject = bpy.data.objects.new("TestArmatureObject0007", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestArmatureBoneName0007")
        myArmatureBone.head = [1, 0, 0]
        myArmatureBone.tail = [0, 0, 0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wyarmature = WYArmature(myObject, None, None)
        wyarmature.init_armature_data()
        wymodelmanager0007 = WYModelManager()
        wymodelmanager0007.export_wyarmature(wyarmature, "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0007.wya")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0007.wya', 'r') as content_file:
            content = content_file.read()    
        print(content)   
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0007'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyarmature_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyarmature function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmature object initialized with default Blender armature object is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0008" through "export_wyarmature" function resulting the string read from the given file path is equal to the object toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to export with..
        :type  wyarmature: WYArmature.
        :test  wyarmature: myArmature=bpy.data.armatures.new("TestArmature0008")
myObject=bpy.data.objects.new("TestArmatureObject0008",myArmature)
bpy.context.scene.objects.link(myObject)
bpy.context.scene.objects.active=myObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myObject.data.edit_bones.new("TestArmatureBoneName0008")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
wyarmature=WYArmature(myObject,None,None).

        :param wyarmature_file_path: String of the file path to export the WYArmature object onto.
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0008.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyarmature)
        """
        myArmature = bpy.data.armatures.new("TestArmature0008")
        myObject = bpy.data.objects.new("TestArmatureObject0008", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestArmatureBoneName0008")
        myArmatureBone.head = [1, 0, 0]
        myArmatureBone.tail = [0, 0, 0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wyarmature = WYArmature(myObject, None, None)
        wyarmature.init_armature_data()
        wymodelmanager0008 = WYModelManager()
        wymodelmanager0008.export_wyarmature(wyarmature, "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0008.wya")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0008.wya', 'r') as content_file:
            content = content_file.read()    
        print(content)   
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0008'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyarmature_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyarmature function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmature object initialized with default Blender armature object is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0009" through "export_wyarmature" function resulting the string read from the given file path is equal to the object toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to export with..
        :type  wyarmature: WYArmature.
        :test  wyarmature: myArmature=bpy.data.armatures.new("TestArmature0009")
myObject=bpy.data.objects.new("TestArmatureObject0009",myArmature)
bpy.context.scene.objects.link(myObject)
bpy.context.scene.objects.active=myObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myObject.data.edit_bones.new("TestArmatureBoneName0009")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
wyarmature=WYArmature(myObject,None,None).

        :param wyarmature_file_path: String of the file path to export the WYArmature object onto.
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0009.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyarmature)
        """
        myArmature = bpy.data.armatures.new("TestArmature0009")
        myObject = bpy.data.objects.new("TestArmatureObject0009", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestArmatureBoneName0009")
        myArmatureBone.head = [1, 0, 0]
        myArmatureBone.tail = [0, 0, 0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wyarmature = WYArmature(myObject, None, None)
        wyarmature.init_armature_data()
        wymodelmanager0009 = WYModelManager()
        wymodelmanager0009.export_wyarmature(wyarmature, "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0009.wya")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0009.wya', 'r') as content_file:
            content = content_file.read()    
        print(content)   
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0009'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyarmature_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyarmature function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmature object initialized with default Blender armature object is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0010" through "export_wyarmature" function resulting the string read from the given file path is equal to the object toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to export with..
        :type  wyarmature: WYArmature.
        :test  wyarmature: myArmature=bpy.data.armatures.new("TestArmature0010")
myObject=bpy.data.objects.new("TestArmatureObject0010",myArmature)
bpy.context.scene.objects.link(myObject)
bpy.context.scene.objects.active=myObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myObject.data.edit_bones.new("TestArmatureBoneName0010")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
wyarmature=WYArmature(myObject,None,None).

        :param wyarmature_file_path: String of the file path to export the WYArmature object onto.
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: ..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0010.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyarmature)
        """
        myArmature = bpy.data.armatures.new("TestArmature0010")
        myObject = bpy.data.objects.new("TestArmatureObject0010", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestArmatureBoneName0010")
        myArmatureBone.head = [1, 0, 0]
        myArmatureBone.tail = [0, 0, 0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wyarmature = WYArmature(myObject, None, None)
        wyarmature.init_armature_data()
        wymodelmanager0010 = WYModelManager()
        wymodelmanager0010.export_wyarmature(wyarmature, "..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0010.wya")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyarmature\\TestFile0010.wya', 'r') as content_file:
            content = content_file.read()    
        print(content)   
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0010'].select = True
        bpy.ops.object.delete()

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_export_wyarmature))
