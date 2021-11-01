import main.cylinder as cylinder
import unittest
import math

class cylinderTest(unittest.TestCase):
    #test negative
    def testcase1_11(self):
        assert(cylinder.calcVolume(-1,1)==None)
    def testcase1_12(self):
        assert(cylinder.calcSurfArea(-1,1)==None)
    def testcase1_13(self):
        assert(cylinder.calcLatSurfArea(-1,1)==None)
    def testcase1_14(self):
        assert(cylinder.endSurfaceArea(-1)==None)
    def testcase1_21(self):
        assert(cylinder.calcVolume(1,-1)==None)
    def testcase1_22(self):
        assert(cylinder.calcSurfArea(1,-1)==None)
    def testcase1_23(self):
        assert(cylinder.calcLatSurfArea(1,-1)==None)
    def testcase1_24(self):
        assert(cylinder.calcEndSurfArea(1)==math.pi)
    #test 1
    def testcase2_1(self):
        vol = cylinder.calcVolume(1,1)
        assert(vol==math.pi)
    def testcase2_2(self):
        sa = cylinder.calcSurfArea(1,1)
        assert(sa>12.55 and sa<12.6)
    def testcase2_3(self):
        latsa = cylinder.calcLatSurfArea(1,1)
        assert(latsa>6.28 and latsa<6.29)
    def testcase2_4(self):
        endsa = cylinder.calcEndSurfArea(1)
        assert(endsa>3.14 and endsa<3.15)
    #test 0
    def testcase3_1(self):
        assert(cylinder.calcVolume(0,1)==0)
    def testcase3_2(self):
        sa = cylinder.calcSurfArea(1,0)
        assert(sa>6.2 or sa<6.3)
    def testcase3_3(self):
        assert(cylinder.calcLatSurfArea(1,0)==0)
    def testcase3_4(self):
        endsa = cylinder.calcEndSurfArea(1)
        assert(endsa>3.14 and endsa<3.15)
    #test long decimal math.pi
    def testcase6_1(self):
        vol = cylinder.calcVolume(math.pi,1)
        assert(vol>31 and vol<31.1)
    def testcase6_2(self):
        sa = cylinder.calcSurfArea(math.pi,1)
        assert(sa>81.75 and sa<81.76)
    def testcase6_3(self):
        latsa =cylinder.calcLatSurfArea(math.pi,1)
        assert(latsa>19.73 and latsa<19.74)
    def testcase6_4(self):
        endsa = cylinder.calcEndSurfArea(math.pi)
        assert(endsa>31 and endsa<31.1)


if __name__=="__main__":
    unittest.main()