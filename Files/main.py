#Main page for the application, including UI
import crater_math as cmath
import calculations
import our_tools as tool

#boolean for verifying user data
exit = False

#UI while loop
while exit != True:
    #String variable for the main menu UI
    str_UI = "\nMenu: \nA: Simulate Your Own Crater\nB: Simulate Crater From Dataset\nC: Temporary_3\nD: Temporary_4\nM: Display these menu options\nQ: Exit the program\n"

    user_input = input("What would you like to do: ")

    #begin making the choices
    if user_input == 'A' or user_input == 'a':
        #Simulate Your Own Crater
        #define local variables
        mass = tool.validFloat("Please enter the Mass of the asteroid in Kilograms:")
        velocity = tool.validFloat("Please enter the Velocity of the asteroid in Meters/Second:")
        kinEnergy = cmath.solveKinEnergy(mass, velocity)
        craterCF = 1.3
        distance = tool.validFloat("Please enter the distance from the Earth in Meters")
        gravAcc = cmath.getGravAcc(mass, distance)
        gravAccSurface
        densityImpactor
        densitySurface

        print("Case A")

    elif user_input == 'B' or user_input == 'b':
        #begin Temporary_2 process
        print("Case B")

    elif user_input == 'C' or user_input == 'c':
        #begin Temporary_3 process
        print("Case C")

    elif user_input == 'D' or user_input == 'd':
        #begin Temporary_4 process
        print("Case D")

    elif user_input == 'M' or user_input == 'm':
        #begin the display menu options process
        print(str_UI)

    elif user_input == 'Q' or user_input == 'q':
        #exit the program
        exit = True

    else:
        print("\nError: Invalid Entry\n")