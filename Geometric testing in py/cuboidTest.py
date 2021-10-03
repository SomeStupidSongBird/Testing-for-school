import cuboid 
import unittest
import math

class cuboidTest(unittest.TestCase):
    #test negative
    def testcase1_11(self):
        assert(cuboid.calcVolume(-1,1,1)==None)
    def testcase1_12(self):
        assert(cuboid.calcSurfArea(-1,1,1)==None)
    def testcase1_21(self):
        assert(cuboid.calcVolume(-1,-1,1)==None)
    def testcase1_22(self):
        assert(cuboid.calcSurfArea(-1,-1,1)==None)
    #test 1
    def testcase2_1(self):
        vol = cuboid.calcVolume(1,1,1)
        assert(vol==1)
    def testcase2_2(self):
        sa = cuboid.calcSurfArea(1,1,1)
        assert(sa==6)
    #test 0
    def testcase3_1(self):
        assert(cuboid.calcVolume(0,1,1)==0)
    def testcase3_2(self):
        assert(cuboid.calcSurfArea(0,1,1)==2)
    #test long decimal math.pi
    def testcase6_1(self):
        vol = cuboid.calcVolume(math.pi,1,1)
        assert(vol==math.pi)
    def tetscase6_2(self):
        sa = cuboid.calcSurfArea(math.pi,1,1)
        assert(sa>14.56 and sa<14.57)

if __name__=="__main__":
    unittest.main()