import cylinder
import unittest
import math

class cylinderTest(unittest.TestCase):
    #test negative
    def testcase1_11():
        assert(cylinder.volume(-1,1)==NULL)
    def testcase1_12():
        assert(cylinder.surfaceArea(-1,1)==NULL)
    def testcase1_21():
        assert(cylinder.volume(1,-1)==NULL)
    def testcase1_22():
        assert(cylinder.surfaceArea(1,-1)==NULL)
    #test 1
    def testcase2_1():
        vol = cylinder.volume(1,1)
        assert(vol>12.55 and vol<12.6)
    def testcase2_2():
        sa = cylinder.surfaceArea(1,1)
        assert(sa==maht.pi)
    #test 0
    def testcase3_1():
        assert(cylinder.volume(0,1)==0)
    def testcase3_2():
        assert(cylinder.surfaceArea(1,0)==0)
    #test long decimal math.pi
    def testcase6_1():
        vol = cylinder.volume(math.pi,1)
        assert(vol>31 and vol<31.1)
    def testcase6_2():
        sa = cylinder.surfaceArea(math.pi,1)
        assert(sa>81.75 and sa<81.76)


if __name__=="__main__":
    unittest.main()