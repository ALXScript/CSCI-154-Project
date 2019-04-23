#separate script for performing the actual calculations from crater_math.py
import crater_math as cmath
import our_tools as tool

def simulateCustomCrater():
    #get the mass from the volume and density - in Kg
    mass = tool.validFloat("\nPlease enter the Mass of the Asteroid in Kilograms: ")

    #get the density of the Asteroid - in Kg/m^3
    densityImpactor = tool.getDensityImpactor("\nPlease select the Asteroid's density:\n(1) Ice\n(2) Porous\n(3) Dense\n(4) Iron\n")
                
    #get the velocity of the Asteroid - in Km/s
    velocity = tool.validFloat("\nPlease enter the Velocity of the asteroid in Kilometers/Second: ")
 
    #use the calculated mass and given velocity for KE - in Joules
    kinEnergy = cmath.solveKinEnergy(mass, velocity)

    #Crater CF Constant for craters > 4km (will keep 1.3 for now)
    craterCF = 1.3
        
    densitySurface = tool.getDensityTarget("\nPlease select the Earth's density:\n(1) Sedimentary\n(2) Igneous\n")

    #Calculate the diameter
    craterDiameter = cmath.solveDiameter(1.3, 1, 1, kinEnergy, densityImpactor, densitySurface)
    craterDepth = cmath.calcdeth(craterDiameter)

    return craterDiameter, craterDepth