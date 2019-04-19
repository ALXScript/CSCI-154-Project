#Math formulas from Theory_Paper.pdf go here


def solveDiameter(craterCF, gravAcc, gravAccSurface, kinEnergy, densityImpactor, densitySurface):
	'''	based off of: https://web.archive.org/web/20170404094017/palaeo.gly.bris.ac.uk/communication/brana/equation.html
		
		craterCF = Crater Collapse Factor
		gravAcc = Gravitational Acceleration at surface of Earth
		gravAccSurface = Acceleration at the surface of body on which crater is formed
		kinEnergy = kinetic energy of impactor
		densityImpactor = denity of impactor in g/ cubic cm
		densitySurface = density of surface
	'''
		diameter = .07* craterCF * pow((gravAcc/gravAccSurface), 0.1667) * pow((kinEnergy * (densityImpactor/densitySurface)), .2941)
		return diameter

