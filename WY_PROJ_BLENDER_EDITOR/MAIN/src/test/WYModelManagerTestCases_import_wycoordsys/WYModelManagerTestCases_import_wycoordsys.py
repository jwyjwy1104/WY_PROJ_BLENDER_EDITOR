"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2017-11-23
Last update                         : 2017-11-23
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_import_wycoordsys\WYModelManagerTestCases_import_wycoordsys.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_import_wycoordsys\WYModelManagerTestCases_import_wycoordsys.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : import_wycoordsys(wycoordsys_file_path)
Unit test case class name           : WYModelManagerTestCases_import_wycoordsys
Unit test case description          : Unit test case for class WYModelManager import_wycoordsys() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_import_wycoordsys\WYModelManagerTestCaseResult_import_wycoordsys.txt
"""
# Pre-condition: WYModel is tested.
# Pre-condition: WYCoordsys::__str__() is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_import_wycoordsys(unittest.TestCase):
    """
    Unit test case for class WYModelManager import_wycoordsys() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :24
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU X\nCF Y\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0001.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU X\\nCF Y\\n
        """
        
        wymodelmanager0001 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0001.wyo", 'w+') as content_file:
            content_file.write("CU X\nCF Y\n")
        wycoordsys = wymodelmanager0001.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0001.wyo")         
        self.assertTrue(str(wycoordsys) == "CU X\nCF Y\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU X\nCF -Y\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0002.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU X\\nCF -Y\\n
        """
        
        wymodelmanager0002 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0002.wyo", 'w+') as content_file:
            content_file.write("CU X\nCF -Y\n")
        wycoordsys = wymodelmanager0002.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0002.wyo")         
        self.assertTrue(str(wycoordsys) == "CU X\nCF -Y\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU X\nCF Z\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0003.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU X\\nCF Z\\n
        """
        
        wymodelmanager0003 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0003.wyo", 'w+') as content_file:
            content_file.write("CU X\nCF Z\n")
        wycoordsys = wymodelmanager0003.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0003.wyo")         
        self.assertTrue(str(wycoordsys) == "CU X\nCF Z\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU X\nCF -Z\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0004.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU X\\nCF -Z\\n
        """
        
        wymodelmanager0004 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0004.wyo", 'w+') as content_file:
            content_file.write("CU X\nCF -Z\n")
        wycoordsys = wymodelmanager0004.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0004.wyo")         
        self.assertTrue(str(wycoordsys) == "CU X\nCF -Z\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU -X\nCF Y\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0005.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU -X\\nCF Y\\n
        """
        
        wymodelmanager0005 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0005.wyo", 'w+') as content_file:
            content_file.write("CU -X\nCF Y\n")
        wycoordsys = wymodelmanager0005.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0005.wyo")         
        self.assertTrue(str(wycoordsys) == "CU -X\nCF Y\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU -X\nCF -Y\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0006.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU -X\\nCF -Y\\n
        """
        
        wymodelmanager0006 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0006.wyo", 'w+') as content_file:
            content_file.write("CU -X\nCF -Y\n")
        wycoordsys = wymodelmanager0006.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0006.wyo")         
        self.assertTrue(str(wycoordsys) == "CU -X\nCF -Y\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU -X\nCF Z\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0007.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU -X\\nCF Z\\n
        """
        
        wymodelmanager0007 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0007.wyo", 'w+') as content_file:
            content_file.write("CU -X\nCF Z\n")
        wycoordsys = wymodelmanager0007.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0007.wyo")         
        self.assertTrue(str(wycoordsys) == "CU -X\nCF Z\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU -X\nCF -Z\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0008.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU -X\\nCF -Z\\n
        """
        
        wymodelmanager0008 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0008.wyo", 'w+') as content_file:
            content_file.write("CU -X\nCF -Z\n")
        wycoordsys = wymodelmanager0008.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0008.wyo")         
        self.assertTrue(str(wycoordsys) == "CU -X\nCF -Z\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU Y\nCF X\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0009.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU Y\\nCF X\\n
        """
        
        wymodelmanager0009 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0009.wyo", 'w+') as content_file:
            content_file.write("CU Y\nCF X\n")
        wycoordsys = wymodelmanager0009.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0009.wyo")         
        self.assertTrue(str(wycoordsys) == "CU Y\nCF X\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU Y\nCF -X\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0010.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU Y\\nCF -X\\n
        """
        
        wymodelmanager0010 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0010.wyo", 'w+') as content_file:
            content_file.write("CU Y\nCF -X\n")
        wycoordsys = wymodelmanager0010.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0010.wyo")         
        self.assertTrue(str(wycoordsys) == "CU Y\nCF -X\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0011(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0011

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU Y\nCF Z\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0011.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU Y\\nCF Z\\n
        """
        
        wymodelmanager0011 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0011.wyo", 'w+') as content_file:
            content_file.write("CU Y\nCF Z\n")
        wycoordsys = wymodelmanager0011.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0011.wyo")         
        self.assertTrue(str(wycoordsys) == "CU Y\nCF Z\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0012(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0012

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU Y\nCF -Z\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0012.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU Y\\nCF -Z\\n
        """
        
        wymodelmanager0012 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0012.wyo", 'w+') as content_file:
            content_file.write("CU Y\nCF -Z\n")
        wycoordsys = wymodelmanager0012.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0012.wyo")         
        self.assertTrue(str(wycoordsys) == "CU Y\nCF -Z\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0013(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0013

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU -Y\nCF X\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0013.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU -Y\\nCF X\\n
        """
        
        wymodelmanager0013 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0013.wyo", 'w+') as content_file:
            content_file.write("CU -Y\nCF X\n")
        wycoordsys = wymodelmanager0013.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0013.wyo")         
        self.assertTrue(str(wycoordsys) == "CU -Y\nCF X\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0014(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0014

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU -Y\nCF -X\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0014.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU -Y\\nCF -X\\n
        """
        
        wymodelmanager0014 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0014.wyo", 'w+') as content_file:
            content_file.write("CU -Y\nCF -X\n")
        wycoordsys = wymodelmanager0014.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0014.wyo")         
        self.assertTrue(str(wycoordsys) == "CU -Y\nCF -X\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0015(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0015

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU -Y\nCF Z\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0015.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU -Y\\nCF Z\\n
        """
        
        wymodelmanager0015 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0015.wyo", 'w+') as content_file:
            content_file.write("CU -Y\nCF Z\n")
        wycoordsys = wymodelmanager0015.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0015.wyo")         
        self.assertTrue(str(wycoordsys) == "CU -Y\nCF Z\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0016(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0016

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU -Y\nCF -Z\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0016.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU -Y\\nCF -Z\\n
        """
        
        wymodelmanager0016 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0016.wyo", 'w+') as content_file:
            content_file.write("CU -Y\nCF -Z\n")
        wycoordsys = wymodelmanager0016.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0016.wyo")         
        self.assertTrue(str(wycoordsys) == "CU -Y\nCF -Z\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0017(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0017

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU Z\nCF X\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0017.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU Z\\nCF X\\n
        """
        
        wymodelmanager0017 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0017.wyo", 'w+') as content_file:
            content_file.write("CU Z\nCF X\n")
        wycoordsys = wymodelmanager0017.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0017.wyo")         
        self.assertTrue(str(wycoordsys) == "CU Z\nCF X\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0018(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0018

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU Z\nCF -X\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0018.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU Z\\nCF -X\\n
        """
        
        wymodelmanager0018 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0018.wyo", 'w+') as content_file:
            content_file.write("CU Z\nCF -X\n")
        wycoordsys = wymodelmanager0018.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0018.wyo")         
        self.assertTrue(str(wycoordsys) == "CU Z\nCF -X\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0019(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0019

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU Z\nCF Y\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0019.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU Z\\nCF Y\\n
        """
        
        wymodelmanager0019 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0019.wyo", 'w+') as content_file:
            content_file.write("CU Z\nCF Y\n")
        wycoordsys = wymodelmanager0019.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0019.wyo")         
        self.assertTrue(str(wycoordsys) == "CU Z\nCF Y\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0020(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0020

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU Z\nCF -Y\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0020.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU Z\\nCF -Y\\n
        """
        
        wymodelmanager0020 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0020.wyo", 'w+') as content_file:
            content_file.write("CU Z\nCF -Y\n")
        wycoordsys = wymodelmanager0020.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0020.wyo")         
        self.assertTrue(str(wycoordsys) == "CU Z\nCF -Y\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0021(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0021

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU -Z\nCF X\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0021.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU -Z\\nCF X\\n
        """
        
        wymodelmanager0021 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0021.wyo", 'w+') as content_file:
            content_file.write("CU -Z\nCF X\n")
        wycoordsys = wymodelmanager0021.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0021.wyo")         
        self.assertTrue(str(wycoordsys) == "CU -Z\nCF X\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0022(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0022

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU -Z\nCF -X\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0022.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU -Z\\nCF -X\\n
        """
        
        wymodelmanager0022 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0022.wyo", 'w+') as content_file:
            content_file.write("CU -Z\nCF -X\n")
        wycoordsys = wymodelmanager0022.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0022.wyo")         
        self.assertTrue(str(wycoordsys) == "CU -Z\nCF -X\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0023(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0023

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU -Z\nCF Y\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0023.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU -Z\\nCF Y\\n
        """
        
        wymodelmanager0023 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0023.wyo", 'w+') as content_file:
            content_file.write("CU -Z\nCF Y\n")
        wycoordsys = wymodelmanager0023.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0023.wyo")         
        self.assertTrue(str(wycoordsys) == "CU -Z\nCF Y\n")
    def test_WYModelManagerTestCase_import_wycoordsys_TC_NC_0024(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wycoordsys function testing normal case 0024

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYCoordsys object is imported properly through import_wycoordsys function, returning the data values initialized onto a WYCoordsys object resulting the returning WYCoordsys final string value "CU -Z\nCF -Y\n".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wycoordsys_file_path: String of the file path to import the WYCoordsys object from..
        :type  wycoordsys_file_path: string.
        :test  wycoordsys_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0024.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYCoordsys
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: CU -Z\\nCF -Y\\n
        """
        
        wymodelmanager0024 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0024.wyo", 'w+') as content_file:
            content_file.write("CU -Z\nCF -Y\n")
        wycoordsys = wymodelmanager0024.import_wycoordsys(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wycoordsys\\Test0024.wyo")         
        self.assertTrue(str(wycoordsys) == "CU -Z\nCF -Y\n")

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_import_wycoordsys))
