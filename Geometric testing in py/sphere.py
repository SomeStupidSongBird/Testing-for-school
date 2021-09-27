#find volume and surface area
import math

def getInput():
    print("----------------------------------")
    radius = int(input("Enter the radius of the circle: "))
    if(radius<0):
        print("Radius must be positive")
    print("----------------------------------")
    return radius

def calcVolume(radius):
    volume = math.pi*(radius**3)*4/3
    return volume

def calcSurfArea(radius):
    surfaceArea = math.pi*4*(radius**2)
    return surfaceArea

def printOutput(volume,surfaceArea):
    print('__________________________________')
    print("The sphere's volume: %.2f"%volume) 
    print("The sphere's surface area: %.2f"%surfaceArea)
    print('__________________________________')

def run(): #defining a run function for better readability and exportability
    r = getInput()
    if (r<0) : return
    volume = calcVolume(r)
    sA = calcSurfArea(r)
    printOutput(volume,sA)

if __name__=='__main__':
    run()