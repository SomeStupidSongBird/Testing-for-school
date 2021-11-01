#find volume and surface area
import math

def getInput(): #user input from command line
    print("----------------------------------")
    radius = int(input("Enter the radius of the sphere: "))
    if(radius<0): #check if positive
        print("Radius must be positive")
    print("----------------------------------")
    return radius

def calcVolume(radius):
    if(radius<0): #check for positive again
        return None
    volume = math.pi*(radius**3)*4/3 # ez math
    return round(volume,2)

def calcSurfArea(radius):
    if(radius<0): #check if positive again
        return None
    surfaceArea = math.pi*4*(radius**2) # ez math 2
    return round(surfaceArea,2)

def printOutput(volume,surfaceArea): #output to command line
    print('----------------------------------')
    print("The sphere's volume: %.2f"%volume) 
    print("The sphere's surface area: %.2f"%surfaceArea)
    print('----------------------------------')

def run(): #defining a run function for better readability and exportability
    # main
    r = getInput()
    if (r<0) : return
    volume = calcVolume(r)
    sA = calcSurfArea(r)
    printOutput(volume,sA)

if __name__=='__main__':
    run()