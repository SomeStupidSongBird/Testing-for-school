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
        assert(cylinder.calcEndSurfArea(-1)==None)
    def testcase1_21(self):
        assert(cylinder.calcVolume(1,-1)==None)
    def testcase1_22(self):
        assert(cylinder.calcSurfArea(1,-1)==None)
    def testcase1_23(self):
        assert(cylinder.calcLatSurfArea(1,-1)==None)
    def testcase1_24(self):
        assert(cylinder.calcEndSurfArea(1)==3.14)
    #test 1
    def testcase2_1(self):
        vol = cylinder.calcVolume(1,1)
        assert(vol==3.14)
    def testcase2_2(self):
        sa = cylinder.calcSurfArea(1,1)
        assert(sa==12.57)
    def testcase2_3(self):
        latsa = cylinder.calcLatSurfArea(1,1)
        assert(latsa==6.28)
    def testcase2_4(self):
        endsa = cylinder.calcEndSurfArea(1)
        assert(endsa==3.14)
    #test 0
    def testcase3_1(self):
        assert(cylinder.calcVolume(0,1)==0)
    def testcase3_2(self):
        sa = cylinder.calcSurfArea(1,0)
        assert(sa==6.28)
    def testcase3_3(self):
        assert(cylinder.calcLatSurfArea(1,0)==0)
    def testcase3_4(self):
        endsa = cylinder.calcEndSurfArea(1)
        assert(endsa==3.14)


if __name__=="__main__":
    unittest.main()