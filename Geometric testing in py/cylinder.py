#find volume and surface area
import math
 
def getInput():
    print("----------------------------------")
    radius = int(input("Enter the radius of the Cylindar: "))
    height = int(input("Enter the height of the Cylindar: "))
    if(radius<0 or height<0):
        print("All values must be positive")
    print("----------------------------------")
    return radius, height

def calcVolume(radius,height):
    if(radius<0 or height<0):
        return None
    volume = math.pi*(radius**2)*height
    return volume

def calcSurfArea(radius,height):
    if(radius<0 or height<0):
        return None
    surfaceArea = math.pi*2*radius*(radius+height)
    return surfaceArea

def printOutput(volume,surfaceArea):
    print('----------------------------------')
    print("The Cylindar's volume: %.2f"%volume)
    print("The Cylindar's surface area: %.2f"%surfaceArea)
    print('----------------------------------')

def run(): #defining a run function for better readability and exportability
    r,h = getInput()
    if (r<0 or h<0) : return
    volume = calcVolume(r,h)
    sA = calcSurfArea(r,h)
    printOutput(volume,sA)

if __name__=='__main__':
    run()