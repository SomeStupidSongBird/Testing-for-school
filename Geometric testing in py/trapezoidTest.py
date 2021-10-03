import trapezoid
import unittest

class trapezoidTest(unittest.TestCase):
    #test negative
    def testcase1_1():
        assert(trapezoid.calcArea(-1,2,1)==NULL)
    def testcase1_2():
        assert(trapezoid.calcArea(1,-2,1)==NULL)
    def testcase1_3():
        assert(trapezoid.calcArea(1,2,-1)==NULL)
    #test 1
    def testcase2_1():
        assert(trapezoid.calcArea(1,2,1)==1.5)
    #test 0
    def testcase3_1():
        assert(trapezoid.calcArea(0,0,0)==0)
    def testcase3_2():
        assert(trapezoid.calcArea(0,1,1)==.5)
    #test very high number 2,555,555,000
    def testcase4_1():
        assert(trapezoid.calcArea(2555555000,2555555000,2555555000)==2555555000**2)
    #test long decimal math.pi
    def testcase6_1():
        area = trapezoid.calcArea(math.pi,1,1)
        assert(area<2.1 and area>2.07)
if __name__=="__main__":
    unittest.main()