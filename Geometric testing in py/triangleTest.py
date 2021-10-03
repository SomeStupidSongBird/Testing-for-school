import triangle
import unittest
import math

class triangleTest(unittest.TestCase):
    def testcase1_1():
        assert(triangle.area(-1,1,1)==NULL)
    #test 1
    def testcase2_1():
        area = triangle.area(1,1,1)
        assert(area>.43 and area<.44)
    #test non-equillateral
    def testcase3_1():
        area = triangle.area(1,3,3)
        assert(area>1.47 and area<1.48)
    #test 0
    def testcase3_1():
        assert(triangle.area(0,1,1)==NULL)
    #test long decimal math.pi
    def testcase6_1():
        area = triangle.area(math.pi,3,3)
        assert(area>4.01 and area< 4.02)

if __name__=="__main__":
    unittest.main()