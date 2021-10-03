import cylinder
import unittest
import math

class cylinderTest(unittest.TestCase):
    #test negative
    def testcase1_11(self):
        assert(cylinder.volume(-1,1)==None)
    def testcase1_12(self):
        assert(cylinder.surfaceArea(-1,1)==None)
    def testcase1_21(self):
        assert(cylinder.volume(1,-1)==None)
    def testcase1_22(self):
        assert(cylinder.surfaceArea(1,-1)==None)
    #test 1
    def testcase2_1(self):
        vol = cylinder.volume(1,1)
        assert(vol>12.55 and vol<12.6)
    def testcase2_2(self):
        sa = cylinder.surfaceArea(1,1)
        assert(sa==math.pi)
    #test 0
    def testcase3_1(self):
        assert(cylinder.volume(0,1)==0)
    def testcase3_2(self):
        assert(cylinder.surfaceArea(1,0)==0)
    #test long decimal math.pi
    def testcase6_1(self):
        vol = cylinder.volume(math.pi,1)
        assert(vol>31 and vol<31.1)
    def testcase6_2(self):
        sa = cylinder.surfaceArea(math.pi,1)
        assert(sa>81.75 and sa<81.76)


if __name__=="__main__":
    unittest.main()