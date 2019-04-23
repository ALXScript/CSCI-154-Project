#Main page for the application, including UI
import crater_math as cmath
import calculations
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
        #get the diameter - in Km
        diameter = tool.validFloat("\nPlease enter the Diameter of the Asteroid in Kilometers: ")

        #get the density of the Asteroid - in Kg/m^3
        densityImpactor = tool.getDensityImpactor("\nPlease select the Asteroid's density:\n(1) Ice\n(2) Porous\n(3) Dense\n(4) Iron\n")
        
        #get the mass from the volume and density - in Kg
        mass = cmath.getVolumeMet(diameter) * densityImpactor
        #print("mass is " , mass)
        
        #get the velocity of the Asteroid - in Km/s
        velocity = tool.validFloat("\nPlease enter the Velocity of the asteroid in Kilometers/Second: ")

        #get the distance from the surface of the earth to the asteroid - in Km
        #distance = tool.validFloat("Please enter the distance from the Earth in Kilometers: ")
 
        #use the calculated mass and given velocity for KE - in KiloTons of TNT
        kinEnergy = cmath.solveKinEnergy(mass, velocity)

        #Crater CF Constant for craters > 4km (will keep 1.3 for now)
        craterCF = 1.3

        #get the gravitational acceleration on the surface of the earth
        gravAcc = cmath.getGravAcc()
        
        #get the acceleration of the earth
        gravAccSurface = 0.006
        
        densitySurface = tool.getDensityTarget("\nPlease select the Earth's density:\n(1) Sedimentary\n(2) Igneous\n")

        #Calculate the diameter
        #craterDiameter = cmath.solveDiameter(1.3, gravAcc, gravAccSurface, kinEnergy, densityImpactor, densitySurface)
        craterDiameter = cmath.solveDiameter(1.3, 1, 1, kinEnergy, densityImpactor, densitySurface)

        #display the diameter
        print("\nThe diameter of the crater is %f meters wide!" % craterDiameter)

        rf.returnReferences(craterDiameter)

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