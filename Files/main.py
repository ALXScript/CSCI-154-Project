#Main page for the application, including UI
import crater_math
import claculations
import our_tools

#boolean for verifying user data
exit = False

#UI while loop
while exit != True:
    #String variable for the main menu UI
    str_UI = "\nMenu: \nA: Temporary_1\nB: Temporary_2\nC: Temporary_3\nD: Temporary_4\nM: Display these menu options\nQ: Exit the program\n"

    user_input = input("What would you like to do: ")

    #begin making the choices
    if user_input == 'A' or user_input == 'a':
        #begin Temporary_1 process

    elif user_input == 'B' or user_input == 'b':
        #begin Temporary_2 process

    elif user_input == 'C' or user_input == 'c':
        #begin Temporary_3 process

    elif user_input == 'D' or user_input == 'd':
        #begin Temporary_4 process

    elif user_input == 'M' or user_input == 'm':
        #begin the display menu options process
        print(str_UI)

    elif user_input == 'Q' or user_input == 'q':
        #exit the program
        exit = True

    else:
        print("\nError: Invalid Entry\n")