#find volume and surface area
import math

def getInput():
    print("----------------------------------")
    radius = int(input("Enter the radius of the Cone: "))
    height = int(input("Enter the height of the Cone: "))
    if(radius<0 or height<0):
        print("All values must be positive")
    print("----------------------------------")
    return radius, height

def calcVolume(radius,height):
    volume = math.pi*(radius**2)*h/3
    return volume

def calcSurfArea(radius,height):
    surfaceArea = math.pi*math.sqrt(radius**2+height**2)*radius + math.pi*radius**2
    return surfaceArea

def printOutput(volume,surfaceArea):
    print('__________________________________')
    print("The Cone's volume: %.2f"%volume)
    print("The Cone's surface area: %.2f"%surfaceArea)
    print('__________________________________')

def run(): #defining a run function for better readability and exportability
    r,h = getInput()
    if (r<0 or h<0) : return
    volume = calcVolume(r,h)
    sA = calcSurfArea(r,h)
    printOutput(volume,sA)

if __name__=='__main__':
    run()