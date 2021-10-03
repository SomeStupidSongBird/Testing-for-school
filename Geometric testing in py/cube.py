#find volume and surface area
import math

def getInput():
    print("----------------------------------")
    side = int(input("Enter the length of a side of the Cube: "))
    if(side<0):
        print("All values must be positive")
    print("----------------------------------")
    return side

def calcVolume(side):
    if(side<0):
        return None
    volume = side**3
    return volume

def calcSurfArea(side):
    if(side<0):
        return None
    surfaceArea = side**2*6
    return surfaceArea

def printOutput(volume,surfaceArea):
    print('----------------------------------')
    print("The Cube's volume: %.2f"%volume)
    print("The Cube's surface area: %.2f"%surfaceArea)
    print('----------------------------------')

def run(): #defining a run function for better readability and exportability
    s = getInput()
    if (s<0) : return
    volume = calcVolume(s)
    sA = calcSurfArea(s)
    printOutput(volume,sA)

if __name__=='__main__':
    run()