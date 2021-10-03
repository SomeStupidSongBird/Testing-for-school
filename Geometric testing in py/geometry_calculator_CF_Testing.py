import geometry_calculator_CF
import unittest
import sys
from io import StringIO

class mainProgramTest(unittest.TestCase):
    def test_main1(self):
        tmpout = StringIO()
        sys.stdout = tmpout
        instr = "help\nexit\n"
        expectedoutstr = "---------------------------------------\nEnter your shape: ---------------------------------------\n"
        expectedoutstr+="Options are: \nSphere,\nCylinder,\nCone,\nCube,\nCuboid,\nTriangle,\nTrapezoid,\nEquillateral Triangle,\nExit\n"
        expectedoutstr+="---------------------------------------\nEnter your shape: ---------------------------------------\n"
        sys.stdin = StringIO(instr)
        geometry_calculator_CF.main()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        assert(expectedoutstr==tmpout.getvalue())

    def test_main2(self):
        tmpout = StringIO()
        sys.stdout = tmpout
        instr = "sphere\n1\nexit\n"
        expectedoutstr = "---------------------------------------\nEnter your shape: ---------------------------------------\n"
        expectedoutstr+="----------------------------------\nEnter the radius of the circle: ----------------------------------\n"
        expectedoutstr+="----------------------------------\nThe sphere's volume: 4.19\nThe sphere's surface area: 12.57\n----------------------------------\n"
        expectedoutstr+="---------------------------------------\nEnter your shape: ---------------------------------------\n"
        sys.stdin = StringIO(instr)
        geometry_calculator_CF.main()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        assert(expectedoutstr==tmpout.getvalue())

    #for each method, test each path
    #so pretty much just run main() then have send through strings to access each calculator and enter a test case that will pass and another that will fail
    #also test exit or failure (can be in the same line) 


if __name__=="__main__":
    unittest.main()