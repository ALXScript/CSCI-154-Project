#separate script for performing the actual calculations from crater_math.py
import crater_math as cmath
import our_tools as tool
import references as rf

def simulateCustomCrater():
    #get the mass from the volume and density - in Kg
    diameter = tool.validFloat("\nPlease enter the Diameter of the Asteroid in Meters: ")

    #get the density of the Asteroid - in Kg/m^3
    densityImpactor = tool.getDensityImpactor("\nPlease select the Asteroid's density:\n(1) Ice\n(2) Porous\n(3) Dense\n(4) Iron\n")

    mass = cmath.getMass(densityImpactor, diameter)
                
    #get the velocity of the Asteroid - in Km/s
    velocity = tool.validFloat("\nPlease enter the Velocity of the asteroid in Kilometers/Second: ")
 
    #use the calculated mass and given velocity for KE - in Joules
    kinEnergy = cmath.solveKinEnergy(mass, velocity)

    #Crater CF Constant for craters > 4km (will keep 1.3 for now)
    craterCF = 1.3

    #get the gravAcc
    gravAcc = cmath.getGravAcc()

    #get the acceleration of the earth
    gravAccSurface = .006
        
    densitySurface = tool.getDensityTarget("\nPlease select the Earth's density:\n(1) Sedimentary\n(2) Igneous\n")

    #Calculate the diameter
    craterDiameter = cmath.solveDiameter(1.3, gravAcc, gravAccSurface, kinEnergy, densityImpactor, densitySurface)
    craterDepth = cmath.calcdeth(craterDiameter)

    return craterDiameter, craterDepth

def simulateMoonCrater():
    moonDiameter = 3.472e6
    moonDensity = rf.dicTargetDensity["igneous"]
    moonMass = 7.34767309e22
    moonVelocity = tool.validFloat("\nPlease enter the Velocity of the Moon in Kilometers/Second: ")
    moonKE = cmath.solveKinEnergy(moonMass, moonVelocity)
    craterCF = 1.3
    gravAcc = cmath.getGravAcc()
    gravAccSurface = .006
    densitySurface = tool.getDensityTarget("\nPlease select the Earth's density:\n(1) Sedimentary\n(2) Igneous\n")

    moonCraterDiameter = cmath.solveDiameter(1.3, gravAcc, gravAccSurface, moonKE, moonDensity, densitySurface)
    moonCraterDepth = cmath.calcdeth(moonCraterDiameter)

    return moonCraterDiameter, moonCraterDepth