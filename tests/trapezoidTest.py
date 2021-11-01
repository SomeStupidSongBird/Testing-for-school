import main.trapezoid as trapezoid
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
        
if __name__=="__main__":
    unittest.main()