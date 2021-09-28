import sphere

def main():

def getInput():
    print("---------------------------------------")
    choice = str(input("Enter your shape: "))
    
    print("---------------------------------------")
    while(True):
        if(choice.lower()=="h"or choice.lower()=="help"): #brings up the menu
            print("Options are: \nSphere,\nCylinder,\nCone,\nCube,\nCuboid,\nTriangle,\nTrapezoid,\nEquillateral Triangle,\nExit")
        else if(choice.lower()=="sphere"):
            shape.run()
        else if(choice.lower()=="cylinder"):
            cylinder.run()
        else if(choice.lower()=="cone"):
            cone.run()
        else if(choice.lower()=="cube"):
            cube.run()
        else if(choice.lower()=="cuboid"):
            cuboid.run()
        else if(choice.lower()=="triangle"):
            triangle.run()
        else if(choice.lower()=="equillateral triangle"):
            equillateral_triangle.run()
        else if(choice.lower()=="trapezid"):
            trapezid.run()
        else if(choice.lower()=="exit"):
            return(null)
        else:
            print("invalid option selected")

if __name__=='__main__':
    main()