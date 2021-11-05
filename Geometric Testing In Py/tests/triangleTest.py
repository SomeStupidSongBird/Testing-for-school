import main.triangle as triangle
import unittest
import math


class triangleTest(unittest.TestCase):
    def testcase1_1(self):
        assert(triangle.calcArea(-1,1,1)==None)
    #test 1
    def testcase2_1(self):
        area = triangle.calcArea(1,1,1)
        assert(area==.43)
    #test non-equillateral
    def testcase3_1(self):
        area = triangle.calcArea(1,3,3)
        assert(area==1.48)
    #test 0
    def testcase3_1(self):
        assert(triangle.calcArea(0,1,1)==None)

if __name__=="__main__":
    unittest.main()