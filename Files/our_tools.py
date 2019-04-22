#script for any tools we create for ourselves
#i.e. functions, classes, etc.
import pandas as pandas

df=read_csv("Datasets/meteorite-landings.csv")

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

#input validation - Density