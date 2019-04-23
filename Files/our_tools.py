#script for any tools we create for ourselves
#i.e. functions, classes, etc.
import pandas as pandas
import references as rf

df=pandas.read_csv("Datasets/meteorite-landings.csv")

#input validation - double
def validFloat(passPropmt):
    while True:
        #prompt the user for entering a double
        try:
            floatValue = float(input(passPropmt))
        #it isn't a double
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        
        if floatValue < 0:
            print("Please enter a non-negative number")
            continue
        else:
            break
    
    return floatValue

#input validation - Integer
def validInt(passPropmt):
    while True:
        #prompt the user for entering a double
        try:
            intValue = int(input(passPropmt))
        #it isn't a double
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        
        if intValue < 0:
            print("Please enter a non-negative number")
            continue
        else:
            break
    
    return intValue

#input validation - Density impactor
def getDensityImpactor(prompt):
    while True:
        intChoice = validInt(passPropmt)
        
        if intChoice == 1:
            return rf.dicProjectileDensity["ice"]
        elif intChoice == 2:
            return rf.dicProjectileDensity["porous"]
        elif intChoice == 3:
            return rf.dicProjectileDensity["dense"]
        elif intChoice == 4:
            return rf.dicProjectileDensity["iron"]
        else:
            print("Invalid choice, please try again")

#input validation - Density Target
def getDensityTarget(prompt):
    while True:
        intChoice = validInt(passPropmt)
        
        if intChoice == 1:
            return rf.dicProjectileDensity["sedimentary"]
        elif intChoice == 2:
            return rf.dicProjectileDensity["igneous"]
        else:
            print("Invalid choice, please try again")