"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2017-11-23
Last update                         : 2018-01-21
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYModelManagerTestCases_import_wymesh\WYModelManagerTestCases_import_wymesh.py
Test case data file name            : ..\..\test\WYModelManagerTestCases_import_wymesh\WYModelManagerTestCases_import_wymesh.txt
Testing class file name             : ..\..\main\WYModelManager\WYModelManager.py
Testing class function name         : import_wymesh(wymesh_file_path)
Unit test case class name           : WYModelManagerTestCases_import_wymesh
Unit test case description          : Unit test case for class WYModelManager import_wymesh() function
Unit test case result file name     : ..\..\test\WYModelManagerTestCases_import_wymesh\WYModelManagerTestCaseResult_import_wymesh.txt
"""
# Pre-condition: WYModel is tested.
# Pre-condition: WYCoordsys::__str__() is tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModelManager\\WYModelManager.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYModelManagerTestCases_import_wymesh(unittest.TestCase):
    """
    Unit test case for class WYModelManager import_wymesh() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :0
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYModelManagerTestCase_import_wymesh_TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wymesh function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYMesh object is imported properly through import_wymesh function, returning the data values initialized onto a WYMesh object resulting the returning WYMesh final string value ""o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymesh_file_path: String of the file path to import the WYMesh object from..
        :type  wymesh_file_path: string.
        :test  wymesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0001.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMesh
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o \\nCU Z\\nCF Y\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nvt 0.0000 0.0000\\nvt 1.0000 0.0000\\nvt 1.0000 1.0000\\nvt 0.0000 1.0000\\nf 2/2/2 3/4/3 1/1/1\\nf 4/2/4 7/4/7 3/1/3\\nf 8/2/8 5/4/5 7/1/7\\nf 6/2/6 1/4/1 5/1/5\\nf 7/2/7 1/4/1 3/1/3\\nf 4/2/4 6/4/6 8/1/8\\nf 2/2/2 4/3/4 3/4/3\\nf 4/2/4 8/3/8 7/4/7\\nf 8/2/8 6/3/6 5/4/5\\nf 6/2/6 2/3/2 1/4/1\\nf 7/2/7 5/3/5 1/4/1\\nf 4/2/4 2/3/2 6/4/6\\n"
        """
        
        wymodelmanager0001 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0001.wyo", 'w+') as content_file:
            content_file.write("o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymesh = wymodelmanager0001.import_wymesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0001.wyo")      
        self.assertTrue(str(wymesh) == "o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
    def test_WYModelManagerTestCase_import_wymesh_TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wymesh function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYMesh object is imported properly through import_wymesh function, returning the data values initialized onto a WYMesh object resulting the returning WYMesh final string value ""o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymesh_file_path: String of the file path to import the WYMesh object from..
        :type  wymesh_file_path: string.
        :test  wymesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0002.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMesh
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o \\nCU Z\\nCF Y\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nvt 0.0000 0.0000\\nvt 1.0000 0.0000\\nvt 1.0000 1.0000\\nvt 0.0000 1.0000\\nf 2/2/2 3/4/3 1/1/1\\nf 4/2/4 7/4/7 3/1/3\\nf 8/2/8 5/4/5 7/1/7\\nf 6/2/6 1/4/1 5/1/5\\nf 7/2/7 1/4/1 3/1/3\\nf 4/2/4 6/4/6 8/1/8\\nf 2/2/2 4/3/4 3/4/3\\nf 4/2/4 8/3/8 7/4/7\\nf 8/2/8 6/3/6 5/4/5\\nf 6/2/6 2/3/2 1/4/1\\nf 7/2/7 5/3/5 1/4/1\\nf 4/2/4 2/3/2 6/4/6\\n"
        """
        
        wymodelmanager0002 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0002.wyo", 'w+') as content_file:
            content_file.write("o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymesh = wymodelmanager0002.import_wymesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0002.wyo")      
        self.assertTrue(str(wymesh) == "o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
    def test_WYModelManagerTestCase_import_wymesh_TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wymesh function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYMesh object is imported properly through import_wymesh function, returning the data values initialized onto a WYMesh object resulting the returning WYMesh final string value ""o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymesh_file_path: String of the file path to import the WYMesh object from..
        :type  wymesh_file_path: string.
        :test  wymesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0003.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMesh
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o \\nCU Z\\nCF Y\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nvt 0.0000 0.0000\\nvt 1.0000 0.0000\\nvt 1.0000 1.0000\\nvt 0.0000 1.0000\\nf 2/2/2 3/4/3 1/1/1\\nf 4/2/4 7/4/7 3/1/3\\nf 8/2/8 5/4/5 7/1/7\\nf 6/2/6 1/4/1 5/1/5\\nf 7/2/7 1/4/1 3/1/3\\nf 4/2/4 6/4/6 8/1/8\\nf 2/2/2 4/3/4 3/4/3\\nf 4/2/4 8/3/8 7/4/7\\nf 8/2/8 6/3/6 5/4/5\\nf 6/2/6 2/3/2 1/4/1\\nf 7/2/7 5/3/5 1/4/1\\nf 4/2/4 2/3/2 6/4/6\\n"
        """
        
        wymodelmanager0003 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0003.wyo", 'w+') as content_file:
            content_file.write("o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymesh = wymodelmanager0003.import_wymesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0003.wyo")      
        self.assertTrue(str(wymesh) == "o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
    def test_WYModelManagerTestCase_import_wymesh_TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wymesh function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYMesh object is imported properly through import_wymesh function, returning the data values initialized onto a WYMesh object resulting the returning WYMesh final string value ""o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymesh_file_path: String of the file path to import the WYMesh object from..
        :type  wymesh_file_path: string.
        :test  wymesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0004.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMesh
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o \\nCU Z\\nCF Y\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nvt 0.0000 0.0000\\nvt 1.0000 0.0000\\nvt 1.0000 1.0000\\nvt 0.0000 1.0000\\nf 2/2/2 3/4/3 1/1/1\\nf 4/2/4 7/4/7 3/1/3\\nf 8/2/8 5/4/5 7/1/7\\nf 6/2/6 1/4/1 5/1/5\\nf 7/2/7 1/4/1 3/1/3\\nf 4/2/4 6/4/6 8/1/8\\nf 2/2/2 4/3/4 3/4/3\\nf 4/2/4 8/3/8 7/4/7\\nf 8/2/8 6/3/6 5/4/5\\nf 6/2/6 2/3/2 1/4/1\\nf 7/2/7 5/3/5 1/4/1\\nf 4/2/4 2/3/2 6/4/6\\n"
        """
        
        wymodelmanager0004 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0004.wyo", 'w+') as content_file:
            content_file.write("o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymesh = wymodelmanager0004.import_wymesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0004.wyo")      
        self.assertTrue(str(wymesh) == "o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
    def test_WYModelManagerTestCase_import_wymesh_TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wymesh function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYMesh object is imported properly through import_wymesh function, returning the data values initialized onto a WYMesh object resulting the returning WYMesh final string value ""o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymesh_file_path: String of the file path to import the WYMesh object from..
        :type  wymesh_file_path: string.
        :test  wymesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0005.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMesh
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o \\nCU Z\\nCF Y\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nvt 0.0000 0.0000\\nvt 1.0000 0.0000\\nvt 1.0000 1.0000\\nvt 0.0000 1.0000\\nf 2/2/2 3/4/3 1/1/1\\nf 4/2/4 7/4/7 3/1/3\\nf 8/2/8 5/4/5 7/1/7\\nf 6/2/6 1/4/1 5/1/5\\nf 7/2/7 1/4/1 3/1/3\\nf 4/2/4 6/4/6 8/1/8\\nf 2/2/2 4/3/4 3/4/3\\nf 4/2/4 8/3/8 7/4/7\\nf 8/2/8 6/3/6 5/4/5\\nf 6/2/6 2/3/2 1/4/1\\nf 7/2/7 5/3/5 1/4/1\\nf 4/2/4 2/3/2 6/4/6\\n"
        """
        
        wymodelmanager0005 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0005.wyo", 'w+') as content_file:
            content_file.write("o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymesh = wymodelmanager0005.import_wymesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0005.wyo")      
        self.assertTrue(str(wymesh) == "o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
    def test_WYModelManagerTestCase_import_wymesh_TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wymesh function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYMesh object is imported properly through import_wymesh function, returning the data values initialized onto a WYMesh object resulting the returning WYMesh final string value ""o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymesh_file_path: String of the file path to import the WYMesh object from..
        :type  wymesh_file_path: string.
        :test  wymesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0006.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMesh
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o \\nCU Z\\nCF Y\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nvt 0.0000 0.0000\\nvt 1.0000 0.0000\\nvt 1.0000 1.0000\\nvt 0.0000 1.0000\\nf 2/2/2 3/4/3 1/1/1\\nf 4/2/4 7/4/7 3/1/3\\nf 8/2/8 5/4/5 7/1/7\\nf 6/2/6 1/4/1 5/1/5\\nf 7/2/7 1/4/1 3/1/3\\nf 4/2/4 6/4/6 8/1/8\\nf 2/2/2 4/3/4 3/4/3\\nf 4/2/4 8/3/8 7/4/7\\nf 8/2/8 6/3/6 5/4/5\\nf 6/2/6 2/3/2 1/4/1\\nf 7/2/7 5/3/5 1/4/1\\nf 4/2/4 2/3/2 6/4/6\\n"
        """
        
        wymodelmanager0006 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0006.wyo", 'w+') as content_file:
            content_file.write("o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymesh = wymodelmanager0006.import_wymesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0006.wyo")      
        self.assertTrue(str(wymesh) == "o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
    def test_WYModelManagerTestCase_import_wymesh_TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wymesh function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYMesh object is imported properly through import_wymesh function, returning the data values initialized onto a WYMesh object resulting the returning WYMesh final string value ""o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymesh_file_path: String of the file path to import the WYMesh object from..
        :type  wymesh_file_path: string.
        :test  wymesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0007.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMesh
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o \\nCU Z\\nCF Y\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nvt 0.0000 0.0000\\nvt 1.0000 0.0000\\nvt 1.0000 1.0000\\nvt 0.0000 1.0000\\nf 2/2/2 3/4/3 1/1/1\\nf 4/2/4 7/4/7 3/1/3\\nf 8/2/8 5/4/5 7/1/7\\nf 6/2/6 1/4/1 5/1/5\\nf 7/2/7 1/4/1 3/1/3\\nf 4/2/4 6/4/6 8/1/8\\nf 2/2/2 4/3/4 3/4/3\\nf 4/2/4 8/3/8 7/4/7\\nf 8/2/8 6/3/6 5/4/5\\nf 6/2/6 2/3/2 1/4/1\\nf 7/2/7 5/3/5 1/4/1\\nf 4/2/4 2/3/2 6/4/6\\n"
        """
        
        wymodelmanager0007 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0007.wyo", 'w+') as content_file:
            content_file.write("o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymesh = wymodelmanager0007.import_wymesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0007.wyo")      
        self.assertTrue(str(wymesh) == "o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
    def test_WYModelManagerTestCase_import_wymesh_TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wymesh function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYMesh object is imported properly through import_wymesh function, returning the data values initialized onto a WYMesh object resulting the returning WYMesh final string value ""o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymesh_file_path: String of the file path to import the WYMesh object from..
        :type  wymesh_file_path: string.
        :test  wymesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0008.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMesh
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o \\nCU Z\\nCF Y\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nvt 0.0000 0.0000\\nvt 1.0000 0.0000\\nvt 1.0000 1.0000\\nvt 0.0000 1.0000\\nf 2/2/2 3/4/3 1/1/1\\nf 4/2/4 7/4/7 3/1/3\\nf 8/2/8 5/4/5 7/1/7\\nf 6/2/6 1/4/1 5/1/5\\nf 7/2/7 1/4/1 3/1/3\\nf 4/2/4 6/4/6 8/1/8\\nf 2/2/2 4/3/4 3/4/3\\nf 4/2/4 8/3/8 7/4/7\\nf 8/2/8 6/3/6 5/4/5\\nf 6/2/6 2/3/2 1/4/1\\nf 7/2/7 5/3/5 1/4/1\\nf 4/2/4 2/3/2 6/4/6\\n"
        """
        
        wymodelmanager0008 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0008.wyo", 'w+') as content_file:
            content_file.write("o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymesh = wymodelmanager0008.import_wymesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0008.wyo")      
        self.assertTrue(str(wymesh) == "o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
    def test_WYModelManagerTestCase_import_wymesh_TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wymesh function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYMesh object is imported properly through import_wymesh function, returning the data values initialized onto a WYMesh object resulting the returning WYMesh final string value ""o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymesh_file_path: String of the file path to import the WYMesh object from..
        :type  wymesh_file_path: string.
        :test  wymesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0009.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMesh
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o \\nCU Z\\nCF Y\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nvt 0.0000 0.0000\\nvt 1.0000 0.0000\\nvt 1.0000 1.0000\\nvt 0.0000 1.0000\\nf 2/2/2 3/4/3 1/1/1\\nf 4/2/4 7/4/7 3/1/3\\nf 8/2/8 5/4/5 7/1/7\\nf 6/2/6 1/4/1 5/1/5\\nf 7/2/7 1/4/1 3/1/3\\nf 4/2/4 6/4/6 8/1/8\\nf 2/2/2 4/3/4 3/4/3\\nf 4/2/4 8/3/8 7/4/7\\nf 8/2/8 6/3/6 5/4/5\\nf 6/2/6 2/3/2 1/4/1\\nf 7/2/7 5/3/5 1/4/1\\nf 4/2/4 2/3/2 6/4/6\\n"
        """
        
        wymodelmanager0009 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0009.wyo", 'w+') as content_file:
            content_file.write("o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymesh = wymodelmanager0009.import_wymesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0009.wyo")      
        self.assertTrue(str(wymesh) == "o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
    def test_WYModelManagerTestCase_import_wymesh_TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYModelManager import_wymesh function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if the WYMesh object is imported properly through import_wymesh function, returning the data values initialized onto a WYMesh object resulting the returning WYMesh final string value ""o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n"".
        
        ----------------------------------------------------------------------
        Testing function input parameters:
        ----------------------------------------------------------------------
        :param wymesh_file_path: String of the file path to import the WYMesh object from..
        :type  wymesh_file_path: string.
        :test  wymesh_file_path: os.getcwd()+"\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0010.wyo".

        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYModelManager object with member variables intialized properly
        :rtype : WYMesh
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        :expect: "o \\nCU Z\\nCF Y\\nv -1.0 -1.0 -1.0\\nv -1.0 -1.0 1.0\\nv -1.0 1.0 -1.0\\nv -1.0 1.0 1.0\\nv 1.0 -1.0 -1.0\\nv 1.0 -1.0 1.0\\nv 1.0 1.0 -1.0\\nv 1.0 1.0 1.0\\nvn -0.5773 -0.5773 -0.5773\\nvn -0.5773 -0.5773 0.5773\\nvn -0.5773 0.5773 -0.5773\\nvn -0.5773 0.5773 0.5773\\nvn 0.5773 -0.5773 -0.5773\\nvn 0.5773 -0.5773 0.5773\\nvn 0.5773 0.5773 -0.5773\\nvn 0.5773 0.5773 0.5773\\nvt 0.0000 0.0000\\nvt 1.0000 0.0000\\nvt 1.0000 1.0000\\nvt 0.0000 1.0000\\nf 2/2/2 3/4/3 1/1/1\\nf 4/2/4 7/4/7 3/1/3\\nf 8/2/8 5/4/5 7/1/7\\nf 6/2/6 1/4/1 5/1/5\\nf 7/2/7 1/4/1 3/1/3\\nf 4/2/4 6/4/6 8/1/8\\nf 2/2/2 4/3/4 3/4/3\\nf 4/2/4 8/3/8 7/4/7\\nf 8/2/8 6/3/6 5/4/5\\nf 6/2/6 2/3/2 1/4/1\\nf 7/2/7 5/3/5 1/4/1\\nf 4/2/4 2/3/2 6/4/6\\n"
        """
        
        wymodelmanager0010 = WYModelManager() 
        with open(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0010.wyo", 'w+') as content_file:
            content_file.write("o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")
        wymesh = wymodelmanager0010.import_wymesh(os.getcwd() + "\\..\\..\\test\\WYModelManagerTestCases_import_wymesh\\Test0010.wyo")      
        self.assertTrue(str(wymesh) == "o \nCU Z\nCF Y\nv -1.0 -1.0 -1.0\nv -1.0 -1.0 1.0\nv -1.0 1.0 -1.0\nv -1.0 1.0 1.0\nv 1.0 -1.0 -1.0\nv 1.0 -1.0 1.0\nv 1.0 1.0 -1.0\nv 1.0 1.0 1.0\nvn -0.5773 -0.5773 -0.5773\nvn -0.5773 -0.5773 0.5773\nvn -0.5773 0.5773 -0.5773\nvn -0.5773 0.5773 0.5773\nvn 0.5773 -0.5773 -0.5773\nvn 0.5773 -0.5773 0.5773\nvn 0.5773 0.5773 -0.5773\nvn 0.5773 0.5773 0.5773\nvt 0.0000 0.0000\nvt 1.0000 0.0000\nvt 1.0000 1.0000\nvt 0.0000 1.0000\nf 2/2/2 3/4/3 1/1/1\nf 4/2/4 7/4/7 3/1/3\nf 8/2/8 5/4/5 7/1/7\nf 6/2/6 1/4/1 5/1/5\nf 7/2/7 1/4/1 3/1/3\nf 4/2/4 6/4/6 8/1/8\nf 2/2/2 4/3/4 3/4/3\nf 4/2/4 8/3/8 7/4/7\nf 8/2/8 6/3/6 5/4/5\nf 6/2/6 2/3/2 1/4/1\nf 7/2/7 5/3/5 1/4/1\nf 4/2/4 2/3/2 6/4/6\n")

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYModelManagerTestCases_import_wymesh))
