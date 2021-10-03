import sphere
import unittest
import math

class sphereTest(unittest.TestCase):
    #test negative
    def testcase1_1(self):
        assert(sphere.volume(-1)==None)
    def testcase1_2(self):
        assert(sphere.surfaceArea(-1)==None)
    #test 1
    def testcase2_1(self):
        vol = sphere.volume(1)
        assert(vol>4.18 and vol<4.19)
    def testcase2_2(self):
        sa = sphere.surfaceArea(1)
        assert(sa>12.56 and sa<12.57)
    #test 0
    def testcase3_1(self):
        assert(sphere.volume(0)==0)
    def testcase3_2(self):
        assert(sphere.surfaceArea(0)==0)
    #test long decimal math.pi
    def testcase5_1(self):
        vol = sphere.volume(math.pi)
        assert(vol>129.87 and vol<129.9)
    def testcase5_2(self):
        surfarea = sphere.surfaceArea(math.pi)
        assert(surfarea>124.02 and surfarea<124.03)


if __name__=="__main__":
    unittest.main()