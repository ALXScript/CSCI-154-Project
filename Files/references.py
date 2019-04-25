#any references to real life structures go here
#define all references in METERS

#Dictionaries for the Densities - IN Kg/(m^3)
dicProjectileDensity = {
	"ice": 1000,
	"porous": 1500,
	"dense": 3000,
	"iron": 8000
}

dicTargetDensity = {
	"sedimentary": 2500,
	#"crystalline": ,
	"igneous": 2750
}

#field references
def soccerFieldWidth():
    return 120

def footballStadiumWidth():
    return 90

def basketballCourtWidth():
    return 28

#Local References
def csuFresnoSquareMeters():
    return 1.469e6

#American References
def statueOfLibertyHeight():
    return 93

def empireStateBuildingHeight():
    return 443

def spaceNeedleHeight():
    return 184

#European References
def romanColosseumWidth():
    return 156

def romanColosseumSquareMeters():
    return 24000

def eiffelTowerHeight():
    return 324

def bigBenHeight():
    return 93

#Other Foreign Country References
#Dubai Skyscraper
def burjKhalifaHeight():
    return 829

#chinese skyscraper
def shanghaiTowerHeight():
    return 632

def returnReferences(passDiameter, passDepth):
    #get the common width comparison
    #field references
    howManySoccer = passDiameter / soccerFieldWidth()
    howManyFootball = passDiameter / footballStadiumWidth()
    howManyBasketball = passDiameter / basketballCourtWidth()

    #building references - American
    howManyStatueOfLiberty = passDepth / statueOfLibertyHeight()
    howManyEmpireState = passDepth / empireStateBuildingHeight()
    howManySpaceNeedle = passDepth / spaceNeedleHeight()

    #building references - European
    howManyEiffelTowers = passDepth / eiffelTowerHeight()
    howManyBigBen = passDepth / bigBenHeight()

    #building references - Foreign countries
    howManyBurjKahlifa = passDepth / burjKhalifaHeight()
    howManyShanghai = passDepth / shanghaiTowerHeight()

    #field references display
    if(passDiameter > 12.7e6 or passDepth > 12.7e6):
        print("This object would destroy the Earth\n")
    elif (passDiameter > 6.371e6 or passDepth > 6.371e6):
        print("This object would destroy half of the Earth\n")
    else:
        if howManySoccer >= 1:
            print("That is %f Soccer fields wide!\n" % round(howManySoccer, 1))
        
        if howManyFootball >= 1:
            print("That is %f Football fields wide!\n" % round(howManyFootball, 1))
        
        if howManyBasketball >= 1:
            print("That is %f Basketball courts wide!\n" % round(howManyBasketball, 1))
        
        #building references display - American
        if howManyStatueOfLiberty >= 1:
            print("That is %f Statues of Liberty deep!\n" % howManyStatueOfLiberty)
    
        if howManyEmpireState >= 1:
            print("That is %f Empire State Buildings deep!\n" % howManyEmpireState)
    
        if howManySpaceNeedle >= 1:
            print("That is %f Space Needles deep!\n" % howManySpaceNeedle)

        if howManyEiffelTowers >= 1:
            print("That is %f Eiffel Towers deep!\n" % howManyEiffelTowers)
    
        if howManyBigBen >= 1:
            print("That is %f Big Bens deep!\n" % howManyBigBen)
    
        if howManyBurjKahlifa >= 1:
            print("That is %f Burj Khalifas deep!\n" % howManyBurjKahlifa)
    
        if howManyShanghai >= 1:
            print("That is %f Shanghai Towers deep!\n" % howManyShanghai)
    
        #print a new line
        print()