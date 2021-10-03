import sphere
import unittest
import math

class sphereTest(unittest.TestCase):
    #test negative
    def testcase1_1():
        assert(sphere.volume(-1)==NULL)
    def testcase1_2():
        assert(sphere.surfaceArea(-1)==NULL)
    #test 1
    def testcase2_1():
        assert(sphere.volume(1)==math.pi)
    def testcase2_2():
        assert(sphere.surfaceArea(1)==math.pi)
    #test 0
    def testcase3_1():
        assert(sphere.volume(0)==0)
    def testcase3_2():
        assert(sphere.surfaceArea(0)==0)
    #test very high number 2,555,555,000
    def testcase4_1():
        assert(sphere.volume(2555555000)==)
    def testcase4_2():
        assert(sphere.surfaceArea(2555555000)==)
    #test long decimal math.pi
    def testcase5_1():
        vol = sphere.volume(math.pi)
        assert(vol>129.87 and vol<129.9)
    def testcase5_2():
        surfarea = sphere.surfaceArea(math,pi)
        assert(surfarea>124.02 and surfarea<124.03)


if __name__=="__main__":
    unittest.main()