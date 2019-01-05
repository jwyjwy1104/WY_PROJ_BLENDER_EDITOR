"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2018-02-20
Last update                         : 2018-02-20
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_import_wyanimationbone\WYModelManagerTestCases_import_wyanimationbone.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_import_wyanimationbone\WYModelManagerTestCases_import_wyanimationbone.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : import_wyanimationbone(wyanimation, wyanimation_file_obj)
Unit test case class name           : WYModelManagerTestCases_import_wyanimationbone
Unit test case description          : Unit test case for class WYModelManager import_wyanimationbone() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_import_wyanimationbone\WYModelManagerTestCaseResult_import_wyanimationbone.txt
"""
# Pre-condition: WYArmature is tested.
# Pre-condition: WYArmatureBone is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_import_wyanimationbone(unittest.TestCase):
    """
    Unit test case for class WYModelManager import_wyanimationbone() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_import_wyanimationbone_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimationbone function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimationBone objects are imported from given path "abn TestAnimationBoneName0001\nkf 0 {\nabh 1.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 1.0 0.0 0.0\nrotq 1.0 1.0 0.0 0.0\nsca 1.0 0.0 0.0\n}\n" through "import_wyanimationbone" function resulting the data values imported from file is equal to the expected value where animation bone is name "TestArmatureObject0001" location vector value[1,0,0], rotation quaternion value [1.0,1.0,0.0,0.0] and scale vector value [1,0,0] on keyframe 1 is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation: WYAnimation object to store the imported WYAnimationBone objects imported from same file..
        :type  wyanimation: WYAnimation.
        :test  wyanimation: myArmature=bpy.data.armatures.new("TestArmatureObject0001")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0001",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestAnimationBoneName0001")
myArmatureBone.head=[1,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[1.0,0,0]
myArmaturePoseBone.rotation_quaternion=[1.0,1.0,0,0]
myArmaturePoseBone.scale=[1.0,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=1)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=1)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=1)
bpy.context.scene.frame_set(1).

        :param wyanimation_file_obj: File object opened for importing WYArmature object..
        :type  wyanimation_file_obj: File.
        :test  wyanimation_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0001.wyan','w+')asfile:
file.write("abnTestAnimationBoneName0001\nkf0{\nabh1.00.00.0\nabt0.00.00.0\nloc1.00.00.0\nrotq1.01.00.00.0\nsca1.00.00.0\n}\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (1.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (1.0,1.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (1.0,0.0,0.0)
        """
        myArmature = bpy.data.armatures.new("TestArmatureObject0001")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0001", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestAnimationBoneName0001")
        myArmatureBone.head = [1,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [1.0, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [1.0,1.0,0,0]
        myArmaturePoseBone.scale = [1.0, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=1)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=1)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=1)
        bpy.context.scene.frame_set(1)
        wyanimation = WYAnimation()
        wymodelmanager0001 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0001.wyan', 'w+') as file:
            file.write("abn TestAnimationBoneName0001\nkf 0 {\nabh 1.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 1.0 0.0 0.0\nrotq 1.0 1.0 0.0 0.0\nsca 1.0 0.0 0.0\n}\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0001.wyan') as content_file:
            wymodelmanager0001.import_wyanimationbone(wyanimation, content_file) 
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale)
        self.assertTrue(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (1.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (1.0,1.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (1.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyanimationbone_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimationbone function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimationBone objects are imported from given path "abn TestAnimationBoneName0002\nkf 0 {\nabh 2.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 2.0 0.0 0.0\nrotq 2.0 2.0 0.0 0.0\nsca 2.0 0.0 0.0\n}\n" through "import_wyanimationbone" function resulting the data values imported from file is equal to the expected value where animation bone is name "TestArmatureObject0002" location vector value[2,0,0], rotation quaternion value [2.0,2.0,0.0,0.0] and scale vector value [2,0,0] on keyframe 2 is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation: WYAnimation object to store the imported WYAnimationBone objects imported from same file..
        :type  wyanimation: WYAnimation.
        :test  wyanimation: myArmature=bpy.data.armatures.new("TestArmatureObject0002")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0002",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestAnimationBoneName0002")
myArmatureBone.head=[2,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[2.0,0,0]
myArmaturePoseBone.rotation_quaternion=[2.0,2.0,0,0]
myArmaturePoseBone.scale=[2.0,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=2)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=2)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=2)
bpy.context.scene.frame_set(2).

        :param wyanimation_file_obj: File object opened for importing WYArmature object..
        :type  wyanimation_file_obj: File.
        :test  wyanimation_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0002.wyan','w+')asfile:
file.write("abnTestAnimationBoneName0002\nkf0{\nabh2.00.00.0\nabt0.00.00.0\nloc2.00.00.0\nrotq2.02.00.00.0\nsca2.00.00.0\n}\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (2.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (2.0,2.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (2.0,0.0,0.0)
        """
        myArmature = bpy.data.armatures.new("TestArmatureObject0002")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0002", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestAnimationBoneName0002")
        myArmatureBone.head = [2,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [2.0, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [2.0,2.0,0,0]
        myArmaturePoseBone.scale = [2.0, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=2)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=2)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=2)
        bpy.context.scene.frame_set(2)
        wyanimation = WYAnimation()
        wymodelmanager0002 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0002.wyan', 'w+') as file:
            file.write("abn TestAnimationBoneName0002\nkf 0 {\nabh 2.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 2.0 0.0 0.0\nrotq 2.0 2.0 0.0 0.0\nsca 2.0 0.0 0.0\n}\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0002.wyan') as content_file:
            wymodelmanager0002.import_wyanimationbone(wyanimation, content_file) 
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale)
        self.assertTrue(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (2.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (2.0,2.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (2.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyanimationbone_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimationbone function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimationBone objects are imported from given path "abn TestAnimationBoneName0003\nkf 0 {\nabh 3.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 3.0 0.0 0.0\nrotq 3.0 3.0 0.0 0.0\nsca 3.0 0.0 0.0\n}\n" through "import_wyanimationbone" function resulting the data values imported from file is equal to the expected value where animation bone is name "TestArmatureObject0003" location vector value[3,0,0], rotation quaternion value [3.0,3.0,0.0,0.0] and scale vector value [3,0,0] on keyframe 3 is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation: WYAnimation object to store the imported WYAnimationBone objects imported from same file..
        :type  wyanimation: WYAnimation.
        :test  wyanimation: myArmature=bpy.data.armatures.new("TestArmatureObject0003")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0003",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestAnimationBoneName0003")
myArmatureBone.head=[3,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[3.0,0,0]
myArmaturePoseBone.rotation_quaternion=[3.0,3.0,0,0]
myArmaturePoseBone.scale=[3.0,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=3)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=3)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=3)
bpy.context.scene.frame_set(3).

        :param wyanimation_file_obj: File object opened for importing WYArmature object..
        :type  wyanimation_file_obj: File.
        :test  wyanimation_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0003.wyan','w+')asfile:
file.write("abnTestAnimationBoneName0003\nkf0{\nabh3.00.00.0\nabt0.00.00.0\nloc3.00.00.0\nrotq3.03.00.00.0\nsca3.00.00.0\n}\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (3.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (3.0,3.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (3.0,0.0,0.0)
        """
        myArmature = bpy.data.armatures.new("TestArmatureObject0003")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0003", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestAnimationBoneName0003")
        myArmatureBone.head = [3,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [3.0, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [3.0,3.0,0,0]
        myArmaturePoseBone.scale = [3.0, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=3)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=3)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=3)
        bpy.context.scene.frame_set(3)
        wyanimation = WYAnimation()
        wymodelmanager0003 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0003.wyan', 'w+') as file:
            file.write("abn TestAnimationBoneName0003\nkf 0 {\nabh 3.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 3.0 0.0 0.0\nrotq 3.0 3.0 0.0 0.0\nsca 3.0 0.0 0.0\n}\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0003.wyan') as content_file:
            wymodelmanager0003.import_wyanimationbone(wyanimation, content_file) 
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale)
        self.assertTrue(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (3.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (3.0,3.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (3.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyanimationbone_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimationbone function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimationBone objects are imported from given path "abn TestAnimationBoneName0004\nkf 0 {\nabh 4.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 4.0 0.0 0.0\nrotq 4.0 4.0 0.0 0.0\nsca 4.0 0.0 0.0\n}\n" through "import_wyanimationbone" function resulting the data values imported from file is equal to the expected value where animation bone is name "TestArmatureObject0004" location vector value[4,0,0], rotation quaternion value [4.0,4.0,0.0,0.0] and scale vector value [4,0,0] on keyframe 4 is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation: WYAnimation object to store the imported WYAnimationBone objects imported from same file..
        :type  wyanimation: WYAnimation.
        :test  wyanimation: myArmature=bpy.data.armatures.new("TestArmatureObject0004")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0004",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestAnimationBoneName0004")
myArmatureBone.head=[4,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[4.0,0,0]
myArmaturePoseBone.rotation_quaternion=[4.0,4.0,0,0]
myArmaturePoseBone.scale=[4.0,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=4)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=4)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=4)
bpy.context.scene.frame_set(4).

        :param wyanimation_file_obj: File object opened for importing WYArmature object..
        :type  wyanimation_file_obj: File.
        :test  wyanimation_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0004.wyan','w+')asfile:
file.write("abnTestAnimationBoneName0004\nkf0{\nabh4.00.00.0\nabt0.00.00.0\nloc4.00.00.0\nrotq4.04.00.00.0\nsca4.00.00.0\n}\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (4.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (4.0,4.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (4.0,0.0,0.0)
        """
        myArmature = bpy.data.armatures.new("TestArmatureObject0004")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0004", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestAnimationBoneName0004")
        myArmatureBone.head = [4,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [4.0, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [4.0,4.0,0,0]
        myArmaturePoseBone.scale = [4.0, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=4)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=4)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=4)
        bpy.context.scene.frame_set(4)
        wyanimation = WYAnimation()
        wymodelmanager0004 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0004.wyan', 'w+') as file:
            file.write("abn TestAnimationBoneName0004\nkf 0 {\nabh 4.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 4.0 0.0 0.0\nrotq 4.0 4.0 0.0 0.0\nsca 4.0 0.0 0.0\n}\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0004.wyan') as content_file:
            wymodelmanager0004.import_wyanimationbone(wyanimation, content_file) 
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale)
        self.assertTrue(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (4.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (4.0,4.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (4.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyanimationbone_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimationbone function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimationBone objects are imported from given path "abn TestAnimationBoneName0005\nkf 0 {\nabh 5.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 5.0 0.0 0.0\nrotq 5.0 5.0 0.0 0.0\nsca 5.0 0.0 0.0\n}\n" through "import_wyanimationbone" function resulting the data values imported from file is equal to the expected value where animation bone is name "TestArmatureObject0005" location vector value[5,0,0], rotation quaternion value [5.0,5.0,0.0,0.0] and scale vector value [5,0,0] on keyframe 5 is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation: WYAnimation object to store the imported WYAnimationBone objects imported from same file..
        :type  wyanimation: WYAnimation.
        :test  wyanimation: myArmature=bpy.data.armatures.new("TestArmatureObject0005")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0005",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestAnimationBoneName0005")
myArmatureBone.head=[5,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[5.0,0,0]
myArmaturePoseBone.rotation_quaternion=[5.0,5.0,0,0]
myArmaturePoseBone.scale=[5.0,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=5)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=5)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=5)
bpy.context.scene.frame_set(5).

        :param wyanimation_file_obj: File object opened for importing WYArmature object..
        :type  wyanimation_file_obj: File.
        :test  wyanimation_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0005.wyan','w+')asfile:
file.write("abnTestAnimationBoneName0005\nkf0{\nabh5.00.00.0\nabt0.00.00.0\nloc5.00.00.0\nrotq5.05.00.00.0\nsca5.00.00.0\n}\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (5.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (5.0,5.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (5.0,0.0,0.0)
        """
        myArmature = bpy.data.armatures.new("TestArmatureObject0005")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0005", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestAnimationBoneName0005")
        myArmatureBone.head = [5,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [5.0, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [5.0,5.0,0,0]
        myArmaturePoseBone.scale = [5.0, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=5)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=5)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=5)
        bpy.context.scene.frame_set(5)
        wyanimation = WYAnimation()
        wymodelmanager0005 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0005.wyan', 'w+') as file:
            file.write("abn TestAnimationBoneName0005\nkf 0 {\nabh 5.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 5.0 0.0 0.0\nrotq 5.0 5.0 0.0 0.0\nsca 5.0 0.0 0.0\n}\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0005.wyan') as content_file:
            wymodelmanager0005.import_wyanimationbone(wyanimation, content_file) 
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale)
        self.assertTrue(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (5.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (5.0,5.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (5.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyanimationbone_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimationbone function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimationBone objects are imported from given path "abn TestAnimationBoneName0006\nkf 0 {\nabh 6.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 6.0 0.0 0.0\nrotq 6.0 6.0 0.0 0.0\nsca 6.0 0.0 0.0\n}\n" through "import_wyanimationbone" function resulting the data values imported from file is equal to the expected value where animation bone is name "TestArmatureObject0006" location vector value[6,0,0], rotation quaternion value [6.0,6.0,0.0,0.0] and scale vector value [6,0,0] on keyframe 6 is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation: WYAnimation object to store the imported WYAnimationBone objects imported from same file..
        :type  wyanimation: WYAnimation.
        :test  wyanimation: myArmature=bpy.data.armatures.new("TestArmatureObject0006")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0006",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestAnimationBoneName0006")
myArmatureBone.head=[6,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[6.0,0,0]
myArmaturePoseBone.rotation_quaternion=[6.0,6.0,0,0]
myArmaturePoseBone.scale=[6.0,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=6)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=6)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=6)
bpy.context.scene.frame_set(6).

        :param wyanimation_file_obj: File object opened for importing WYArmature object..
        :type  wyanimation_file_obj: File.
        :test  wyanimation_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0006.wyan','w+')asfile:
file.write("abnTestAnimationBoneName0006\nkf0{\nabh6.00.00.0\nabt0.00.00.0\nloc6.00.00.0\nrotq6.06.00.00.0\nsca6.00.00.0\n}\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (6.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (6.0,6.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (6.0,0.0,0.0)
        """
        myArmature = bpy.data.armatures.new("TestArmatureObject0006")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0006", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestAnimationBoneName0006")
        myArmatureBone.head = [6,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [6.0, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [6.0,6.0,0,0]
        myArmaturePoseBone.scale = [6.0, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=6)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=6)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=6)
        bpy.context.scene.frame_set(6)
        wyanimation = WYAnimation()
        wymodelmanager0006 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0006.wyan', 'w+') as file:
            file.write("abn TestAnimationBoneName0006\nkf 0 {\nabh 6.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 6.0 0.0 0.0\nrotq 6.0 6.0 0.0 0.0\nsca 6.0 0.0 0.0\n}\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0006.wyan') as content_file:
            wymodelmanager0006.import_wyanimationbone(wyanimation, content_file) 
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale)
        self.assertTrue(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (6.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (6.0,6.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (6.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyanimationbone_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimationbone function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimationBone objects are imported from given path "abn TestAnimationBoneName0007\nkf 0 {\nabh 7.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 7.0 0.0 0.0\nrotq 7.0 7.0 0.0 0.0\nsca 7.0 0.0 0.0\n}\n" through "import_wyanimationbone" function resulting the data values imported from file is equal to the expected value where animation bone is name "TestArmatureObject0007" location vector value[7,0,0], rotation quaternion value [7.0,7.0,0.0,0.0] and scale vector value [7,0,0] on keyframe 7 is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation: WYAnimation object to store the imported WYAnimationBone objects imported from same file..
        :type  wyanimation: WYAnimation.
        :test  wyanimation: myArmature=bpy.data.armatures.new("TestArmatureObject0007")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0007",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestAnimationBoneName0007")
myArmatureBone.head=[7,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[7.0,0,0]
myArmaturePoseBone.rotation_quaternion=[7.0,7.0,0,0]
myArmaturePoseBone.scale=[7.0,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=7)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=7)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=7)
bpy.context.scene.frame_set(7).

        :param wyanimation_file_obj: File object opened for importing WYArmature object..
        :type  wyanimation_file_obj: File.
        :test  wyanimation_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0007.wyan','w+')asfile:
file.write("abnTestAnimationBoneName0007\nkf0{\nabh7.00.00.0\nabt0.00.00.0\nloc7.00.00.0\nrotq7.07.00.00.0\nsca7.00.00.0\n}\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (7.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (7.0,7.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (7.0,0.0,0.0)
        """
        myArmature = bpy.data.armatures.new("TestArmatureObject0007")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0007", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestAnimationBoneName0007")
        myArmatureBone.head = [7,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [7.0, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [7.0,7.0,0,0]
        myArmaturePoseBone.scale = [7.0, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=7)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=7)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=7)
        bpy.context.scene.frame_set(7)
        wyanimation = WYAnimation()
        wymodelmanager0007 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0007.wyan', 'w+') as file:
            file.write("abn TestAnimationBoneName0007\nkf 0 {\nabh 7.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 7.0 0.0 0.0\nrotq 7.0 7.0 0.0 0.0\nsca 7.0 0.0 0.0\n}\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0007.wyan') as content_file:
            wymodelmanager0007.import_wyanimationbone(wyanimation, content_file) 
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale)
        self.assertTrue(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (7.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (7.0,7.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (7.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyanimationbone_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimationbone function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimationBone objects are imported from given path "abn TestAnimationBoneName0008\nkf 0 {\nabh 8.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 8.0 0.0 0.0\nrotq 8.0 8.0 0.0 0.0\nsca 8.0 0.0 0.0\n}\n" through "import_wyanimationbone" function resulting the data values imported from file is equal to the expected value where animation bone is name "TestArmatureObject0008" location vector value[8,0,0], rotation quaternion value [8.0,8.0,0.0,0.0] and scale vector value [8,0,0] on keyframe 8 is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation: WYAnimation object to store the imported WYAnimationBone objects imported from same file..
        :type  wyanimation: WYAnimation.
        :test  wyanimation: myArmature=bpy.data.armatures.new("TestArmatureObject0008")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0008",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestAnimationBoneName0008")
myArmatureBone.head=[8,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[8.0,0,0]
myArmaturePoseBone.rotation_quaternion=[8.0,8.0,0,0]
myArmaturePoseBone.scale=[8.0,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=8)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=8)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=8)
bpy.context.scene.frame_set(8).

        :param wyanimation_file_obj: File object opened for importing WYArmature object..
        :type  wyanimation_file_obj: File.
        :test  wyanimation_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0008.wyan','w+')asfile:
file.write("abnTestAnimationBoneName0008\nkf0{\nabh8.00.00.0\nabt0.00.00.0\nloc8.00.00.0\nrotq8.08.00.00.0\nsca8.00.00.0\n}\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (8.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (8.0,8.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (8.0,0.0,0.0)
        """
        myArmature = bpy.data.armatures.new("TestArmatureObject0008")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0008", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestAnimationBoneName0008")
        myArmatureBone.head = [8,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [8.0, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [8.0,8.0,0,0]
        myArmaturePoseBone.scale = [8.0, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=8)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=8)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=8)
        bpy.context.scene.frame_set(8)
        wyanimation = WYAnimation()
        wymodelmanager0008 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0008.wyan', 'w+') as file:
            file.write("abn TestAnimationBoneName0008\nkf 0 {\nabh 8.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 8.0 0.0 0.0\nrotq 8.0 8.0 0.0 0.0\nsca 8.0 0.0 0.0\n}\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0008.wyan') as content_file:
            wymodelmanager0008.import_wyanimationbone(wyanimation, content_file) 
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale)
        self.assertTrue(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (8.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (8.0,8.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (8.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyanimationbone_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimationbone function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimationBone objects are imported from given path "abn TestAnimationBoneName0009\nkf 0 {\nabh 9.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 9.0 0.0 0.0\nrotq 9.0 9.0 0.0 0.0\nsca 9.0 0.0 0.0\n}\n" through "import_wyanimationbone" function resulting the data values imported from file is equal to the expected value where animation bone is name "TestArmatureObject0009" location vector value[9,0,0], rotation quaternion value [9.0,9.0,0.0,0.0] and scale vector value [9,0,0] on keyframe 9 is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation: WYAnimation object to store the imported WYAnimationBone objects imported from same file..
        :type  wyanimation: WYAnimation.
        :test  wyanimation: myArmature=bpy.data.armatures.new("TestArmatureObject0009")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0009",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestAnimationBoneName0009")
myArmatureBone.head=[9,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[9.0,0,0]
myArmaturePoseBone.rotation_quaternion=[9.0,9.0,0,0]
myArmaturePoseBone.scale=[9.0,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=9)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=9)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=9)
bpy.context.scene.frame_set(9).

        :param wyanimation_file_obj: File object opened for importing WYArmature object..
        :type  wyanimation_file_obj: File.
        :test  wyanimation_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0009.wyan','w+')asfile:
file.write("abnTestAnimationBoneName0009\nkf0{\nabh9.00.00.0\nabt0.00.00.0\nloc9.00.00.0\nrotq9.09.00.00.0\nsca9.00.00.0\n}\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (9.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (9.0,9.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (9.0,0.0,0.0)
        """
        myArmature = bpy.data.armatures.new("TestArmatureObject0009")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0009", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestAnimationBoneName0009")
        myArmatureBone.head = [9,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [9.0, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [9.0,9.0,0,0]
        myArmaturePoseBone.scale = [9.0, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=9)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=9)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=9)
        bpy.context.scene.frame_set(9)
        wyanimation = WYAnimation()
        wymodelmanager0009 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0009.wyan', 'w+') as file:
            file.write("abn TestAnimationBoneName0009\nkf 0 {\nabh 9.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 9.0 0.0 0.0\nrotq 9.0 9.0 0.0 0.0\nsca 9.0 0.0 0.0\n}\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0009.wyan') as content_file:
            wymodelmanager0009.import_wyanimationbone(wyanimation, content_file) 
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale)
        self.assertTrue(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (9.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (9.0,9.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (9.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyanimationbone_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimationbone function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimationBone objects are imported from given path "abn TestAnimationBoneName0010\nkf 0 {\nabh 10.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 10.0 0.0 0.0\nrotq 10.0 10.0 0.0 0.0\nsca 10.0 0.0 0.0\n}\n" through "import_wyanimationbone" function resulting the data values imported from file is equal to the expected value where animation bone is name "TestArmatureObject0010" location vector value[10,0,0], rotation quaternion value [10.0,10.0,0.0,0.0] and scale vector value [10,0,0] on keyframe 10 is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation: WYAnimation object to store the imported WYAnimationBone objects imported from same file..
        :type  wyanimation: WYAnimation.
        :test  wyanimation: myArmature=bpy.data.armatures.new("TestArmatureObject0010")
myArmatureObject=bpy.data.objects.new("TestArmatureObject0010",myArmature)
bpy.context.scene.objects.link(myArmatureObject)
bpy.context.scene.objects.active=myArmatureObject
bpy.ops.object.mode_set(mode='EDIT')
myArmatureObject.select=True
myArmatureBone=myArmatureObject.data.edit_bones.new("TestAnimationBoneName0010")
myArmatureBone.head=[10,0,0]
myArmatureBone.tail=[0,0,0]
bpy.ops.object.mode_set(mode='OBJECT')
myArmaturePoseBone=myArmatureObject.pose.bones[myArmatureBone.name]
myArmaturePoseBone.location=[10.0,0,0]
myArmaturePoseBone.rotation_quaternion=[10.0,10.0,0,0]
myArmaturePoseBone.scale=[10.0,0,0]
myArmaturePoseBone.keyframe_insert(data_path='location',frame=10)
myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=10)
myArmaturePoseBone.keyframe_insert(data_path='scale',frame=10)
bpy.context.scene.frame_set(10).

        :param wyanimation_file_obj: File object opened for importing WYArmature object..
        :type  wyanimation_file_obj: File.
        :test  wyanimation_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0010.wyan','w+')asfile:
file.write("abnTestAnimationBoneName0010\nkf0{\nabh10.00.00.0\nabt0.00.00.0\nloc10.00.00.0\nrotq10.010.00.00.0\nsca10.00.00.0\n}\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (10.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (10.0,10.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (10.0,0.0,0.0)
        """
        myArmature = bpy.data.armatures.new("TestArmatureObject0010")
        myArmatureObject = bpy.data.objects.new("TestArmatureObject0010", myArmature)
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT')  
        myArmatureObject.select = True
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestAnimationBoneName0010")
        myArmatureBone.head = [10,0,0]
        myArmatureBone.tail = [0,0,0]
        bpy.ops.object.mode_set(mode='OBJECT')
        myArmaturePoseBone = myArmatureObject.pose.bones[myArmatureBone.name]
        myArmaturePoseBone.location = [10.0, 0, 0]
        myArmaturePoseBone.rotation_quaternion = [10.0,10.0,0,0]
        myArmaturePoseBone.scale = [10.0, 0, 0]
        myArmaturePoseBone.keyframe_insert(data_path='location',frame=10)
        myArmaturePoseBone.keyframe_insert(data_path='rotation_quaternion',frame=10)
        myArmaturePoseBone.keyframe_insert(data_path='scale',frame=10)
        bpy.context.scene.frame_set(10)
        wyanimation = WYAnimation()
        wymodelmanager0010 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0010.wyan', 'w+') as file:
            file.write("abn TestAnimationBoneName0010\nkf 0 {\nabh 10.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 10.0 0.0 0.0\nrotq 10.0 10.0 0.0 0.0\nsca 10.0 0.0 0.0\n}\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimationbone\\TestFile0010.wyan') as content_file:
            wymodelmanager0010.import_wyanimationbone(wyanimation, content_file) 
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion)
        print(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale)
        self.assertTrue(wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_location == (10.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_rotation_quaternion == (10.0,10.0,0.0,0.0) and wyanimation.animation_bones_arr[0].animation_bone_keyframe_arr[0].animation_bone_scale == (10.0,0.0,0.0))

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_import_wyanimationbone))
