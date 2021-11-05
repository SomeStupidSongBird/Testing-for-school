import main.sphere as sphere
import unittest
import math

class sphereTest(unittest.TestCase):
    #test negative
    def testcase1_1(self):
        assert(sphere.calcVolume(-1)==None)
    def testcase1_2(self):
        assert(sphere.calcSurfArea(-1)==None)
    #test 1
    def testcase2_1(self):
        vol = sphere.calcVolume(1)
        assert(vol==4.19)
    def testcase2_2(self):
        sa = sphere.calcSurfArea(1)
        assert(sa==12.57)
    #test 0
    def testcase3_1(self):
        assert(sphere.calcVolume(0)==0)
    def testcase3_2(self):
        assert(sphere.calcSurfArea(0)==0)

if __name__=="__main__":
    unittest.main()