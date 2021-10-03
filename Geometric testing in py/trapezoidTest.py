import trapezoid
import unittest
import math

class trapezoidTest(unittest.TestCase):
    #test negative
    def testcase1_1(self):
        assert(trapezoid.calcArea(-1,2,1)==None)
    def testcase1_2(self):
        assert(trapezoid.calcArea(1,-2,1)==None)
    def testcase1_3(self):
        assert(trapezoid.calcArea(1,2,-1)==None)
    #test 1
    def testcase2_1(self):
        assert(trapezoid.calcArea(1,2,1)==1.5)
    #test 0
    def testcase3_1(self):
        assert(trapezoid.calcArea(0,0,0)==0)
    def testcase3_2(self):
        assert(trapezoid.calcArea(0,1,1)==.5)
    #test very high number 2,555,555,000
    def testcase4_1(self):
        assert(trapezoid.calcArea(2555555000,2555555000,2555555000)==2555555000**2)
    #test long decimal math.pi
    def testcase6_1(self):
        area = trapezoid.calcArea(math.pi,1,1)
        assert(area<2.1 and area>2.07)
if __name__=="__main__":
    unittest.main()