"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2018-01-24
Last update                         : 2018-01-31
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_export_animation_model\WYModelManagerTestCases_export_animation_model.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_export_animation_model\WYModelManagerTestCases_export_animation_model.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : export_animation_model(animation, armature, model, wycoordsys, file_path)
Unit test case class name           : WYModelManagerTestCases_export_animation_model
Unit test case description          : Unit test case for class WYModelManager export_animation_model() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_export_animation_model\WYModelManagerTestCaseResult_export_animation_model.txt
"""
# Pre-condition: WYAnimation is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_export_animation_model(unittest.TestCase):
    """
    Unit test case for class WYModelManager export_animation_model() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_export_animation_model_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_animation_model function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0001" through "export_animation_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param animation: Blender pose object to export with..
        :type  animation: bpy.data.pose.
        :test  animation: myArmatureObject.pose.

        :param armature: Blender armature object which animation is mapped onto..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0001")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0001",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0001")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[1,0,0]
myArmaturePoseBone.rotation_quaternion=[1,1,0,0]
myArmaturePoseBone.scale=[1,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=1)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=1)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=1)
bpy.context.scene.frame_set(1).

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0001.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyanimation)
        """
        myArmature = bpy.data.armatures.new("TestArmature0001")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0001", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0001")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [1, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [1,1,0,0]
        myArmaturePoseBone.scale = [1, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=1)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=1)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=1)
        bpy.context.scene.frame_set(1)
        wymodelmanager0001 = WYModelManager()
        wyanimation = wymodelmanager0001.export_animation_model(myArmatureObject.pose, myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False), 1-1, 1, "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0001")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0001.wyan', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyanimation)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0001'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_animation_model_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_animation_model function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0002" through "export_animation_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param animation: Blender pose object to export with..
        :type  animation: bpy.data.pose.
        :test  animation: myArmatureObject.pose.

        :param armature: Blender armature object which animation is mapped onto..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0002")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0002",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0002")
myArmatureBone.head=[2,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[2,0,0]
myArmaturePoseBone.rotation_quaternion=[1,2,0,0]
myArmaturePoseBone.scale=[2,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=2)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=2)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=2)
bpy.context.scene.frame_set(2).

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0002.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyanimation)
        """
        myArmature = bpy.data.armatures.new("TestArmature0002")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0002", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0002")
        myArmatureBone.head = [2,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [2, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [1,2,0,0]
        myArmaturePoseBone.scale = [2, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=2)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=2)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=2)
        bpy.context.scene.frame_set(2)
        wymodelmanager0002 = WYModelManager()
        wyanimation = wymodelmanager0002.export_animation_model(myArmatureObject.pose, myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False), 2-1, 2, "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0002")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0002.wyan', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyanimation)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0002'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_animation_model_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_animation_model function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0003" through "export_animation_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param animation: Blender pose object to export with..
        :type  animation: bpy.data.pose.
        :test  animation: myArmatureObject.pose.

        :param armature: Blender armature object which animation is mapped onto..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0003")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0003",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0003")
myArmatureBone.head=[3,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[3,0,0]
myArmaturePoseBone.rotation_quaternion=[1,3,0,0]
myArmaturePoseBone.scale=[3,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=3)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=3)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=3)
bpy.context.scene.frame_set(3).

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0003.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyanimation)
        """
        myArmature = bpy.data.armatures.new("TestArmature0003")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0003", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0003")
        myArmatureBone.head = [3,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [3, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [1,3,0,0]
        myArmaturePoseBone.scale = [3, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=3)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=3)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=3)
        bpy.context.scene.frame_set(3)
        wymodelmanager0003 = WYModelManager()
        wyanimation = wymodelmanager0003.export_animation_model(myArmatureObject.pose, myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False), 3-1, 3, "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0003")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0003.wyan', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyanimation)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0003'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_animation_model_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_animation_model function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0004" through "export_animation_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param animation: Blender pose object to export with..
        :type  animation: bpy.data.pose.
        :test  animation: myArmatureObject.pose.

        :param armature: Blender armature object which animation is mapped onto..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0004")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0004",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0004")
myArmatureBone.head=[4,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[4,0,0]
myArmaturePoseBone.rotation_quaternion=[1,4,0,0]
myArmaturePoseBone.scale=[4,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=4)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=4)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=4)
bpy.context.scene.frame_set(4).

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0004.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyanimation)
        """
        myArmature = bpy.data.armatures.new("TestArmature0004")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0004", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0004")
        myArmatureBone.head = [4,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [4, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [1,4,0,0]
        myArmaturePoseBone.scale = [4, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=4)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=4)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=4)
        bpy.context.scene.frame_set(4)
        wymodelmanager0004 = WYModelManager()
        wyanimation = wymodelmanager0004.export_animation_model(myArmatureObject.pose, myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False), 4-1, 4, "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0004")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0004.wyan', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyanimation)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0004'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_animation_model_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_animation_model function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0005" through "export_animation_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param animation: Blender pose object to export with..
        :type  animation: bpy.data.pose.
        :test  animation: myArmatureObject.pose.

        :param armature: Blender armature object which animation is mapped onto..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0005")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0005",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0005")
myArmatureBone.head=[5,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[5,0,0]
myArmaturePoseBone.rotation_quaternion=[1,5,0,0]
myArmaturePoseBone.scale=[5,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=5)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=5)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=5)
bpy.context.scene.frame_set(5).

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0005.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyanimation)
        """
        myArmature = bpy.data.armatures.new("TestArmature0005")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0005", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0005")
        myArmatureBone.head = [5,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [5, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [1,5,0,0]
        myArmaturePoseBone.scale = [5, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=5)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=5)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=5)
        bpy.context.scene.frame_set(5)
        wymodelmanager0005 = WYModelManager()
        wyanimation = wymodelmanager0005.export_animation_model(myArmatureObject.pose, myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False), 5-1, 5, "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0005")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0005.wyan', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyanimation)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0005'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_animation_model_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_animation_model function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0006" through "export_animation_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param animation: Blender pose object to export with..
        :type  animation: bpy.data.pose.
        :test  animation: myArmatureObject.pose.

        :param armature: Blender armature object which animation is mapped onto..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0006")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0006",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0006")
myArmatureBone.head=[6,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[6,0,0]
myArmaturePoseBone.rotation_quaternion=[1,6,0,0]
myArmaturePoseBone.scale=[6,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=6)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=6)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=6)
bpy.context.scene.frame_set(6).

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0006.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyanimation)
        """
        myArmature = bpy.data.armatures.new("TestArmature0006")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0006", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0006")
        myArmatureBone.head = [6,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [6, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [1,6,0,0]
        myArmaturePoseBone.scale = [6, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=6)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=6)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=6)
        bpy.context.scene.frame_set(6)
        wymodelmanager0006 = WYModelManager()
        wyanimation = wymodelmanager0006.export_animation_model(myArmatureObject.pose, myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False), 6-1, 6, "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0006")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0006.wyan', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyanimation)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0006'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_animation_model_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_animation_model function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0007" through "export_animation_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param animation: Blender pose object to export with..
        :type  animation: bpy.data.pose.
        :test  animation: myArmatureObject.pose.

        :param armature: Blender armature object which animation is mapped onto..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0007")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0007",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0007")
myArmatureBone.head=[7,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[7,0,0]
myArmaturePoseBone.rotation_quaternion=[1,7,0,0]
myArmaturePoseBone.scale=[7,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=7)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=7)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=7)
bpy.context.scene.frame_set(7).

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0007.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyanimation)
        """
        myArmature = bpy.data.armatures.new("TestArmature0007")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0007", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0007")
        myArmatureBone.head = [7,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [7, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [1,7,0,0]
        myArmaturePoseBone.scale = [7, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=7)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=7)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=7)
        bpy.context.scene.frame_set(7)
        wymodelmanager0007 = WYModelManager()
        wyanimation = wymodelmanager0007.export_animation_model(myArmatureObject.pose, myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False), 7-1, 7, "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0007")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0007.wyan', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyanimation)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0007'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_animation_model_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_animation_model function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0008" through "export_animation_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param animation: Blender pose object to export with..
        :type  animation: bpy.data.pose.
        :test  animation: myArmatureObject.pose.

        :param armature: Blender armature object which animation is mapped onto..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0008")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0008",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0008")
myArmatureBone.head=[8,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[8,0,0]
myArmaturePoseBone.rotation_quaternion=[1,8,0,0]
myArmaturePoseBone.scale=[8,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=8)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=8)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=8)
bpy.context.scene.frame_set(8).

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0008.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyanimation)
        """
        myArmature = bpy.data.armatures.new("TestArmature0008")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0008", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0008")
        myArmatureBone.head = [8,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [8, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [1,8,0,0]
        myArmaturePoseBone.scale = [8, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=8)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=8)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=8)
        bpy.context.scene.frame_set(8)
        wymodelmanager0008 = WYModelManager()
        wyanimation = wymodelmanager0008.export_animation_model(myArmatureObject.pose, myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False), 8-1, 8, "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0008")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0008.wyan', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyanimation)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0008'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_animation_model_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_animation_model function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0009" through "export_animation_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param animation: Blender pose object to export with..
        :type  animation: bpy.data.pose.
        :test  animation: myArmatureObject.pose.

        :param armature: Blender armature object which animation is mapped onto..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0009")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0009",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0009")
myArmatureBone.head=[9,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[9,0,0]
myArmaturePoseBone.rotation_quaternion=[1,9,0,0]
myArmaturePoseBone.scale=[9,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=9)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=9)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=9)
bpy.context.scene.frame_set(9).

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0009.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyanimation)
        """
        myArmature = bpy.data.armatures.new("TestArmature0009")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0009", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0009")
        myArmatureBone.head = [9,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [9, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [1,9,0,0]
        myArmaturePoseBone.scale = [9, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=9)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=9)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=9)
        bpy.context.scene.frame_set(9)
        wymodelmanager0009 = WYModelManager()
        wyanimation = wymodelmanager0009.export_animation_model(myArmatureObject.pose, myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False), 9-1, 9, "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0009")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0009.wyan', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyanimation)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0009'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_animation_model_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_animation_model function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature is exported onto the given path "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0010" through "export_animation_model" function resulting the string read from the given file path is equal to the function returned WYArmature object's toString value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param animation: Blender pose object to export with..
        :type  animation: bpy.data.pose.
        :test  animation: myArmatureObject.pose.

        :param armature: Blender armature object which animation is mapped onto..
        :type  armature: bpy.data.armature.
        :test  armature: myArmature=bpy.data.armatures.new("TestArmature0010")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0010",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestArmatureBoneName0010")
myArmatureBone.head=[10,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[10,0,0]
myArmaturePoseBone.rotation_quaternion=[1,10,0,0]
myArmaturePoseBone.scale=[10,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=10)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=10)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=10)
bpy.context.scene.frame_set(10).

        :param model: Blender model object which current armature is mapped onto..
        :type  model: bpy.data.object.
        :test  model: None.

        :param wycoordsys: Coordinate system to export with..
        :type  wycoordsys: WYCoordsys.
        :test  wycoordsys: WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False).

        :param file_path: String of the file path to export the Blender armature object onto..
        :type  file_path: string.
        :test  file_path: ..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0010.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: content == str(wyanimation)
        """
        myArmature = bpy.data.armatures.new("TestArmature0010")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0010", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBoneName0010")
        myArmatureBone.head = [10,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [10, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [1,10,0,0]
        myArmaturePoseBone.scale = [10, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=10)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=10)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=10)
        bpy.context.scene.frame_set(10)
        wymodelmanager0010 = WYModelManager()
        wyanimation = wymodelmanager0010.export_animation_model(myArmatureObject.pose, myArmatureObject, None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False), 10-1, 10, "..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0010")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_animation_model\\TestFile0010.wyan', 'r') as content_file:
            content = content_file.read()    
        self.assertTrue(content == str(wyanimation)) 
        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.data.objects['TestArmatureObject0010'].select = True
        bpy.ops.object.delete()

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_export_animation_model))
