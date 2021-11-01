import main.triangle as triangle
import unittest
import math


class triangleTest(unittest.TestCase):
    def testcase1_1(self):
        assert(triangle.calcArea(-1,1,1)==None)
    #test 1
    def testcase2_1(self):
        area = triangle.calcArea(1,1,1)
        assert(area>.43 and area<.44)
    #test non-equillateral
    def testcase3_1(self):
        area = triangle.calcArea(1,3,3)
        assert(area>1.47 and area<1.48)
    #test 0
    def testcase3_1(self):
        assert(triangle.calcArea(0,1,1)==None)
    #test long decimal math.pi
    def testcase6_1(self):
        area = triangle.calcArea(math.pi,3,3)
        assert(area>4.01 and area< 4.02)

if __name__=="__main__":
    unittest.main()