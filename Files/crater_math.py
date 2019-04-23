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

def getVolumeMet(diameter):
	''' based off of: http://keyah.asu.edu/lessons/MeteorCrater/KM13.html
		
		diameter = diameter of asteroid in km
		volume = volume of meteorite in m^3
	'''
	#convert diameter (km) to meters
	diameterMeters = diameter * 1000

	#volume = mass/density
	volume = float(4/3) * math.pi * pow((diameterMeters / 2), 2)
	return volume

#function for getting gravitational acceleration
def getGravAcc():
	#define the universal gravitational constant - m^3 / kg*s^2
	uniGravConst = 6.673e-11

	#define the mass of the earth - Kg
	earthMass = 5.972e24

	#define the radius of the earth - meters
	earthRadius = 6.356e6

	#return the gravitational acceleration on earth
	return ((uniGravConst * earthMass) / pow(earthRadius, 2))