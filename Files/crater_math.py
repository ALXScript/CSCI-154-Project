#Math formulas from Theory_Paper.pdf go here

def solveDiameter(craterCF, gravAcc, gravAccSurface, kinEnergy, densityImpactor, densitySurface):
	'''	based off of: https://web.archive.org/web/20170404094017/palaeo.gly.bris.ac.uk/communication/brana/equation.html
		
		craterCF = Crater Collapse Factor
		gravAcc = Gravitational Acceleration at surface of Earth
		gravAccSurface = Acceleration at the surface of body on which crater is formed
		kinEnergy = kinetic energy of impactor
		densityImpactor = denity of impactor in g/ cubic cm
		densitySurface = density of surface also g / cubic cm
	'''
	densImp = densityImpactor/1000.00
	densSurf = densitySurface/1000.00

	diameter = .07* craterCF * pow((gravAcc/gravAccSurface), .1667) * pow((kinEnergy * (densImp/densSurf)), .2941)
	return diameter

def solveKinEnergy(mass, velocity):
	''' based off of: http://keyah.asu.edu/lessons/MeteorCrater/KM13.html

		mass = mass of metoerite in g to convert to kg
		s = velocity of meteorite in meters/second (according to webpage avg speed of metoerites is 20k m/s)

		kinEnergy = kinetic energy in joules

	'''
	#massKG = mass/1000.00
	
	kinEnergy = (.5) * mass * pow(velocity, 2)
	return kinEnergy

def getVolumeMet(density, mass):
	''' based off of: http://keyah.asu.edu/lessons/MeteorCrater/KM13.html
		
		density = density of meteorite material in kg/m^3
		mass = mass in grams
		volume = volume of meteorite in m^3
	'''
	#massKG = mass/1000.00

	volume = mass/density
	return volume

#function for getting gravitational acceleration
def getGravAcc(mass, distance):
	#define the universal gravitational constant - m^3 / kg*s^2
	uniGravConst = 6.673e-11

	#define the mass of the earth - Kg
	earthMass = 5.972e24

	#define the radius of the earth - meters
	earthRadius = 6.356e6

	#return the gravitational acceleration on earth
	return ((uniGravConst * earthMass) / pow(earthRadius, 2))