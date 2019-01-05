"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2018-01-22
Last update                         : 2018-01-22
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_import_wyarmaturebone\WYModelManagerTestCases_import_wyarmaturebone.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_import_wyarmaturebone\WYModelManagerTestCases_import_wyarmaturebone.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : import_wyarmaturebone(wyarmature, wyarmature_file_obj)
Unit test case class name           : WYModelManagerTestCases_import_wyarmaturebone
Unit test case description          : Unit test case for class WYModelManager import_wyarmaturebone() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_import_wyarmaturebone\WYModelManagerTestCaseResult_import_wyarmaturebone.txt
"""
# Pre-condition: WYArmature is tested.
# Pre-condition: WYArmatureBone is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_import_wyarmaturebone(unittest.TestCase):
    """
    Unit test case for class WYModelManager import_wyarmaturebone() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :252
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0001" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0001" head (1, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0001.wya','w+')asfile:
file.write("bnTestArmatureBoneName0001\nbh10.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0001"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (1, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0001 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0001.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0001\nbh 1 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0001.wya') as content_file:
            wymodelmanager0001.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0001")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (1, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0002" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0002" head (0.1, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0002.wya','w+')asfile:
file.write("bnTestArmatureBoneName0002\nbh0.10.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0002"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.1, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0002 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0002.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0002\nbh 0.1 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0002.wya') as content_file:
            wymodelmanager0002.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0002")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.1, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0003" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0003" head (0.001, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0003.wya','w+')asfile:
file.write("bnTestArmatureBoneName0003\nbh0.0010.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0003"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.001, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0003 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0003.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0003\nbh 0.001 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0003.wya') as content_file:
            wymodelmanager0003.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0003")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.001, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0004" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0004" head (0.0001, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0004.wya','w+')asfile:
file.write("bnTestArmatureBoneName0004\nbh0.00010.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0004"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0001, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0004 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0004.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0004\nbh 0.0001 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0004.wya') as content_file:
            wymodelmanager0004.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0004")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0001, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0005" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0005" head (2, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0005.wya','w+')asfile:
file.write("bnTestArmatureBoneName0005\nbh20.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0005"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (2, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0005 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0005.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0005\nbh 2 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0005.wya') as content_file:
            wymodelmanager0005.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0005")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (2, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0006" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0006" head (3, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0006.wya','w+')asfile:
file.write("bnTestArmatureBoneName0006\nbh30.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0006"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (3, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0006 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0006.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0006\nbh 3 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0006.wya') as content_file:
            wymodelmanager0006.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0006")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (3, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0007" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0007" head (10, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0007.wya','w+')asfile:
file.write("bnTestArmatureBoneName0007\nbh100.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0007"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (10, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0007 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0007.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0007\nbh 10 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0007.wya') as content_file:
            wymodelmanager0007.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0007")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (10, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0008" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0008" head (20, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0008.wya','w+')asfile:
file.write("bnTestArmatureBoneName0008\nbh200.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0008"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (20, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0008 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0008.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0008\nbh 20 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0008.wya') as content_file:
            wymodelmanager0008.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0008")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (20, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0009" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0009" head (30, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0009.wya','w+')asfile:
file.write("bnTestArmatureBoneName0009\nbh300.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0009"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (30, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0009 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0009.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0009\nbh 30 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0009.wya') as content_file:
            wymodelmanager0009.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0009")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (30, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0010" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0010" head (100, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0010.wya','w+')asfile:
file.write("bnTestArmatureBoneName0010\nbh1000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0010"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (100, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0010 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0010.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0010\nbh 100 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0010.wya') as content_file:
            wymodelmanager0010.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0010")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (100, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0011(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0011

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0011" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0011" head (200, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0011.wya','w+')asfile:
file.write("bnTestArmatureBoneName0011\nbh2000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0011"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (200, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0011 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0011.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0011\nbh 200 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0011.wya') as content_file:
            wymodelmanager0011.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0011")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (200, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0012(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0012

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0012" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0012" head (300, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0012.wya','w+')asfile:
file.write("bnTestArmatureBoneName0012\nbh3000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0012"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (300, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0012 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0012.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0012\nbh 300 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0012.wya') as content_file:
            wymodelmanager0012.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0012")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (300, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0013(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0013

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0013" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0013" head (10000, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0013.wya','w+')asfile:
file.write("bnTestArmatureBoneName0013\nbh100000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0013"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (10000, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0013 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0013.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0013\nbh 10000 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0013.wya') as content_file:
            wymodelmanager0013.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0013")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (10000, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0014(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0014

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0014" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0014" head (20000, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0014.wya','w+')asfile:
file.write("bnTestArmatureBoneName0014\nbh200000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0014"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (20000, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0014 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0014.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0014\nbh 20000 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0014.wya') as content_file:
            wymodelmanager0014.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0014")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (20000, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0015(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0015

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0015" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0015" head (30000, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0015.wya','w+')asfile:
file.write("bnTestArmatureBoneName0015\nbh300000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0015"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (30000, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0015 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0015.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0015\nbh 30000 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0015.wya') as content_file:
            wymodelmanager0015.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0015")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (30000, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0016(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0016

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0016" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0016" head (1000000, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0016.wya','w+')asfile:
file.write("bnTestArmatureBoneName0016\nbh10000000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0016"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (1000000, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0016 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0016.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0016\nbh 1000000 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0016.wya') as content_file:
            wymodelmanager0016.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0016")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (1000000, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0017(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0017

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0017" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0017" head (2000000, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0017.wya','w+')asfile:
file.write("bnTestArmatureBoneName0017\nbh20000000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0017"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (2000000, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0017 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0017.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0017\nbh 2000000 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0017.wya') as content_file:
            wymodelmanager0017.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0017")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (2000000, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0018(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0018

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0018" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0018" head (3000000, 0, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0018.wya','w+')asfile:
file.write("bnTestArmatureBoneName0018\nbh30000000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0018"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (3000000, 0, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0018 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0018.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0018\nbh 3000000 0.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0018.wya') as content_file:
            wymodelmanager0018.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0018")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (3000000, 0, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0019(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0019

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0019" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0019" head (0, 1, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0019.wya','w+')asfile:
file.write("bnTestArmatureBoneName0019\nbh01.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0019"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 1, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0019 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0019.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0019\nbh 0 1.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0019.wya') as content_file:
            wymodelmanager0019.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0019")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 1, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0020(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0020

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0020" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0020" head (0, 0.1, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0020.wya','w+')asfile:
file.write("bnTestArmatureBoneName0020\nbh00.10\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0020"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0.1, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0020 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0020.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0020\nbh 0 0.1 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0020.wya') as content_file:
            wymodelmanager0020.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0020")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0.1, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0021(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0021

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0021" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0021" head (0, 0.001, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0021.wya','w+')asfile:
file.write("bnTestArmatureBoneName0021\nbh00.0010\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0021"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0.001, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0021 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0021.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0021\nbh 0 0.001 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0021.wya') as content_file:
            wymodelmanager0021.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0021")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0.001, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0022(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0022

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0022" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0022" head (0, 0.0001, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0022.wya','w+')asfile:
file.write("bnTestArmatureBoneName0022\nbh00.00010\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0022"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0.0001, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0022 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0022.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0022\nbh 0 0.0001 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0022.wya') as content_file:
            wymodelmanager0022.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0022")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0.0001, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0023(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0023

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0023" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0023" head (0, 2, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0023.wya','w+')asfile:
file.write("bnTestArmatureBoneName0023\nbh02.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0023"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 2, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0023 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0023.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0023\nbh 0 2.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0023.wya') as content_file:
            wymodelmanager0023.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0023")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 2, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0024(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0024

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0024" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0024" head (0, 3, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0024.wya','w+')asfile:
file.write("bnTestArmatureBoneName0024\nbh03.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0024"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 3, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0024 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0024.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0024\nbh 0 3.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0024.wya') as content_file:
            wymodelmanager0024.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0024")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 3, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0025(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0025

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0025" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0025" head (0, 10, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0025.wya','w+')asfile:
file.write("bnTestArmatureBoneName0025\nbh010.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0025"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 10, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0025 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0025.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0025\nbh 0 10.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0025.wya') as content_file:
            wymodelmanager0025.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0025")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 10, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0026(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0026

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0026" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0026" head (0, 20, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0026.wya','w+')asfile:
file.write("bnTestArmatureBoneName0026\nbh020.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0026"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 20, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0026 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0026.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0026\nbh 0 20.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0026.wya') as content_file:
            wymodelmanager0026.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0026")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 20, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0027(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0027

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0027" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0027" head (0, 30, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0027.wya','w+')asfile:
file.write("bnTestArmatureBoneName0027\nbh030.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0027"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 30, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0027 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0027.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0027\nbh 0 30.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0027.wya') as content_file:
            wymodelmanager0027.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0027")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 30, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0028(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0028

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0028" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0028" head (0, 100, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0028.wya','w+')asfile:
file.write("bnTestArmatureBoneName0028\nbh0100.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0028"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 100, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0028 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0028.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0028\nbh 0 100.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0028.wya') as content_file:
            wymodelmanager0028.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0028")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 100, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0029(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0029

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0029" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0029" head (0, 200, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0029.wya','w+')asfile:
file.write("bnTestArmatureBoneName0029\nbh0200.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0029"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 200, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0029 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0029.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0029\nbh 0 200.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0029.wya') as content_file:
            wymodelmanager0029.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0029")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 200, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0030(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0030

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0030" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0030" head (0, 300, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0030.wya','w+')asfile:
file.write("bnTestArmatureBoneName0030\nbh0300.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0030"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 300, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0030 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0030.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0030\nbh 0 300.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0030.wya') as content_file:
            wymodelmanager0030.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0030")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 300, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0031(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0031

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0031" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0031" head (0, 10000, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0031.wya','w+')asfile:
file.write("bnTestArmatureBoneName0031\nbh010000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0031"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 10000, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0031 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0031.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0031\nbh 0 10000.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0031.wya') as content_file:
            wymodelmanager0031.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0031")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 10000, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0032(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0032

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0032" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0032" head (0, 20000, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0032.wya','w+')asfile:
file.write("bnTestArmatureBoneName0032\nbh020000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0032"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 20000, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0032 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0032.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0032\nbh 0 20000.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0032.wya') as content_file:
            wymodelmanager0032.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0032")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 20000, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0033(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0033

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0033" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0033" head (0, 30000, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0033.wya','w+')asfile:
file.write("bnTestArmatureBoneName0033\nbh030000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0033"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 30000, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0033 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0033.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0033\nbh 0 30000.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0033.wya') as content_file:
            wymodelmanager0033.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0033")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 30000, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0034(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0034

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0034" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0034" head (0, 1000000, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0034.wya','w+')asfile:
file.write("bnTestArmatureBoneName0034\nbh01000000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0034"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 1000000, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0034 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0034.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0034\nbh 0 1000000.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0034.wya') as content_file:
            wymodelmanager0034.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0034")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 1000000, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0035(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0035

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0035" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0035" head (0, 2000000, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0035.wya','w+')asfile:
file.write("bnTestArmatureBoneName0035\nbh02000000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0035"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 2000000, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0035 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0035.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0035\nbh 0 2000000.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0035.wya') as content_file:
            wymodelmanager0035.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0035")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 2000000, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0036(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0036

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0036" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0036" head (0, 3000000, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0036.wya','w+')asfile:
file.write("bnTestArmatureBoneName0036\nbh03000000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0036"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 3000000, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0036 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0036.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0036\nbh 0 3000000.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0036.wya') as content_file:
            wymodelmanager0036.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0036")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 3000000, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0037(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0037

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0037" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0037" head (0, 0, 1) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0037.wya','w+')asfile:
file.write("bnTestArmatureBoneName0037\nbh00.01\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0037"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 1)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0037 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0037.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0037\nbh 0 0.0 1\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0037.wya') as content_file:
            wymodelmanager0037.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0037")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 1))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0038(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0038

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0038" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0038" head (0, 0, 0.1) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0038.wya','w+')asfile:
file.write("bnTestArmatureBoneName0038\nbh00.00.1\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0038"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 0.1)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0038 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0038.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0038\nbh 0 0.0 0.1\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0038.wya') as content_file:
            wymodelmanager0038.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0038")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 0.1))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0039(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0039

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0039" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0039" head (0, 0, 0.001) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0039.wya','w+')asfile:
file.write("bnTestArmatureBoneName0039\nbh00.00.001\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0039"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 0.001)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0039 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0039.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0039\nbh 0 0.0 0.001\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0039.wya') as content_file:
            wymodelmanager0039.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0039")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 0.001))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0040(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0040

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0040" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0040" head (0, 0, 0.0001) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0040.wya','w+')asfile:
file.write("bnTestArmatureBoneName0040\nbh00.00.0001\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0040"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 0.0001)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0040 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0040.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0040\nbh 0 0.0 0.0001\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0040.wya') as content_file:
            wymodelmanager0040.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0040")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 0.0001))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0041(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0041

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0041" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0041" head (0, 0, 2) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0041.wya','w+')asfile:
file.write("bnTestArmatureBoneName0041\nbh00.02\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0041"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 2)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0041 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0041.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0041\nbh 0 0.0 2\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0041.wya') as content_file:
            wymodelmanager0041.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0041")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 2))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0042(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0042

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0042" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0042" head (0, 0, 3) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0042.wya','w+')asfile:
file.write("bnTestArmatureBoneName0042\nbh00.03\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0042"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 3)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0042 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0042.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0042\nbh 0 0.0 3\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0042.wya') as content_file:
            wymodelmanager0042.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0042")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 3))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0043(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0043

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0043" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0043" head (0, 0, 10) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0043.wya','w+')asfile:
file.write("bnTestArmatureBoneName0043\nbh00.010\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0043"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 10)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0043 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0043.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0043\nbh 0 0.0 10\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0043.wya') as content_file:
            wymodelmanager0043.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0043")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 10))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0044(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0044

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0044" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0044" head (0, 0, 20) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0044.wya','w+')asfile:
file.write("bnTestArmatureBoneName0044\nbh00.020\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0044"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 20)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0044 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0044.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0044\nbh 0 0.0 20\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0044.wya') as content_file:
            wymodelmanager0044.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0044")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 20))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0045(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0045

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0045" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0045" head (0, 0, 30) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0045.wya','w+')asfile:
file.write("bnTestArmatureBoneName0045\nbh00.030\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0045"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 30)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0045 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0045.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0045\nbh 0 0.0 30\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0045.wya') as content_file:
            wymodelmanager0045.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0045")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 30))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0046(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0046

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0046" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0046" head (0, 0, 100) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0046.wya','w+')asfile:
file.write("bnTestArmatureBoneName0046\nbh00.0100\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0046"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 100)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0046 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0046.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0046\nbh 0 0.0 100\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0046.wya') as content_file:
            wymodelmanager0046.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0046")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 100))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0047(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0047

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0047" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0047" head (0, 0, 200) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0047.wya','w+')asfile:
file.write("bnTestArmatureBoneName0047\nbh00.0200\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0047"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 200)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0047 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0047.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0047\nbh 0 0.0 200\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0047.wya') as content_file:
            wymodelmanager0047.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0047")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 200))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0048(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0048

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0048" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0048" head (0, 0, 300) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0048.wya','w+')asfile:
file.write("bnTestArmatureBoneName0048\nbh00.0300\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0048"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 300)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0048 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0048.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0048\nbh 0 0.0 300\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0048.wya') as content_file:
            wymodelmanager0048.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0048")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 300))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0049(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0049

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0049" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0049" head (0, 0, 10000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0049.wya','w+')asfile:
file.write("bnTestArmatureBoneName0049\nbh00.010000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0049"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 10000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0049 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0049.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0049\nbh 0 0.0 10000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0049.wya') as content_file:
            wymodelmanager0049.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0049")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 10000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0050(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0050

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0050" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0050" head (0, 0, 20000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0050.wya','w+')asfile:
file.write("bnTestArmatureBoneName0050\nbh00.020000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0050"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 20000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0050 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0050.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0050\nbh 0 0.0 20000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0050.wya') as content_file:
            wymodelmanager0050.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0050")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 20000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0051(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0051

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0051" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0051" head (0, 0, 30000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0051.wya','w+')asfile:
file.write("bnTestArmatureBoneName0051\nbh00.030000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0051"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 30000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0051 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0051.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0051\nbh 0 0.0 30000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0051.wya') as content_file:
            wymodelmanager0051.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0051")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 30000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0052(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0052

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0052" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0052" head (0, 0, 1000000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0052.wya','w+')asfile:
file.write("bnTestArmatureBoneName0052\nbh00.01000000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0052"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 1000000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0052 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0052.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0052\nbh 0 0.0 1000000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0052.wya') as content_file:
            wymodelmanager0052.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0052")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 1000000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0053(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0053

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0053" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0053" head (0, 0, 2000000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0053.wya','w+')asfile:
file.write("bnTestArmatureBoneName0053\nbh00.02000000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0053"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 2000000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0053 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0053.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0053\nbh 0 0.0 2000000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0053.wya') as content_file:
            wymodelmanager0053.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0053")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 2000000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0054(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0054

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0054" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0054" head (0, 0, 3000000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0054.wya','w+')asfile:
file.write("bnTestArmatureBoneName0054\nbh00.03000000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0054"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 3000000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0054 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0054.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0054\nbh 0 0.0 3000000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0054.wya') as content_file:
            wymodelmanager0054.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0054")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0, 3000000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0055(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0055

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0055" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0055" head (1, 1, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0055.wya','w+')asfile:
file.write("bnTestArmatureBoneName0055\nbh11.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0055"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (1, 1, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0055 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0055.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0055\nbh 1 1.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0055.wya') as content_file:
            wymodelmanager0055.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0055")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (1, 1, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0056(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0056

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0056" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0056" head (0.1, 0.1, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0056.wya','w+')asfile:
file.write("bnTestArmatureBoneName0056\nbh0.10.10\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0056"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.1, 0.1, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0056 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0056.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0056\nbh 0.1 0.1 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0056.wya') as content_file:
            wymodelmanager0056.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0056")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.1, 0.1, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0057(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0057

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0057" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0057" head (0.001, 0.001, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0057.wya','w+')asfile:
file.write("bnTestArmatureBoneName0057\nbh0.0010.0010\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0057"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.001, 0.001, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0057 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0057.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0057\nbh 0.001 0.001 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0057.wya') as content_file:
            wymodelmanager0057.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0057")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.001, 0.001, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0058(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0058

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0058" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0058" head (0.0001, 0.0001, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0058.wya','w+')asfile:
file.write("bnTestArmatureBoneName0058\nbh0.00010.00010\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0058"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0001, 0.0001, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0058 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0058.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0058\nbh 0.0001 0.0001 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0058.wya') as content_file:
            wymodelmanager0058.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0058")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0001, 0.0001, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0059(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0059

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0059" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0059" head (2, 2, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0059.wya','w+')asfile:
file.write("bnTestArmatureBoneName0059\nbh22.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0059"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (2, 2, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0059 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0059.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0059\nbh 2 2.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0059.wya') as content_file:
            wymodelmanager0059.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0059")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (2, 2, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0060(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0060

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0060" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0060" head (3, 3, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0060.wya','w+')asfile:
file.write("bnTestArmatureBoneName0060\nbh33.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0060"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (3, 3, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0060 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0060.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0060\nbh 3 3.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0060.wya') as content_file:
            wymodelmanager0060.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0060")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (3, 3, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0061(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0061

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0061" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0061" head (10, 10, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0061.wya','w+')asfile:
file.write("bnTestArmatureBoneName0061\nbh1010.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0061"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (10, 10, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0061 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0061.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0061\nbh 10 10.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0061.wya') as content_file:
            wymodelmanager0061.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0061")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (10, 10, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0062(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0062

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0062" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0062" head (20, 20, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0062.wya','w+')asfile:
file.write("bnTestArmatureBoneName0062\nbh2020.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0062"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (20, 20, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0062 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0062.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0062\nbh 20 20.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0062.wya') as content_file:
            wymodelmanager0062.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0062")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (20, 20, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0063(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0063

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0063" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0063" head (30, 30, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0063.wya','w+')asfile:
file.write("bnTestArmatureBoneName0063\nbh3030.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0063"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (30, 30, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0063 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0063.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0063\nbh 30 30.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0063.wya') as content_file:
            wymodelmanager0063.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0063")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (30, 30, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0064(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0064

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0064" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0064" head (100, 100, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0064.wya','w+')asfile:
file.write("bnTestArmatureBoneName0064\nbh100100.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0064"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (100, 100, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0064 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0064.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0064\nbh 100 100.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0064.wya') as content_file:
            wymodelmanager0064.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0064")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (100, 100, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0065(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0065

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0065" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0065" head (200, 200, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0065.wya','w+')asfile:
file.write("bnTestArmatureBoneName0065\nbh200200.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0065"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (200, 200, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0065 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0065.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0065\nbh 200 200.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0065.wya') as content_file:
            wymodelmanager0065.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0065")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (200, 200, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0066(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0066

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0066" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0066" head (300, 300, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0066.wya','w+')asfile:
file.write("bnTestArmatureBoneName0066\nbh300300.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0066"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (300, 300, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0066 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0066.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0066\nbh 300 300.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0066.wya') as content_file:
            wymodelmanager0066.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0066")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (300, 300, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0067(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0067

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0067" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0067" head (10000, 10000, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0067.wya','w+')asfile:
file.write("bnTestArmatureBoneName0067\nbh1000010000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0067"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (10000, 10000, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0067 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0067.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0067\nbh 10000 10000.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0067.wya') as content_file:
            wymodelmanager0067.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0067")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (10000, 10000, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0068(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0068

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0068" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0068" head (20000, 20000, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0068.wya','w+')asfile:
file.write("bnTestArmatureBoneName0068\nbh2000020000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0068"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (20000, 20000, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0068 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0068.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0068\nbh 20000 20000.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0068.wya') as content_file:
            wymodelmanager0068.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0068")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (20000, 20000, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0069(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0069

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0069" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0069" head (30000, 30000, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0069.wya','w+')asfile:
file.write("bnTestArmatureBoneName0069\nbh3000030000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0069"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (30000, 30000, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0069 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0069.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0069\nbh 30000 30000.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0069.wya') as content_file:
            wymodelmanager0069.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0069")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (30000, 30000, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0070(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0070

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0070" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0070" head (1000000, 1000000, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0070.wya','w+')asfile:
file.write("bnTestArmatureBoneName0070\nbh10000001000000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0070"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (1000000, 1000000, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0070 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0070.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0070\nbh 1000000 1000000.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0070.wya') as content_file:
            wymodelmanager0070.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0070")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (1000000, 1000000, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0071(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0071

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0071" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0071" head (2000000, 2000000, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0071.wya','w+')asfile:
file.write("bnTestArmatureBoneName0071\nbh20000002000000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0071"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (2000000, 2000000, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0071 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0071.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0071\nbh 2000000 2000000.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0071.wya') as content_file:
            wymodelmanager0071.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0071")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (2000000, 2000000, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0072(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0072

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0072" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0072" head (3000000, 3000000, 0) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0072.wya','w+')asfile:
file.write("bnTestArmatureBoneName0072\nbh30000003000000.00\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0072"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (3000000, 3000000, 0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0072 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0072.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0072\nbh 3000000 3000000.0 0\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0072.wya') as content_file:
            wymodelmanager0072.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0072")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (3000000, 3000000, 0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0073(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0073

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0073" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0073" head (1, 0, 1) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0073.wya','w+')asfile:
file.write("bnTestArmatureBoneName0073\nbh10.01\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0073"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (1, 0, 1)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0073 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0073.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0073\nbh 1 0.0 1\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0073.wya') as content_file:
            wymodelmanager0073.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0073")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (1, 0, 1))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0074(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0074

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0074" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0074" head (0.1, 0, 0.1) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0074.wya','w+')asfile:
file.write("bnTestArmatureBoneName0074\nbh0.10.00.1\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0074"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.1, 0, 0.1)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0074 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0074.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0074\nbh 0.1 0.0 0.1\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0074.wya') as content_file:
            wymodelmanager0074.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0074")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.1, 0, 0.1))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0075(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0075

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0075" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0075" head (0.001, 0, 0.001) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0075.wya','w+')asfile:
file.write("bnTestArmatureBoneName0075\nbh0.0010.00.001\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0075"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.001, 0, 0.001)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0075 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0075.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0075\nbh 0.001 0.0 0.001\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0075.wya') as content_file:
            wymodelmanager0075.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0075")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.001, 0, 0.001))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0076(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0076

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0076" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0076" head (0.0001, 0, 0.0001) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0076.wya','w+')asfile:
file.write("bnTestArmatureBoneName0076\nbh0.00010.00.0001\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0076"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0001, 0, 0.0001)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0076 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0076.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0076\nbh 0.0001 0.0 0.0001\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0076.wya') as content_file:
            wymodelmanager0076.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0076")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0001, 0, 0.0001))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0077(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0077

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0077" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0077" head (2, 0, 2) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0077.wya','w+')asfile:
file.write("bnTestArmatureBoneName0077\nbh20.02\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0077"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (2, 0, 2)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0077 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0077.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0077\nbh 2 0.0 2\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0077.wya') as content_file:
            wymodelmanager0077.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0077")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (2, 0, 2))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0078(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0078

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0078" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0078" head (3, 0, 3) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0078.wya','w+')asfile:
file.write("bnTestArmatureBoneName0078\nbh30.03\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0078"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (3, 0, 3)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0078 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0078.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0078\nbh 3 0.0 3\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0078.wya') as content_file:
            wymodelmanager0078.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0078")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (3, 0, 3))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0079(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0079

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0079" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0079" head (10, 0, 10) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0079.wya','w+')asfile:
file.write("bnTestArmatureBoneName0079\nbh100.010\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0079"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (10, 0, 10)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0079 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0079.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0079\nbh 10 0.0 10\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0079.wya') as content_file:
            wymodelmanager0079.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0079")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (10, 0, 10))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0080(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0080

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0080" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0080" head (20, 0, 20) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0080.wya','w+')asfile:
file.write("bnTestArmatureBoneName0080\nbh200.020\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0080"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (20, 0, 20)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0080 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0080.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0080\nbh 20 0.0 20\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0080.wya') as content_file:
            wymodelmanager0080.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0080")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (20, 0, 20))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0081(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0081

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0081" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0081" head (30, 0, 30) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0081.wya','w+')asfile:
file.write("bnTestArmatureBoneName0081\nbh300.030\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0081"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (30, 0, 30)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0081 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0081.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0081\nbh 30 0.0 30\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0081.wya') as content_file:
            wymodelmanager0081.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0081")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (30, 0, 30))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0082(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0082

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0082" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0082" head (100, 0, 100) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0082.wya','w+')asfile:
file.write("bnTestArmatureBoneName0082\nbh1000.0100\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0082"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (100, 0, 100)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0082 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0082.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0082\nbh 100 0.0 100\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0082.wya') as content_file:
            wymodelmanager0082.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0082")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (100, 0, 100))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0083(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0083

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0083" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0083" head (200, 0, 200) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0083.wya','w+')asfile:
file.write("bnTestArmatureBoneName0083\nbh2000.0200\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0083"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (200, 0, 200)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0083 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0083.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0083\nbh 200 0.0 200\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0083.wya') as content_file:
            wymodelmanager0083.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0083")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (200, 0, 200))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0084(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0084

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0084" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0084" head (300, 0, 300) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0084.wya','w+')asfile:
file.write("bnTestArmatureBoneName0084\nbh3000.0300\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0084"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (300, 0, 300)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0084 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0084.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0084\nbh 300 0.0 300\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0084.wya') as content_file:
            wymodelmanager0084.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0084")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (300, 0, 300))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0085(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0085

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0085" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0085" head (10000, 0,  10000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0085.wya','w+')asfile:
file.write("bnTestArmatureBoneName0085\nbh100000.010000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0085"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (10000, 0,  10000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0085 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0085.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0085\nbh 10000 0.0 10000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0085.wya') as content_file:
            wymodelmanager0085.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0085")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (10000, 0,  10000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0086(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0086

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0086" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0086" head (20000, 0,  20000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0086.wya','w+')asfile:
file.write("bnTestArmatureBoneName0086\nbh200000.020000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0086"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (20000, 0,  20000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0086 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0086.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0086\nbh 20000 0.0 20000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0086.wya') as content_file:
            wymodelmanager0086.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0086")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (20000, 0,  20000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0087(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0087

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0087" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0087" head (30000, 0,  30000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0087.wya','w+')asfile:
file.write("bnTestArmatureBoneName0087\nbh300000.030000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0087"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (30000, 0,  30000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0087 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0087.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0087\nbh 30000 0.0 30000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0087.wya') as content_file:
            wymodelmanager0087.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0087")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (30000, 0,  30000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0088(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0088

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0088" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0088" head (1000000, 0,  1000000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0088.wya','w+')asfile:
file.write("bnTestArmatureBoneName0088\nbh10000000.01000000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0088"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (1000000, 0,  1000000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0088 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0088.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0088\nbh 1000000 0.0 1000000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0088.wya') as content_file:
            wymodelmanager0088.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0088")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (1000000, 0,  1000000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0089(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0089

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0089" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0089" head (2000000, 0,  2000000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0089.wya','w+')asfile:
file.write("bnTestArmatureBoneName0089\nbh20000000.02000000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0089"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (2000000, 0,  2000000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0089 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0089.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0089\nbh 2000000 0.0 2000000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0089.wya') as content_file:
            wymodelmanager0089.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0089")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (2000000, 0,  2000000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0090(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0090

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0090" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0090" head (3000000, 0,  3000000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0090.wya','w+')asfile:
file.write("bnTestArmatureBoneName0090\nbh30000000.03000000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0090"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (3000000, 0,  3000000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0090 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0090.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0090\nbh 3000000 0.0 3000000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0090.wya') as content_file:
            wymodelmanager0090.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0090")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (3000000, 0,  3000000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0091(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0091

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0091" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0091" head (0, 1, 1) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0091.wya','w+')asfile:
file.write("bnTestArmatureBoneName0091\nbh01.01\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0091"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 1, 1)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0091 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0091.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0091\nbh 0 1.0 1\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0091.wya') as content_file:
            wymodelmanager0091.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0091")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 1, 1))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0092(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0092

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0092" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0092" head (0, 0.1, 0.1) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0092.wya','w+')asfile:
file.write("bnTestArmatureBoneName0092\nbh00.10.1\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0092"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0.1, 0.1)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0092 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0092.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0092\nbh 0 0.1 0.1\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0092.wya') as content_file:
            wymodelmanager0092.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0092")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0.1, 0.1))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0093(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0093

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0093" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0093" head (0, 0.01, 0.001) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0093.wya','w+')asfile:
file.write("bnTestArmatureBoneName0093\nbh00.010.001\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0093"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0.01, 0.001)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0093 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0093.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0093\nbh 0 0.01 0.001\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0093.wya') as content_file:
            wymodelmanager0093.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0093")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0.01, 0.001))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0094(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0094

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0094" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0094" head (0, 0.0001, 0.0001) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0094.wya','w+')asfile:
file.write("bnTestArmatureBoneName0094\nbh00.00010.0001\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0094"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0.0001, 0.0001)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0094 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0094.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0094\nbh 0 0.0001 0.0001\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0094.wya') as content_file:
            wymodelmanager0094.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0094")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 0.0001, 0.0001))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0095(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0095

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0095" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0095" head (0, 2, 2) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0095.wya','w+')asfile:
file.write("bnTestArmatureBoneName0095\nbh02.02\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0095"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 2, 2)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0095 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0095.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0095\nbh 0 2.0 2\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0095.wya') as content_file:
            wymodelmanager0095.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0095")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 2, 2))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0096(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0096

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0096" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0096" head (0, 3, 3) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0096.wya','w+')asfile:
file.write("bnTestArmatureBoneName0096\nbh03.03\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0096"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 3, 3)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0096 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0096.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0096\nbh 0 3.0 3\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0096.wya') as content_file:
            wymodelmanager0096.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0096")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 3, 3))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0097(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0097

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0097" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0097" head (0, 10, 10) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0097.wya','w+')asfile:
file.write("bnTestArmatureBoneName0097\nbh010.010\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0097"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 10, 10)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0097 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0097.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0097\nbh 0 10.0 10\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0097.wya') as content_file:
            wymodelmanager0097.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0097")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 10, 10))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0098(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0098

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0098" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0098" head (0, 20, 20) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0098.wya','w+')asfile:
file.write("bnTestArmatureBoneName0098\nbh020.020\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0098"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 20, 20)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0098 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0098.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0098\nbh 0 20.0 20\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0098.wya') as content_file:
            wymodelmanager0098.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0098")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 20, 20))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0099(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0099

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0099" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0099" head (0, 30, 30) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0099.wya','w+')asfile:
file.write("bnTestArmatureBoneName0099\nbh030.030\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0099"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 30, 30)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0099 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0099.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0099\nbh 0 30.0 30\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0099.wya') as content_file:
            wymodelmanager0099.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0099")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 30, 30))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0100(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0100

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0100" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0100" head (0, 100, 100) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0100.wya','w+')asfile:
file.write("bnTestArmatureBoneName0100\nbh0100.0100\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0100"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 100, 100)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0100 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0100.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0100\nbh 0 100.0 100\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0100.wya') as content_file:
            wymodelmanager0100.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0100")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 100, 100))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0101(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0101

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0101" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0101" head (0, 200, 200) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0101.wya','w+')asfile:
file.write("bnTestArmatureBoneName0101\nbh0200.0200\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0101"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 200, 200)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0101 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0101.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0101\nbh 0 200.0 200\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0101.wya') as content_file:
            wymodelmanager0101.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0101")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 200, 200))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0102(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0102

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0102" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0102" head (0, 300, 300) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0102.wya','w+')asfile:
file.write("bnTestArmatureBoneName0102\nbh0300.0300\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0102"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 300, 300)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0102 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0102.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0102\nbh 0 300.0 300\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0102.wya') as content_file:
            wymodelmanager0102.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0102")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 300, 300))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0103(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0103

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0103" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0103" head (0, 10000, 10000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0103.wya','w+')asfile:
file.write("bnTestArmatureBoneName0103\nbh010000.010000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0103"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 10000, 10000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0103 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0103.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0103\nbh 0 10000.0 10000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0103.wya') as content_file:
            wymodelmanager0103.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0103")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 10000, 10000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0104(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0104

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0104" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0104" head (0, 20000, 20000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0104.wya','w+')asfile:
file.write("bnTestArmatureBoneName0104\nbh020000.020000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0104"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 20000, 20000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0104 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0104.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0104\nbh 0 20000.0 20000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0104.wya') as content_file:
            wymodelmanager0104.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0104")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 20000, 20000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0105(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0105

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0105" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0105" head (0, 30000, 30000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0105.wya','w+')asfile:
file.write("bnTestArmatureBoneName0105\nbh030000.030000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0105"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 30000, 30000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0105 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0105.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0105\nbh 0 30000.0 30000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0105.wya') as content_file:
            wymodelmanager0105.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0105")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 30000, 30000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0106(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0106

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0106" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0106" head (0, 1000000, 1000000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0106.wya','w+')asfile:
file.write("bnTestArmatureBoneName0106\nbh01000000.01000000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0106"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 1000000, 1000000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0106 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0106.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0106\nbh 0 1000000.0 1000000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0106.wya') as content_file:
            wymodelmanager0106.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0106")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 1000000, 1000000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0107(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0107

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0107" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0107" head (0, 2000000, 2000000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0107.wya','w+')asfile:
file.write("bnTestArmatureBoneName0107\nbh02000000.02000000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0107"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 2000000, 2000000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0107 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0107.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0107\nbh 0 2000000.0 2000000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0107.wya') as content_file:
            wymodelmanager0107.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0107")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 2000000, 2000000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0108(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0108

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0108" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0108" head (0, 3000000, 3000000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0108.wya','w+')asfile:
file.write("bnTestArmatureBoneName0108\nbh03000000.03000000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0108"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0, 3000000, 3000000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0108 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0108.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0108\nbh 0 3000000.0 3000000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0108.wya') as content_file:
            wymodelmanager0108.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0108")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0, 3000000, 3000000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0109(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0109

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0109" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0109" head (1, 1, 1) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0109.wya','w+')asfile:
file.write("bnTestArmatureBoneName0109\nbh11.01\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0109"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (1, 1, 1)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0109 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0109.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0109\nbh 1 1.0 1\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0109.wya') as content_file:
            wymodelmanager0109.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0109")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (1, 1, 1))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0110(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0110

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0110" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0110" head (0.1, 0.1, 0.1) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0110.wya','w+')asfile:
file.write("bnTestArmatureBoneName0110\nbh0.10.10.1\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0110"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.1, 0.1, 0.1)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0110 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0110.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0110\nbh 0.1 0.1 0.1\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0110.wya') as content_file:
            wymodelmanager0110.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0110")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.1, 0.1, 0.1))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0111(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0111

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0111" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0111" head (0.001, 0.01, 0.001) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0111.wya','w+')asfile:
file.write("bnTestArmatureBoneName0111\nbh0.0010.010.001\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0111"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.001, 0.01, 0.001)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0111 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0111.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0111\nbh 0.001 0.01 0.001\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0111.wya') as content_file:
            wymodelmanager0111.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0111")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.001, 0.01, 0.001))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0112(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0112

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0112" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0112" head (0.0001, 0.0001, 0.0001) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0112.wya','w+')asfile:
file.write("bnTestArmatureBoneName0112\nbh0.00010.00010.0001\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0112"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0001, 0.0001, 0.0001)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0112 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0112.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0112\nbh 0.0001 0.0001 0.0001\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0112.wya') as content_file:
            wymodelmanager0112.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0112")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0001, 0.0001, 0.0001))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0113(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0113

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0113" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0113" head (2, 2, 2) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0113.wya','w+')asfile:
file.write("bnTestArmatureBoneName0113\nbh22.02\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0113"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (2, 2, 2)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0113 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0113.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0113\nbh 2 2.0 2\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0113.wya') as content_file:
            wymodelmanager0113.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0113")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (2, 2, 2))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0114(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0114

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0114" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0114" head (3, 3, 3) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0114.wya','w+')asfile:
file.write("bnTestArmatureBoneName0114\nbh33.03\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0114"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (3, 3, 3)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0114 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0114.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0114\nbh 3 3.0 3\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0114.wya') as content_file:
            wymodelmanager0114.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0114")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (3, 3, 3))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0115(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0115

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0115" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0115" head (10, 10, 10) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0115.wya','w+')asfile:
file.write("bnTestArmatureBoneName0115\nbh1010.010\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0115"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (10, 10, 10)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0115 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0115.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0115\nbh 10 10.0 10\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0115.wya') as content_file:
            wymodelmanager0115.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0115")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (10, 10, 10))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0116(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0116

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0116" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0116" head (20, 20, 20) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0116.wya','w+')asfile:
file.write("bnTestArmatureBoneName0116\nbh2020.020\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0116"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (20, 20, 20)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0116 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0116.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0116\nbh 20 20.0 20\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0116.wya') as content_file:
            wymodelmanager0116.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0116")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (20, 20, 20))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0117(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0117

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0117" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0117" head (30, 30, 30) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0117.wya','w+')asfile:
file.write("bnTestArmatureBoneName0117\nbh3030.030\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0117"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (30, 30, 30)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0117 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0117.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0117\nbh 30 30.0 30\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0117.wya') as content_file:
            wymodelmanager0117.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0117")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (30, 30, 30))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0118(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0118

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0118" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0118" head (100, 100, 100) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0118.wya','w+')asfile:
file.write("bnTestArmatureBoneName0118\nbh100100.0100\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0118"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (100, 100, 100)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0118 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0118.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0118\nbh 100 100.0 100\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0118.wya') as content_file:
            wymodelmanager0118.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0118")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (100, 100, 100))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0119(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0119

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0119" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0119" head (200, 200, 200) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0119.wya','w+')asfile:
file.write("bnTestArmatureBoneName0119\nbh200200.0200\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0119"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (200, 200, 200)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0119 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0119.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0119\nbh 200 200.0 200\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0119.wya') as content_file:
            wymodelmanager0119.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0119")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (200, 200, 200))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0120(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0120

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0120" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0120" head (300, 300, 300) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0120.wya','w+')asfile:
file.write("bnTestArmatureBoneName0120\nbh300300.0300\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0120"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (300, 300, 300)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0120 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0120.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0120\nbh 300 300.0 300\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0120.wya') as content_file:
            wymodelmanager0120.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0120")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (300, 300, 300))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0121(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0121

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0121" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0121" head (10000, 10000, 10000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0121.wya','w+')asfile:
file.write("bnTestArmatureBoneName0121\nbh1000010000.010000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0121"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (10000, 10000, 10000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0121 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0121.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0121\nbh 10000 10000.0 10000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0121.wya') as content_file:
            wymodelmanager0121.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0121")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (10000, 10000, 10000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0122(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0122

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0122" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0122" head (20000, 20000, 20000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0122.wya','w+')asfile:
file.write("bnTestArmatureBoneName0122\nbh2000020000.020000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0122"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (20000, 20000, 20000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0122 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0122.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0122\nbh 20000 20000.0 20000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0122.wya') as content_file:
            wymodelmanager0122.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0122")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (20000, 20000, 20000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0123(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0123

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0123" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0123" head (30000, 30000, 30000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0123.wya','w+')asfile:
file.write("bnTestArmatureBoneName0123\nbh3000030000.030000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0123"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (30000, 30000, 30000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0123 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0123.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0123\nbh 30000 30000.0 30000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0123.wya') as content_file:
            wymodelmanager0123.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0123")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (30000, 30000, 30000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0124(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0124

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0124" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0124" head (1000000, 1000000, 1000000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0124.wya','w+')asfile:
file.write("bnTestArmatureBoneName0124\nbh10000001000000.01000000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0124"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (1000000, 1000000, 1000000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0124 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0124.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0124\nbh 1000000 1000000.0 1000000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0124.wya') as content_file:
            wymodelmanager0124.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0124")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (1000000, 1000000, 1000000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0125(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0125

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0125" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0125" head (2000000, 2000000, 2000000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0125.wya','w+')asfile:
file.write("bnTestArmatureBoneName0125\nbh20000002000000.02000000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0125"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (2000000, 2000000, 2000000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0125 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0125.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0125\nbh 2000000 2000000.0 2000000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0125.wya') as content_file:
            wymodelmanager0125.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0125")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (2000000, 2000000, 2000000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0126(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0126

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0126" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0126" head (3000000, 3000000, 3000000) and tail (0.0,0.0,0.0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0126.wya','w+')asfile:
file.write("bnTestArmatureBoneName0126\nbh30000003000000.03000000\nbt0.00.00.0\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0126"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (3000000, 3000000, 3000000)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0126 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0126.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0126\nbh 3000000 3000000.0 3000000\nbt 0.0 0.0 0.0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0126.wya') as content_file:
            wymodelmanager0126.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0126")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (3000000, 3000000, 3000000))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0,0.0,0.0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0127(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0127

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0127" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0127" head (0.0,0.0,0.0) and tail (1, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0127.wya','w+')asfile:
file.write("bnTestArmatureBoneName0127\nbh0.00.00.0\nbt10.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0127"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (1, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0127 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0127.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0127\nbh 0.0 0.0 0.0\nbt 1 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0127.wya') as content_file:
            wymodelmanager0127.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0127")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (1, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0128(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0128

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0128" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0128" head (0.0,0.0,0.0) and tail (0.1, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0128.wya','w+')asfile:
file.write("bnTestArmatureBoneName0128\nbh0.00.00.0\nbt0.10.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0128"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.1, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0128 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0128.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0128\nbh 0.0 0.0 0.0\nbt 0.1 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0128.wya') as content_file:
            wymodelmanager0128.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0128")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.1, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0129(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0129

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0129" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0129" head (0.0,0.0,0.0) and tail (0.001, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0129.wya','w+')asfile:
file.write("bnTestArmatureBoneName0129\nbh0.00.00.0\nbt0.0010.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0129"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.001, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0129 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0129.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0129\nbh 0.0 0.0 0.0\nbt 0.001 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0129.wya') as content_file:
            wymodelmanager0129.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0129")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.001, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0130(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0130

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0130" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0130" head (0.0,0.0,0.0) and tail (0.0001, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0130.wya','w+')asfile:
file.write("bnTestArmatureBoneName0130\nbh0.00.00.0\nbt0.00010.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0130"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0001, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0130 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0130.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0130\nbh 0.0 0.0 0.0\nbt 0.0001 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0130.wya') as content_file:
            wymodelmanager0130.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0130")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0001, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0131(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0131

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0131" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0131" head (0.0,0.0,0.0) and tail (2, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0131.wya','w+')asfile:
file.write("bnTestArmatureBoneName0131\nbh0.00.00.0\nbt20.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0131"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (2, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0131 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0131.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0131\nbh 0.0 0.0 0.0\nbt 2 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0131.wya') as content_file:
            wymodelmanager0131.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0131")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (2, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0132(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0132

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0132" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0132" head (0.0,0.0,0.0) and tail (3, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0132.wya','w+')asfile:
file.write("bnTestArmatureBoneName0132\nbh0.00.00.0\nbt30.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0132"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (3, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0132 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0132.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0132\nbh 0.0 0.0 0.0\nbt 3 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0132.wya') as content_file:
            wymodelmanager0132.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0132")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (3, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0133(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0133

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0133" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0133" head (0.0,0.0,0.0) and tail (10, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0133.wya','w+')asfile:
file.write("bnTestArmatureBoneName0133\nbh0.00.00.0\nbt100.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0133"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (10, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0133 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0133.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0133\nbh 0.0 0.0 0.0\nbt 10 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0133.wya') as content_file:
            wymodelmanager0133.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0133")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (10, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0134(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0134

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0134" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0134" head (0.0,0.0,0.0) and tail (20, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0134.wya','w+')asfile:
file.write("bnTestArmatureBoneName0134\nbh0.00.00.0\nbt200.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0134"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (20, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0134 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0134.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0134\nbh 0.0 0.0 0.0\nbt 20 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0134.wya') as content_file:
            wymodelmanager0134.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0134")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (20, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0135(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0135

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0135" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0135" head (0.0,0.0,0.0) and tail (30, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0135.wya','w+')asfile:
file.write("bnTestArmatureBoneName0135\nbh0.00.00.0\nbt300.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0135"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (30, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0135 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0135.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0135\nbh 0.0 0.0 0.0\nbt 30 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0135.wya') as content_file:
            wymodelmanager0135.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0135")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (30, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0136(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0136

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0136" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0136" head (0.0,0.0,0.0) and tail (100, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0136.wya','w+')asfile:
file.write("bnTestArmatureBoneName0136\nbh0.00.00.0\nbt1000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0136"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (100, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0136 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0136.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0136\nbh 0.0 0.0 0.0\nbt 100 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0136.wya') as content_file:
            wymodelmanager0136.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0136")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (100, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0137(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0137

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0137" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0137" head (0.0,0.0,0.0) and tail (200, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0137.wya','w+')asfile:
file.write("bnTestArmatureBoneName0137\nbh0.00.00.0\nbt2000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0137"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (200, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0137 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0137.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0137\nbh 0.0 0.0 0.0\nbt 200 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0137.wya') as content_file:
            wymodelmanager0137.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0137")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (200, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0138(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0138

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0138" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0138" head (0.0,0.0,0.0) and tail (300, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0138.wya','w+')asfile:
file.write("bnTestArmatureBoneName0138\nbh0.00.00.0\nbt3000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0138"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (300, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0138 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0138.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0138\nbh 0.0 0.0 0.0\nbt 300 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0138.wya') as content_file:
            wymodelmanager0138.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0138")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (300, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0139(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0139

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0139" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0139" head (0.0,0.0,0.0) and tail (10000, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0139.wya','w+')asfile:
file.write("bnTestArmatureBoneName0139\nbh0.00.00.0\nbt100000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0139"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (10000, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0139 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0139.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0139\nbh 0.0 0.0 0.0\nbt 10000 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0139.wya') as content_file:
            wymodelmanager0139.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0139")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (10000, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0140(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0140

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0140" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0140" head (0.0,0.0,0.0) and tail (20000, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0140.wya','w+')asfile:
file.write("bnTestArmatureBoneName0140\nbh0.00.00.0\nbt200000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0140"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (20000, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0140 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0140.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0140\nbh 0.0 0.0 0.0\nbt 20000 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0140.wya') as content_file:
            wymodelmanager0140.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0140")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (20000, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0141(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0141

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0141" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0141" head (0.0,0.0,0.0) and tail (30000, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0141.wya','w+')asfile:
file.write("bnTestArmatureBoneName0141\nbh0.00.00.0\nbt300000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0141"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (30000, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0141 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0141.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0141\nbh 0.0 0.0 0.0\nbt 30000 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0141.wya') as content_file:
            wymodelmanager0141.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0141")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (30000, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0142(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0142

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0142" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0142" head (0.0,0.0,0.0) and tail (1000000, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0142.wya','w+')asfile:
file.write("bnTestArmatureBoneName0142\nbh0.00.00.0\nbt10000000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0142"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (1000000, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0142 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0142.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0142\nbh 0.0 0.0 0.0\nbt 1000000 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0142.wya') as content_file:
            wymodelmanager0142.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0142")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (1000000, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0143(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0143

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0143" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0143" head (0.0,0.0,0.0) and tail (2000000, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0143.wya','w+')asfile:
file.write("bnTestArmatureBoneName0143\nbh0.00.00.0\nbt20000000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0143"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (2000000, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0143 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0143.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0143\nbh 0.0 0.0 0.0\nbt 2000000 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0143.wya') as content_file:
            wymodelmanager0143.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0143")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (2000000, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0144(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0144

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0144" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0144" head (0.0,0.0,0.0) and tail (3000000, 0, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0144.wya','w+')asfile:
file.write("bnTestArmatureBoneName0144\nbh0.00.00.0\nbt30000000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0144"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (3000000, 0, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0144 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0144.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0144\nbh 0.0 0.0 0.0\nbt 3000000 0.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0144.wya') as content_file:
            wymodelmanager0144.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0144")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (3000000, 0, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0145(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0145

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0145" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0145" head (0.0,0.0,0.0) and tail (0, 1, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0145.wya','w+')asfile:
file.write("bnTestArmatureBoneName0145\nbh0.00.00.0\nbt01.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0145"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 1, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0145 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0145.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0145\nbh 0.0 0.0 0.0\nbt 0 1.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0145.wya') as content_file:
            wymodelmanager0145.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0145")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 1, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0146(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0146

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0146" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0146" head (0.0,0.0,0.0) and tail (0, 0.1, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0146.wya','w+')asfile:
file.write("bnTestArmatureBoneName0146\nbh0.00.00.0\nbt00.10\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0146"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0.1, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0146 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0146.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0146\nbh 0.0 0.0 0.0\nbt 0 0.1 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0146.wya') as content_file:
            wymodelmanager0146.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0146")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0.1, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0147(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0147

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0147" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0147" head (0.0,0.0,0.0) and tail (0, 0.001, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0147.wya','w+')asfile:
file.write("bnTestArmatureBoneName0147\nbh0.00.00.0\nbt00.0010\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0147"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0.001, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0147 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0147.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0147\nbh 0.0 0.0 0.0\nbt 0 0.001 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0147.wya') as content_file:
            wymodelmanager0147.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0147")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0.001, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0148(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0148

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0148" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0148" head (0.0,0.0,0.0) and tail (0, 0.0001, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0148.wya','w+')asfile:
file.write("bnTestArmatureBoneName0148\nbh0.00.00.0\nbt00.00010\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0148"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0.0001, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0148 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0148.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0148\nbh 0.0 0.0 0.0\nbt 0 0.0001 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0148.wya') as content_file:
            wymodelmanager0148.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0148")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0.0001, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0149(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0149

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0149" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0149" head (0.0,0.0,0.0) and tail (0, 2, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0149.wya','w+')asfile:
file.write("bnTestArmatureBoneName0149\nbh0.00.00.0\nbt02.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0149"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 2, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0149 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0149.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0149\nbh 0.0 0.0 0.0\nbt 0 2.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0149.wya') as content_file:
            wymodelmanager0149.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0149")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 2, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0150(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0150

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0150" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0150" head (0.0,0.0,0.0) and tail (0, 3, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0150.wya','w+')asfile:
file.write("bnTestArmatureBoneName0150\nbh0.00.00.0\nbt03.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0150"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 3, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0150 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0150.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0150\nbh 0.0 0.0 0.0\nbt 0 3.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0150.wya') as content_file:
            wymodelmanager0150.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0150")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 3, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0151(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0151

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0151" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0151" head (0.0,0.0,0.0) and tail (0, 10, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0151.wya','w+')asfile:
file.write("bnTestArmatureBoneName0151\nbh0.00.00.0\nbt010.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0151"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 10, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0151 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0151.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0151\nbh 0.0 0.0 0.0\nbt 0 10.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0151.wya') as content_file:
            wymodelmanager0151.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0151")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 10, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0152(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0152

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0152" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0152" head (0.0,0.0,0.0) and tail (0, 20, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0152.wya','w+')asfile:
file.write("bnTestArmatureBoneName0152\nbh0.00.00.0\nbt020.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0152"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 20, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0152 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0152.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0152\nbh 0.0 0.0 0.0\nbt 0 20.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0152.wya') as content_file:
            wymodelmanager0152.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0152")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 20, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0153(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0153

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0153" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0153" head (0.0,0.0,0.0) and tail (0, 30, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0153.wya','w+')asfile:
file.write("bnTestArmatureBoneName0153\nbh0.00.00.0\nbt030.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0153"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 30, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0153 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0153.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0153\nbh 0.0 0.0 0.0\nbt 0 30.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0153.wya') as content_file:
            wymodelmanager0153.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0153")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 30, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0154(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0154

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0154" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0154" head (0.0,0.0,0.0) and tail (0, 100, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0154.wya','w+')asfile:
file.write("bnTestArmatureBoneName0154\nbh0.00.00.0\nbt0100.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0154"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 100, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0154 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0154.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0154\nbh 0.0 0.0 0.0\nbt 0 100.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0154.wya') as content_file:
            wymodelmanager0154.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0154")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 100, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0155(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0155

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0155" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0155" head (0.0,0.0,0.0) and tail (0, 200, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0155.wya','w+')asfile:
file.write("bnTestArmatureBoneName0155\nbh0.00.00.0\nbt0200.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0155"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 200, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0155 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0155.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0155\nbh 0.0 0.0 0.0\nbt 0 200.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0155.wya') as content_file:
            wymodelmanager0155.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0155")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 200, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0156(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0156

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0156" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0156" head (0.0,0.0,0.0) and tail (0, 300, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0156.wya','w+')asfile:
file.write("bnTestArmatureBoneName0156\nbh0.00.00.0\nbt0300.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0156"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 300, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0156 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0156.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0156\nbh 0.0 0.0 0.0\nbt 0 300.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0156.wya') as content_file:
            wymodelmanager0156.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0156")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 300, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0157(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0157

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0157" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0157" head (0.0,0.0,0.0) and tail (0, 10000, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0157.wya','w+')asfile:
file.write("bnTestArmatureBoneName0157\nbh0.00.00.0\nbt010000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0157"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 10000, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0157 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0157.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0157\nbh 0.0 0.0 0.0\nbt 0 10000.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0157.wya') as content_file:
            wymodelmanager0157.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0157")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 10000, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0158(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0158

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0158" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0158" head (0.0,0.0,0.0) and tail (0, 20000, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0158.wya','w+')asfile:
file.write("bnTestArmatureBoneName0158\nbh0.00.00.0\nbt020000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0158"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 20000, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0158 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0158.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0158\nbh 0.0 0.0 0.0\nbt 0 20000.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0158.wya') as content_file:
            wymodelmanager0158.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0158")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 20000, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0159(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0159

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0159" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0159" head (0.0,0.0,0.0) and tail (0, 30000, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0159.wya','w+')asfile:
file.write("bnTestArmatureBoneName0159\nbh0.00.00.0\nbt030000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0159"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 30000, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0159 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0159.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0159\nbh 0.0 0.0 0.0\nbt 0 30000.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0159.wya') as content_file:
            wymodelmanager0159.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0159")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 30000, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0160(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0160

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0160" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0160" head (0.0,0.0,0.0) and tail (0, 1000000, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0160.wya','w+')asfile:
file.write("bnTestArmatureBoneName0160\nbh0.00.00.0\nbt01000000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0160"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 1000000, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0160 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0160.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0160\nbh 0.0 0.0 0.0\nbt 0 1000000.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0160.wya') as content_file:
            wymodelmanager0160.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0160")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 1000000, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0161(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0161

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0161" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0161" head (0.0,0.0,0.0) and tail (0, 2000000, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0161.wya','w+')asfile:
file.write("bnTestArmatureBoneName0161\nbh0.00.00.0\nbt02000000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0161"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 2000000, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0161 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0161.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0161\nbh 0.0 0.0 0.0\nbt 0 2000000.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0161.wya') as content_file:
            wymodelmanager0161.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0161")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 2000000, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0162(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0162

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0162" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0162" head (0.0,0.0,0.0) and tail (0, 3000000, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0162.wya','w+')asfile:
file.write("bnTestArmatureBoneName0162\nbh0.00.00.0\nbt03000000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0162"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 3000000, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0162 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0162.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0162\nbh 0.0 0.0 0.0\nbt 0 3000000.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0162.wya') as content_file:
            wymodelmanager0162.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0162")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 3000000, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0163(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0163

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0163" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0163" head (0.0,0.0,0.0) and tail (0, 0, 1) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0163.wya','w+')asfile:
file.write("bnTestArmatureBoneName0163\nbh0.00.00.0\nbt00.01\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0163"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 1)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0163 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0163.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0163\nbh 0.0 0.0 0.0\nbt 0 0.0 1\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0163.wya') as content_file:
            wymodelmanager0163.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0163")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 1))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0164(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0164

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0164" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0164" head (0.0,0.0,0.0) and tail (0, 0, 0.1) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0164.wya','w+')asfile:
file.write("bnTestArmatureBoneName0164\nbh0.00.00.0\nbt00.00.1\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0164"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 0.1)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0164 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0164.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0164\nbh 0.0 0.0 0.0\nbt 0 0.0 0.1\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0164.wya') as content_file:
            wymodelmanager0164.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0164")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 0.1))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0165(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0165

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0165" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0165" head (0.0,0.0,0.0) and tail (0, 0, 0.001) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0165.wya','w+')asfile:
file.write("bnTestArmatureBoneName0165\nbh0.00.00.0\nbt00.00.001\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0165"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 0.001)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0165 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0165.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0165\nbh 0.0 0.0 0.0\nbt 0 0.0 0.001\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0165.wya') as content_file:
            wymodelmanager0165.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0165")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 0.001))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0166(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0166

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0166" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0166" head (0.0,0.0,0.0) and tail (0, 0, 0.0001) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0166.wya','w+')asfile:
file.write("bnTestArmatureBoneName0166\nbh0.00.00.0\nbt00.00.0001\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0166"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 0.0001)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0166 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0166.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0166\nbh 0.0 0.0 0.0\nbt 0 0.0 0.0001\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0166.wya') as content_file:
            wymodelmanager0166.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0166")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 0.0001))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0167(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0167

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0167" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0167" head (0.0,0.0,0.0) and tail (0, 0, 2) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0167.wya','w+')asfile:
file.write("bnTestArmatureBoneName0167\nbh0.00.00.0\nbt00.02\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0167"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 2)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0167 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0167.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0167\nbh 0.0 0.0 0.0\nbt 0 0.0 2\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0167.wya') as content_file:
            wymodelmanager0167.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0167")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 2))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0168(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0168

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0168" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0168" head (0.0,0.0,0.0) and tail (0, 0, 3) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0168.wya','w+')asfile:
file.write("bnTestArmatureBoneName0168\nbh0.00.00.0\nbt00.03\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0168"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 3)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0168 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0168.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0168\nbh 0.0 0.0 0.0\nbt 0 0.0 3\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0168.wya') as content_file:
            wymodelmanager0168.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0168")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 3))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0169(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0169

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0169" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0169" head (0.0,0.0,0.0) and tail (0, 0, 10) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0169.wya','w+')asfile:
file.write("bnTestArmatureBoneName0169\nbh0.00.00.0\nbt00.010\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0169"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 10)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0169 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0169.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0169\nbh 0.0 0.0 0.0\nbt 0 0.0 10\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0169.wya') as content_file:
            wymodelmanager0169.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0169")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 10))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0170(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0170

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0170" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0170" head (0.0,0.0,0.0) and tail (0, 0, 20) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0170.wya','w+')asfile:
file.write("bnTestArmatureBoneName0170\nbh0.00.00.0\nbt00.020\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0170"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 20)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0170 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0170.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0170\nbh 0.0 0.0 0.0\nbt 0 0.0 20\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0170.wya') as content_file:
            wymodelmanager0170.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0170")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 20))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0171(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0171

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0171" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0171" head (0.0,0.0,0.0) and tail (0, 0, 30) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0171.wya','w+')asfile:
file.write("bnTestArmatureBoneName0171\nbh0.00.00.0\nbt00.030\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0171"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 30)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0171 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0171.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0171\nbh 0.0 0.0 0.0\nbt 0 0.0 30\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0171.wya') as content_file:
            wymodelmanager0171.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0171")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 30))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0172(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0172

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0172" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0172" head (0.0,0.0,0.0) and tail (0, 0, 100) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0172.wya','w+')asfile:
file.write("bnTestArmatureBoneName0172\nbh0.00.00.0\nbt00.0100\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0172"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 100)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0172 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0172.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0172\nbh 0.0 0.0 0.0\nbt 0 0.0 100\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0172.wya') as content_file:
            wymodelmanager0172.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0172")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 100))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0173(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0173

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0173" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0173" head (0.0,0.0,0.0) and tail (0, 0, 200) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0173.wya','w+')asfile:
file.write("bnTestArmatureBoneName0173\nbh0.00.00.0\nbt00.0200\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0173"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 200)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0173 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0173.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0173\nbh 0.0 0.0 0.0\nbt 0 0.0 200\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0173.wya') as content_file:
            wymodelmanager0173.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0173")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 200))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0174(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0174

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0174" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0174" head (0.0,0.0,0.0) and tail (0, 0, 300) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0174.wya','w+')asfile:
file.write("bnTestArmatureBoneName0174\nbh0.00.00.0\nbt00.0300\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0174"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 300)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0174 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0174.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0174\nbh 0.0 0.0 0.0\nbt 0 0.0 300\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0174.wya') as content_file:
            wymodelmanager0174.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0174")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 300))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0175(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0175

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0175" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0175" head (0.0,0.0,0.0) and tail (0, 0, 10000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0175.wya','w+')asfile:
file.write("bnTestArmatureBoneName0175\nbh0.00.00.0\nbt00.010000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0175"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 10000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0175 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0175.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0175\nbh 0.0 0.0 0.0\nbt 0 0.0 10000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0175.wya') as content_file:
            wymodelmanager0175.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0175")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 10000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0176(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0176

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0176" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0176" head (0.0,0.0,0.0) and tail (0, 0, 20000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0176.wya','w+')asfile:
file.write("bnTestArmatureBoneName0176\nbh0.00.00.0\nbt00.020000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0176"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 20000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0176 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0176.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0176\nbh 0.0 0.0 0.0\nbt 0 0.0 20000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0176.wya') as content_file:
            wymodelmanager0176.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0176")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 20000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0177(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0177

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0177" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0177" head (0.0,0.0,0.0) and tail (0, 0, 30000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0177.wya','w+')asfile:
file.write("bnTestArmatureBoneName0177\nbh0.00.00.0\nbt00.030000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0177"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 30000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0177 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0177.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0177\nbh 0.0 0.0 0.0\nbt 0 0.0 30000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0177.wya') as content_file:
            wymodelmanager0177.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0177")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 30000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0178(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0178

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0178" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0178" head (0.0,0.0,0.0) and tail (0, 0, 1000000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0178.wya','w+')asfile:
file.write("bnTestArmatureBoneName0178\nbh0.00.00.0\nbt00.01000000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0178"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 1000000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0178 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0178.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0178\nbh 0.0 0.0 0.0\nbt 0 0.0 1000000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0178.wya') as content_file:
            wymodelmanager0178.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0178")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 1000000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0179(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0179

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0179" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0179" head (0.0,0.0,0.0) and tail (0, 0, 2000000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0179.wya','w+')asfile:
file.write("bnTestArmatureBoneName0179\nbh0.00.00.0\nbt00.02000000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0179"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 2000000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0179 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0179.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0179\nbh 0.0 0.0 0.0\nbt 0 0.0 2000000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0179.wya') as content_file:
            wymodelmanager0179.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0179")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 2000000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0180(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0180

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0180" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0180" head (0.0,0.0,0.0) and tail (0, 0, 3000000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0180.wya','w+')asfile:
file.write("bnTestArmatureBoneName0180\nbh0.00.00.0\nbt00.03000000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0180"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 3000000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0180 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0180.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0180\nbh 0.0 0.0 0.0\nbt 0 0.0 3000000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0180.wya') as content_file:
            wymodelmanager0180.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0180")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0, 3000000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0181(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0181

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0181" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0181" head (0.0,0.0,0.0) and tail (1, 1, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0181.wya','w+')asfile:
file.write("bnTestArmatureBoneName0181\nbh0.00.00.0\nbt11.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0181"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (1, 1, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0181 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0181.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0181\nbh 0.0 0.0 0.0\nbt 1 1.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0181.wya') as content_file:
            wymodelmanager0181.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0181")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (1, 1, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0182(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0182

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0182" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0182" head (0.0,0.0,0.0) and tail (0.1, 0.1, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0182.wya','w+')asfile:
file.write("bnTestArmatureBoneName0182\nbh0.00.00.0\nbt0.10.10\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0182"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.1, 0.1, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0182 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0182.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0182\nbh 0.0 0.0 0.0\nbt 0.1 0.1 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0182.wya') as content_file:
            wymodelmanager0182.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0182")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.1, 0.1, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0183(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0183

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0183" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0183" head (0.0,0.0,0.0) and tail (0.001, 0.001, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0183.wya','w+')asfile:
file.write("bnTestArmatureBoneName0183\nbh0.00.00.0\nbt0.0010.0010\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0183"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.001, 0.001, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0183 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0183.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0183\nbh 0.0 0.0 0.0\nbt 0.001 0.001 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0183.wya') as content_file:
            wymodelmanager0183.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0183")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.001, 0.001, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0184(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0184

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0184" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0184" head (0.0,0.0,0.0) and tail (0.0001, 0.0001, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0184.wya','w+')asfile:
file.write("bnTestArmatureBoneName0184\nbh0.00.00.0\nbt0.00010.00010\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0184"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0001, 0.0001, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0184 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0184.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0184\nbh 0.0 0.0 0.0\nbt 0.0001 0.0001 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0184.wya') as content_file:
            wymodelmanager0184.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0184")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0001, 0.0001, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0185(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0185

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0185" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0185" head (0.0,0.0,0.0) and tail (2, 2, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0185.wya','w+')asfile:
file.write("bnTestArmatureBoneName0185\nbh0.00.00.0\nbt22.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0185"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (2, 2, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0185 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0185.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0185\nbh 0.0 0.0 0.0\nbt 2 2.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0185.wya') as content_file:
            wymodelmanager0185.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0185")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (2, 2, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0186(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0186

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0186" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0186" head (0.0,0.0,0.0) and tail (3, 3, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0186.wya','w+')asfile:
file.write("bnTestArmatureBoneName0186\nbh0.00.00.0\nbt33.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0186"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (3, 3, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0186 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0186.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0186\nbh 0.0 0.0 0.0\nbt 3 3.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0186.wya') as content_file:
            wymodelmanager0186.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0186")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (3, 3, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0187(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0187

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0187" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0187" head (0.0,0.0,0.0) and tail (10, 10, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0187.wya','w+')asfile:
file.write("bnTestArmatureBoneName0187\nbh0.00.00.0\nbt1010.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0187"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (10, 10, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0187 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0187.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0187\nbh 0.0 0.0 0.0\nbt 10 10.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0187.wya') as content_file:
            wymodelmanager0187.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0187")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (10, 10, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0188(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0188

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0188" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0188" head (0.0,0.0,0.0) and tail (20, 20, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0188.wya','w+')asfile:
file.write("bnTestArmatureBoneName0188\nbh0.00.00.0\nbt2020.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0188"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (20, 20, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0188 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0188.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0188\nbh 0.0 0.0 0.0\nbt 20 20.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0188.wya') as content_file:
            wymodelmanager0188.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0188")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (20, 20, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0189(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0189

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0189" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0189" head (0.0,0.0,0.0) and tail (30, 30, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0189.wya','w+')asfile:
file.write("bnTestArmatureBoneName0189\nbh0.00.00.0\nbt3030.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0189"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (30, 30, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0189 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0189.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0189\nbh 0.0 0.0 0.0\nbt 30 30.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0189.wya') as content_file:
            wymodelmanager0189.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0189")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (30, 30, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0190(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0190

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0190" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0190" head (0.0,0.0,0.0) and tail (100, 100, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0190.wya','w+')asfile:
file.write("bnTestArmatureBoneName0190\nbh0.00.00.0\nbt100100.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0190"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (100, 100, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0190 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0190.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0190\nbh 0.0 0.0 0.0\nbt 100 100.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0190.wya') as content_file:
            wymodelmanager0190.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0190")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (100, 100, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0191(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0191

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0191" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0191" head (0.0,0.0,0.0) and tail (200, 200, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0191.wya','w+')asfile:
file.write("bnTestArmatureBoneName0191\nbh0.00.00.0\nbt200200.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0191"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (200, 200, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0191 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0191.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0191\nbh 0.0 0.0 0.0\nbt 200 200.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0191.wya') as content_file:
            wymodelmanager0191.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0191")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (200, 200, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0192(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0192

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0192" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0192" head (0.0,0.0,0.0) and tail (300, 300, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0192.wya','w+')asfile:
file.write("bnTestArmatureBoneName0192\nbh0.00.00.0\nbt300300.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0192"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (300, 300, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0192 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0192.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0192\nbh 0.0 0.0 0.0\nbt 300 300.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0192.wya') as content_file:
            wymodelmanager0192.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0192")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (300, 300, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0193(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0193

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0193" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0193" head (0.0,0.0,0.0) and tail (10000, 10000, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0193.wya','w+')asfile:
file.write("bnTestArmatureBoneName0193\nbh0.00.00.0\nbt1000010000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0193"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (10000, 10000, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0193 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0193.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0193\nbh 0.0 0.0 0.0\nbt 10000 10000.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0193.wya') as content_file:
            wymodelmanager0193.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0193")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (10000, 10000, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0194(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0194

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0194" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0194" head (0.0,0.0,0.0) and tail (20000, 20000, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0194.wya','w+')asfile:
file.write("bnTestArmatureBoneName0194\nbh0.00.00.0\nbt2000020000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0194"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (20000, 20000, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0194 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0194.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0194\nbh 0.0 0.0 0.0\nbt 20000 20000.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0194.wya') as content_file:
            wymodelmanager0194.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0194")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (20000, 20000, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0195(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0195

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0195" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0195" head (0.0,0.0,0.0) and tail (30000, 30000, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0195.wya','w+')asfile:
file.write("bnTestArmatureBoneName0195\nbh0.00.00.0\nbt3000030000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0195"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (30000, 30000, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0195 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0195.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0195\nbh 0.0 0.0 0.0\nbt 30000 30000.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0195.wya') as content_file:
            wymodelmanager0195.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0195")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (30000, 30000, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0196(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0196

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0196" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0196" head (0.0,0.0,0.0) and tail (1000000, 1000000, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0196.wya','w+')asfile:
file.write("bnTestArmatureBoneName0196\nbh0.00.00.0\nbt10000001000000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0196"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (1000000, 1000000, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0196 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0196.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0196\nbh 0.0 0.0 0.0\nbt 1000000 1000000.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0196.wya') as content_file:
            wymodelmanager0196.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0196")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (1000000, 1000000, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0197(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0197

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0197" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0197" head (0.0,0.0,0.0) and tail (2000000, 2000000, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0197.wya','w+')asfile:
file.write("bnTestArmatureBoneName0197\nbh0.00.00.0\nbt20000002000000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0197"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (2000000, 2000000, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0197 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0197.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0197\nbh 0.0 0.0 0.0\nbt 2000000 2000000.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0197.wya') as content_file:
            wymodelmanager0197.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0197")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (2000000, 2000000, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0198(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0198

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0198" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0198" head (0.0,0.0,0.0) and tail (3000000, 3000000, 0) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0198.wya','w+')asfile:
file.write("bnTestArmatureBoneName0198\nbh0.00.00.0\nbt30000003000000.00\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0198"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (3000000, 3000000, 0)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0198 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0198.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0198\nbh 0.0 0.0 0.0\nbt 3000000 3000000.0 0\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0198.wya') as content_file:
            wymodelmanager0198.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0198")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (3000000, 3000000, 0))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0199(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0199

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0199" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0199" head (0.0,0.0,0.0) and tail (1, 0, 1) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0199.wya','w+')asfile:
file.write("bnTestArmatureBoneName0199\nbh0.00.00.0\nbt10.01\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0199"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (1, 0, 1)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0199 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0199.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0199\nbh 0.0 0.0 0.0\nbt 1 0.0 1\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0199.wya') as content_file:
            wymodelmanager0199.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0199")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (1, 0, 1))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0200(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0200

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0200" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0200" head (0.0,0.0,0.0) and tail (0.1, 0, 0.1) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0200.wya','w+')asfile:
file.write("bnTestArmatureBoneName0200\nbh0.00.00.0\nbt0.10.00.1\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0200"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.1, 0, 0.1)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0200 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0200.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0200\nbh 0.0 0.0 0.0\nbt 0.1 0.0 0.1\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0200.wya') as content_file:
            wymodelmanager0200.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0200")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.1, 0, 0.1))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0201(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0201

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0201" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0201" head (0.0,0.0,0.0) and tail (0.001, 0, 0.001) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0201.wya','w+')asfile:
file.write("bnTestArmatureBoneName0201\nbh0.00.00.0\nbt0.0010.00.001\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0201"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.001, 0, 0.001)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0201 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0201.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0201\nbh 0.0 0.0 0.0\nbt 0.001 0.0 0.001\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0201.wya') as content_file:
            wymodelmanager0201.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0201")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.001, 0, 0.001))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0202(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0202

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0202" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0202" head (0.0,0.0,0.0) and tail (0.0001, 0, 0.0001) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0202.wya','w+')asfile:
file.write("bnTestArmatureBoneName0202\nbh0.00.00.0\nbt0.00010.00.0001\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0202"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0001, 0, 0.0001)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0202 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0202.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0202\nbh 0.0 0.0 0.0\nbt 0.0001 0.0 0.0001\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0202.wya') as content_file:
            wymodelmanager0202.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0202")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0001, 0, 0.0001))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0203(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0203

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0203" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0203" head (0.0,0.0,0.0) and tail (2, 0, 2) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0203.wya','w+')asfile:
file.write("bnTestArmatureBoneName0203\nbh0.00.00.0\nbt20.02\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0203"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (2, 0, 2)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0203 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0203.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0203\nbh 0.0 0.0 0.0\nbt 2 0.0 2\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0203.wya') as content_file:
            wymodelmanager0203.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0203")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (2, 0, 2))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0204(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0204

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0204" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0204" head (0.0,0.0,0.0) and tail (3, 0, 3) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0204.wya','w+')asfile:
file.write("bnTestArmatureBoneName0204\nbh0.00.00.0\nbt30.03\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0204"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (3, 0, 3)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0204 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0204.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0204\nbh 0.0 0.0 0.0\nbt 3 0.0 3\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0204.wya') as content_file:
            wymodelmanager0204.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0204")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (3, 0, 3))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0205(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0205

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0205" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0205" head (0.0,0.0,0.0) and tail (10, 0, 10) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0205.wya','w+')asfile:
file.write("bnTestArmatureBoneName0205\nbh0.00.00.0\nbt100.010\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0205"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (10, 0, 10)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0205 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0205.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0205\nbh 0.0 0.0 0.0\nbt 10 0.0 10\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0205.wya') as content_file:
            wymodelmanager0205.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0205")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (10, 0, 10))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0206(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0206

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0206" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0206" head (0.0,0.0,0.0) and tail (20, 0, 20) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0206.wya','w+')asfile:
file.write("bnTestArmatureBoneName0206\nbh0.00.00.0\nbt200.020\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0206"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (20, 0, 20)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0206 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0206.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0206\nbh 0.0 0.0 0.0\nbt 20 0.0 20\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0206.wya') as content_file:
            wymodelmanager0206.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0206")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (20, 0, 20))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0207(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0207

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0207" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0207" head (0.0,0.0,0.0) and tail (30, 0, 30) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0207.wya','w+')asfile:
file.write("bnTestArmatureBoneName0207\nbh0.00.00.0\nbt300.030\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0207"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (30, 0, 30)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0207 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0207.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0207\nbh 0.0 0.0 0.0\nbt 30 0.0 30\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0207.wya') as content_file:
            wymodelmanager0207.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0207")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (30, 0, 30))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0208(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0208

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0208" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0208" head (0.0,0.0,0.0) and tail (100, 0, 100) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0208.wya','w+')asfile:
file.write("bnTestArmatureBoneName0208\nbh0.00.00.0\nbt1000.0100\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0208"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (100, 0, 100)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0208 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0208.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0208\nbh 0.0 0.0 0.0\nbt 100 0.0 100\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0208.wya') as content_file:
            wymodelmanager0208.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0208")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (100, 0, 100))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0209(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0209

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0209" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0209" head (0.0,0.0,0.0) and tail (200, 0, 200) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0209.wya','w+')asfile:
file.write("bnTestArmatureBoneName0209\nbh0.00.00.0\nbt2000.0200\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0209"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (200, 0, 200)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0209 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0209.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0209\nbh 0.0 0.0 0.0\nbt 200 0.0 200\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0209.wya') as content_file:
            wymodelmanager0209.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0209")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (200, 0, 200))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0210(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0210

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0210" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0210" head (0.0,0.0,0.0) and tail (300, 0, 300) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0210.wya','w+')asfile:
file.write("bnTestArmatureBoneName0210\nbh0.00.00.0\nbt3000.0300\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0210"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (300, 0, 300)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0210 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0210.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0210\nbh 0.0 0.0 0.0\nbt 300 0.0 300\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0210.wya') as content_file:
            wymodelmanager0210.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0210")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (300, 0, 300))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0211(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0211

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0211" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0211" head (0.0,0.0,0.0) and tail (10000, 0,  10000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0211.wya','w+')asfile:
file.write("bnTestArmatureBoneName0211\nbh0.00.00.0\nbt100000.010000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0211"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (10000, 0,  10000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0211 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0211.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0211\nbh 0.0 0.0 0.0\nbt 10000 0.0 10000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0211.wya') as content_file:
            wymodelmanager0211.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0211")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (10000, 0,  10000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0212(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0212

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0212" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0212" head (0.0,0.0,0.0) and tail (20000, 0,  20000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0212.wya','w+')asfile:
file.write("bnTestArmatureBoneName0212\nbh0.00.00.0\nbt200000.020000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0212"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (20000, 0,  20000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0212 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0212.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0212\nbh 0.0 0.0 0.0\nbt 20000 0.0 20000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0212.wya') as content_file:
            wymodelmanager0212.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0212")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (20000, 0,  20000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0213(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0213

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0213" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0213" head (0.0,0.0,0.0) and tail (30000, 0,  30000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0213.wya','w+')asfile:
file.write("bnTestArmatureBoneName0213\nbh0.00.00.0\nbt300000.030000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0213"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (30000, 0,  30000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0213 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0213.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0213\nbh 0.0 0.0 0.0\nbt 30000 0.0 30000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0213.wya') as content_file:
            wymodelmanager0213.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0213")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (30000, 0,  30000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0214(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0214

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0214" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0214" head (0.0,0.0,0.0) and tail (1000000, 0,  1000000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0214.wya','w+')asfile:
file.write("bnTestArmatureBoneName0214\nbh0.00.00.0\nbt10000000.01000000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0214"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (1000000, 0,  1000000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0214 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0214.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0214\nbh 0.0 0.0 0.0\nbt 1000000 0.0 1000000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0214.wya') as content_file:
            wymodelmanager0214.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0214")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (1000000, 0,  1000000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0215(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0215

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0215" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0215" head (0.0,0.0,0.0) and tail (2000000, 0,  2000000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0215.wya','w+')asfile:
file.write("bnTestArmatureBoneName0215\nbh0.00.00.0\nbt20000000.02000000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0215"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (2000000, 0,  2000000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0215 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0215.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0215\nbh 0.0 0.0 0.0\nbt 2000000 0.0 2000000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0215.wya') as content_file:
            wymodelmanager0215.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0215")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (2000000, 0,  2000000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0216(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0216

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0216" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0216" head (0.0,0.0,0.0) and tail (3000000, 0,  3000000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0216.wya','w+')asfile:
file.write("bnTestArmatureBoneName0216\nbh0.00.00.0\nbt30000000.03000000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0216"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (3000000, 0,  3000000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0216 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0216.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0216\nbh 0.0 0.0 0.0\nbt 3000000 0.0 3000000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0216.wya') as content_file:
            wymodelmanager0216.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0216")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (3000000, 0,  3000000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0217(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0217

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0217" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0217" head (0.0,0.0,0.0) and tail (0, 1, 1) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0217.wya','w+')asfile:
file.write("bnTestArmatureBoneName0217\nbh0.00.00.0\nbt01.01\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0217"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 1, 1)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0217 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0217.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0217\nbh 0.0 0.0 0.0\nbt 0 1.0 1\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0217.wya') as content_file:
            wymodelmanager0217.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0217")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 1, 1))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0218(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0218

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0218" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0218" head (0.0,0.0,0.0) and tail (0, 0.1, 0.1) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0218.wya','w+')asfile:
file.write("bnTestArmatureBoneName0218\nbh0.00.00.0\nbt00.10.1\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0218"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0.1, 0.1)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0218 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0218.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0218\nbh 0.0 0.0 0.0\nbt 0 0.1 0.1\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0218.wya') as content_file:
            wymodelmanager0218.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0218")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0.1, 0.1))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0219(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0219

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0219" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0219" head (0.0,0.0,0.0) and tail (0, 0.01, 0.001) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0219.wya','w+')asfile:
file.write("bnTestArmatureBoneName0219\nbh0.00.00.0\nbt00.010.001\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0219"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0.01, 0.001)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0219 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0219.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0219\nbh 0.0 0.0 0.0\nbt 0 0.01 0.001\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0219.wya') as content_file:
            wymodelmanager0219.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0219")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0.01, 0.001))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0220(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0220

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0220" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0220" head (0.0,0.0,0.0) and tail (0, 0.0001, 0.0001) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0220.wya','w+')asfile:
file.write("bnTestArmatureBoneName0220\nbh0.00.00.0\nbt00.00010.0001\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0220"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0.0001, 0.0001)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0220 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0220.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0220\nbh 0.0 0.0 0.0\nbt 0 0.0001 0.0001\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0220.wya') as content_file:
            wymodelmanager0220.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0220")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 0.0001, 0.0001))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0221(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0221

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0221" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0221" head (0.0,0.0,0.0) and tail (0, 2, 2) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0221.wya','w+')asfile:
file.write("bnTestArmatureBoneName0221\nbh0.00.00.0\nbt02.02\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0221"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 2, 2)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0221 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0221.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0221\nbh 0.0 0.0 0.0\nbt 0 2.0 2\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0221.wya') as content_file:
            wymodelmanager0221.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0221")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 2, 2))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0222(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0222

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0222" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0222" head (0.0,0.0,0.0) and tail (0, 3, 3) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0222.wya','w+')asfile:
file.write("bnTestArmatureBoneName0222\nbh0.00.00.0\nbt03.03\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0222"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 3, 3)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0222 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0222.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0222\nbh 0.0 0.0 0.0\nbt 0 3.0 3\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0222.wya') as content_file:
            wymodelmanager0222.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0222")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 3, 3))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0223(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0223

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0223" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0223" head (0.0,0.0,0.0) and tail (0, 10, 10) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0223.wya','w+')asfile:
file.write("bnTestArmatureBoneName0223\nbh0.00.00.0\nbt010.010\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0223"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 10, 10)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0223 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0223.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0223\nbh 0.0 0.0 0.0\nbt 0 10.0 10\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0223.wya') as content_file:
            wymodelmanager0223.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0223")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 10, 10))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0224(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0224

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0224" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0224" head (0.0,0.0,0.0) and tail (0, 20, 20) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0224.wya','w+')asfile:
file.write("bnTestArmatureBoneName0224\nbh0.00.00.0\nbt020.020\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0224"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 20, 20)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0224 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0224.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0224\nbh 0.0 0.0 0.0\nbt 0 20.0 20\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0224.wya') as content_file:
            wymodelmanager0224.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0224")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 20, 20))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0225(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0225

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0225" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0225" head (0.0,0.0,0.0) and tail (0, 30, 30) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0225.wya','w+')asfile:
file.write("bnTestArmatureBoneName0225\nbh0.00.00.0\nbt030.030\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0225"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 30, 30)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0225 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0225.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0225\nbh 0.0 0.0 0.0\nbt 0 30.0 30\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0225.wya') as content_file:
            wymodelmanager0225.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0225")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 30, 30))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0226(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0226

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0226" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0226" head (0.0,0.0,0.0) and tail (0, 100, 100) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0226.wya','w+')asfile:
file.write("bnTestArmatureBoneName0226\nbh0.00.00.0\nbt0100.0100\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0226"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 100, 100)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0226 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0226.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0226\nbh 0.0 0.0 0.0\nbt 0 100.0 100\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0226.wya') as content_file:
            wymodelmanager0226.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0226")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 100, 100))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0227(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0227

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0227" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0227" head (0.0,0.0,0.0) and tail (0, 200, 200) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0227.wya','w+')asfile:
file.write("bnTestArmatureBoneName0227\nbh0.00.00.0\nbt0200.0200\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0227"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 200, 200)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0227 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0227.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0227\nbh 0.0 0.0 0.0\nbt 0 200.0 200\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0227.wya') as content_file:
            wymodelmanager0227.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0227")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 200, 200))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0228(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0228

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0228" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0228" head (0.0,0.0,0.0) and tail (0, 300, 300) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0228.wya','w+')asfile:
file.write("bnTestArmatureBoneName0228\nbh0.00.00.0\nbt0300.0300\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0228"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 300, 300)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0228 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0228.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0228\nbh 0.0 0.0 0.0\nbt 0 300.0 300\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0228.wya') as content_file:
            wymodelmanager0228.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0228")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 300, 300))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0229(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0229

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0229" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0229" head (0.0,0.0,0.0) and tail (0, 10000, 10000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0229.wya','w+')asfile:
file.write("bnTestArmatureBoneName0229\nbh0.00.00.0\nbt010000.010000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0229"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 10000, 10000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0229 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0229.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0229\nbh 0.0 0.0 0.0\nbt 0 10000.0 10000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0229.wya') as content_file:
            wymodelmanager0229.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0229")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 10000, 10000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0230(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0230

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0230" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0230" head (0.0,0.0,0.0) and tail (0, 20000, 20000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0230.wya','w+')asfile:
file.write("bnTestArmatureBoneName0230\nbh0.00.00.0\nbt020000.020000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0230"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 20000, 20000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0230 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0230.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0230\nbh 0.0 0.0 0.0\nbt 0 20000.0 20000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0230.wya') as content_file:
            wymodelmanager0230.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0230")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 20000, 20000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0231(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0231

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0231" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0231" head (0.0,0.0,0.0) and tail (0, 30000, 30000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0231.wya','w+')asfile:
file.write("bnTestArmatureBoneName0231\nbh0.00.00.0\nbt030000.030000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0231"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 30000, 30000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0231 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0231.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0231\nbh 0.0 0.0 0.0\nbt 0 30000.0 30000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0231.wya') as content_file:
            wymodelmanager0231.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0231")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 30000, 30000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0232(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0232

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0232" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0232" head (0.0,0.0,0.0) and tail (0, 1000000, 1000000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0232.wya','w+')asfile:
file.write("bnTestArmatureBoneName0232\nbh0.00.00.0\nbt01000000.01000000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0232"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 1000000, 1000000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0232 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0232.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0232\nbh 0.0 0.0 0.0\nbt 0 1000000.0 1000000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0232.wya') as content_file:
            wymodelmanager0232.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0232")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 1000000, 1000000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0233(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0233

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0233" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0233" head (0.0,0.0,0.0) and tail (0, 2000000, 2000000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0233.wya','w+')asfile:
file.write("bnTestArmatureBoneName0233\nbh0.00.00.0\nbt02000000.02000000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0233"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 2000000, 2000000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0233 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0233.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0233\nbh 0.0 0.0 0.0\nbt 0 2000000.0 2000000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0233.wya') as content_file:
            wymodelmanager0233.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0233")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 2000000, 2000000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0234(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0234

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0234" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0234" head (0.0,0.0,0.0) and tail (0, 3000000, 3000000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0234.wya','w+')asfile:
file.write("bnTestArmatureBoneName0234\nbh0.00.00.0\nbt03000000.03000000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0234"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 3000000, 3000000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0234 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0234.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0234\nbh 0.0 0.0 0.0\nbt 0 3000000.0 3000000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0234.wya') as content_file:
            wymodelmanager0234.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0234")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0, 3000000, 3000000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0235(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0235

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0235" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0235" head (0.0,0.0,0.0) and tail (1, 1, 1) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0235.wya','w+')asfile:
file.write("bnTestArmatureBoneName0235\nbh0.00.00.0\nbt11.01\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0235"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (1, 1, 1)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0235 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0235.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0235\nbh 0.0 0.0 0.0\nbt 1 1.0 1\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0235.wya') as content_file:
            wymodelmanager0235.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0235")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (1, 1, 1))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0236(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0236

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0236" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0236" head (0.0,0.0,0.0) and tail (0.1, 0.1, 0.1) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0236.wya','w+')asfile:
file.write("bnTestArmatureBoneName0236\nbh0.00.00.0\nbt0.10.10.1\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0236"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.1, 0.1, 0.1)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0236 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0236.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0236\nbh 0.0 0.0 0.0\nbt 0.1 0.1 0.1\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0236.wya') as content_file:
            wymodelmanager0236.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0236")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.1, 0.1, 0.1))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0237(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0237

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0237" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0237" head (0.0,0.0,0.0) and tail (0.001, 0.01, 0.001) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0237.wya','w+')asfile:
file.write("bnTestArmatureBoneName0237\nbh0.00.00.0\nbt0.0010.010.001\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0237"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.001, 0.01, 0.001)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0237 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0237.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0237\nbh 0.0 0.0 0.0\nbt 0.001 0.01 0.001\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0237.wya') as content_file:
            wymodelmanager0237.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0237")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.001, 0.01, 0.001))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0238(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0238

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0238" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0238" head (0.0,0.0,0.0) and tail (0.0001, 0.0001, 0.0001) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0238.wya','w+')asfile:
file.write("bnTestArmatureBoneName0238\nbh0.00.00.0\nbt0.00010.00010.0001\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0238"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0001, 0.0001, 0.0001)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0238 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0238.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0238\nbh 0.0 0.0 0.0\nbt 0.0001 0.0001 0.0001\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0238.wya') as content_file:
            wymodelmanager0238.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0238")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (0.0001, 0.0001, 0.0001))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0239(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0239

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0239" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0239" head (0.0,0.0,0.0) and tail (2, 2, 2) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0239.wya','w+')asfile:
file.write("bnTestArmatureBoneName0239\nbh0.00.00.0\nbt22.02\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0239"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (2, 2, 2)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0239 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0239.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0239\nbh 0.0 0.0 0.0\nbt 2 2.0 2\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0239.wya') as content_file:
            wymodelmanager0239.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0239")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (2, 2, 2))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0240(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0240

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0240" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0240" head (0.0,0.0,0.0) and tail (3, 3, 3) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0240.wya','w+')asfile:
file.write("bnTestArmatureBoneName0240\nbh0.00.00.0\nbt33.03\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0240"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (3, 3, 3)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0240 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0240.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0240\nbh 0.0 0.0 0.0\nbt 3 3.0 3\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0240.wya') as content_file:
            wymodelmanager0240.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0240")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (3, 3, 3))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0241(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0241

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0241" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0241" head (0.0,0.0,0.0) and tail (10, 10, 10) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0241.wya','w+')asfile:
file.write("bnTestArmatureBoneName0241\nbh0.00.00.0\nbt1010.010\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0241"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (10, 10, 10)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0241 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0241.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0241\nbh 0.0 0.0 0.0\nbt 10 10.0 10\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0241.wya') as content_file:
            wymodelmanager0241.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0241")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (10, 10, 10))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0242(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0242

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0242" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0242" head (0.0,0.0,0.0) and tail (20, 20, 20) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0242.wya','w+')asfile:
file.write("bnTestArmatureBoneName0242\nbh0.00.00.0\nbt2020.020\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0242"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (20, 20, 20)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0242 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0242.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0242\nbh 0.0 0.0 0.0\nbt 20 20.0 20\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0242.wya') as content_file:
            wymodelmanager0242.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0242")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (20, 20, 20))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0243(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0243

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0243" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0243" head (0.0,0.0,0.0) and tail (30, 30, 30) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0243.wya','w+')asfile:
file.write("bnTestArmatureBoneName0243\nbh0.00.00.0\nbt3030.030\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0243"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (30, 30, 30)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0243 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0243.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0243\nbh 0.0 0.0 0.0\nbt 30 30.0 30\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0243.wya') as content_file:
            wymodelmanager0243.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0243")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (30, 30, 30))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0244(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0244

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0244" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0244" head (0.0,0.0,0.0) and tail (100, 100, 100) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0244.wya','w+')asfile:
file.write("bnTestArmatureBoneName0244\nbh0.00.00.0\nbt100100.0100\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0244"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (100, 100, 100)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0244 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0244.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0244\nbh 0.0 0.0 0.0\nbt 100 100.0 100\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0244.wya') as content_file:
            wymodelmanager0244.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0244")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (100, 100, 100))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0245(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0245

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0245" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0245" head (0.0,0.0,0.0) and tail (200, 200, 200) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0245.wya','w+')asfile:
file.write("bnTestArmatureBoneName0245\nbh0.00.00.0\nbt200200.0200\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0245"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (200, 200, 200)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0245 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0245.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0245\nbh 0.0 0.0 0.0\nbt 200 200.0 200\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0245.wya') as content_file:
            wymodelmanager0245.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0245")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (200, 200, 200))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0246(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0246

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0246" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0246" head (0.0,0.0,0.0) and tail (300, 300, 300) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0246.wya','w+')asfile:
file.write("bnTestArmatureBoneName0246\nbh0.00.00.0\nbt300300.0300\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0246"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (300, 300, 300)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0246 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0246.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0246\nbh 0.0 0.0 0.0\nbt 300 300.0 300\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0246.wya') as content_file:
            wymodelmanager0246.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0246")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (300, 300, 300))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0247(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0247

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0247" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0247" head (0.0,0.0,0.0) and tail (10000, 10000, 10000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0247.wya','w+')asfile:
file.write("bnTestArmatureBoneName0247\nbh0.00.00.0\nbt1000010000.010000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0247"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (10000, 10000, 10000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0247 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0247.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0247\nbh 0.0 0.0 0.0\nbt 10000 10000.0 10000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0247.wya') as content_file:
            wymodelmanager0247.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0247")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (10000, 10000, 10000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0248(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0248

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0248" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0248" head (0.0,0.0,0.0) and tail (20000, 20000, 20000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0248.wya','w+')asfile:
file.write("bnTestArmatureBoneName0248\nbh0.00.00.0\nbt2000020000.020000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0248"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (20000, 20000, 20000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0248 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0248.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0248\nbh 0.0 0.0 0.0\nbt 20000 20000.0 20000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0248.wya') as content_file:
            wymodelmanager0248.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0248")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (20000, 20000, 20000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0249(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0249

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0249" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0249" head (0.0,0.0,0.0) and tail (30000, 30000, 30000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0249.wya','w+')asfile:
file.write("bnTestArmatureBoneName0249\nbh0.00.00.0\nbt3000030000.030000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0249"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (30000, 30000, 30000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0249 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0249.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0249\nbh 0.0 0.0 0.0\nbt 30000 30000.0 30000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0249.wya') as content_file:
            wymodelmanager0249.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0249")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (30000, 30000, 30000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0250(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0250

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0250" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0250" head (0.0,0.0,0.0) and tail (1000000, 1000000, 1000000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0250.wya','w+')asfile:
file.write("bnTestArmatureBoneName0250\nbh0.00.00.0\nbt10000001000000.01000000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0250"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (1000000, 1000000, 1000000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0250 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0250.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0250\nbh 0.0 0.0 0.0\nbt 1000000 1000000.0 1000000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0250.wya') as content_file:
            wymodelmanager0250.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0250")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (1000000, 1000000, 1000000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0251(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0251

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0251" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0251" head (0.0,0.0,0.0) and tail (2000000, 2000000, 2000000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0251.wya','w+')asfile:
file.write("bnTestArmatureBoneName0251\nbh0.00.00.0\nbt20000002000000.02000000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0251"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (2000000, 2000000, 2000000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0251 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0251.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0251\nbh 0.0 0.0 0.0\nbt 2000000 2000000.0 2000000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0251.wya') as content_file:
            wymodelmanager0251.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0251")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (2000000, 2000000, 2000000))
    def test_WYModelManagerTestCase_import_wyarmaturebone_TC_NC_0252(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wyarmaturebone function testing normal case 0252

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYArmatureBone objects are imported from given path "..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0252" through "import_wyarmaturebone" function resulting the data values exported to file is equal to the expected value where armature bone is name "TestArmatureBoneName0252" head (0.0,0.0,0.0) and tail (3000000, 3000000, 3000000) is exported.
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wyarmature: WYArmature object to store the imported WYArmatureBone objects imported from same file..
        :type  wyarmature: WYArmature.
        :test  wyarmature: wyarmature=WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)).

        :param wyarmature_file_obj: File object opened for importing WYArmature object..
        :type  wyarmature_file_obj: File.
        :test  wyarmature_file_obj: withopen(os.getcwd()+"\\"+'..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0252.wya','w+')asfile:
file.write("bnTestArmatureBoneName0252\nbh0.00.00.0\nbt30000003000000.03000000\n").

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : void
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0252"
        :expect: wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0)
        :expect: wyarmature.armature_bones_arr[0].armature_bone_tail == (3000000, 3000000, 3000000)
        """
        wyarmature = WYArmature(None,None,WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymodelmanager0252 = WYModelManager()
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0252.wya', 'w+') as file:
            file.write("bn TestArmatureBoneName0252\nbh 0.0 0.0 0.0\nbt 3000000 3000000.0 3000000\n")
        with open(os.getcwd() + "\\" + '..\\..\\test\\WYModelManagerTestCases_import_wyarmaturebone\\TestFile0252.wya') as content_file:
            wymodelmanager0252.import_wyarmaturebone(wyarmature, content_file) 
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_name == "TestArmatureBoneName0252")
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_head == (0.0,0.0,0.0))
        self.assertTrue(wyarmature.armature_bones_arr[0].armature_bone_tail == (3000000, 3000000, 3000000))

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_import_wyarmaturebone))
