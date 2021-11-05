import main.equillateral_triangle as equillateral_triangle
import unittest
import math

class equillateral_triangleTest(unittest.TestCase):
    #test negative
    def testcase1_1(self):
        assert(equillateral_triangle.calcArea(-1)==None)
    #test 1
    def testcase2_1(self):
        area = equillateral_triangle.calcArea(1)
        assert(area==.43)
    #test 0
    def testcase3_1(self):
        assert(equillateral_triangle.calcArea(0)==0)
        
if __name__=="__main__":
    unittest.main()