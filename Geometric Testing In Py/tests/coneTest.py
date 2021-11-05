import main.cone as cone
import unittest
import math

class coneTest(unittest.TestCase):
    #test negative
    def testcase1_11(self):
        assert(cone.calcVolume(-1,1)==None)
    def testcase1_12(self):
        assert(cone.calcSurfArea(-1,1)==None)
    def testcase1_13(self):
        assert(cone.calcLatteralSurfArea(-1,1)==None)
    def testcase1_21(self):
        assert(cone.calcVolume(1,-1)==None)
    def testcase1_22(self):
        assert(cone.calcSurfArea(1,-1)==None)
    def testcase1_23(self):
        assert(cone.calcLatteralSurfArea(1,-1)==None)
    #test 1
    def testcase2_1(self):
        assert(cone.calcVolume(1,1)==1.05)
    def testcase2_2(self):
        assert(cone.calcSurfArea(1,1)==7.58)
    def testcase2_3(self):
        assert(cone.calcLatteralSurfArea(1,1)==4.44)
    #test 0
    def testcase3_1(self):
        assert(cone.calcVolume(0,1)==0)
    def testcase3_2(self):
        assert(cone.calcSurfArea(0,1)==0)
    def testcase3_3(self):
        assert(cone.calcLatteralSurfArea(0,1)==0)

if __name__=="__main__":
    unittest.main()