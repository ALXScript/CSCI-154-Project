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
    str_UI = "\nMenu: \nA: Simulate Your Own Crater\nB: Simulate the Moon hitting Earth\nC: Simulate the Asteroid that killed the dinosaurs\nM: Display these menu options\nQ: Exit the program\n"

    user_input = input("What would you like to do: ")

    #begin making the choices
    #simulate your own crater
    if user_input == 'A' or user_input == 'a':
        craterDiameter, craterDepth = calc.simulateCustomCrater()

        #display the diameter
        print("\nThe diameter of the crater is ", round(craterDiameter, 1) ," meters wide!")
        print("\nThe depth of the crater is ", round(craterDepth, 1) ," meters deep!\n")

        rf.returnReferences(craterDiameter, craterDepth)

    #Simulate the Moon
    elif user_input == 'B' or user_input == 'b':
        moonCraterDiameter, moonCraterDepth = calc.simulateMoonCrater()

        #display the diameter
        print("\nThe diameter of the crater is ", round(moonCraterDiameter,1) , " meters wide!")
        print("\nThe depth of the crater is ", round(moonCraterDepth,1) , " meters deep!\n")

        rf.returnReferences(moonCraterDiameter, moonCraterDepth)

    #Simulate Asteroid that killed the dinosaurs
    elif user_input == 'C' or user_input == 'c':
        dinoCraterDiameter, dinoCraterDepth = calc.simulateDinosaurAsteroid()

        #display the diameter
        print("\nThe diameter of the crater is ", round(dinoCraterDiameter, 1) , " meters wide!")
        print("\nThe depth of the crater is ", round(dinoCraterDepth, 1) , " meters deep!\n")

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