import main.cone as cone
import unittest
import math

class coneTest(unittest.TestCase):
    #test negative
    def testcase1_11(self):
        assert(cone.calcVolume(-1,1)==None)
    def testcase1_12(self):
        assert(cone.calcSurfArea(-1,1)==None)
    def testcase1_21(self):
        assert(cone.calcVolume(1,-1)==None)
    def testcase1_22(self):
        assert(cone.calcSurfArea(1,-1)==None)
    #test 1
    def testcase2_1(self):
        vol = cone.calcVolume(1,1)
        assert(vol>1.04 and vol<1.05)
    def testcase2_2(self):
        sa = cone.calcSurfArea(1,1)
        assert(sa>7.58 and sa<7.593)
    #test 0
    def testcase3_1(self):
        assert(cone.calcVolume(0,1)==0)
    def testcase3_2(self):
        assert(cone.calcSurfArea(0,1)==0)
    #test long decimal math.pi
    def testcase6_1(self):
        vol = cone.calcVolume(math.pi,1)
        assert(vol>10.33 and vol< 10.34)
    def tetscase6_2(self):
        sa = cone.calcSurfArea(math.pi,1)
        assert(sa>44.96 and sa<44.97)

if __name__=="__main__":
    unittest.main()