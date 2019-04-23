import math 

#Math formulas from Theory_Paper.pdf go here
import math

def solveDiameter(craterCF, gravAcc, gravAccSurface, kinEnergy, densityImpactor, densitySurface):
	'''	based off of: https://web.archive.org/web/20170404094017/palaeo.gly.bris.ac.uk/communication/brana/equation.html

		craterCF = Crater Collapse Factor
		gravAcc = Gravitational Acceleration at surface of Earth
		gravAccSurface = Acceleration at the surface of body on which crater is formed
		kinEnergy = kinetic energy of impactor
		densityImpactor = denity of impactor in g/ cubic cm
		densitySurface = density of surface also g / cubic cm
	'''

	diameter = .7 * craterCF * pow((gravAcc/gravAccSurface), .1667) * pow((kinEnergy * (densityImpactor/densitySurface)), .2941)

	return diameter

def solveKinEnergy(mass, velocity):
	''' based off of: http://keyah.asu.edu/lessons/MeteorCrater/KM13.html

		mass = mass of metoerite in kg
		s = velocity of meteorite in km/s - convert to meters/second (according to webpage avg speed of metoerites is 20k m/s)

		kinEnergy = kinetic energy in joules - Kg * m^2 / s^2

		Convert Joules to KiloTons of TNT - j / 4.1842e12
	'''
	#convert velocity to M/s
	velocityMeters = velocity * 1000

	#get KEinitial and PEinitial
	kinEnergyInitial = (.5) * mass * pow(velocityMeters, 2)

	return kinEnergyInitial

#function for getting the diameter of the asteroid
def getDiameterAsteroid(density, mass):
	''' based off of: http://keyah.asu.edu/lessons/MeteorCrater/KM13.html

		density = density of meteorite material in kg/m^3
		mass = mass in grams

	'''
	top = 3 * mass
	bot = 4 * math.pi * density
	radius = math.sqrt(top/bot)

	return (radius * 2)
def calcdeth(diameter):
	if (diameter <= 1400):
		depth = diameter * math.tan(.1423) 
	else:
		depth = diameter * math.tan(.0747)
	return depth
