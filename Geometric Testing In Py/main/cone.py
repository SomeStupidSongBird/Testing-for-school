#find volume and surface area
import math

def getInput():
    # function that takes input from the user
    print("----------------------------------")
    radius = int(input("Enter the radius of the Cone: "))
    height = int(input("Enter the height of the Cone: "))
    if(radius<0 or height<0):
        print("All values must be positive")
    print("----------------------------------")
    return radius, height

def calcVolume(radius,height):
    if(radius<0 or height<0): #check if it's positive again
        return None
    volume = math.pi*(radius**2)*height/3  #math
    return volume

def calcSurfArea(radius,height):
    if(radius<0 or height<0): #check if it's positive again
        return None
    surfaceArea = math.pi*(math.sqrt(radius**2+height**2)+radius)*radius  # math
    return surfaceArea

def printOutput(volume,surfaceArea): #just formatted printing
    print('----------------------------------')
    print("The Cone's volume: %.2f"%volume)
    print("The Cone's surface area: %.2f"%surfaceArea)
    print('----------------------------------')

def run(): #defining a run function for better readability and exportability
    # this is basically the main function
    r,h = getInput()
    if (r<0 or h<0) : return
    volume = calcVolume(r,h)
    sA = calcSurfArea(r,h)
    printOutput(volume,sA)

if __name__=='__main__':
    run()