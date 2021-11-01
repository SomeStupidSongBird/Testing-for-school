import main.cuboid as cuboid 
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

if __name__=="__main__":
    unittest.main()