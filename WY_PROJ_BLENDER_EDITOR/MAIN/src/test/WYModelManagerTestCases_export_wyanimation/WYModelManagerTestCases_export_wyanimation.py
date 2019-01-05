"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2018-02-20
Last update                         : 2018-02-20
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_export_wyanimation\WYModelManagerTestCases_export_wyanimation.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_export_wyanimation\WYModelManagerTestCases_export_wyanimation.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : export_wyanimation(wyanimation, wyanimation_file_path)
Unit test case class name           : WYModelManagerTestCases_export_wyanimation
Unit test case description          : Unit test case for class WYAnimation export_wyanimation() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_export_wyanimation\WYAnimationTestCaseResult_export_wyanimation.txt
"""
# Pre-condition: WYAnimation is tested.

import bpy
from mathutils import Vector, geometry, Quaternion
import os
filename = os.getcwd() + "\\..\\..\\main\\WYArmature\\WYArmature.py" 
exec(compile(open(filename).read(), filename, 'exec'))
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_export_wyanimation(unittest.TestCase):
    """
    Unit test case for class WYAnimation export_wyanimation() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_export_wyanimation_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyanimation function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if animation is exported properly through "export_wyanimation" function, resulting the string read back from exported file path is equal to the exported object's toString value, content == str(wyanimation).
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
        myArmature = bpy.data.armatures.new("TestArmatureObject0001")
        myObject = bpy.data.objects.new("TestArmatureObject0001", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        myObject.select = True
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestAnimaitonBoneName0001")
        myArmatureBone.head = Vector((1,0,0))
        myArmatureBone.tail = Vector((0,0,0))
        bpy.ops.object.mode_set(mode='OBJECT') 
        myArmaturePoseBone = myObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [1, 0, 0]
        myArmaturePoseBone.rotation_quaternion = Quaternion((1, 1, 0, 0))
        myArmaturePoseBone.scale = [1, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=1)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=1)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=1)
        bpy.context.scene.frame_set(1)
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0001"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myObject.pose, wyarmature)
        wyanimation.init_animation_data(1-1,1)
        wymodelmanager = WYModelManager()
        wymodelmanager.export_wyanimation(wyanimation, "..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0001.wyan")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0001.wyan', 'r') as content_file:
            content = content_file.read() 
        self.assertTrue(content == str(wyanimation))
        bpy.data.objects['TestArmatureObject0001'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyanimation_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyanimation function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if animation is exported properly through "export_wyanimation" function, resulting the string read back from exported file path is equal to the exported object's toString value, content == str(wyanimation).
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
        myArmature = bpy.data.armatures.new("TestArmatureObject0002")
        myObject = bpy.data.objects.new("TestArmatureObject0002", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        myObject.select = True
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestAnimaitonBoneName0002")
        myArmatureBone.head = Vector((1,0,0))
        myArmatureBone.tail = Vector((0,0,0))
        bpy.ops.object.mode_set(mode='OBJECT') 
        myArmaturePoseBone = myObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [1, 0, 0]
        myArmaturePoseBone.rotation_quaternion = Quaternion((1, 1, 0, 0))
        myArmaturePoseBone.scale = [1, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=2)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=2)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=2)
        bpy.context.scene.frame_set(2)
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0002"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myObject.pose, wyarmature)
        wyanimation.init_animation_data(2-1,2)
        wymodelmanager = WYModelManager()
        wymodelmanager.export_wyanimation(wyanimation, "..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0002.wyan")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0002.wyan', 'r') as content_file:
            content = content_file.read() 
        self.assertTrue(content == str(wyanimation))
        bpy.data.objects['TestArmatureObject0002'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyanimation_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyanimation function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if animation is exported properly through "export_wyanimation" function, resulting the string read back from exported file path is equal to the exported object's toString value, content == str(wyanimation).
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
        myArmature = bpy.data.armatures.new("TestArmatureObject0003")
        myObject = bpy.data.objects.new("TestArmatureObject0003", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        myObject.select = True
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestAnimaitonBoneName0003")
        myArmatureBone.head = Vector((1,0,0))
        myArmatureBone.tail = Vector((0,0,0))
        bpy.ops.object.mode_set(mode='OBJECT') 
        myArmaturePoseBone = myObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [1, 0, 0]
        myArmaturePoseBone.rotation_quaternion = Quaternion((1, 1, 0, 0))
        myArmaturePoseBone.scale = [1, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=3)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=3)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=3)
        bpy.context.scene.frame_set(3)
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0003"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myObject.pose, wyarmature)
        wyanimation.init_animation_data(3-1,3)
        wymodelmanager = WYModelManager()
        wymodelmanager.export_wyanimation(wyanimation, "..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0003.wyan")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0003.wyan', 'r') as content_file:
            content = content_file.read() 
        self.assertTrue(content == str(wyanimation))
        bpy.data.objects['TestArmatureObject0003'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyanimation_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyanimation function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if animation is exported properly through "export_wyanimation" function, resulting the string read back from exported file path is equal to the exported object's toString value, content == str(wyanimation).
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
        myArmature = bpy.data.armatures.new("TestArmatureObject0004")
        myObject = bpy.data.objects.new("TestArmatureObject0004", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        myObject.select = True
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestAnimaitonBoneName0004")
        myArmatureBone.head = Vector((1,0,0))
        myArmatureBone.tail = Vector((0,0,0))
        bpy.ops.object.mode_set(mode='OBJECT') 
        myArmaturePoseBone = myObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [1, 0, 0]
        myArmaturePoseBone.rotation_quaternion = Quaternion((1, 1, 0, 0))
        myArmaturePoseBone.scale = [1, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=4)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=4)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=4)
        bpy.context.scene.frame_set(4)
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0004"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myObject.pose, wyarmature)
        wyanimation.init_animation_data(4-1,4)
        wymodelmanager = WYModelManager()
        wymodelmanager.export_wyanimation(wyanimation, "..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0004.wyan")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0004.wyan', 'r') as content_file:
            content = content_file.read() 
        self.assertTrue(content == str(wyanimation))
        bpy.data.objects['TestArmatureObject0004'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyanimation_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyanimation function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if animation is exported properly through "export_wyanimation" function, resulting the string read back from exported file path is equal to the exported object's toString value, content == str(wyanimation).
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
        myArmature = bpy.data.armatures.new("TestArmatureObject0005")
        myObject = bpy.data.objects.new("TestArmatureObject0005", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        myObject.select = True
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestAnimaitonBoneName0005")
        myArmatureBone.head = Vector((1,0,0))
        myArmatureBone.tail = Vector((0,0,0))
        bpy.ops.object.mode_set(mode='OBJECT') 
        myArmaturePoseBone = myObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [1, 0, 0]
        myArmaturePoseBone.rotation_quaternion = Quaternion((1, 1, 0, 0))
        myArmaturePoseBone.scale = [1, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=5)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=5)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=5)
        bpy.context.scene.frame_set(5)
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0005"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myObject.pose, wyarmature)
        wyanimation.init_animation_data(5-1,5)
        wymodelmanager = WYModelManager()
        wymodelmanager.export_wyanimation(wyanimation, "..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0005.wyan")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0005.wyan', 'r') as content_file:
            content = content_file.read() 
        self.assertTrue(content == str(wyanimation))
        bpy.data.objects['TestArmatureObject0005'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyanimation_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyanimation function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if animation is exported properly through "export_wyanimation" function, resulting the string read back from exported file path is equal to the exported object's toString value, content == str(wyanimation).
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
        myArmature = bpy.data.armatures.new("TestArmatureObject0006")
        myObject = bpy.data.objects.new("TestArmatureObject0006", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        myObject.select = True
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestAnimaitonBoneName0006")
        myArmatureBone.head = Vector((1,0,0))
        myArmatureBone.tail = Vector((0,0,0))
        bpy.ops.object.mode_set(mode='OBJECT') 
        myArmaturePoseBone = myObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [1, 0, 0]
        myArmaturePoseBone.rotation_quaternion = Quaternion((1, 1, 0, 0))
        myArmaturePoseBone.scale = [1, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=6)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=6)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=6)
        bpy.context.scene.frame_set(6)
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0006"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myObject.pose, wyarmature)
        wyanimation.init_animation_data(6-1,6)
        wymodelmanager = WYModelManager()
        wymodelmanager.export_wyanimation(wyanimation, "..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0006.wyan")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0006.wyan', 'r') as content_file:
            content = content_file.read() 
        self.assertTrue(content == str(wyanimation))
        bpy.data.objects['TestArmatureObject0006'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyanimation_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyanimation function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if animation is exported properly through "export_wyanimation" function, resulting the string read back from exported file path is equal to the exported object's toString value, content == str(wyanimation).
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
        myArmature = bpy.data.armatures.new("TestArmatureObject0007")
        myObject = bpy.data.objects.new("TestArmatureObject0007", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        myObject.select = True
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestAnimaitonBoneName0007")
        myArmatureBone.head = Vector((1,0,0))
        myArmatureBone.tail = Vector((0,0,0))
        bpy.ops.object.mode_set(mode='OBJECT') 
        myArmaturePoseBone = myObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [1, 0, 0]
        myArmaturePoseBone.rotation_quaternion = Quaternion((1, 1, 0, 0))
        myArmaturePoseBone.scale = [1, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=7)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=7)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=7)
        bpy.context.scene.frame_set(7)
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0007"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myObject.pose, wyarmature)
        wyanimation.init_animation_data(7-1,7)
        wymodelmanager = WYModelManager()
        wymodelmanager.export_wyanimation(wyanimation, "..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0007.wyan")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0007.wyan', 'r') as content_file:
            content = content_file.read() 
        self.assertTrue(content == str(wyanimation))
        bpy.data.objects['TestArmatureObject0007'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyanimation_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyanimation function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if animation is exported properly through "export_wyanimation" function, resulting the string read back from exported file path is equal to the exported object's toString value, content == str(wyanimation).
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
        myArmature = bpy.data.armatures.new("TestArmatureObject0008")
        myObject = bpy.data.objects.new("TestArmatureObject0008", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        myObject.select = True
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestAnimaitonBoneName0008")
        myArmatureBone.head = Vector((1,0,0))
        myArmatureBone.tail = Vector((0,0,0))
        bpy.ops.object.mode_set(mode='OBJECT') 
        myArmaturePoseBone = myObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [1, 0, 0]
        myArmaturePoseBone.rotation_quaternion = Quaternion((1, 1, 0, 0))
        myArmaturePoseBone.scale = [1, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=8)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=8)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=8)
        bpy.context.scene.frame_set(8)
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0008"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myObject.pose, wyarmature)
        wyanimation.init_animation_data(8-1,8)
        wymodelmanager = WYModelManager()
        wymodelmanager.export_wyanimation(wyanimation, "..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0008.wyan")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0008.wyan', 'r') as content_file:
            content = content_file.read() 
        self.assertTrue(content == str(wyanimation))
        bpy.data.objects['TestArmatureObject0008'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyanimation_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyanimation function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if animation is exported properly through "export_wyanimation" function, resulting the string read back from exported file path is equal to the exported object's toString value, content == str(wyanimation).
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
        myArmature = bpy.data.armatures.new("TestArmatureObject0009")
        myObject = bpy.data.objects.new("TestArmatureObject0009", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        myObject.select = True
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestAnimaitonBoneName0009")
        myArmatureBone.head = Vector((1,0,0))
        myArmatureBone.tail = Vector((0,0,0))
        bpy.ops.object.mode_set(mode='OBJECT') 
        myArmaturePoseBone = myObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [1, 0, 0]
        myArmaturePoseBone.rotation_quaternion = Quaternion((1, 1, 0, 0))
        myArmaturePoseBone.scale = [1, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=9)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=9)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=9)
        bpy.context.scene.frame_set(9)
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0009"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myObject.pose, wyarmature)
        wyanimation.init_animation_data(9-1,9)
        wymodelmanager = WYModelManager()
        wymodelmanager.export_wyanimation(wyanimation, "..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0009.wyan")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0009.wyan', 'r') as content_file:
            content = content_file.read() 
        self.assertTrue(content == str(wyanimation))
        bpy.data.objects['TestArmatureObject0009'].select = True
        bpy.ops.object.delete()
    def test_WYModelManagerTestCase_export_wyanimation_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager export_wyanimation function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if animation is exported properly through "export_wyanimation" function, resulting the string read back from exported file path is equal to the exported object's toString value, content == str(wyanimation).
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
        myArmature = bpy.data.armatures.new("TestArmatureObject0010")
        myObject = bpy.data.objects.new("TestArmatureObject0010", myArmature)
        bpy.context.scene.objects.link(myObject)
        bpy.context.scene.objects.active = myObject
        myObject.select = True
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureBone = myObject.data.edit_bones.new("TestAnimaitonBoneName0010")
        myArmatureBone.head = Vector((1,0,0))
        myArmatureBone.tail = Vector((0,0,0))
        bpy.ops.object.mode_set(mode='OBJECT') 
        myArmaturePoseBone = myObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [1, 0, 0]
        myArmaturePoseBone.rotation_quaternion = Quaternion((1, 1, 0, 0))
        myArmaturePoseBone.scale = [1, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=10)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=10)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=10)
        bpy.context.scene.frame_set(10)
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0010"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myObject.pose, wyarmature)
        wyanimation.init_animation_data(10-1,10)
        wymodelmanager = WYModelManager()
        wymodelmanager.export_wyanimation(wyanimation, "..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0010.wyan")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_export_wyanimation\\TestFile0010.wyan', 'r') as content_file:
            content = content_file.read() 
        self.assertTrue(content == str(wyanimation))
        bpy.data.objects['TestArmatureObject0010'].select = True
        bpy.ops.object.delete()

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_export_wyanimation))
