"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2018-02-20
Last update                         : 2018-02-21
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_import_wyanimation\WYModelManagerTestCases_import_wyanimation.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_import_wyanimation\WYModelManagerTestCases_import_wyanimation.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : import_wyanimation(wyanimation_file)
Unit test case class name           : WYModelManagerTestCases_import_wyanimation
Unit test case description          : Unit test case for class WYModelManager import_wyanimation() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_import_wyanimation\WYModelManagerTestCaseResult_import_wyanimation.txt
"""
# Pre-condition: WYAnimation is tested.
# Pre-condition: WYAnimationBone is tested.
# Pre-condition: WYAnimationBoneKeyframe is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_import_wyanimation(unittest.TestCase):
    """
    Unit test case for class WYModelManager import_wyanimation() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_import_wyanimation_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimation function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimation object is imported from given path "ann TestArmatureObject0001\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0001\nkf 0 {\nabh 1.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 1.0 0.0 0.0\nrotq 1.0 1.0 0.0 0.0\nsca 1.0 0.0 0.0\n}\n" through "import_wyanimation" function resulting the data values imported from file is equal to the expected value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation_file: File path to import from..
        :type  wyanimation_file: String.
        :test  wyanimation_file: ..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0001.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: str(wyanimation) == str(wyanimationimported)
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
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0001"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myArmatureObject.pose, wyarmature, None)
        wyanimation.init_animation_data(1-1, 1)
        wymodelmanager0001 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0001.wyan', 'w+') as file:
            file.write("ann TestArmatureObject0001\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0001\nkf 0 {\nabh 1.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 1.0 0.0 0.0\nrotq 1.0 1.0 0.0 0.0\nsca 1.0 0.0 0.0\n}\n")
        wyanimationimported = wymodelmanager0001.import_wyanimation("..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0001.wyan")  
        self.assertTrue(str(wyanimation) == str(wyanimationimported))
    def test_WYModelManagerTestCase_import_wyanimation_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimation function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimation object is imported from given path "ann TestArmatureObject0002\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0002\nkf 0 {\nabh 2.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 2.0 0.0 0.0\nrotq 2.0 2.0 0.0 0.0\nsca 2.0 0.0 0.0\n}\n" through "import_wyanimation" function resulting the data values imported from file is equal to the expected value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation_file: File path to import from..
        :type  wyanimation_file: String.
        :test  wyanimation_file: ..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0002.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: str(wyanimation) == str(wyanimationimported)
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
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0002"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myArmatureObject.pose, wyarmature, None)
        wyanimation.init_animation_data(2-1, 2)
        wymodelmanager0002 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0002.wyan', 'w+') as file:
            file.write("ann TestArmatureObject0002\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0002\nkf 0 {\nabh 2.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 2.0 0.0 0.0\nrotq 2.0 2.0 0.0 0.0\nsca 2.0 0.0 0.0\n}\n")
        wyanimationimported = wymodelmanager0002.import_wyanimation("..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0002.wyan")  
        self.assertTrue(str(wyanimation) == str(wyanimationimported))
    def test_WYModelManagerTestCase_import_wyanimation_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimation function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimation object is imported from given path "ann TestArmatureObject0003\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0003\nkf 0 {\nabh 3.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 3.0 0.0 0.0\nrotq 3.0 3.0 0.0 0.0\nsca 3.0 0.0 0.0\n}\n" through "import_wyanimation" function resulting the data values imported from file is equal to the expected value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation_file: File path to import from..
        :type  wyanimation_file: String.
        :test  wyanimation_file: ..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0003.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: str(wyanimation) == str(wyanimationimported)
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
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0003"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myArmatureObject.pose, wyarmature, None)
        wyanimation.init_animation_data(3-1, 3)
        wymodelmanager0003 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0003.wyan', 'w+') as file:
            file.write("ann TestArmatureObject0003\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0003\nkf 0 {\nabh 3.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 3.0 0.0 0.0\nrotq 3.0 3.0 0.0 0.0\nsca 3.0 0.0 0.0\n}\n")
        wyanimationimported = wymodelmanager0003.import_wyanimation("..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0003.wyan")  
        self.assertTrue(str(wyanimation) == str(wyanimationimported))
    def test_WYModelManagerTestCase_import_wyanimation_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimation function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimation object is imported from given path "ann TestArmatureObject0004\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0004\nkf 0 {\nabh 4.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 4.0 0.0 0.0\nrotq 4.0 4.0 0.0 0.0\nsca 4.0 0.0 0.0\n}\n" through "import_wyanimation" function resulting the data values imported from file is equal to the expected value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation_file: File path to import from..
        :type  wyanimation_file: String.
        :test  wyanimation_file: ..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0004.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: str(wyanimation) == str(wyanimationimported)
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
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0004"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myArmatureObject.pose, wyarmature, None)
        wyanimation.init_animation_data(4-1, 4)
        wymodelmanager0004 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0004.wyan', 'w+') as file:
            file.write("ann TestArmatureObject0004\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0004\nkf 0 {\nabh 4.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 4.0 0.0 0.0\nrotq 4.0 4.0 0.0 0.0\nsca 4.0 0.0 0.0\n}\n")
        wyanimationimported = wymodelmanager0004.import_wyanimation("..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0004.wyan")  
        self.assertTrue(str(wyanimation) == str(wyanimationimported))
    def test_WYModelManagerTestCase_import_wyanimation_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimation function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimation object is imported from given path "ann TestArmatureObject0005\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0005\nkf 0 {\nabh 5.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 5.0 0.0 0.0\nrotq 5.0 5.0 0.0 0.0\nsca 5.0 0.0 0.0\n}\n" through "import_wyanimation" function resulting the data values imported from file is equal to the expected value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation_file: File path to import from..
        :type  wyanimation_file: String.
        :test  wyanimation_file: ..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0005.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: str(wyanimation) == str(wyanimationimported)
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
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0005"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myArmatureObject.pose, wyarmature, None)
        wyanimation.init_animation_data(5-1, 5)
        wymodelmanager0005 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0005.wyan', 'w+') as file:
            file.write("ann TestArmatureObject0005\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0005\nkf 0 {\nabh 5.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 5.0 0.0 0.0\nrotq 5.0 5.0 0.0 0.0\nsca 5.0 0.0 0.0\n}\n")
        wyanimationimported = wymodelmanager0005.import_wyanimation("..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0005.wyan")  
        self.assertTrue(str(wyanimation) == str(wyanimationimported))
    def test_WYModelManagerTestCase_import_wyanimation_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimation function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimation object is imported from given path "ann TestArmatureObject0006\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0006\nkf 0 {\nabh 6.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 6.0 0.0 0.0\nrotq 6.0 6.0 0.0 0.0\nsca 6.0 0.0 0.0\n}\n" through "import_wyanimation" function resulting the data values imported from file is equal to the expected value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation_file: File path to import from..
        :type  wyanimation_file: String.
        :test  wyanimation_file: ..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0006.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: str(wyanimation) == str(wyanimationimported)
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
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0006"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myArmatureObject.pose, wyarmature, None)
        wyanimation.init_animation_data(6-1, 6)
        wymodelmanager0006 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0006.wyan', 'w+') as file:
            file.write("ann TestArmatureObject0006\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0006\nkf 0 {\nabh 6.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 6.0 0.0 0.0\nrotq 6.0 6.0 0.0 0.0\nsca 6.0 0.0 0.0\n}\n")
        wyanimationimported = wymodelmanager0006.import_wyanimation("..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0006.wyan")  
        self.assertTrue(str(wyanimation) == str(wyanimationimported))
    def test_WYModelManagerTestCase_import_wyanimation_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimation function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimation object is imported from given path "ann TestArmatureObject0007\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0007\nkf 0 {\nabh 7.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 7.0 0.0 0.0\nrotq 7.0 7.0 0.0 0.0\nsca 7.0 0.0 0.0\n}\n" through "import_wyanimation" function resulting the data values imported from file is equal to the expected value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation_file: File path to import from..
        :type  wyanimation_file: String.
        :test  wyanimation_file: ..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0007.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: str(wyanimation) == str(wyanimationimported)
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
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0007"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myArmatureObject.pose, wyarmature, None)
        wyanimation.init_animation_data(7-1, 7)
        wymodelmanager0007 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0007.wyan', 'w+') as file:
            file.write("ann TestArmatureObject0007\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0007\nkf 0 {\nabh 7.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 7.0 0.0 0.0\nrotq 7.0 7.0 0.0 0.0\nsca 7.0 0.0 0.0\n}\n")
        wyanimationimported = wymodelmanager0007.import_wyanimation("..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0007.wyan")  
        self.assertTrue(str(wyanimation) == str(wyanimationimported))
    def test_WYModelManagerTestCase_import_wyanimation_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimation function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimation object is imported from given path "ann TestArmatureObject0008\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0008\nkf 0 {\nabh 8.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 8.0 0.0 0.0\nrotq 8.0 8.0 0.0 0.0\nsca 8.0 0.0 0.0\n}\n" through "import_wyanimation" function resulting the data values imported from file is equal to the expected value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation_file: File path to import from..
        :type  wyanimation_file: String.
        :test  wyanimation_file: ..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0008.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: str(wyanimation) == str(wyanimationimported)
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
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0008"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myArmatureObject.pose, wyarmature, None)
        wyanimation.init_animation_data(8-1, 8)
        wymodelmanager0008 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0008.wyan', 'w+') as file:
            file.write("ann TestArmatureObject0008\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0008\nkf 0 {\nabh 8.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 8.0 0.0 0.0\nrotq 8.0 8.0 0.0 0.0\nsca 8.0 0.0 0.0\n}\n")
        wyanimationimported = wymodelmanager0008.import_wyanimation("..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0008.wyan")  
        self.assertTrue(str(wyanimation) == str(wyanimationimported))
    def test_WYModelManagerTestCase_import_wyanimation_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimation function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimation object is imported from given path "ann TestArmatureObject0009\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0009\nkf 0 {\nabh 9.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 9.0 0.0 0.0\nrotq 9.0 9.0 0.0 0.0\nsca 9.0 0.0 0.0\n}\n" through "import_wyanimation" function resulting the data values imported from file is equal to the expected value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation_file: File path to import from..
        :type  wyanimation_file: String.
        :test  wyanimation_file: ..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0009.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: str(wyanimation) == str(wyanimationimported)
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
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0009"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myArmatureObject.pose, wyarmature, None)
        wyanimation.init_animation_data(9-1, 9)
        wymodelmanager0009 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0009.wyan', 'w+') as file:
            file.write("ann TestArmatureObject0009\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0009\nkf 0 {\nabh 9.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 9.0 0.0 0.0\nrotq 9.0 9.0 0.0 0.0\nsca 9.0 0.0 0.0\n}\n")
        wyanimationimported = wymodelmanager0009.import_wyanimation("..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0009.wyan")  
        self.assertTrue(str(wyanimation) == str(wyanimationimported))
    def test_WYModelManagerTestCase_import_wyanimation_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyanimation function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYAnimation object is imported from given path "ann TestArmatureObject0010\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0010\nkf 0 {\nabh 10.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 10.0 0.0 0.0\nrotq 10.0 10.0 0.0 0.0\nsca 10.0 0.0 0.0\n}\n" through "import_wyanimation" function resulting the data values imported from file is equal to the expected value.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyanimation_file: File path to import from..
        :type  wyanimation_file: String.
        :test  wyanimation_file: ..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0010.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: str(wyanimation) == str(wyanimationimported)
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
        wyarmature = WYArmature(bpy.data.objects["TestArmatureObject0010"], None, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wyarmature.init_armature_data()
        wyanimation = WYAnimation(myArmatureObject.pose, wyarmature, None)
        wyanimation.init_animation_data(10-1, 10)
        wymodelmanager0010 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0010.wyan', 'w+') as file:
            file.write("ann TestArmatureObject0010\nabc 1\nCU Z\nCF Y\nabn TestAnimationBoneName0010\nkf 0 {\nabh 10.0 0.0 0.0\nabt 0.0 0.0 0.0\nloc 10.0 0.0 0.0\nrotq 10.0 10.0 0.0 0.0\nsca 10.0 0.0 0.0\n}\n")
        wyanimationimported = wymodelmanager0010.import_wyanimation("..\\..\\test\\WYModelManagerTestCases_import_wyanimation\\TestFile0010.wyan")  
        self.assertTrue(str(wyanimation) == str(wyanimationimported))

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_import_wyanimation))
