import main.cube as cube 
import unittest
import math

class cubeTest(unittest.TestCase):
    #test negative
    def testcase1_11(self):
        assert(cube.calcVolume(-1)==None)
    def testcase1_12(self):
        assert(cube.calcSurfArea(-1)==None)
    def testcase2_1(self):
        vol = cube.calcVolume(1)
        assert(vol==1)
    def testcase2_2(self):
        sa = cube.calcSurfArea(1)
        assert(sa==6)
    #test 0
    def testcase3_1(self):
        assert(cube.calcVolume(0)==0)
    def testcase3_2(self):
        assert(cube.calcSurfArea(0)==0)
    #test long decimal math.pi
    def testcase6_1(self):
        vol = cube.calcVolume(math.pi)
        assert(vol > 31 and vol < 31.01)
    def tetscase6_2(self):
        sa = cube.calcSurfArea(math.pi)
        assert(sa>59.21 and sa<59.22)

if __name__=="__main__":
    unittest.main()