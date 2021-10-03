import equillateral_triangle
import unittest
import math

class equillateral_triangleTest(unittest.TestCase):
    #test negative
    def testcase1_1(self):
        assert(equillateral_triangle.area(-1)==None)
    #test 1
    def testcase2_1(self):
        area = equillateral_triangle.area(1)
        assert(area>.43 and area<.44)
    #test 0
    def testcase3_1(self):
        assert(equillateral_triangle.area(0)==0)
    #test long decimal math.pi
    def testcase6_1(self):
        area = equillateral_triangle.area(math.pi)
        assert(area>4.27 and area< 4.28)

if __name__=="__main__":
    unittest.main()