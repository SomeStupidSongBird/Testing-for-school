import main.cylinder as cylinder
import unittest
import math

class cylinderTest(unittest.TestCase):
    #test negative
    def testcase1_11(self):
        assert(cylinder.calcVolume(-1,1)==None)
    def testcase1_12(self):
        assert(cylinder.calcSurfArea(-1,1)==None)
    def testcase1_21(self):
        assert(cylinder.calcVolume(1,-1)==None)
    def testcase1_22(self):
        assert(cylinder.calcSurfArea(1,-1)==None)
    #test 1
    def testcase2_1(self):
        vol = cylinder.calcVolume(1,1)
        assert(vol==math.pi)
    def testcase2_2(self):
        sa = cylinder.calcSurfArea(1,1)
        assert(sa>12.55 and sa<12.6)
    #test 0
    def testcase3_1(self):
        assert(cylinder.calcVolume(0,1)==0)
    def testcase3_2(self):
        sa = cylinder.calcSurfArea(1,0)
        assert(sa>6.2 or sa<6.3)
    #test long decimal math.pi
    def testcase6_1(self):
        vol = cylinder.calcVolume(math.pi,1)
        assert(vol>31 and vol<31.1)
    def testcase6_2(self):
        sa = cylinder.calcSurfArea(math.pi,1)
        assert(sa>81.75 and sa<81.76)


if __name__=="__main__":
    unittest.main()