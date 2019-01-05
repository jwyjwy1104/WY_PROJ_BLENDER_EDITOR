"""
Project name                        : WY_PROJ_BLENDER_EDITOR
Date of creation                    : 2017-11-09
Last update                         : 2017-11-09
Created by                          : NICK JANG
Test case file name                 : ..\..\test\WYMeshTestCases___eq__\WYMeshTestCases___eq__.py
Test case data file name            : ..\..\test\WYMeshTestCases___eq__\WYMeshTestCases___eq__.txt
Testing class file name             : ..\..\main\WYModel\WYModel.py
Testing class function name         : __eq__(other)
Unit test case class name           : WYMeshTestCases___eq__
Unit test case description          : Unit test case for class WYMesh __eq__() function
Unit test case result file name     : ..\..\test\WYMeshTestCases___eq__\WYMeshTestCaseResult___eq__.txt
"""
# Pre-condition: WYMesh must be tested.
# Pre-condition: WYMaterial must be tested.
# Pre-condition: WYUtil must be tested.
# Pre-condition: WYCoordsys must be tested.
import os
import sys
import math
import unittest
precompile_filename = "C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\tools\\OAuthTestGenerator\\..\\..\\main\\WYModel\\WYModel.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYMeshTestCases___eq__(unittest.TestCase):
    """
    Unit test case for class WYMesh __eq__() function

    ----------------------------------------------------------------------
    Summary
    ----------------------------------------------------------------------
        Number of normal case test     :10
        Number of boundary case test   :0
        Number of error case test      :10
        Number of white box test       :0
        Number of black box test       :0
    """
    def test_WYMeshTestCase___eq___TC_NC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing normal case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns True resulting wymesh == wymesh2.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0001"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh2 = WYMesh(cube,wycoordsys)
        self.assertTrue(wymesh == wymesh2)
    def test_WYMeshTestCase___eq___TC_NC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing normal case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns True resulting wymesh == wymesh3.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0002"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh3 = WYMesh(cube,wycoordsys)
        self.assertTrue(wymesh == wymesh3)
    def test_WYMeshTestCase___eq___TC_NC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing normal case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns True resulting wymesh == wymesh4.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0003"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh4 = WYMesh(cube,wycoordsys)
        self.assertTrue(wymesh == wymesh4)
    def test_WYMeshTestCase___eq___TC_NC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing normal case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns True resulting wymesh == wymesh5.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0004"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh5 = WYMesh(cube,wycoordsys)
        self.assertTrue(wymesh == wymesh5)
    def test_WYMeshTestCase___eq___TC_NC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing normal case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns True resulting wymesh == wymesh6.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0005"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh6 = WYMesh(cube,wycoordsys)
        self.assertTrue(wymesh == wymesh6)
    def test_WYMeshTestCase___eq___TC_NC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing normal case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns True resulting wymesh == wymesh7.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0006"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh7 = WYMesh(cube,wycoordsys)
        self.assertTrue(wymesh == wymesh7)
    def test_WYMeshTestCase___eq___TC_NC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing normal case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns True resulting wymesh == wymesh8.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0007"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh8 = WYMesh(cube,wycoordsys)
        self.assertTrue(wymesh == wymesh8)
    def test_WYMeshTestCase___eq___TC_NC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing normal case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns True resulting wymesh == wymesh9.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0008"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh9 = WYMesh(cube,wycoordsys)
        self.assertTrue(wymesh == wymesh9)
    def test_WYMeshTestCase___eq___TC_NC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing normal case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns True resulting wymesh == wymesh10.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0009"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh10 = WYMesh(cube,wycoordsys)
        self.assertTrue(wymesh == wymesh10)
    def test_WYMeshTestCase___eq___TC_NC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing normal case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns True resulting wymesh == wymesh11.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys =  WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0010"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh11 = WYMesh(cube,wycoordsys)
        self.assertTrue(wymesh == wymesh11)
    def test_WYMeshTestCase___eq___TC_EC_0001(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing error case 0001

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns False when initialized with different values, one with WYCoordsys init code WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False) and other one with init codeWYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False) resulting wymesh != wymesh12.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys = WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        wycoordsys2 = WYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0011"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh12 = WYMesh(cube,wycoordsys2)
        self.assertTrue(wymesh != wymesh12)
    def test_WYMeshTestCase___eq___TC_EC_0002(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing error case 0002

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns False when initialized with different values, one with WYCoordsys init code WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False) and other one with init codeWYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False) resulting wymesh != wymesh13.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys = WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        wycoordsys2 = WYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0012"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh13 = WYMesh(cube,wycoordsys2)
        self.assertTrue(wymesh != wymesh13)
    def test_WYMeshTestCase___eq___TC_EC_0003(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing error case 0003

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns False when initialized with different values, one with WYCoordsys init code WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False) and other one with init codeWYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False) resulting wymesh != wymesh14.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys = WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        wycoordsys2 = WYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0013"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh14 = WYMesh(cube,wycoordsys2)
        self.assertTrue(wymesh != wymesh14)
    def test_WYMeshTestCase___eq___TC_EC_0004(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing error case 0004

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns False when initialized with different values, one with WYCoordsys init code WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False) and other one with init codeWYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False) resulting wymesh != wymesh15.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys = WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        wycoordsys2 = WYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0014"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh15 = WYMesh(cube,wycoordsys2)
        self.assertTrue(wymesh != wymesh15)
    def test_WYMeshTestCase___eq___TC_EC_0005(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing error case 0005

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns False when initialized with different values, one with WYCoordsys init code WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False) and other one with init codeWYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False) resulting wymesh != wymesh16.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys = WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        wycoordsys2 = WYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0015"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh16 = WYMesh(cube,wycoordsys2)
        self.assertTrue(wymesh != wymesh16)
    def test_WYMeshTestCase___eq___TC_EC_0006(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing error case 0006

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns False when initialized with different values, one with WYCoordsys init code WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False) and other one with init codeWYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False) resulting wymesh != wymesh17.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys = WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        wycoordsys2 = WYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0016"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh17 = WYMesh(cube,wycoordsys2)
        self.assertTrue(wymesh != wymesh17)
    def test_WYMeshTestCase___eq___TC_EC_0007(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing error case 0007

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns False when initialized with different values, one with WYCoordsys init code WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False) and other one with init codeWYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False) resulting wymesh != wymesh18.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys = WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        wycoordsys2 = WYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0017"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh18 = WYMesh(cube,wycoordsys2)
        self.assertTrue(wymesh != wymesh18)
    def test_WYMeshTestCase___eq___TC_EC_0008(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing error case 0008

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns False when initialized with different values, one with WYCoordsys init code WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False) and other one with init codeWYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False) resulting wymesh != wymesh19.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys = WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        wycoordsys2 = WYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0018"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh19 = WYMesh(cube,wycoordsys2)
        self.assertTrue(wymesh != wymesh19)
    def test_WYMeshTestCase___eq___TC_EC_0009(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing error case 0009

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns False when initialized with different values, one with WYCoordsys init code WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False) and other one with init codeWYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False) resulting wymesh != wymesh20.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys = WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        wycoordsys2 = WYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0019"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh20 = WYMesh(cube,wycoordsys2)
        self.assertTrue(wymesh != wymesh20)
    def test_WYMeshTestCase___eq___TC_EC_0010(self):
        """
        ----------------------------------------------------------------------
        Title:
        ----------------------------------------------------------------------
        WYMesh __eq__ function testing error case 0010

        ----------------------------------------------------------------------
        Description:
        ----------------------------------------------------------------------
        Testing if 2 same WYMesh object compare with "__eq__" function returns False when initialized with different values, one with WYCoordsys init code WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False) and other one with init codeWYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False) resulting wymesh != wymesh21.
        ----------------------------------------------------------------------
        Return:
        ----------------------------------------------------------------------
        :return: Return initialized WYMesh object with member variables intialized properly
        :rtype : boolean
        ----------------------------------------------------------------------
        Expected result:
        ----------------------------------------------------------------------
        """
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        wycoordsys = WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False)
        wycoordsys2 = WYCoordsys(False,False,False,False,True,False,False,False,False,True,False,False)
        cube = bpy.context.object
        cube.name = "TestCube0020"
        wymesh = WYMesh(cube,wycoordsys)
        wymesh21 = WYMesh(cube,wycoordsys2)
        self.assertTrue(wymesh != wymesh21)

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYMeshTestCases___eq__))
