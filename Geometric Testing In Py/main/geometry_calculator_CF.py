from main import sphere,cylinder,cone,cube,cuboid,triangle,trapezoid,equillateral_triangle

def main():  #very practical and useful main function yes?  yes.. very necessary indeed
    getInput()
    return


def getInput():
    while(True): #normal command line loop
        print("---------------------------------------")
        choice = str(input("Enter your shape or enter h for help: "))
        print("---------------------------------------")
        if(choice.lower()=="h"or choice.lower()=="help"): #brings up the menu
            print("Options are: \nSphere,\nCylinder,\nCone,\nCube,\nCuboid,\nTriangle,\nTrapezoid,\nEquillateral Triangle,\nExit")
        elif(choice.lower()=="sphere"):
            sphere.run()
        elif(choice.lower()=="cylinder"):
            cylinder.run()
        elif(choice.lower()=="cone"):
            cone.run()
        elif(choice.lower()=="cube"):
            cube.run()
        elif(choice.lower()=="cuboid"):
            cuboid.run()
        elif(choice.lower()=="triangle"):
            triangle.run()
        elif(choice.lower()=="equillateral triangle"):
            equillateral_triangle.run()
        elif(choice.lower()=="trapezoid"):
            trapezoid.run()
        elif(choice.lower()=="exit"):
            return
        else:
            print("invalid option selected")

if __name__=='__main__':
    main()