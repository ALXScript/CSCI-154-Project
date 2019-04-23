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
    str_UI = "\nMenu: \nA: Simulate Your Own Crater\nB: Simulate Crater From Dataset\nC: Temporary_3\nD: Temporary_4\nM: Display these menu options\nQ: Exit the program\n"

    user_input = input("What would you like to do: ")

    #begin making the choices
    #simulate your own crater
    if user_input == 'A' or user_input == 'a':
        craterDiameter = calc.simulateCustomCrater()

        #display the diameter
        print("\nThe diameter of the crater is %f meters wide!" % craterDiameter)

        rf.returnReferences(craterDiameter)

    #Get Crater Data from Dataset
    elif user_input == 'B' or user_input == 'b':
        #begin Temporary_2 process
        print("Case B")

    #still unknown
    elif user_input == 'C' or user_input == 'c':
        #begin Temporary_3 process
        print("Case C")

    #still unknown
    elif user_input == 'D' or user_input == 'd':
        #begin Temporary_4 process
        print("Case D")

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