import cone
import unittest
import math

class coneTest(unittest.TestCase):
    #test negative
    def testcase1_11():
        assert(cone.calcVolume(-1,1)==NULL)
    def testcase1_12():
        assert(cone.calcSurfArea(-1,1)==NULL)
    def testcase1_21():
        assert(cone.calcVolume(1,-1)==NULL)
    def testcase1_22():
        assert(cone.calcSurfArea(1,-1)==NULL)
    #test 1
    def testcase2_1():
        vol = cone.calcVolume(1,1)
        assert(vol>7.58 and vol<7.593)
    def testcase2_2():
        sa = cone.calcSurfArea(1,1)
        assert(sa>1.04 and sa<1.05)
    #test 0
    def testcase3_1():
        assert(cone.calcVolume(0,1)==0)
    def testcase3_2():
        assert(cone.calcSurfArea(0,1)==0)
    #test long decimal math.pi
    def testcase6_1():
        vol = cone.calcVolume(math.pi,1)
        assert(vol>10.33 and vol< 10.34)
    def tetscase6_2():
        sa = cone.calcSurfArea(math.pi,1)
        assert(sa>44.96 and sa<44.97)

if __name__=="__main__":
    unittest.main()