"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2018-01-22
Last update                         : 2018-01-22
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_export_armature_model\WYModelManagerTestCases_export_armature_model.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_export_armature_model\WYModelManagerTestCases_export_armature_model.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : export_armature_model(armature, model, wycoordsys, file_path)
Unit test case class name           : WYModelManagerTestCases_export_armature_model
Unit test case description          : Unit test case for class WYModelManager export_armature_model() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_export_armature_model\WYModelManagerTestCaseResult_export_armature_model.txt
"""
# Pre-condition: WYArmature is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_export_armature_model(unittest.TestCase):
    """
    Unit test case for class WYModelManager export_armature_model() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :11
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_export_armature_model_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_armature_model function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0001" through "export_armature_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param armature: Blender armature object to export with..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0001")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0001",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0001")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0001.

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
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0001", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0001")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0001 = WYModelManager()
        wyarmature = wymodelmanager0001.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0001")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0001.wya', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0001'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_armature_model_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_armature_model function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0002" through "export_armature_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param armature: Blender armature object to export with..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0002")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0002",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0002")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0002.

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
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0002", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0002")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0002 = WYModelManager()
        wyarmature = wymodelmanager0002.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0002")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0002.wya', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0002'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_armature_model_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_armature_model function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0003" through "export_armature_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param armature: Blender armature object to export with..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0003")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0003",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0003")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0003.

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
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0003", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0003")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0003 = WYModelManager()
        wyarmature = wymodelmanager0003.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0003")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0003.wya', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0003'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_armature_model_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_armature_model function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0004" through "export_armature_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param armature: Blender armature object to export with..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0004")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0004",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0004")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0004.

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
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0004", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0004")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0004 = WYModelManager()
        wyarmature = wymodelmanager0004.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0004")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0004.wya', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0004'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_armature_model_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_armature_model function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0005" through "export_armature_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param armature: Blender armature object to export with..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0005")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0005",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0005")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0005.

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
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0005", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0005")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0005 = WYModelManager()
        wyarmature = wymodelmanager0005.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0005")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0005.wya', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0005'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_armature_model_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_armature_model function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0006" through "export_armature_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param armature: Blender armature object to export with..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0006")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0006",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0006")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0006.

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
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0006", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0006")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0006 = WYModelManager()
        wyarmature = wymodelmanager0006.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0006")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0006.wya', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0006'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_armature_model_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_armature_model function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0007" through "export_armature_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param armature: Blender armature object to export with..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0007")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0007",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0007")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0007.

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
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0007", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0007")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0007 = WYModelManager()
        wyarmature = wymodelmanager0007.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0007")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0007.wya', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0007'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_armature_model_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_armature_model function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0008" through "export_armature_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param armature: Blender armature object to export with..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0008")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0008",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0008")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0008.

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
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0008", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0008")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0008 = WYModelManager()
        wyarmature = wymodelmanager0008.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0008")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0008.wya', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0008'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_armature_model_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_armature_model function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0009" through "export_armature_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param armature: Blender armature object to export with..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0009")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0009",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0009")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0009.

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
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0009", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0009")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0009 = WYModelManager()
        wyarmature = wymodelmanager0009.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0009")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0009.wya', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0009'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_armature_model_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_armature_model function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0010" through "export_armature_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param armature: Blender armature object to export with..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0010")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0010",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0010")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0010.

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
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0010", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0010")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        wymodelmanager0010 = WYModelManager()
        wyarmature = wymodelmanager0010.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0010")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0010.wya', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0010'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_armature_model_TC_NC_0011(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_armature_model function testing normal case 0011

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0011" through "export_armature_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param armature: Blender armature object to export with..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0011")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0011",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0011")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT').

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0011.

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
        wyarmature = wymodelmanager0011.export_armature_model(myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False),"..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0011")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_armature_model\\TestFile0011.wya', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyarmature)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0011'].select = True
        bpy.ops.object.delete()

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_export_armature_model))
