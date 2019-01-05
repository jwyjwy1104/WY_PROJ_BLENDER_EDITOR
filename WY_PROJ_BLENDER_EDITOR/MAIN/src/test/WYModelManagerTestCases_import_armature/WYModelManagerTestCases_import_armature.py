"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2018-01-23
Last update                         : 2018-01-23
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_import_armature\WYModelManagerTestCases_import_armature.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_import_armature\WYModelManagerTestCases_import_armature.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : import_armature(armature_file_path)
Unit test case class name           : WYModelManagerTestCases_import_armature
Unit test case description          : Unit test case for class WYModelManager import_armature() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_import_armature\WYModelManagerTestCaseResult_import_armature.txt
"""
# Pre-condition: WYArmature is tested.
# Pre-condition: WYArmatureBone is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_import_armature(unittest.TestCase):
    """
    Unit test case for class WYModelManager import_armature() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :252
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_import_armature_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0001" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0001.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0001"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0001" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0001 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0001.wya', 'w+') as file:
            file.write("an TestArmatureObject0001\nmdllib TestModelFile0001\nbc 1\nbn TestArmatureBoneName0001\nbh 1 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0001.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0001.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0001")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0001" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0002" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0002.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0002"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0002" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.1, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0002 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0002.wya', 'w+') as file:
            file.write("an TestArmatureObject0002\nmdllib TestModelFile0002\nbc 1\nbn TestArmatureBoneName0002\nbh 0.1 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0002.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0002.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0002")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0002" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.1, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0003" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0003.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0003"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0003" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.001, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0003 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0003.wya', 'w+') as file:
            file.write("an TestArmatureObject0003\nmdllib TestModelFile0003\nbc 1\nbn TestArmatureBoneName0003\nbh 0.001 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0003.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0003.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0003")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0003" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.001, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0004" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0004.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0004"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0004" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0001, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0004 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0004.wya', 'w+') as file:
            file.write("an TestArmatureObject0004\nmdllib TestModelFile0004\nbc 1\nbn TestArmatureBoneName0004\nbh 0.0001 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0004.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0004.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0004")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0004" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0001, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0005" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0005.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0005"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0005" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0005 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0005.wya', 'w+') as file:
            file.write("an TestArmatureObject0005\nmdllib TestModelFile0005\nbc 1\nbn TestArmatureBoneName0005\nbh 2 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0005.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0005.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0005")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0005" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0006" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0006.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0006"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0006" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0006 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0006.wya', 'w+') as file:
            file.write("an TestArmatureObject0006\nmdllib TestModelFile0006\nbc 1\nbn TestArmatureBoneName0006\nbh 3 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0006.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0006.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0006")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0006" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0007" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0007.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0007"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0007" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0007 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0007.wya', 'w+') as file:
            file.write("an TestArmatureObject0007\nmdllib TestModelFile0007\nbc 1\nbn TestArmatureBoneName0007\nbh 10 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0007.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0007.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0007")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0007" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0008" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0008.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0008"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0008" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0008 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0008.wya', 'w+') as file:
            file.write("an TestArmatureObject0008\nmdllib TestModelFile0008\nbc 1\nbn TestArmatureBoneName0008\nbh 20 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0008.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0008.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0008")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0008" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0009" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0009.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0009"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0009" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0009 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0009.wya', 'w+') as file:
            file.write("an TestArmatureObject0009\nmdllib TestModelFile0009\nbc 1\nbn TestArmatureBoneName0009\nbh 30 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0009.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0009.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0009")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0009" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0010" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0010.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0010"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0010" and wyarmature.main_armature_obj.data.bones[0].head == Vector((100, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0010 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0010.wya', 'w+') as file:
            file.write("an TestArmatureObject0010\nmdllib TestModelFile0010\nbc 1\nbn TestArmatureBoneName0010\nbh 100 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0010.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0010.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0010")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0010" and wyarmature.main_armature_obj.data.bones[0].head == Vector((100, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0011(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0011

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0011" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0011.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0011"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0011" and wyarmature.main_armature_obj.data.bones[0].head == Vector((200, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0011 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0011.wya', 'w+') as file:
            file.write("an TestArmatureObject0011\nmdllib TestModelFile0011\nbc 1\nbn TestArmatureBoneName0011\nbh 200 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0011.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0011.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0011")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0011" and wyarmature.main_armature_obj.data.bones[0].head == Vector((200, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0012(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0012

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0012" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0012.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0012"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0012" and wyarmature.main_armature_obj.data.bones[0].head == Vector((300, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0012 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0012.wya', 'w+') as file:
            file.write("an TestArmatureObject0012\nmdllib TestModelFile0012\nbc 1\nbn TestArmatureBoneName0012\nbh 300 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0012.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0012.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0012")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0012" and wyarmature.main_armature_obj.data.bones[0].head == Vector((300, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0013(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0013

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0013" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0013.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0013"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0013" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10000, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0013 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0013.wya', 'w+') as file:
            file.write("an TestArmatureObject0013\nmdllib TestModelFile0013\nbc 1\nbn TestArmatureBoneName0013\nbh 10000 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0013.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0013.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0013")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0013" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10000, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0014(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0014

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0014" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0014.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0014"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0014" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20000, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0014 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0014.wya', 'w+') as file:
            file.write("an TestArmatureObject0014\nmdllib TestModelFile0014\nbc 1\nbn TestArmatureBoneName0014\nbh 20000 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0014.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0014.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0014")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0014" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20000, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0015(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0015

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0015" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0015.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0015"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0015" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30000, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0015 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0015.wya', 'w+') as file:
            file.write("an TestArmatureObject0015\nmdllib TestModelFile0015\nbc 1\nbn TestArmatureBoneName0015\nbh 30000 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0015.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0015.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0015")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0015" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30000, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0016(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0016

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0016" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0016.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0016"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0016" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1000000, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0016 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0016.wya', 'w+') as file:
            file.write("an TestArmatureObject0016\nmdllib TestModelFile0016\nbc 1\nbn TestArmatureBoneName0016\nbh 1000000 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0016.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0016.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0016")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0016" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1000000, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0017(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0017

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0017" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0017.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0017"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0017" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2000000, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0017 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0017.wya', 'w+') as file:
            file.write("an TestArmatureObject0017\nmdllib TestModelFile0017\nbc 1\nbn TestArmatureBoneName0017\nbh 2000000 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0017.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0017.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0017")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0017" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2000000, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0018(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0018

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0018" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0018.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0018"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0018" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3000000, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0018 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0018.wya', 'w+') as file:
            file.write("an TestArmatureObject0018\nmdllib TestModelFile0018\nbc 1\nbn TestArmatureBoneName0018\nbh 3000000 0.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0018.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0018.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0018")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0018" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3000000, 0, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0019(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0019

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0019" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0019.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0019"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0019" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 1, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0019 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0019.wya', 'w+') as file:
            file.write("an TestArmatureObject0019\nmdllib TestModelFile0019\nbc 1\nbn TestArmatureBoneName0019\nbh 0 1.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0019.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0019.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0019")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0019" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 1, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0020(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0020

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0020" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0020.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0020"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0020" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0.1, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0020 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0020.wya', 'w+') as file:
            file.write("an TestArmatureObject0020\nmdllib TestModelFile0020\nbc 1\nbn TestArmatureBoneName0020\nbh 0 0.1 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0020.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0020.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0020")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0020" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0.1, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0021(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0021

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0021" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0021.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0021"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0021" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0.001, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0021 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0021.wya', 'w+') as file:
            file.write("an TestArmatureObject0021\nmdllib TestModelFile0021\nbc 1\nbn TestArmatureBoneName0021\nbh 0 0.001 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0021.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0021.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0021")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0021" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0.001, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0022(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0022

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0022" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0022.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0022"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0022" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0.0001, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0022 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0022.wya', 'w+') as file:
            file.write("an TestArmatureObject0022\nmdllib TestModelFile0022\nbc 1\nbn TestArmatureBoneName0022\nbh 0 0.0001 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0022.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0022.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0022")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0022" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0.0001, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0023(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0023

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0023" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0023.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0023"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0023" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 2, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0023 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0023.wya', 'w+') as file:
            file.write("an TestArmatureObject0023\nmdllib TestModelFile0023\nbc 1\nbn TestArmatureBoneName0023\nbh 0 2.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0023.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0023.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0023")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0023" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 2, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0024(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0024

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0024" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0024.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0024"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0024" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 3, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0024 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0024.wya', 'w+') as file:
            file.write("an TestArmatureObject0024\nmdllib TestModelFile0024\nbc 1\nbn TestArmatureBoneName0024\nbh 0 3.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0024.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0024.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0024")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0024" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 3, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0025(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0025

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0025" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0025.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0025"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0025" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 10, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0025 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0025.wya', 'w+') as file:
            file.write("an TestArmatureObject0025\nmdllib TestModelFile0025\nbc 1\nbn TestArmatureBoneName0025\nbh 0 10.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0025.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0025.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0025")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0025" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 10, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0026(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0026

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0026" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0026.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0026"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0026" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 20, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0026 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0026.wya', 'w+') as file:
            file.write("an TestArmatureObject0026\nmdllib TestModelFile0026\nbc 1\nbn TestArmatureBoneName0026\nbh 0 20.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0026.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0026.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0026")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0026" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 20, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0027(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0027

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0027" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0027.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0027"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0027" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 30, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0027 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0027.wya', 'w+') as file:
            file.write("an TestArmatureObject0027\nmdllib TestModelFile0027\nbc 1\nbn TestArmatureBoneName0027\nbh 0 30.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0027.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0027.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0027")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0027" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 30, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0028(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0028

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0028" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0028.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0028"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0028" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 100, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0028 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0028.wya', 'w+') as file:
            file.write("an TestArmatureObject0028\nmdllib TestModelFile0028\nbc 1\nbn TestArmatureBoneName0028\nbh 0 100.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0028.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0028.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0028")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0028" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 100, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0029(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0029

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0029" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0029.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0029"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0029" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 200, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0029 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0029.wya', 'w+') as file:
            file.write("an TestArmatureObject0029\nmdllib TestModelFile0029\nbc 1\nbn TestArmatureBoneName0029\nbh 0 200.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0029.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0029.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0029")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0029" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 200, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0030(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0030

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0030" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0030.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0030"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0030" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 300, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0030 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0030.wya', 'w+') as file:
            file.write("an TestArmatureObject0030\nmdllib TestModelFile0030\nbc 1\nbn TestArmatureBoneName0030\nbh 0 300.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0030.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0030.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0030")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0030" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 300, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0031(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0031

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0031" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0031.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0031"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0031" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 10000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0031 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0031.wya', 'w+') as file:
            file.write("an TestArmatureObject0031\nmdllib TestModelFile0031\nbc 1\nbn TestArmatureBoneName0031\nbh 0 10000.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0031.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0031.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0031")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0031" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 10000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0032(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0032

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0032" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0032.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0032"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0032" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 20000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0032 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0032.wya', 'w+') as file:
            file.write("an TestArmatureObject0032\nmdllib TestModelFile0032\nbc 1\nbn TestArmatureBoneName0032\nbh 0 20000.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0032.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0032.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0032")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0032" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 20000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0033(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0033

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0033" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0033.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0033"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0033" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 30000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0033 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0033.wya', 'w+') as file:
            file.write("an TestArmatureObject0033\nmdllib TestModelFile0033\nbc 1\nbn TestArmatureBoneName0033\nbh 0 30000.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0033.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0033.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0033")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0033" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 30000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0034(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0034

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0034" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0034.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0034"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0034" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 1000000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0034 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0034.wya', 'w+') as file:
            file.write("an TestArmatureObject0034\nmdllib TestModelFile0034\nbc 1\nbn TestArmatureBoneName0034\nbh 0 1000000.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0034.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0034.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0034")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0034" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 1000000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0035(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0035

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0035" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0035.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0035"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0035" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 2000000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0035 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0035.wya', 'w+') as file:
            file.write("an TestArmatureObject0035\nmdllib TestModelFile0035\nbc 1\nbn TestArmatureBoneName0035\nbh 0 2000000.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0035.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0035.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0035")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0035" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 2000000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0036(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0036

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0036" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0036.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0036"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0036" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 3000000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0036 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0036.wya', 'w+') as file:
            file.write("an TestArmatureObject0036\nmdllib TestModelFile0036\nbc 1\nbn TestArmatureBoneName0036\nbh 0 3000000.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0036.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0036.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0036")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0036" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 3000000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0037(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0037

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0037" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0037.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0037"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0037" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0037 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0037.wya', 'w+') as file:
            file.write("an TestArmatureObject0037\nmdllib TestModelFile0037\nbc 1\nbn TestArmatureBoneName0037\nbh 0 0.0 1\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0037.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0037.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0037")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0037" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0038(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0038

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0038" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0038.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0038"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0038" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 0.1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0038 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0038.wya', 'w+') as file:
            file.write("an TestArmatureObject0038\nmdllib TestModelFile0038\nbc 1\nbn TestArmatureBoneName0038\nbh 0 0.0 0.1\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0038.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0038.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0038")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0038" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 0.1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0039(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0039

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0039" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0039.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0039"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0039" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 0.001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0039 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0039.wya', 'w+') as file:
            file.write("an TestArmatureObject0039\nmdllib TestModelFile0039\nbc 1\nbn TestArmatureBoneName0039\nbh 0 0.0 0.001\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0039.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0039.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0039")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0039" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 0.001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0040(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0040

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0040" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0040.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0040"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0040" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 0.0001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0040 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0040.wya', 'w+') as file:
            file.write("an TestArmatureObject0040\nmdllib TestModelFile0040\nbc 1\nbn TestArmatureBoneName0040\nbh 0 0.0 0.0001\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0040.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0040.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0040")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0040" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 0.0001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0041(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0041

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0041" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0041.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0041"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0041" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 2)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0041 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0041.wya', 'w+') as file:
            file.write("an TestArmatureObject0041\nmdllib TestModelFile0041\nbc 1\nbn TestArmatureBoneName0041\nbh 0 0.0 2\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0041.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0041.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0041")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0041" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 2)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0042(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0042

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0042" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0042.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0042"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0042" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 3)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0042 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0042.wya', 'w+') as file:
            file.write("an TestArmatureObject0042\nmdllib TestModelFile0042\nbc 1\nbn TestArmatureBoneName0042\nbh 0 0.0 3\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0042.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0042.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0042")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0042" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 3)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0043(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0043

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0043" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0043.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0043"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0043" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 10)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0043 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0043.wya', 'w+') as file:
            file.write("an TestArmatureObject0043\nmdllib TestModelFile0043\nbc 1\nbn TestArmatureBoneName0043\nbh 0 0.0 10\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0043.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0043.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0043")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0043" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 10)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0044(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0044

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0044" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0044.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0044"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0044" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 20)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0044 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0044.wya', 'w+') as file:
            file.write("an TestArmatureObject0044\nmdllib TestModelFile0044\nbc 1\nbn TestArmatureBoneName0044\nbh 0 0.0 20\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0044.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0044.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0044")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0044" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 20)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0045(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0045

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0045" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0045.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0045"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0045" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 30)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0045 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0045.wya', 'w+') as file:
            file.write("an TestArmatureObject0045\nmdllib TestModelFile0045\nbc 1\nbn TestArmatureBoneName0045\nbh 0 0.0 30\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0045.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0045.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0045")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0045" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 30)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0046(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0046

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0046" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0046.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0046"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0046" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 100)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0046 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0046.wya', 'w+') as file:
            file.write("an TestArmatureObject0046\nmdllib TestModelFile0046\nbc 1\nbn TestArmatureBoneName0046\nbh 0 0.0 100\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0046.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0046.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0046")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0046" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 100)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0047(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0047

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0047" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0047.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0047"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0047" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 200)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0047 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0047.wya', 'w+') as file:
            file.write("an TestArmatureObject0047\nmdllib TestModelFile0047\nbc 1\nbn TestArmatureBoneName0047\nbh 0 0.0 200\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0047.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0047.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0047")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0047" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 200)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0048(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0048

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0048" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0048.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0048"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0048" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 300)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0048 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0048.wya', 'w+') as file:
            file.write("an TestArmatureObject0048\nmdllib TestModelFile0048\nbc 1\nbn TestArmatureBoneName0048\nbh 0 0.0 300\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0048.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0048.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0048")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0048" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 300)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0049(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0049

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0049" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0049.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0049"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0049" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 10000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0049 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0049.wya', 'w+') as file:
            file.write("an TestArmatureObject0049\nmdllib TestModelFile0049\nbc 1\nbn TestArmatureBoneName0049\nbh 0 0.0 10000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0049.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0049.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0049")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0049" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 10000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0050(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0050

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0050" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0050.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0050"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0050" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 20000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0050 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0050.wya', 'w+') as file:
            file.write("an TestArmatureObject0050\nmdllib TestModelFile0050\nbc 1\nbn TestArmatureBoneName0050\nbh 0 0.0 20000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0050.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0050.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0050")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0050" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 20000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0051(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0051

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0051" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0051.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0051"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0051" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 30000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0051 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0051.wya', 'w+') as file:
            file.write("an TestArmatureObject0051\nmdllib TestModelFile0051\nbc 1\nbn TestArmatureBoneName0051\nbh 0 0.0 30000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0051.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0051.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0051")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0051" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 30000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0052(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0052

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0052" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0052.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0052"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0052" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 1000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0052 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0052.wya', 'w+') as file:
            file.write("an TestArmatureObject0052\nmdllib TestModelFile0052\nbc 1\nbn TestArmatureBoneName0052\nbh 0 0.0 1000000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0052.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0052.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0052")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0052" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 1000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0053(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0053

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0053" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0053.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0053"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0053" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 2000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0053 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0053.wya', 'w+') as file:
            file.write("an TestArmatureObject0053\nmdllib TestModelFile0053\nbc 1\nbn TestArmatureBoneName0053\nbh 0 0.0 2000000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0053.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0053.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0053")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0053" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 2000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0054(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0054

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0054" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0054.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0054"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0054" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 3000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0054 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0054.wya', 'w+') as file:
            file.write("an TestArmatureObject0054\nmdllib TestModelFile0054\nbc 1\nbn TestArmatureBoneName0054\nbh 0 0.0 3000000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0054.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0054.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0054")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0054" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0, 3000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0055(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0055

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0055" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0055.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0055"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0055" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1, 1, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0055 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0055.wya', 'w+') as file:
            file.write("an TestArmatureObject0055\nmdllib TestModelFile0055\nbc 1\nbn TestArmatureBoneName0055\nbh 1 1.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0055.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0055.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0055")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0055" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1, 1, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0056(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0056

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0056" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0056.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0056"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0056" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.1, 0.1, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0056 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0056.wya', 'w+') as file:
            file.write("an TestArmatureObject0056\nmdllib TestModelFile0056\nbc 1\nbn TestArmatureBoneName0056\nbh 0.1 0.1 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0056.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0056.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0056")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0056" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.1, 0.1, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0057(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0057

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0057" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0057.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0057"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0057" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.001, 0.001, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0057 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0057.wya', 'w+') as file:
            file.write("an TestArmatureObject0057\nmdllib TestModelFile0057\nbc 1\nbn TestArmatureBoneName0057\nbh 0.001 0.001 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0057.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0057.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0057")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0057" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.001, 0.001, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0058(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0058

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0058" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0058.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0058"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0058" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0001, 0.0001, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0058 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0058.wya', 'w+') as file:
            file.write("an TestArmatureObject0058\nmdllib TestModelFile0058\nbc 1\nbn TestArmatureBoneName0058\nbh 0.0001 0.0001 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0058.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0058.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0058")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0058" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0001, 0.0001, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0059(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0059

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0059" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0059.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0059"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0059" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2, 2, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0059 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0059.wya', 'w+') as file:
            file.write("an TestArmatureObject0059\nmdllib TestModelFile0059\nbc 1\nbn TestArmatureBoneName0059\nbh 2 2.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0059.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0059.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0059")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0059" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2, 2, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0060(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0060

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0060" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0060.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0060"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0060" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3, 3, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0060 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0060.wya', 'w+') as file:
            file.write("an TestArmatureObject0060\nmdllib TestModelFile0060\nbc 1\nbn TestArmatureBoneName0060\nbh 3 3.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0060.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0060.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0060")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0060" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3, 3, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0061(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0061

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0061" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0061.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0061"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0061" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10, 10, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0061 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0061.wya', 'w+') as file:
            file.write("an TestArmatureObject0061\nmdllib TestModelFile0061\nbc 1\nbn TestArmatureBoneName0061\nbh 10 10.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0061.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0061.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0061")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0061" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10, 10, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0062(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0062

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0062" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0062.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0062"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0062" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20, 20, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0062 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0062.wya', 'w+') as file:
            file.write("an TestArmatureObject0062\nmdllib TestModelFile0062\nbc 1\nbn TestArmatureBoneName0062\nbh 20 20.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0062.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0062.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0062")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0062" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20, 20, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0063(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0063

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0063" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0063.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0063"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0063" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30, 30, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0063 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0063.wya', 'w+') as file:
            file.write("an TestArmatureObject0063\nmdllib TestModelFile0063\nbc 1\nbn TestArmatureBoneName0063\nbh 30 30.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0063.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0063.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0063")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0063" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30, 30, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0064(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0064

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0064" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0064.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0064"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0064" and wyarmature.main_armature_obj.data.bones[0].head == Vector((100, 100, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0064 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0064.wya', 'w+') as file:
            file.write("an TestArmatureObject0064\nmdllib TestModelFile0064\nbc 1\nbn TestArmatureBoneName0064\nbh 100 100.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0064.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0064.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0064")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0064" and wyarmature.main_armature_obj.data.bones[0].head == Vector((100, 100, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0065(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0065

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0065" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0065.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0065"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0065" and wyarmature.main_armature_obj.data.bones[0].head == Vector((200, 200, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0065 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0065.wya', 'w+') as file:
            file.write("an TestArmatureObject0065\nmdllib TestModelFile0065\nbc 1\nbn TestArmatureBoneName0065\nbh 200 200.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0065.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0065.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0065")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0065" and wyarmature.main_armature_obj.data.bones[0].head == Vector((200, 200, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0066(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0066

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0066" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0066.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0066"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0066" and wyarmature.main_armature_obj.data.bones[0].head == Vector((300, 300, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0066 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0066.wya', 'w+') as file:
            file.write("an TestArmatureObject0066\nmdllib TestModelFile0066\nbc 1\nbn TestArmatureBoneName0066\nbh 300 300.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0066.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0066.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0066")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0066" and wyarmature.main_armature_obj.data.bones[0].head == Vector((300, 300, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0067(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0067

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0067" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0067.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0067"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0067" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10000, 10000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0067 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0067.wya', 'w+') as file:
            file.write("an TestArmatureObject0067\nmdllib TestModelFile0067\nbc 1\nbn TestArmatureBoneName0067\nbh 10000 10000.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0067.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0067.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0067")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0067" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10000, 10000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0068(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0068

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0068" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0068.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0068"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0068" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20000, 20000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0068 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0068.wya', 'w+') as file:
            file.write("an TestArmatureObject0068\nmdllib TestModelFile0068\nbc 1\nbn TestArmatureBoneName0068\nbh 20000 20000.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0068.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0068.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0068")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0068" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20000, 20000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0069(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0069

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0069" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0069.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0069"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0069" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30000, 30000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0069 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0069.wya', 'w+') as file:
            file.write("an TestArmatureObject0069\nmdllib TestModelFile0069\nbc 1\nbn TestArmatureBoneName0069\nbh 30000 30000.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0069.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0069.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0069")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0069" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30000, 30000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0070(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0070

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0070" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0070.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0070"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0070" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1000000, 1000000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0070 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0070.wya', 'w+') as file:
            file.write("an TestArmatureObject0070\nmdllib TestModelFile0070\nbc 1\nbn TestArmatureBoneName0070\nbh 1000000 1000000.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0070.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0070.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0070")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0070" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1000000, 1000000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0071(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0071

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0071" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0071.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0071"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0071" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2000000, 2000000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0071 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0071.wya', 'w+') as file:
            file.write("an TestArmatureObject0071\nmdllib TestModelFile0071\nbc 1\nbn TestArmatureBoneName0071\nbh 2000000 2000000.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0071.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0071.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0071")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0071" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2000000, 2000000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0072(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0072

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0072" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0072.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0072"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0072" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3000000, 3000000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0072 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0072.wya', 'w+') as file:
            file.write("an TestArmatureObject0072\nmdllib TestModelFile0072\nbc 1\nbn TestArmatureBoneName0072\nbh 3000000 3000000.0 0\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0072.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0072.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0072")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0072" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3000000, 3000000, 0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0073(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0073

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0073" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0073.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0073"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0073" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1, 0, 1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0073 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0073.wya', 'w+') as file:
            file.write("an TestArmatureObject0073\nmdllib TestModelFile0073\nbc 1\nbn TestArmatureBoneName0073\nbh 1 0.0 1\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0073.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0073.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0073")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0073" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1, 0, 1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0074(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0074

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0074" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0074.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0074"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0074" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.1, 0, 0.1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0074 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0074.wya', 'w+') as file:
            file.write("an TestArmatureObject0074\nmdllib TestModelFile0074\nbc 1\nbn TestArmatureBoneName0074\nbh 0.1 0.0 0.1\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0074.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0074.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0074")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0074" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.1, 0, 0.1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0075(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0075

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0075" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0075.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0075"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0075" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.001, 0, 0.001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0075 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0075.wya', 'w+') as file:
            file.write("an TestArmatureObject0075\nmdllib TestModelFile0075\nbc 1\nbn TestArmatureBoneName0075\nbh 0.001 0.0 0.001\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0075.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0075.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0075")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0075" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.001, 0, 0.001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0076(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0076

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0076" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0076.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0076"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0076" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0001, 0, 0.0001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0076 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0076.wya', 'w+') as file:
            file.write("an TestArmatureObject0076\nmdllib TestModelFile0076\nbc 1\nbn TestArmatureBoneName0076\nbh 0.0001 0.0 0.0001\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0076.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0076.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0076")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0076" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0001, 0, 0.0001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0077(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0077

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0077" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0077.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0077"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0077" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2, 0, 2)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0077 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0077.wya', 'w+') as file:
            file.write("an TestArmatureObject0077\nmdllib TestModelFile0077\nbc 1\nbn TestArmatureBoneName0077\nbh 2 0.0 2\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0077.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0077.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0077")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0077" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2, 0, 2)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0078(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0078

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0078" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0078.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0078"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0078" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3, 0, 3)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0078 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0078.wya', 'w+') as file:
            file.write("an TestArmatureObject0078\nmdllib TestModelFile0078\nbc 1\nbn TestArmatureBoneName0078\nbh 3 0.0 3\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0078.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0078.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0078")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0078" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3, 0, 3)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0079(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0079

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0079" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0079.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0079"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0079" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10, 0, 10)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0079 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0079.wya', 'w+') as file:
            file.write("an TestArmatureObject0079\nmdllib TestModelFile0079\nbc 1\nbn TestArmatureBoneName0079\nbh 10 0.0 10\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0079.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0079.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0079")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0079" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10, 0, 10)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0080(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0080

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0080" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0080.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0080"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0080" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20, 0, 20)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0080 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0080.wya', 'w+') as file:
            file.write("an TestArmatureObject0080\nmdllib TestModelFile0080\nbc 1\nbn TestArmatureBoneName0080\nbh 20 0.0 20\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0080.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0080.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0080")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0080" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20, 0, 20)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0081(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0081

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0081" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0081.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0081"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0081" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30, 0, 30)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0081 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0081.wya', 'w+') as file:
            file.write("an TestArmatureObject0081\nmdllib TestModelFile0081\nbc 1\nbn TestArmatureBoneName0081\nbh 30 0.0 30\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0081.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0081.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0081")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0081" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30, 0, 30)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0082(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0082

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0082" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0082.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0082"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0082" and wyarmature.main_armature_obj.data.bones[0].head == Vector((100, 0, 100)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0082 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0082.wya', 'w+') as file:
            file.write("an TestArmatureObject0082\nmdllib TestModelFile0082\nbc 1\nbn TestArmatureBoneName0082\nbh 100 0.0 100\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0082.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0082.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0082")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0082" and wyarmature.main_armature_obj.data.bones[0].head == Vector((100, 0, 100)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0083(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0083

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0083" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0083.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0083"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0083" and wyarmature.main_armature_obj.data.bones[0].head == Vector((200, 0, 200)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0083 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0083.wya', 'w+') as file:
            file.write("an TestArmatureObject0083\nmdllib TestModelFile0083\nbc 1\nbn TestArmatureBoneName0083\nbh 200 0.0 200\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0083.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0083.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0083")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0083" and wyarmature.main_armature_obj.data.bones[0].head == Vector((200, 0, 200)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0084(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0084

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0084" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0084.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0084"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0084" and wyarmature.main_armature_obj.data.bones[0].head == Vector((300, 0, 300)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0084 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0084.wya', 'w+') as file:
            file.write("an TestArmatureObject0084\nmdllib TestModelFile0084\nbc 1\nbn TestArmatureBoneName0084\nbh 300 0.0 300\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0084.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0084.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0084")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0084" and wyarmature.main_armature_obj.data.bones[0].head == Vector((300, 0, 300)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0085(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0085

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0085" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0085.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0085"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0085" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10000, 0,  10000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0085 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0085.wya', 'w+') as file:
            file.write("an TestArmatureObject0085\nmdllib TestModelFile0085\nbc 1\nbn TestArmatureBoneName0085\nbh 10000 0.0 10000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0085.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0085.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0085")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0085" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10000, 0,  10000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0086(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0086

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0086" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0086.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0086"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0086" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20000, 0,  20000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0086 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0086.wya', 'w+') as file:
            file.write("an TestArmatureObject0086\nmdllib TestModelFile0086\nbc 1\nbn TestArmatureBoneName0086\nbh 20000 0.0 20000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0086.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0086.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0086")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0086" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20000, 0,  20000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0087(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0087

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0087" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0087.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0087"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0087" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30000, 0,  30000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0087 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0087.wya', 'w+') as file:
            file.write("an TestArmatureObject0087\nmdllib TestModelFile0087\nbc 1\nbn TestArmatureBoneName0087\nbh 30000 0.0 30000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0087.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0087.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0087")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0087" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30000, 0,  30000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0088(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0088

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0088" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0088.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0088"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0088" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1000000, 0,  1000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0088 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0088.wya', 'w+') as file:
            file.write("an TestArmatureObject0088\nmdllib TestModelFile0088\nbc 1\nbn TestArmatureBoneName0088\nbh 1000000 0.0 1000000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0088.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0088.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0088")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0088" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1000000, 0,  1000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0089(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0089

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0089" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0089.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0089"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0089" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2000000, 0,  2000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0089 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0089.wya', 'w+') as file:
            file.write("an TestArmatureObject0089\nmdllib TestModelFile0089\nbc 1\nbn TestArmatureBoneName0089\nbh 2000000 0.0 2000000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0089.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0089.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0089")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0089" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2000000, 0,  2000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0090(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0090

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0090" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0090.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0090"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0090" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3000000, 0,  3000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0090 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0090.wya', 'w+') as file:
            file.write("an TestArmatureObject0090\nmdllib TestModelFile0090\nbc 1\nbn TestArmatureBoneName0090\nbh 3000000 0.0 3000000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0090.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0090.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0090")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0090" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3000000, 0,  3000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0091(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0091

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0091" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0091.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0091"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0091" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 1, 1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0091 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0091.wya', 'w+') as file:
            file.write("an TestArmatureObject0091\nmdllib TestModelFile0091\nbc 1\nbn TestArmatureBoneName0091\nbh 0 1.0 1\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0091.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0091.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0091")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0091" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 1, 1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0092(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0092

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0092" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0092.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0092"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0092" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0.1, 0.1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0092 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0092.wya', 'w+') as file:
            file.write("an TestArmatureObject0092\nmdllib TestModelFile0092\nbc 1\nbn TestArmatureBoneName0092\nbh 0 0.1 0.1\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0092.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0092.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0092")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0092" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0.1, 0.1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0093(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0093

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0093" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0093.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0093"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0093" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0.01, 0.001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0093 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0093.wya', 'w+') as file:
            file.write("an TestArmatureObject0093\nmdllib TestModelFile0093\nbc 1\nbn TestArmatureBoneName0093\nbh 0 0.01 0.001\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0093.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0093.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0093")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0093" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0.01, 0.001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0094(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0094

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0094" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0094.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0094"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0094" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0.0001, 0.0001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0094 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0094.wya', 'w+') as file:
            file.write("an TestArmatureObject0094\nmdllib TestModelFile0094\nbc 1\nbn TestArmatureBoneName0094\nbh 0 0.0001 0.0001\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0094.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0094.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0094")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0094" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 0.0001, 0.0001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0095(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0095

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0095" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0095.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0095"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0095" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 2, 2)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0095 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0095.wya', 'w+') as file:
            file.write("an TestArmatureObject0095\nmdllib TestModelFile0095\nbc 1\nbn TestArmatureBoneName0095\nbh 0 2.0 2\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0095.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0095.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0095")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0095" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 2, 2)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0096(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0096

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0096" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0096.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0096"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0096" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 3, 3)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0096 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0096.wya', 'w+') as file:
            file.write("an TestArmatureObject0096\nmdllib TestModelFile0096\nbc 1\nbn TestArmatureBoneName0096\nbh 0 3.0 3\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0096.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0096.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0096")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0096" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 3, 3)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0097(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0097

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0097" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0097.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0097"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0097" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 10, 10)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0097 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0097.wya', 'w+') as file:
            file.write("an TestArmatureObject0097\nmdllib TestModelFile0097\nbc 1\nbn TestArmatureBoneName0097\nbh 0 10.0 10\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0097.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0097.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0097")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0097" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 10, 10)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0098(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0098

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0098" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0098.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0098"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0098" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 20, 20)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0098 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0098.wya', 'w+') as file:
            file.write("an TestArmatureObject0098\nmdllib TestModelFile0098\nbc 1\nbn TestArmatureBoneName0098\nbh 0 20.0 20\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0098.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0098.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0098")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0098" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 20, 20)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0099(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0099

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0099" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0099.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0099"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0099" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 30, 30)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0099 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0099.wya', 'w+') as file:
            file.write("an TestArmatureObject0099\nmdllib TestModelFile0099\nbc 1\nbn TestArmatureBoneName0099\nbh 0 30.0 30\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0099.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0099.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0099")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0099" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 30, 30)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0100(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0100

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0100" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0100.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0100"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0100" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 100, 100)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0100 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0100.wya', 'w+') as file:
            file.write("an TestArmatureObject0100\nmdllib TestModelFile0100\nbc 1\nbn TestArmatureBoneName0100\nbh 0 100.0 100\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0100.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0100.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0100")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0100" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 100, 100)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0101(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0101

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0101" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0101.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0101"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0101" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 200, 200)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0101 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0101.wya', 'w+') as file:
            file.write("an TestArmatureObject0101\nmdllib TestModelFile0101\nbc 1\nbn TestArmatureBoneName0101\nbh 0 200.0 200\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0101.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0101.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0101")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0101" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 200, 200)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0102(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0102

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0102" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0102.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0102"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0102" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 300, 300)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0102 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0102.wya', 'w+') as file:
            file.write("an TestArmatureObject0102\nmdllib TestModelFile0102\nbc 1\nbn TestArmatureBoneName0102\nbh 0 300.0 300\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0102.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0102.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0102")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0102" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 300, 300)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0103(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0103

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0103" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0103.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0103"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0103" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 10000, 10000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0103 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0103.wya', 'w+') as file:
            file.write("an TestArmatureObject0103\nmdllib TestModelFile0103\nbc 1\nbn TestArmatureBoneName0103\nbh 0 10000.0 10000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0103.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0103.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0103")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0103" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 10000, 10000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0104(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0104

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0104" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0104.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0104"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0104" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 20000, 20000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0104 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0104.wya', 'w+') as file:
            file.write("an TestArmatureObject0104\nmdllib TestModelFile0104\nbc 1\nbn TestArmatureBoneName0104\nbh 0 20000.0 20000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0104.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0104.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0104")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0104" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 20000, 20000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0105(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0105

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0105" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0105.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0105"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0105" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 30000, 30000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0105 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0105.wya', 'w+') as file:
            file.write("an TestArmatureObject0105\nmdllib TestModelFile0105\nbc 1\nbn TestArmatureBoneName0105\nbh 0 30000.0 30000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0105.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0105.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0105")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0105" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 30000, 30000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0106(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0106

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0106" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0106.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0106"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0106" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 1000000, 1000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0106 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0106.wya', 'w+') as file:
            file.write("an TestArmatureObject0106\nmdllib TestModelFile0106\nbc 1\nbn TestArmatureBoneName0106\nbh 0 1000000.0 1000000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0106.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0106.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0106")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0106" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 1000000, 1000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0107(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0107

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0107" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0107.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0107"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0107" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 2000000, 2000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0107 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0107.wya', 'w+') as file:
            file.write("an TestArmatureObject0107\nmdllib TestModelFile0107\nbc 1\nbn TestArmatureBoneName0107\nbh 0 2000000.0 2000000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0107.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0107.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0107")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0107" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 2000000, 2000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0108(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0108

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0108" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0108.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0108"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0108" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 3000000, 3000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0108 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0108.wya', 'w+') as file:
            file.write("an TestArmatureObject0108\nmdllib TestModelFile0108\nbc 1\nbn TestArmatureBoneName0108\nbh 0 3000000.0 3000000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0108.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0108.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0108")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0108" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0, 3000000, 3000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0109(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0109

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0109" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0109.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0109"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0109" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1, 1, 1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0109 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0109.wya', 'w+') as file:
            file.write("an TestArmatureObject0109\nmdllib TestModelFile0109\nbc 1\nbn TestArmatureBoneName0109\nbh 1 1.0 1\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0109.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0109.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0109")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0109" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1, 1, 1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0110(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0110

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0110" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0110.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0110"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0110" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.1, 0.1, 0.1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0110 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0110.wya', 'w+') as file:
            file.write("an TestArmatureObject0110\nmdllib TestModelFile0110\nbc 1\nbn TestArmatureBoneName0110\nbh 0.1 0.1 0.1\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0110.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0110.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0110")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0110" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.1, 0.1, 0.1)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0111(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0111

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0111" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0111.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0111"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0111" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.001, 0.01, 0.001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0111 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0111.wya', 'w+') as file:
            file.write("an TestArmatureObject0111\nmdllib TestModelFile0111\nbc 1\nbn TestArmatureBoneName0111\nbh 0.001 0.01 0.001\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0111.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0111.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0111")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0111" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.001, 0.01, 0.001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0112(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0112

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0112" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0112.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0112"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0112" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0001, 0.0001, 0.0001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0112 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0112.wya', 'w+') as file:
            file.write("an TestArmatureObject0112\nmdllib TestModelFile0112\nbc 1\nbn TestArmatureBoneName0112\nbh 0.0001 0.0001 0.0001\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0112.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0112.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0112")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0112" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0001, 0.0001, 0.0001)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0113(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0113

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0113" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0113.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0113"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0113" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2, 2, 2)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0113 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0113.wya', 'w+') as file:
            file.write("an TestArmatureObject0113\nmdllib TestModelFile0113\nbc 1\nbn TestArmatureBoneName0113\nbh 2 2.0 2\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0113.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0113.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0113")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0113" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2, 2, 2)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0114(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0114

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0114" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0114.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0114"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0114" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3, 3, 3)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0114 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0114.wya', 'w+') as file:
            file.write("an TestArmatureObject0114\nmdllib TestModelFile0114\nbc 1\nbn TestArmatureBoneName0114\nbh 3 3.0 3\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0114.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0114.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0114")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0114" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3, 3, 3)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0115(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0115

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0115" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0115.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0115"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0115" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10, 10, 10)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0115 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0115.wya', 'w+') as file:
            file.write("an TestArmatureObject0115\nmdllib TestModelFile0115\nbc 1\nbn TestArmatureBoneName0115\nbh 10 10.0 10\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0115.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0115.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0115")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0115" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10, 10, 10)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0116(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0116

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0116" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0116.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0116"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0116" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20, 20, 20)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0116 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0116.wya', 'w+') as file:
            file.write("an TestArmatureObject0116\nmdllib TestModelFile0116\nbc 1\nbn TestArmatureBoneName0116\nbh 20 20.0 20\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0116.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0116.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0116")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0116" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20, 20, 20)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0117(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0117

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0117" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0117.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0117"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0117" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30, 30, 30)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0117 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0117.wya', 'w+') as file:
            file.write("an TestArmatureObject0117\nmdllib TestModelFile0117\nbc 1\nbn TestArmatureBoneName0117\nbh 30 30.0 30\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0117.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0117.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0117")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0117" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30, 30, 30)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0118(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0118

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0118" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0118.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0118"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0118" and wyarmature.main_armature_obj.data.bones[0].head == Vector((100, 100, 100)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0118 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0118.wya', 'w+') as file:
            file.write("an TestArmatureObject0118\nmdllib TestModelFile0118\nbc 1\nbn TestArmatureBoneName0118\nbh 100 100.0 100\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0118.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0118.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0118")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0118" and wyarmature.main_armature_obj.data.bones[0].head == Vector((100, 100, 100)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0119(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0119

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0119" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0119.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0119"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0119" and wyarmature.main_armature_obj.data.bones[0].head == Vector((200, 200, 200)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0119 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0119.wya', 'w+') as file:
            file.write("an TestArmatureObject0119\nmdllib TestModelFile0119\nbc 1\nbn TestArmatureBoneName0119\nbh 200 200.0 200\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0119.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0119.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0119")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0119" and wyarmature.main_armature_obj.data.bones[0].head == Vector((200, 200, 200)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0120(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0120

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0120" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0120.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0120"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0120" and wyarmature.main_armature_obj.data.bones[0].head == Vector((300, 300, 300)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0120 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0120.wya', 'w+') as file:
            file.write("an TestArmatureObject0120\nmdllib TestModelFile0120\nbc 1\nbn TestArmatureBoneName0120\nbh 300 300.0 300\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0120.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0120.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0120")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0120" and wyarmature.main_armature_obj.data.bones[0].head == Vector((300, 300, 300)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0121(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0121

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0121" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0121.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0121"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0121" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10000, 10000, 10000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0121 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0121.wya', 'w+') as file:
            file.write("an TestArmatureObject0121\nmdllib TestModelFile0121\nbc 1\nbn TestArmatureBoneName0121\nbh 10000 10000.0 10000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0121.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0121.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0121")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0121" and wyarmature.main_armature_obj.data.bones[0].head == Vector((10000, 10000, 10000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0122(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0122

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0122" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0122.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0122"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0122" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20000, 20000, 20000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0122 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0122.wya', 'w+') as file:
            file.write("an TestArmatureObject0122\nmdllib TestModelFile0122\nbc 1\nbn TestArmatureBoneName0122\nbh 20000 20000.0 20000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0122.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0122.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0122")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0122" and wyarmature.main_armature_obj.data.bones[0].head == Vector((20000, 20000, 20000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0123(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0123

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0123" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0123.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0123"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0123" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30000, 30000, 30000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0123 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0123.wya', 'w+') as file:
            file.write("an TestArmatureObject0123\nmdllib TestModelFile0123\nbc 1\nbn TestArmatureBoneName0123\nbh 30000 30000.0 30000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0123.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0123.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0123")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0123" and wyarmature.main_armature_obj.data.bones[0].head == Vector((30000, 30000, 30000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0124(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0124

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0124" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0124.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0124"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0124" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1000000, 1000000, 1000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0124 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0124.wya', 'w+') as file:
            file.write("an TestArmatureObject0124\nmdllib TestModelFile0124\nbc 1\nbn TestArmatureBoneName0124\nbh 1000000 1000000.0 1000000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0124.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0124.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0124")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0124" and wyarmature.main_armature_obj.data.bones[0].head == Vector((1000000, 1000000, 1000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0125(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0125

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0125" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0125.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0125"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0125" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2000000, 2000000, 2000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0125 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0125.wya', 'w+') as file:
            file.write("an TestArmatureObject0125\nmdllib TestModelFile0125\nbc 1\nbn TestArmatureBoneName0125\nbh 2000000 2000000.0 2000000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0125.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0125.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0125")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0125" and wyarmature.main_armature_obj.data.bones[0].head == Vector((2000000, 2000000, 2000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0126(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0126

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0126" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0126.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0126"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0126" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3000000, 3000000, 3000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0))
        """
        wymodelmanager0126 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0126.wya', 'w+') as file:
            file.write("an TestArmatureObject0126\nmdllib TestModelFile0126\nbc 1\nbn TestArmatureBoneName0126\nbh 3000000 3000000.0 3000000\nbt 0.0 0.0 0.0\n")
        wyarmature = wymodelmanager0126.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0126.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0126")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0126" and wyarmature.main_armature_obj.data.bones[0].head == Vector((3000000, 3000000, 3000000)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0,0.0,0.0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0127(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0127

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0127" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0127.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0127"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0127" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1, 0, 0))
        """
        wymodelmanager0127 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0127.wya', 'w+') as file:
            file.write("an TestArmatureObject0127\nmdllib TestModelFile0127\nbc 1\nbn TestArmatureBoneName0127\nbh 0.0 0.0 0.0\nbt 1 0.0 0\n")
        wyarmature = wymodelmanager0127.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0127.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0127")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0127" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0128(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0128

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0128" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0128.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0128"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0128" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.1, 0, 0))
        """
        wymodelmanager0128 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0128.wya', 'w+') as file:
            file.write("an TestArmatureObject0128\nmdllib TestModelFile0128\nbc 1\nbn TestArmatureBoneName0128\nbh 0.0 0.0 0.0\nbt 0.1 0.0 0\n")
        wyarmature = wymodelmanager0128.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0128.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0128")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0128" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.1, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0129(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0129

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0129" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0129.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0129"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0129" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.001, 0, 0))
        """
        wymodelmanager0129 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0129.wya', 'w+') as file:
            file.write("an TestArmatureObject0129\nmdllib TestModelFile0129\nbc 1\nbn TestArmatureBoneName0129\nbh 0.0 0.0 0.0\nbt 0.001 0.0 0\n")
        wyarmature = wymodelmanager0129.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0129.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0129")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0129" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.001, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0130(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0130

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0130" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0130.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0130"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0130" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0001, 0, 0))
        """
        wymodelmanager0130 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0130.wya', 'w+') as file:
            file.write("an TestArmatureObject0130\nmdllib TestModelFile0130\nbc 1\nbn TestArmatureBoneName0130\nbh 0.0 0.0 0.0\nbt 0.0001 0.0 0\n")
        wyarmature = wymodelmanager0130.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0130.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0130")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0130" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0001, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0131(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0131

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0131" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0131.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0131"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0131" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2, 0, 0))
        """
        wymodelmanager0131 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0131.wya', 'w+') as file:
            file.write("an TestArmatureObject0131\nmdllib TestModelFile0131\nbc 1\nbn TestArmatureBoneName0131\nbh 0.0 0.0 0.0\nbt 2 0.0 0\n")
        wyarmature = wymodelmanager0131.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0131.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0131")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0131" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0132(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0132

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0132" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0132.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0132"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0132" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3, 0, 0))
        """
        wymodelmanager0132 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0132.wya', 'w+') as file:
            file.write("an TestArmatureObject0132\nmdllib TestModelFile0132\nbc 1\nbn TestArmatureBoneName0132\nbh 0.0 0.0 0.0\nbt 3 0.0 0\n")
        wyarmature = wymodelmanager0132.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0132.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0132")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0132" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0133(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0133

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0133" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0133.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0133"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0133" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10, 0, 0))
        """
        wymodelmanager0133 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0133.wya', 'w+') as file:
            file.write("an TestArmatureObject0133\nmdllib TestModelFile0133\nbc 1\nbn TestArmatureBoneName0133\nbh 0.0 0.0 0.0\nbt 10 0.0 0\n")
        wyarmature = wymodelmanager0133.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0133.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0133")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0133" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0134(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0134

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0134" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0134.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0134"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0134" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20, 0, 0))
        """
        wymodelmanager0134 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0134.wya', 'w+') as file:
            file.write("an TestArmatureObject0134\nmdllib TestModelFile0134\nbc 1\nbn TestArmatureBoneName0134\nbh 0.0 0.0 0.0\nbt 20 0.0 0\n")
        wyarmature = wymodelmanager0134.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0134.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0134")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0134" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0135(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0135

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0135" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0135.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0135"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0135" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30, 0, 0))
        """
        wymodelmanager0135 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0135.wya', 'w+') as file:
            file.write("an TestArmatureObject0135\nmdllib TestModelFile0135\nbc 1\nbn TestArmatureBoneName0135\nbh 0.0 0.0 0.0\nbt 30 0.0 0\n")
        wyarmature = wymodelmanager0135.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0135.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0135")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0135" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0136(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0136

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0136" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0136.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0136"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0136" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((100, 0, 0))
        """
        wymodelmanager0136 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0136.wya', 'w+') as file:
            file.write("an TestArmatureObject0136\nmdllib TestModelFile0136\nbc 1\nbn TestArmatureBoneName0136\nbh 0.0 0.0 0.0\nbt 100 0.0 0\n")
        wyarmature = wymodelmanager0136.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0136.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0136")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0136" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((100, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0137(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0137

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0137" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0137.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0137"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0137" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((200, 0, 0))
        """
        wymodelmanager0137 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0137.wya', 'w+') as file:
            file.write("an TestArmatureObject0137\nmdllib TestModelFile0137\nbc 1\nbn TestArmatureBoneName0137\nbh 0.0 0.0 0.0\nbt 200 0.0 0\n")
        wyarmature = wymodelmanager0137.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0137.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0137")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0137" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((200, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0138(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0138

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0138" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0138.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0138"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0138" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((300, 0, 0))
        """
        wymodelmanager0138 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0138.wya', 'w+') as file:
            file.write("an TestArmatureObject0138\nmdllib TestModelFile0138\nbc 1\nbn TestArmatureBoneName0138\nbh 0.0 0.0 0.0\nbt 300 0.0 0\n")
        wyarmature = wymodelmanager0138.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0138.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0138")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0138" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((300, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0139(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0139

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0139" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0139.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0139"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0139" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10000, 0, 0))
        """
        wymodelmanager0139 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0139.wya', 'w+') as file:
            file.write("an TestArmatureObject0139\nmdllib TestModelFile0139\nbc 1\nbn TestArmatureBoneName0139\nbh 0.0 0.0 0.0\nbt 10000 0.0 0\n")
        wyarmature = wymodelmanager0139.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0139.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0139")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0139" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10000, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0140(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0140

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0140" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0140.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0140"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0140" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20000, 0, 0))
        """
        wymodelmanager0140 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0140.wya', 'w+') as file:
            file.write("an TestArmatureObject0140\nmdllib TestModelFile0140\nbc 1\nbn TestArmatureBoneName0140\nbh 0.0 0.0 0.0\nbt 20000 0.0 0\n")
        wyarmature = wymodelmanager0140.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0140.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0140")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0140" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20000, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0141(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0141

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0141" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0141.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0141"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0141" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30000, 0, 0))
        """
        wymodelmanager0141 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0141.wya', 'w+') as file:
            file.write("an TestArmatureObject0141\nmdllib TestModelFile0141\nbc 1\nbn TestArmatureBoneName0141\nbh 0.0 0.0 0.0\nbt 30000 0.0 0\n")
        wyarmature = wymodelmanager0141.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0141.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0141")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0141" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30000, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0142(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0142

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0142" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0142.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0142"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0142" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1000000, 0, 0))
        """
        wymodelmanager0142 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0142.wya', 'w+') as file:
            file.write("an TestArmatureObject0142\nmdllib TestModelFile0142\nbc 1\nbn TestArmatureBoneName0142\nbh 0.0 0.0 0.0\nbt 1000000 0.0 0\n")
        wyarmature = wymodelmanager0142.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0142.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0142")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0142" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1000000, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0143(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0143

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0143" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0143.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0143"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0143" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2000000, 0, 0))
        """
        wymodelmanager0143 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0143.wya', 'w+') as file:
            file.write("an TestArmatureObject0143\nmdllib TestModelFile0143\nbc 1\nbn TestArmatureBoneName0143\nbh 0.0 0.0 0.0\nbt 2000000 0.0 0\n")
        wyarmature = wymodelmanager0143.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0143.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0143")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0143" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2000000, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0144(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0144

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0144" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0144.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0144"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0144" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3000000, 0, 0))
        """
        wymodelmanager0144 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0144.wya', 'w+') as file:
            file.write("an TestArmatureObject0144\nmdllib TestModelFile0144\nbc 1\nbn TestArmatureBoneName0144\nbh 0.0 0.0 0.0\nbt 3000000 0.0 0\n")
        wyarmature = wymodelmanager0144.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0144.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0144")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0144" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3000000, 0, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0145(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0145

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0145" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0145.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0145"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0145" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 1, 0))
        """
        wymodelmanager0145 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0145.wya', 'w+') as file:
            file.write("an TestArmatureObject0145\nmdllib TestModelFile0145\nbc 1\nbn TestArmatureBoneName0145\nbh 0.0 0.0 0.0\nbt 0 1.0 0\n")
        wyarmature = wymodelmanager0145.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0145.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0145")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0145" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 1, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0146(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0146

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0146" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0146.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0146"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0146" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0.1, 0))
        """
        wymodelmanager0146 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0146.wya', 'w+') as file:
            file.write("an TestArmatureObject0146\nmdllib TestModelFile0146\nbc 1\nbn TestArmatureBoneName0146\nbh 0.0 0.0 0.0\nbt 0 0.1 0\n")
        wyarmature = wymodelmanager0146.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0146.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0146")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0146" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0.1, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0147(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0147

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0147" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0147.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0147"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0147" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0.001, 0))
        """
        wymodelmanager0147 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0147.wya', 'w+') as file:
            file.write("an TestArmatureObject0147\nmdllib TestModelFile0147\nbc 1\nbn TestArmatureBoneName0147\nbh 0.0 0.0 0.0\nbt 0 0.001 0\n")
        wyarmature = wymodelmanager0147.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0147.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0147")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0147" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0.001, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0148(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0148

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0148" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0148.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0148"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0148" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0.0001, 0))
        """
        wymodelmanager0148 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0148.wya', 'w+') as file:
            file.write("an TestArmatureObject0148\nmdllib TestModelFile0148\nbc 1\nbn TestArmatureBoneName0148\nbh 0.0 0.0 0.0\nbt 0 0.0001 0\n")
        wyarmature = wymodelmanager0148.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0148.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0148")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0148" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0.0001, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0149(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0149

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0149" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0149.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0149"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0149" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 2, 0))
        """
        wymodelmanager0149 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0149.wya', 'w+') as file:
            file.write("an TestArmatureObject0149\nmdllib TestModelFile0149\nbc 1\nbn TestArmatureBoneName0149\nbh 0.0 0.0 0.0\nbt 0 2.0 0\n")
        wyarmature = wymodelmanager0149.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0149.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0149")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0149" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 2, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0150(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0150

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0150" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0150.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0150"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0150" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 3, 0))
        """
        wymodelmanager0150 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0150.wya', 'w+') as file:
            file.write("an TestArmatureObject0150\nmdllib TestModelFile0150\nbc 1\nbn TestArmatureBoneName0150\nbh 0.0 0.0 0.0\nbt 0 3.0 0\n")
        wyarmature = wymodelmanager0150.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0150.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0150")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0150" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 3, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0151(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0151

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0151" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0151.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0151"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0151" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 10, 0))
        """
        wymodelmanager0151 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0151.wya', 'w+') as file:
            file.write("an TestArmatureObject0151\nmdllib TestModelFile0151\nbc 1\nbn TestArmatureBoneName0151\nbh 0.0 0.0 0.0\nbt 0 10.0 0\n")
        wyarmature = wymodelmanager0151.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0151.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0151")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0151" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 10, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0152(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0152

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0152" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0152.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0152"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0152" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 20, 0))
        """
        wymodelmanager0152 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0152.wya', 'w+') as file:
            file.write("an TestArmatureObject0152\nmdllib TestModelFile0152\nbc 1\nbn TestArmatureBoneName0152\nbh 0.0 0.0 0.0\nbt 0 20.0 0\n")
        wyarmature = wymodelmanager0152.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0152.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0152")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0152" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 20, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0153(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0153

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0153" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0153.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0153"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0153" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 30, 0))
        """
        wymodelmanager0153 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0153.wya', 'w+') as file:
            file.write("an TestArmatureObject0153\nmdllib TestModelFile0153\nbc 1\nbn TestArmatureBoneName0153\nbh 0.0 0.0 0.0\nbt 0 30.0 0\n")
        wyarmature = wymodelmanager0153.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0153.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0153")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0153" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 30, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0154(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0154

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0154" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0154.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0154"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0154" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 100, 0))
        """
        wymodelmanager0154 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0154.wya', 'w+') as file:
            file.write("an TestArmatureObject0154\nmdllib TestModelFile0154\nbc 1\nbn TestArmatureBoneName0154\nbh 0.0 0.0 0.0\nbt 0 100.0 0\n")
        wyarmature = wymodelmanager0154.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0154.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0154")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0154" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 100, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0155(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0155

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0155" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0155.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0155"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0155" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 200, 0))
        """
        wymodelmanager0155 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0155.wya', 'w+') as file:
            file.write("an TestArmatureObject0155\nmdllib TestModelFile0155\nbc 1\nbn TestArmatureBoneName0155\nbh 0.0 0.0 0.0\nbt 0 200.0 0\n")
        wyarmature = wymodelmanager0155.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0155.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0155")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0155" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 200, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0156(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0156

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0156" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0156.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0156"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0156" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 300, 0))
        """
        wymodelmanager0156 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0156.wya', 'w+') as file:
            file.write("an TestArmatureObject0156\nmdllib TestModelFile0156\nbc 1\nbn TestArmatureBoneName0156\nbh 0.0 0.0 0.0\nbt 0 300.0 0\n")
        wyarmature = wymodelmanager0156.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0156.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0156")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0156" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 300, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0157(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0157

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0157" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0157.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0157"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0157" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 10000, 0))
        """
        wymodelmanager0157 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0157.wya', 'w+') as file:
            file.write("an TestArmatureObject0157\nmdllib TestModelFile0157\nbc 1\nbn TestArmatureBoneName0157\nbh 0.0 0.0 0.0\nbt 0 10000.0 0\n")
        wyarmature = wymodelmanager0157.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0157.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0157")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0157" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 10000, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0158(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0158

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0158" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0158.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0158"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0158" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 20000, 0))
        """
        wymodelmanager0158 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0158.wya', 'w+') as file:
            file.write("an TestArmatureObject0158\nmdllib TestModelFile0158\nbc 1\nbn TestArmatureBoneName0158\nbh 0.0 0.0 0.0\nbt 0 20000.0 0\n")
        wyarmature = wymodelmanager0158.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0158.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0158")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0158" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 20000, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0159(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0159

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0159" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0159.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0159"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0159" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 30000, 0))
        """
        wymodelmanager0159 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0159.wya', 'w+') as file:
            file.write("an TestArmatureObject0159\nmdllib TestModelFile0159\nbc 1\nbn TestArmatureBoneName0159\nbh 0.0 0.0 0.0\nbt 0 30000.0 0\n")
        wyarmature = wymodelmanager0159.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0159.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0159")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0159" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 30000, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0160(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0160

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0160" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0160.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0160"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0160" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 1000000, 0))
        """
        wymodelmanager0160 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0160.wya', 'w+') as file:
            file.write("an TestArmatureObject0160\nmdllib TestModelFile0160\nbc 1\nbn TestArmatureBoneName0160\nbh 0.0 0.0 0.0\nbt 0 1000000.0 0\n")
        wyarmature = wymodelmanager0160.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0160.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0160")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0160" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 1000000, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0161(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0161

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0161" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0161.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0161"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0161" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 2000000, 0))
        """
        wymodelmanager0161 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0161.wya', 'w+') as file:
            file.write("an TestArmatureObject0161\nmdllib TestModelFile0161\nbc 1\nbn TestArmatureBoneName0161\nbh 0.0 0.0 0.0\nbt 0 2000000.0 0\n")
        wyarmature = wymodelmanager0161.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0161.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0161")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0161" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 2000000, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0162(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0162

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0162" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0162.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0162"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0162" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 3000000, 0))
        """
        wymodelmanager0162 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0162.wya', 'w+') as file:
            file.write("an TestArmatureObject0162\nmdllib TestModelFile0162\nbc 1\nbn TestArmatureBoneName0162\nbh 0.0 0.0 0.0\nbt 0 3000000.0 0\n")
        wyarmature = wymodelmanager0162.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0162.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0162")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0162" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 3000000, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0163(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0163

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0163" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0163.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0163"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0163" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 1))
        """
        wymodelmanager0163 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0163.wya', 'w+') as file:
            file.write("an TestArmatureObject0163\nmdllib TestModelFile0163\nbc 1\nbn TestArmatureBoneName0163\nbh 0.0 0.0 0.0\nbt 0 0.0 1\n")
        wyarmature = wymodelmanager0163.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0163.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0163")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0163" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 1)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0164(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0164

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0164" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0164.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0164"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0164" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 0.1))
        """
        wymodelmanager0164 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0164.wya', 'w+') as file:
            file.write("an TestArmatureObject0164\nmdllib TestModelFile0164\nbc 1\nbn TestArmatureBoneName0164\nbh 0.0 0.0 0.0\nbt 0 0.0 0.1\n")
        wyarmature = wymodelmanager0164.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0164.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0164")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0164" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 0.1)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0165(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0165

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0165" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0165.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0165"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0165" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 0.001))
        """
        wymodelmanager0165 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0165.wya', 'w+') as file:
            file.write("an TestArmatureObject0165\nmdllib TestModelFile0165\nbc 1\nbn TestArmatureBoneName0165\nbh 0.0 0.0 0.0\nbt 0 0.0 0.001\n")
        wyarmature = wymodelmanager0165.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0165.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0165")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0165" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 0.001)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0166(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0166

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0166" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0166.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0166"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0166" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 0.0001))
        """
        wymodelmanager0166 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0166.wya', 'w+') as file:
            file.write("an TestArmatureObject0166\nmdllib TestModelFile0166\nbc 1\nbn TestArmatureBoneName0166\nbh 0.0 0.0 0.0\nbt 0 0.0 0.0001\n")
        wyarmature = wymodelmanager0166.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0166.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0166")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0166" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 0.0001)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0167(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0167

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0167" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0167.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0167"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0167" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 2))
        """
        wymodelmanager0167 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0167.wya', 'w+') as file:
            file.write("an TestArmatureObject0167\nmdllib TestModelFile0167\nbc 1\nbn TestArmatureBoneName0167\nbh 0.0 0.0 0.0\nbt 0 0.0 2\n")
        wyarmature = wymodelmanager0167.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0167.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0167")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0167" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 2)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0168(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0168

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0168" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0168.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0168"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0168" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 3))
        """
        wymodelmanager0168 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0168.wya', 'w+') as file:
            file.write("an TestArmatureObject0168\nmdllib TestModelFile0168\nbc 1\nbn TestArmatureBoneName0168\nbh 0.0 0.0 0.0\nbt 0 0.0 3\n")
        wyarmature = wymodelmanager0168.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0168.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0168")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0168" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 3)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0169(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0169

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0169" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0169.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0169"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0169" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 10))
        """
        wymodelmanager0169 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0169.wya', 'w+') as file:
            file.write("an TestArmatureObject0169\nmdllib TestModelFile0169\nbc 1\nbn TestArmatureBoneName0169\nbh 0.0 0.0 0.0\nbt 0 0.0 10\n")
        wyarmature = wymodelmanager0169.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0169.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0169")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0169" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 10)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0170(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0170

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0170" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0170.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0170"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0170" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 20))
        """
        wymodelmanager0170 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0170.wya', 'w+') as file:
            file.write("an TestArmatureObject0170\nmdllib TestModelFile0170\nbc 1\nbn TestArmatureBoneName0170\nbh 0.0 0.0 0.0\nbt 0 0.0 20\n")
        wyarmature = wymodelmanager0170.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0170.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0170")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0170" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 20)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0171(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0171

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0171" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0171.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0171"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0171" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 30))
        """
        wymodelmanager0171 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0171.wya', 'w+') as file:
            file.write("an TestArmatureObject0171\nmdllib TestModelFile0171\nbc 1\nbn TestArmatureBoneName0171\nbh 0.0 0.0 0.0\nbt 0 0.0 30\n")
        wyarmature = wymodelmanager0171.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0171.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0171")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0171" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 30)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0172(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0172

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0172" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0172.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0172"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0172" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 100))
        """
        wymodelmanager0172 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0172.wya', 'w+') as file:
            file.write("an TestArmatureObject0172\nmdllib TestModelFile0172\nbc 1\nbn TestArmatureBoneName0172\nbh 0.0 0.0 0.0\nbt 0 0.0 100\n")
        wyarmature = wymodelmanager0172.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0172.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0172")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0172" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 100)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0173(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0173

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0173" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0173.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0173"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0173" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 200))
        """
        wymodelmanager0173 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0173.wya', 'w+') as file:
            file.write("an TestArmatureObject0173\nmdllib TestModelFile0173\nbc 1\nbn TestArmatureBoneName0173\nbh 0.0 0.0 0.0\nbt 0 0.0 200\n")
        wyarmature = wymodelmanager0173.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0173.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0173")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0173" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 200)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0174(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0174

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0174" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0174.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0174"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0174" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 300))
        """
        wymodelmanager0174 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0174.wya', 'w+') as file:
            file.write("an TestArmatureObject0174\nmdllib TestModelFile0174\nbc 1\nbn TestArmatureBoneName0174\nbh 0.0 0.0 0.0\nbt 0 0.0 300\n")
        wyarmature = wymodelmanager0174.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0174.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0174")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0174" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 300)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0175(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0175

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0175" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0175.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0175"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0175" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 10000))
        """
        wymodelmanager0175 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0175.wya', 'w+') as file:
            file.write("an TestArmatureObject0175\nmdllib TestModelFile0175\nbc 1\nbn TestArmatureBoneName0175\nbh 0.0 0.0 0.0\nbt 0 0.0 10000\n")
        wyarmature = wymodelmanager0175.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0175.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0175")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0175" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 10000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0176(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0176

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0176" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0176.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0176"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0176" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 20000))
        """
        wymodelmanager0176 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0176.wya', 'w+') as file:
            file.write("an TestArmatureObject0176\nmdllib TestModelFile0176\nbc 1\nbn TestArmatureBoneName0176\nbh 0.0 0.0 0.0\nbt 0 0.0 20000\n")
        wyarmature = wymodelmanager0176.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0176.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0176")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0176" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 20000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0177(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0177

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0177" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0177.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0177"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0177" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 30000))
        """
        wymodelmanager0177 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0177.wya', 'w+') as file:
            file.write("an TestArmatureObject0177\nmdllib TestModelFile0177\nbc 1\nbn TestArmatureBoneName0177\nbh 0.0 0.0 0.0\nbt 0 0.0 30000\n")
        wyarmature = wymodelmanager0177.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0177.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0177")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0177" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 30000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0178(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0178

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0178" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0178.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0178"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0178" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 1000000))
        """
        wymodelmanager0178 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0178.wya', 'w+') as file:
            file.write("an TestArmatureObject0178\nmdllib TestModelFile0178\nbc 1\nbn TestArmatureBoneName0178\nbh 0.0 0.0 0.0\nbt 0 0.0 1000000\n")
        wyarmature = wymodelmanager0178.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0178.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0178")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0178" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 1000000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0179(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0179

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0179" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0179.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0179"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0179" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 2000000))
        """
        wymodelmanager0179 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0179.wya', 'w+') as file:
            file.write("an TestArmatureObject0179\nmdllib TestModelFile0179\nbc 1\nbn TestArmatureBoneName0179\nbh 0.0 0.0 0.0\nbt 0 0.0 2000000\n")
        wyarmature = wymodelmanager0179.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0179.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0179")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0179" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 2000000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0180(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0180

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0180" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0180.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0180"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0180" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 3000000))
        """
        wymodelmanager0180 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0180.wya', 'w+') as file:
            file.write("an TestArmatureObject0180\nmdllib TestModelFile0180\nbc 1\nbn TestArmatureBoneName0180\nbh 0.0 0.0 0.0\nbt 0 0.0 3000000\n")
        wyarmature = wymodelmanager0180.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0180.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0180")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0180" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0, 3000000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0181(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0181

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0181" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0181.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0181"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0181" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1, 1, 0))
        """
        wymodelmanager0181 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0181.wya', 'w+') as file:
            file.write("an TestArmatureObject0181\nmdllib TestModelFile0181\nbc 1\nbn TestArmatureBoneName0181\nbh 0.0 0.0 0.0\nbt 1 1.0 0\n")
        wyarmature = wymodelmanager0181.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0181.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0181")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0181" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1, 1, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0182(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0182

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0182" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0182.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0182"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0182" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.1, 0.1, 0))
        """
        wymodelmanager0182 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0182.wya', 'w+') as file:
            file.write("an TestArmatureObject0182\nmdllib TestModelFile0182\nbc 1\nbn TestArmatureBoneName0182\nbh 0.0 0.0 0.0\nbt 0.1 0.1 0\n")
        wyarmature = wymodelmanager0182.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0182.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0182")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0182" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.1, 0.1, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0183(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0183

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0183" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0183.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0183"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0183" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.001, 0.001, 0))
        """
        wymodelmanager0183 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0183.wya', 'w+') as file:
            file.write("an TestArmatureObject0183\nmdllib TestModelFile0183\nbc 1\nbn TestArmatureBoneName0183\nbh 0.0 0.0 0.0\nbt 0.001 0.001 0\n")
        wyarmature = wymodelmanager0183.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0183.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0183")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0183" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.001, 0.001, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0184(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0184

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0184" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0184.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0184"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0184" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0001, 0.0001, 0))
        """
        wymodelmanager0184 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0184.wya', 'w+') as file:
            file.write("an TestArmatureObject0184\nmdllib TestModelFile0184\nbc 1\nbn TestArmatureBoneName0184\nbh 0.0 0.0 0.0\nbt 0.0001 0.0001 0\n")
        wyarmature = wymodelmanager0184.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0184.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0184")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0184" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0001, 0.0001, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0185(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0185

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0185" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0185.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0185"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0185" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2, 2, 0))
        """
        wymodelmanager0185 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0185.wya', 'w+') as file:
            file.write("an TestArmatureObject0185\nmdllib TestModelFile0185\nbc 1\nbn TestArmatureBoneName0185\nbh 0.0 0.0 0.0\nbt 2 2.0 0\n")
        wyarmature = wymodelmanager0185.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0185.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0185")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0185" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2, 2, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0186(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0186

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0186" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0186.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0186"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0186" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3, 3, 0))
        """
        wymodelmanager0186 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0186.wya', 'w+') as file:
            file.write("an TestArmatureObject0186\nmdllib TestModelFile0186\nbc 1\nbn TestArmatureBoneName0186\nbh 0.0 0.0 0.0\nbt 3 3.0 0\n")
        wyarmature = wymodelmanager0186.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0186.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0186")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0186" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3, 3, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0187(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0187

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0187" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0187.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0187"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0187" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10, 10, 0))
        """
        wymodelmanager0187 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0187.wya', 'w+') as file:
            file.write("an TestArmatureObject0187\nmdllib TestModelFile0187\nbc 1\nbn TestArmatureBoneName0187\nbh 0.0 0.0 0.0\nbt 10 10.0 0\n")
        wyarmature = wymodelmanager0187.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0187.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0187")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0187" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10, 10, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0188(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0188

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0188" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0188.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0188"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0188" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20, 20, 0))
        """
        wymodelmanager0188 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0188.wya', 'w+') as file:
            file.write("an TestArmatureObject0188\nmdllib TestModelFile0188\nbc 1\nbn TestArmatureBoneName0188\nbh 0.0 0.0 0.0\nbt 20 20.0 0\n")
        wyarmature = wymodelmanager0188.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0188.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0188")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0188" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20, 20, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0189(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0189

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0189" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0189.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0189"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0189" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30, 30, 0))
        """
        wymodelmanager0189 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0189.wya', 'w+') as file:
            file.write("an TestArmatureObject0189\nmdllib TestModelFile0189\nbc 1\nbn TestArmatureBoneName0189\nbh 0.0 0.0 0.0\nbt 30 30.0 0\n")
        wyarmature = wymodelmanager0189.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0189.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0189")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0189" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30, 30, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0190(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0190

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0190" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0190.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0190"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0190" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((100, 100, 0))
        """
        wymodelmanager0190 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0190.wya', 'w+') as file:
            file.write("an TestArmatureObject0190\nmdllib TestModelFile0190\nbc 1\nbn TestArmatureBoneName0190\nbh 0.0 0.0 0.0\nbt 100 100.0 0\n")
        wyarmature = wymodelmanager0190.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0190.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0190")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0190" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((100, 100, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0191(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0191

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0191" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0191.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0191"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0191" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((200, 200, 0))
        """
        wymodelmanager0191 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0191.wya', 'w+') as file:
            file.write("an TestArmatureObject0191\nmdllib TestModelFile0191\nbc 1\nbn TestArmatureBoneName0191\nbh 0.0 0.0 0.0\nbt 200 200.0 0\n")
        wyarmature = wymodelmanager0191.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0191.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0191")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0191" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((200, 200, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0192(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0192

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0192" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0192.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0192"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0192" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((300, 300, 0))
        """
        wymodelmanager0192 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0192.wya', 'w+') as file:
            file.write("an TestArmatureObject0192\nmdllib TestModelFile0192\nbc 1\nbn TestArmatureBoneName0192\nbh 0.0 0.0 0.0\nbt 300 300.0 0\n")
        wyarmature = wymodelmanager0192.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0192.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0192")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0192" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((300, 300, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0193(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0193

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0193" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0193.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0193"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0193" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10000, 10000, 0))
        """
        wymodelmanager0193 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0193.wya', 'w+') as file:
            file.write("an TestArmatureObject0193\nmdllib TestModelFile0193\nbc 1\nbn TestArmatureBoneName0193\nbh 0.0 0.0 0.0\nbt 10000 10000.0 0\n")
        wyarmature = wymodelmanager0193.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0193.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0193")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0193" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10000, 10000, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0194(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0194

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0194" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0194.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0194"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0194" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20000, 20000, 0))
        """
        wymodelmanager0194 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0194.wya', 'w+') as file:
            file.write("an TestArmatureObject0194\nmdllib TestModelFile0194\nbc 1\nbn TestArmatureBoneName0194\nbh 0.0 0.0 0.0\nbt 20000 20000.0 0\n")
        wyarmature = wymodelmanager0194.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0194.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0194")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0194" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20000, 20000, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0195(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0195

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0195" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0195.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0195"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0195" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30000, 30000, 0))
        """
        wymodelmanager0195 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0195.wya', 'w+') as file:
            file.write("an TestArmatureObject0195\nmdllib TestModelFile0195\nbc 1\nbn TestArmatureBoneName0195\nbh 0.0 0.0 0.0\nbt 30000 30000.0 0\n")
        wyarmature = wymodelmanager0195.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0195.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0195")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0195" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30000, 30000, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0196(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0196

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0196" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0196.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0196"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0196" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1000000, 1000000, 0))
        """
        wymodelmanager0196 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0196.wya', 'w+') as file:
            file.write("an TestArmatureObject0196\nmdllib TestModelFile0196\nbc 1\nbn TestArmatureBoneName0196\nbh 0.0 0.0 0.0\nbt 1000000 1000000.0 0\n")
        wyarmature = wymodelmanager0196.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0196.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0196")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0196" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1000000, 1000000, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0197(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0197

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0197" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0197.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0197"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0197" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2000000, 2000000, 0))
        """
        wymodelmanager0197 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0197.wya', 'w+') as file:
            file.write("an TestArmatureObject0197\nmdllib TestModelFile0197\nbc 1\nbn TestArmatureBoneName0197\nbh 0.0 0.0 0.0\nbt 2000000 2000000.0 0\n")
        wyarmature = wymodelmanager0197.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0197.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0197")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0197" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2000000, 2000000, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0198(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0198

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0198" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0198.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0198"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0198" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3000000, 3000000, 0))
        """
        wymodelmanager0198 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0198.wya', 'w+') as file:
            file.write("an TestArmatureObject0198\nmdllib TestModelFile0198\nbc 1\nbn TestArmatureBoneName0198\nbh 0.0 0.0 0.0\nbt 3000000 3000000.0 0\n")
        wyarmature = wymodelmanager0198.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0198.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0198")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0198" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3000000, 3000000, 0)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0199(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0199

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0199" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0199.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0199"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0199" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1, 0, 1))
        """
        wymodelmanager0199 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0199.wya', 'w+') as file:
            file.write("an TestArmatureObject0199\nmdllib TestModelFile0199\nbc 1\nbn TestArmatureBoneName0199\nbh 0.0 0.0 0.0\nbt 1 0.0 1\n")
        wyarmature = wymodelmanager0199.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0199.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0199")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0199" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1, 0, 1)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0200(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0200

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0200" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0200.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0200"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0200" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.1, 0, 0.1))
        """
        wymodelmanager0200 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0200.wya', 'w+') as file:
            file.write("an TestArmatureObject0200\nmdllib TestModelFile0200\nbc 1\nbn TestArmatureBoneName0200\nbh 0.0 0.0 0.0\nbt 0.1 0.0 0.1\n")
        wyarmature = wymodelmanager0200.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0200.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0200")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0200" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.1, 0, 0.1)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0201(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0201

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0201" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0201.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0201"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0201" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.001, 0, 0.001))
        """
        wymodelmanager0201 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0201.wya', 'w+') as file:
            file.write("an TestArmatureObject0201\nmdllib TestModelFile0201\nbc 1\nbn TestArmatureBoneName0201\nbh 0.0 0.0 0.0\nbt 0.001 0.0 0.001\n")
        wyarmature = wymodelmanager0201.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0201.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0201")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0201" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.001, 0, 0.001)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0202(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0202

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0202" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0202.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0202"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0202" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0001, 0, 0.0001))
        """
        wymodelmanager0202 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0202.wya', 'w+') as file:
            file.write("an TestArmatureObject0202\nmdllib TestModelFile0202\nbc 1\nbn TestArmatureBoneName0202\nbh 0.0 0.0 0.0\nbt 0.0001 0.0 0.0001\n")
        wyarmature = wymodelmanager0202.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0202.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0202")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0202" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0001, 0, 0.0001)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0203(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0203

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0203" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0203.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0203"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0203" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2, 0, 2))
        """
        wymodelmanager0203 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0203.wya', 'w+') as file:
            file.write("an TestArmatureObject0203\nmdllib TestModelFile0203\nbc 1\nbn TestArmatureBoneName0203\nbh 0.0 0.0 0.0\nbt 2 0.0 2\n")
        wyarmature = wymodelmanager0203.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0203.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0203")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0203" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2, 0, 2)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0204(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0204

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0204" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0204.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0204"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0204" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3, 0, 3))
        """
        wymodelmanager0204 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0204.wya', 'w+') as file:
            file.write("an TestArmatureObject0204\nmdllib TestModelFile0204\nbc 1\nbn TestArmatureBoneName0204\nbh 0.0 0.0 0.0\nbt 3 0.0 3\n")
        wyarmature = wymodelmanager0204.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0204.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0204")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0204" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3, 0, 3)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0205(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0205

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0205" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0205.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0205"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0205" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10, 0, 10))
        """
        wymodelmanager0205 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0205.wya', 'w+') as file:
            file.write("an TestArmatureObject0205\nmdllib TestModelFile0205\nbc 1\nbn TestArmatureBoneName0205\nbh 0.0 0.0 0.0\nbt 10 0.0 10\n")
        wyarmature = wymodelmanager0205.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0205.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0205")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0205" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10, 0, 10)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0206(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0206

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0206" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0206.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0206"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0206" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20, 0, 20))
        """
        wymodelmanager0206 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0206.wya', 'w+') as file:
            file.write("an TestArmatureObject0206\nmdllib TestModelFile0206\nbc 1\nbn TestArmatureBoneName0206\nbh 0.0 0.0 0.0\nbt 20 0.0 20\n")
        wyarmature = wymodelmanager0206.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0206.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0206")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0206" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20, 0, 20)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0207(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0207

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0207" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0207.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0207"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0207" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30, 0, 30))
        """
        wymodelmanager0207 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0207.wya', 'w+') as file:
            file.write("an TestArmatureObject0207\nmdllib TestModelFile0207\nbc 1\nbn TestArmatureBoneName0207\nbh 0.0 0.0 0.0\nbt 30 0.0 30\n")
        wyarmature = wymodelmanager0207.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0207.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0207")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0207" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30, 0, 30)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0208(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0208

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0208" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0208.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0208"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0208" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((100, 0, 100))
        """
        wymodelmanager0208 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0208.wya', 'w+') as file:
            file.write("an TestArmatureObject0208\nmdllib TestModelFile0208\nbc 1\nbn TestArmatureBoneName0208\nbh 0.0 0.0 0.0\nbt 100 0.0 100\n")
        wyarmature = wymodelmanager0208.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0208.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0208")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0208" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((100, 0, 100)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0209(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0209

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0209" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0209.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0209"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0209" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((200, 0, 200))
        """
        wymodelmanager0209 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0209.wya', 'w+') as file:
            file.write("an TestArmatureObject0209\nmdllib TestModelFile0209\nbc 1\nbn TestArmatureBoneName0209\nbh 0.0 0.0 0.0\nbt 200 0.0 200\n")
        wyarmature = wymodelmanager0209.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0209.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0209")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0209" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((200, 0, 200)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0210(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0210

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0210" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0210.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0210"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0210" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((300, 0, 300))
        """
        wymodelmanager0210 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0210.wya', 'w+') as file:
            file.write("an TestArmatureObject0210\nmdllib TestModelFile0210\nbc 1\nbn TestArmatureBoneName0210\nbh 0.0 0.0 0.0\nbt 300 0.0 300\n")
        wyarmature = wymodelmanager0210.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0210.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0210")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0210" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((300, 0, 300)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0211(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0211

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0211" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0211.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0211"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0211" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10000, 0,  10000))
        """
        wymodelmanager0211 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0211.wya', 'w+') as file:
            file.write("an TestArmatureObject0211\nmdllib TestModelFile0211\nbc 1\nbn TestArmatureBoneName0211\nbh 0.0 0.0 0.0\nbt 10000 0.0 10000\n")
        wyarmature = wymodelmanager0211.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0211.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0211")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0211" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10000, 0,  10000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0212(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0212

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0212" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0212.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0212"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0212" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20000, 0,  20000))
        """
        wymodelmanager0212 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0212.wya', 'w+') as file:
            file.write("an TestArmatureObject0212\nmdllib TestModelFile0212\nbc 1\nbn TestArmatureBoneName0212\nbh 0.0 0.0 0.0\nbt 20000 0.0 20000\n")
        wyarmature = wymodelmanager0212.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0212.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0212")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0212" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20000, 0,  20000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0213(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0213

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0213" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0213.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0213"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0213" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30000, 0,  30000))
        """
        wymodelmanager0213 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0213.wya', 'w+') as file:
            file.write("an TestArmatureObject0213\nmdllib TestModelFile0213\nbc 1\nbn TestArmatureBoneName0213\nbh 0.0 0.0 0.0\nbt 30000 0.0 30000\n")
        wyarmature = wymodelmanager0213.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0213.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0213")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0213" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30000, 0,  30000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0214(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0214

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0214" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0214.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0214"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0214" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1000000, 0,  1000000))
        """
        wymodelmanager0214 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0214.wya', 'w+') as file:
            file.write("an TestArmatureObject0214\nmdllib TestModelFile0214\nbc 1\nbn TestArmatureBoneName0214\nbh 0.0 0.0 0.0\nbt 1000000 0.0 1000000\n")
        wyarmature = wymodelmanager0214.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0214.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0214")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0214" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1000000, 0,  1000000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0215(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0215

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0215" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0215.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0215"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0215" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2000000, 0,  2000000))
        """
        wymodelmanager0215 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0215.wya', 'w+') as file:
            file.write("an TestArmatureObject0215\nmdllib TestModelFile0215\nbc 1\nbn TestArmatureBoneName0215\nbh 0.0 0.0 0.0\nbt 2000000 0.0 2000000\n")
        wyarmature = wymodelmanager0215.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0215.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0215")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0215" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2000000, 0,  2000000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0216(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0216

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0216" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0216.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0216"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0216" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3000000, 0,  3000000))
        """
        wymodelmanager0216 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0216.wya', 'w+') as file:
            file.write("an TestArmatureObject0216\nmdllib TestModelFile0216\nbc 1\nbn TestArmatureBoneName0216\nbh 0.0 0.0 0.0\nbt 3000000 0.0 3000000\n")
        wyarmature = wymodelmanager0216.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0216.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0216")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0216" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3000000, 0,  3000000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0217(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0217

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0217" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0217.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0217"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0217" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 1, 1))
        """
        wymodelmanager0217 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0217.wya', 'w+') as file:
            file.write("an TestArmatureObject0217\nmdllib TestModelFile0217\nbc 1\nbn TestArmatureBoneName0217\nbh 0.0 0.0 0.0\nbt 0 1.0 1\n")
        wyarmature = wymodelmanager0217.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0217.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0217")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0217" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 1, 1)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0218(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0218

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0218" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0218.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0218"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0218" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0.1, 0.1))
        """
        wymodelmanager0218 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0218.wya', 'w+') as file:
            file.write("an TestArmatureObject0218\nmdllib TestModelFile0218\nbc 1\nbn TestArmatureBoneName0218\nbh 0.0 0.0 0.0\nbt 0 0.1 0.1\n")
        wyarmature = wymodelmanager0218.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0218.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0218")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0218" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0.1, 0.1)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0219(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0219

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0219" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0219.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0219"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0219" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0.01, 0.001))
        """
        wymodelmanager0219 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0219.wya', 'w+') as file:
            file.write("an TestArmatureObject0219\nmdllib TestModelFile0219\nbc 1\nbn TestArmatureBoneName0219\nbh 0.0 0.0 0.0\nbt 0 0.01 0.001\n")
        wyarmature = wymodelmanager0219.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0219.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0219")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0219" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0.01, 0.001)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0220(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0220

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0220" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0220.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0220"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0220" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0.0001, 0.0001))
        """
        wymodelmanager0220 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0220.wya', 'w+') as file:
            file.write("an TestArmatureObject0220\nmdllib TestModelFile0220\nbc 1\nbn TestArmatureBoneName0220\nbh 0.0 0.0 0.0\nbt 0 0.0001 0.0001\n")
        wyarmature = wymodelmanager0220.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0220.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0220")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0220" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 0.0001, 0.0001)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0221(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0221

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0221" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0221.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0221"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0221" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 2, 2))
        """
        wymodelmanager0221 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0221.wya', 'w+') as file:
            file.write("an TestArmatureObject0221\nmdllib TestModelFile0221\nbc 1\nbn TestArmatureBoneName0221\nbh 0.0 0.0 0.0\nbt 0 2.0 2\n")
        wyarmature = wymodelmanager0221.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0221.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0221")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0221" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 2, 2)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0222(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0222

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0222" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0222.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0222"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0222" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 3, 3))
        """
        wymodelmanager0222 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0222.wya', 'w+') as file:
            file.write("an TestArmatureObject0222\nmdllib TestModelFile0222\nbc 1\nbn TestArmatureBoneName0222\nbh 0.0 0.0 0.0\nbt 0 3.0 3\n")
        wyarmature = wymodelmanager0222.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0222.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0222")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0222" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 3, 3)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0223(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0223

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0223" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0223.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0223"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0223" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 10, 10))
        """
        wymodelmanager0223 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0223.wya', 'w+') as file:
            file.write("an TestArmatureObject0223\nmdllib TestModelFile0223\nbc 1\nbn TestArmatureBoneName0223\nbh 0.0 0.0 0.0\nbt 0 10.0 10\n")
        wyarmature = wymodelmanager0223.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0223.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0223")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0223" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 10, 10)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0224(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0224

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0224" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0224.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0224"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0224" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 20, 20))
        """
        wymodelmanager0224 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0224.wya', 'w+') as file:
            file.write("an TestArmatureObject0224\nmdllib TestModelFile0224\nbc 1\nbn TestArmatureBoneName0224\nbh 0.0 0.0 0.0\nbt 0 20.0 20\n")
        wyarmature = wymodelmanager0224.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0224.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0224")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0224" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 20, 20)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0225(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0225

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0225" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0225.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0225"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0225" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 30, 30))
        """
        wymodelmanager0225 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0225.wya', 'w+') as file:
            file.write("an TestArmatureObject0225\nmdllib TestModelFile0225\nbc 1\nbn TestArmatureBoneName0225\nbh 0.0 0.0 0.0\nbt 0 30.0 30\n")
        wyarmature = wymodelmanager0225.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0225.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0225")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0225" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 30, 30)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0226(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0226

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0226" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0226.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0226"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0226" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 100, 100))
        """
        wymodelmanager0226 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0226.wya', 'w+') as file:
            file.write("an TestArmatureObject0226\nmdllib TestModelFile0226\nbc 1\nbn TestArmatureBoneName0226\nbh 0.0 0.0 0.0\nbt 0 100.0 100\n")
        wyarmature = wymodelmanager0226.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0226.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0226")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0226" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 100, 100)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0227(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0227

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0227" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0227.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0227"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0227" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 200, 200))
        """
        wymodelmanager0227 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0227.wya', 'w+') as file:
            file.write("an TestArmatureObject0227\nmdllib TestModelFile0227\nbc 1\nbn TestArmatureBoneName0227\nbh 0.0 0.0 0.0\nbt 0 200.0 200\n")
        wyarmature = wymodelmanager0227.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0227.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0227")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0227" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 200, 200)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0228(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0228

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0228" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0228.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0228"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0228" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 300, 300))
        """
        wymodelmanager0228 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0228.wya', 'w+') as file:
            file.write("an TestArmatureObject0228\nmdllib TestModelFile0228\nbc 1\nbn TestArmatureBoneName0228\nbh 0.0 0.0 0.0\nbt 0 300.0 300\n")
        wyarmature = wymodelmanager0228.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0228.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0228")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0228" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 300, 300)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0229(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0229

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0229" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0229.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0229"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0229" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 10000, 10000))
        """
        wymodelmanager0229 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0229.wya', 'w+') as file:
            file.write("an TestArmatureObject0229\nmdllib TestModelFile0229\nbc 1\nbn TestArmatureBoneName0229\nbh 0.0 0.0 0.0\nbt 0 10000.0 10000\n")
        wyarmature = wymodelmanager0229.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0229.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0229")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0229" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 10000, 10000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0230(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0230

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0230" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0230.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0230"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0230" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 20000, 20000))
        """
        wymodelmanager0230 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0230.wya', 'w+') as file:
            file.write("an TestArmatureObject0230\nmdllib TestModelFile0230\nbc 1\nbn TestArmatureBoneName0230\nbh 0.0 0.0 0.0\nbt 0 20000.0 20000\n")
        wyarmature = wymodelmanager0230.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0230.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0230")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0230" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 20000, 20000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0231(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0231

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0231" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0231.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0231"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0231" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 30000, 30000))
        """
        wymodelmanager0231 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0231.wya', 'w+') as file:
            file.write("an TestArmatureObject0231\nmdllib TestModelFile0231\nbc 1\nbn TestArmatureBoneName0231\nbh 0.0 0.0 0.0\nbt 0 30000.0 30000\n")
        wyarmature = wymodelmanager0231.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0231.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0231")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0231" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 30000, 30000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0232(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0232

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0232" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0232.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0232"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0232" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 1000000, 1000000))
        """
        wymodelmanager0232 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0232.wya', 'w+') as file:
            file.write("an TestArmatureObject0232\nmdllib TestModelFile0232\nbc 1\nbn TestArmatureBoneName0232\nbh 0.0 0.0 0.0\nbt 0 1000000.0 1000000\n")
        wyarmature = wymodelmanager0232.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0232.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0232")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0232" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 1000000, 1000000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0233(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0233

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0233" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0233.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0233"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0233" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 2000000, 2000000))
        """
        wymodelmanager0233 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0233.wya', 'w+') as file:
            file.write("an TestArmatureObject0233\nmdllib TestModelFile0233\nbc 1\nbn TestArmatureBoneName0233\nbh 0.0 0.0 0.0\nbt 0 2000000.0 2000000\n")
        wyarmature = wymodelmanager0233.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0233.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0233")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0233" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 2000000, 2000000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0234(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0234

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0234" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0234.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0234"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0234" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 3000000, 3000000))
        """
        wymodelmanager0234 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0234.wya', 'w+') as file:
            file.write("an TestArmatureObject0234\nmdllib TestModelFile0234\nbc 1\nbn TestArmatureBoneName0234\nbh 0.0 0.0 0.0\nbt 0 3000000.0 3000000\n")
        wyarmature = wymodelmanager0234.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0234.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0234")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0234" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0, 3000000, 3000000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0235(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0235

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0235" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0235.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0235"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0235" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1, 1, 1))
        """
        wymodelmanager0235 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0235.wya', 'w+') as file:
            file.write("an TestArmatureObject0235\nmdllib TestModelFile0235\nbc 1\nbn TestArmatureBoneName0235\nbh 0.0 0.0 0.0\nbt 1 1.0 1\n")
        wyarmature = wymodelmanager0235.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0235.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0235")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0235" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1, 1, 1)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0236(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0236

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0236" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0236.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0236"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0236" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.1, 0.1, 0.1))
        """
        wymodelmanager0236 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0236.wya', 'w+') as file:
            file.write("an TestArmatureObject0236\nmdllib TestModelFile0236\nbc 1\nbn TestArmatureBoneName0236\nbh 0.0 0.0 0.0\nbt 0.1 0.1 0.1\n")
        wyarmature = wymodelmanager0236.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0236.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0236")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0236" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.1, 0.1, 0.1)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0237(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0237

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0237" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0237.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0237"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0237" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.001, 0.01, 0.001))
        """
        wymodelmanager0237 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0237.wya', 'w+') as file:
            file.write("an TestArmatureObject0237\nmdllib TestModelFile0237\nbc 1\nbn TestArmatureBoneName0237\nbh 0.0 0.0 0.0\nbt 0.001 0.01 0.001\n")
        wyarmature = wymodelmanager0237.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0237.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0237")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0237" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.001, 0.01, 0.001)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0238(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0238

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0238" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0238.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0238"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0238" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0001, 0.0001, 0.0001))
        """
        wymodelmanager0238 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0238.wya', 'w+') as file:
            file.write("an TestArmatureObject0238\nmdllib TestModelFile0238\nbc 1\nbn TestArmatureBoneName0238\nbh 0.0 0.0 0.0\nbt 0.0001 0.0001 0.0001\n")
        wyarmature = wymodelmanager0238.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0238.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0238")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0238" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((0.0001, 0.0001, 0.0001)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0239(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0239

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0239" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0239.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0239"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0239" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2, 2, 2))
        """
        wymodelmanager0239 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0239.wya', 'w+') as file:
            file.write("an TestArmatureObject0239\nmdllib TestModelFile0239\nbc 1\nbn TestArmatureBoneName0239\nbh 0.0 0.0 0.0\nbt 2 2.0 2\n")
        wyarmature = wymodelmanager0239.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0239.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0239")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0239" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2, 2, 2)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0240(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0240

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0240" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0240.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0240"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0240" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3, 3, 3))
        """
        wymodelmanager0240 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0240.wya', 'w+') as file:
            file.write("an TestArmatureObject0240\nmdllib TestModelFile0240\nbc 1\nbn TestArmatureBoneName0240\nbh 0.0 0.0 0.0\nbt 3 3.0 3\n")
        wyarmature = wymodelmanager0240.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0240.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0240")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0240" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3, 3, 3)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0241(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0241

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0241" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0241.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0241"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0241" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10, 10, 10))
        """
        wymodelmanager0241 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0241.wya', 'w+') as file:
            file.write("an TestArmatureObject0241\nmdllib TestModelFile0241\nbc 1\nbn TestArmatureBoneName0241\nbh 0.0 0.0 0.0\nbt 10 10.0 10\n")
        wyarmature = wymodelmanager0241.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0241.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0241")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0241" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10, 10, 10)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0242(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0242

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0242" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0242.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0242"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0242" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20, 20, 20))
        """
        wymodelmanager0242 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0242.wya', 'w+') as file:
            file.write("an TestArmatureObject0242\nmdllib TestModelFile0242\nbc 1\nbn TestArmatureBoneName0242\nbh 0.0 0.0 0.0\nbt 20 20.0 20\n")
        wyarmature = wymodelmanager0242.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0242.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0242")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0242" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20, 20, 20)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0243(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0243

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0243" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0243.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0243"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0243" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30, 30, 30))
        """
        wymodelmanager0243 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0243.wya', 'w+') as file:
            file.write("an TestArmatureObject0243\nmdllib TestModelFile0243\nbc 1\nbn TestArmatureBoneName0243\nbh 0.0 0.0 0.0\nbt 30 30.0 30\n")
        wyarmature = wymodelmanager0243.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0243.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0243")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0243" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30, 30, 30)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0244(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0244

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0244" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0244.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0244"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0244" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((100, 100, 100))
        """
        wymodelmanager0244 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0244.wya', 'w+') as file:
            file.write("an TestArmatureObject0244\nmdllib TestModelFile0244\nbc 1\nbn TestArmatureBoneName0244\nbh 0.0 0.0 0.0\nbt 100 100.0 100\n")
        wyarmature = wymodelmanager0244.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0244.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0244")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0244" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((100, 100, 100)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0245(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0245

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0245" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0245.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0245"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0245" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((200, 200, 200))
        """
        wymodelmanager0245 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0245.wya', 'w+') as file:
            file.write("an TestArmatureObject0245\nmdllib TestModelFile0245\nbc 1\nbn TestArmatureBoneName0245\nbh 0.0 0.0 0.0\nbt 200 200.0 200\n")
        wyarmature = wymodelmanager0245.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0245.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0245")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0245" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((200, 200, 200)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0246(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0246

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0246" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0246.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0246"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0246" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((300, 300, 300))
        """
        wymodelmanager0246 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0246.wya', 'w+') as file:
            file.write("an TestArmatureObject0246\nmdllib TestModelFile0246\nbc 1\nbn TestArmatureBoneName0246\nbh 0.0 0.0 0.0\nbt 300 300.0 300\n")
        wyarmature = wymodelmanager0246.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0246.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0246")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0246" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((300, 300, 300)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0247(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0247

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0247" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0247.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0247"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0247" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10000, 10000, 10000))
        """
        wymodelmanager0247 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0247.wya', 'w+') as file:
            file.write("an TestArmatureObject0247\nmdllib TestModelFile0247\nbc 1\nbn TestArmatureBoneName0247\nbh 0.0 0.0 0.0\nbt 10000 10000.0 10000\n")
        wyarmature = wymodelmanager0247.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0247.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0247")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0247" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((10000, 10000, 10000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0248(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0248

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0248" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0248.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0248"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0248" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20000, 20000, 20000))
        """
        wymodelmanager0248 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0248.wya', 'w+') as file:
            file.write("an TestArmatureObject0248\nmdllib TestModelFile0248\nbc 1\nbn TestArmatureBoneName0248\nbh 0.0 0.0 0.0\nbt 20000 20000.0 20000\n")
        wyarmature = wymodelmanager0248.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0248.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0248")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0248" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((20000, 20000, 20000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0249(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0249

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0249" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0249.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0249"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0249" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30000, 30000, 30000))
        """
        wymodelmanager0249 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0249.wya', 'w+') as file:
            file.write("an TestArmatureObject0249\nmdllib TestModelFile0249\nbc 1\nbn TestArmatureBoneName0249\nbh 0.0 0.0 0.0\nbt 30000 30000.0 30000\n")
        wyarmature = wymodelmanager0249.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0249.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0249")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0249" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((30000, 30000, 30000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0250(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0250

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0250" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0250.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0250"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0250" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1000000, 1000000, 1000000))
        """
        wymodelmanager0250 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0250.wya', 'w+') as file:
            file.write("an TestArmatureObject0250\nmdllib TestModelFile0250\nbc 1\nbn TestArmatureBoneName0250\nbh 0.0 0.0 0.0\nbt 1000000 1000000.0 1000000\n")
        wyarmature = wymodelmanager0250.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0250.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0250")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0250" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((1000000, 1000000, 1000000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0251(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0251

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0251" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0251.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0251"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0251" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2000000, 2000000, 2000000))
        """
        wymodelmanager0251 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0251.wya', 'w+') as file:
            file.write("an TestArmatureObject0251\nmdllib TestModelFile0251\nbc 1\nbn TestArmatureBoneName0251\nbh 0.0 0.0 0.0\nbt 2000000 2000000.0 2000000\n")
        wyarmature = wymodelmanager0251.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0251.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0251")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0251" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((2000000, 2000000, 2000000)))
    def test_WYModelManagerTestCase_import_armature_TC_NC_0252(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_armature function testing normal case 0252

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the Blender armature object is imported from given path "..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0252" through "import_armature" function resulting the imported Blender armature object data values are equal to the exported values.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature_file_path: String of the file path to import the WYArmature object from..
        :type  wyarmature_file_path: string.
        :test  wyarmature_file_path: os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0252.wya'.

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.main_armature_obj.name == "TestArmatureObject0252"
        :expect: len(wyarmature.main_armature_obj.data.bones) == 1
        :expect: wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0252" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3000000, 3000000, 3000000))
        """
        wymodelmanager0252 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0252.wya', 'w+') as file:
            file.write("an TestArmatureObject0252\nmdllib TestModelFile0252\nbc 1\nbn TestArmatureBoneName0252\nbh 0.0 0.0 0.0\nbt 3000000 3000000.0 3000000\n")
        wyarmature = wymodelmanager0252.import_armature(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_armature\\TestFile0252.wya') 
        self.assertTrue(wyarmature.main_armature_obj.name == "TestArmatureObject0252")
        self.assertTrue(len(wyarmature.main_armature_obj.data.bones) == 1)
        self.assertTrue(wyarmature.main_armature_obj.data.bones[0].name == "TestArmatureBoneName0252" and wyarmature.main_armature_obj.data.bones[0].head == Vector((0.0,0.0,0.0)) and wyarmature.main_armature_obj.data.bones[0].tail == Vector((3000000, 3000000, 3000000)))

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_import_armature))
