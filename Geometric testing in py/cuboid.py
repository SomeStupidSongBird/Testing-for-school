#find volume and surface area
import math

def getInput():
    print("----------------------------------")
    length = int(input("Enter the length of the Cubeoidoid: "))
    width = int(input("Enter the width of the Cubeoid: "))
    height = int(input("Enter the height of the Cubeoid: "))
    if(length<0 or height<0 or width<0):
        print("All values must be positive")
    print("----------------------------------")
    return length,width,height

def calcVolume(length,width,height):
    if(length<0 or height<0 or width<0):
        return NULL
    volume = length*width*height
    if(volume<0):
        return NULL
    return volume

def calcSurfArea(length,width,height):
    if(length<0 or height<0 or width<0):
        return NULL
    surfaceArea = length*width*2 + length*height*2 + width*height*2
    if(surfaceArea<0):
        return NULL
    return surfaceArea

def printOutput(volume,surfaceArea):
    print('----------------------------------')
    print("The Cubeoidoid's volume: %.2f"%volume)
    print("The Cubeoidoid's volume: %.2f"%surfaceArea)
    print('----------------------------------')

def run(): #defining a run function for better readability and exportability
    r,w,h = getInput()
    if (l<0 or h<0 or w<0) : return
    volume = calcVolume(l,w,h)
    sA = calcSurfArea(l,w,h)
    printOutput(volume,sA)

if __name__=='__main__':
    run()