#Main page for the application, including UI
import crater_math as cmath
import calculations as calc
import our_tools as tool
import references as rf

#boolean for verifying user data
exit = False

#UI while loop
while exit != True:
    #String variable for the main menu UI
    str_UI = "\nMenu: \nA: Simulate Your Own Crater\nB: Simulate Crater From Dataset\nC: Simulate the Moon hitting Earth\nD: Simulate the Asteroid that killed the dinosaurs\nM: Display these menu options\nQ: Exit the program\n"

    user_input = input("What would you like to do: ")

    #begin making the choices
    #simulate your own crater
    if user_input == 'A' or user_input == 'a':
        craterDiameter, craterDepth = calc.simulateCustomCrater()

        #display the diameter
        print("\nThe diameter of the crater is %f meters wide!" % craterDiameter)
        print("\nThe depth of the crater is %f meters deep!\n" % craterDepth)

        rf.returnReferences(craterDiameter, craterDepth)

    #Get Crater Data from Dataset
    elif user_input == 'B' or user_input == 'b':
        #begin Temporary_2 process
        print("Case B")

    #Simulate the Moon
    elif user_input == 'C' or user_input == 'c':
        moonCraterDiameter, moonCraterDepth = calc.simulateMoonCrater()

        #display the diameter
        print("\nThe diameter of the crater is %f meters wide!" % moonCraterDiameter)
        print("\nThe depth of the crater is %f meters deep!\n" % moonCraterDepth)

        rf.returnReferences(moonCraterDiameter, moonCraterDepth)

    #Simulate Asteroid that killed the dinosaurs
    elif user_input == 'D' or user_input == 'd':
        dinoCraterDiameter, dinoCraterDepth = calc.simulateDinosaurAsteroid()

        #display the diameter
        print("\nThe diameter of the crater is %f meters wide!" % dinoCraterDiameter)
        print("\nThe depth of the crater is %f meters deep!\n" % dinoCraterDepth)

        rf.returnReferences(dinoCraterDiameter, dinoCraterDepth)

    #Print the menu
    elif user_input == 'M' or user_input == 'm':
        #begin the display menu options process
        print(str_UI)

    #quit the program
    elif user_input == 'Q' or user_input == 'q':
        #exit the program
        exit = True

    else:
        print("\nError: Invalid Entry\n")