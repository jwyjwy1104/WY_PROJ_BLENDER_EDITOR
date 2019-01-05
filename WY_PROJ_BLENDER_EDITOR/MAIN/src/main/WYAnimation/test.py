import os
import sys
import math
import unittest
precompile_filename = "WYUtil.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYUtilTestCase_triangulate_mesh(unittest.TestCase):
    def test_WYUtilTestCase_triangulate_mesh_TC_NC_0001(self):
        wyutil_nc0001 = WYUtil()
        self.assertTrue(wycoordsys_nc0001.XU == True)
        self.assertTrue(wycoordsys_nc0001.YF == True)
        self.assertTrue(wycoordsys_nc0001.coordoption_up_str == "X")
        self.assertTrue(wycoordsys_nc0001.coordoption_forward_str == "Y")
    
if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYCoordsysTestCases___init__))
