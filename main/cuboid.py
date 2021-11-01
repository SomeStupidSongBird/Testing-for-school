#find volume and surface area
import math

def getInput(): #cl input
    print("----------------------------------")
    length = int(input("Enter the length of the Cubeoidoid: "))
    width = int(input("Enter the width of the Cubeoid: "))
    height = int(input("Enter the height of the Cubeoid: "))
    if(length<0 or height<0 or width<0):
        print("All values must be positive")
    print("----------------------------------")
    return length,width,height

def calcVolume(length,width,height):
    if(length<0 or height<0 or width<0): #positive check
        return None
    volume = length*width*height #ez math
    if(volume<0): #technically this should be an irrelevent but I'll leave it in just in case
        return None
    return round(volume,2)

def calcSurfArea(length,width,height):
    if(length<0 or height<0 or width<0): #vibe check
        return None
    surfaceArea = length*width*2 + length*height*2 + width*height*2 #math
    if(surfaceArea<0): # again, dont know if this is needed still but eh
        return None
    return round(surfaceArea,2)

def printOutput(volume,surfaceArea): #cl output bonanza
    print('----------------------------------')
    print("The Cubeoidoid's volume: %.2f"%volume)
    print("The Cubeoidoid's volume: %.2f"%surfaceArea)
    print('----------------------------------')

def run(): #defining a run function for better readability and exportability
    l,w,h = getInput()
    if (l<0 or h<0 or w<0) : return
    volume = calcVolume(l,w,h)
    sA = calcSurfArea(l,w,h)
    printOutput(volume,sA)

if __name__=='__main__':
    run()