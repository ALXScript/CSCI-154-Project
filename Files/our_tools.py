#script for any tools we create for ourselves
#i.e. functions, classes, etc.
import pandas as pandas


#input validation - double
def validDouble(passPropmt):
    while True:
        #prompt the user for entering a double
        try:
            doubleValue = double(input(passPropmt))
        #it isn't a double
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        
        if doubleValue < 0:
            print("Please enter a non-negative number")
            continue
        else:
            break
    
    return doubleValue

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
