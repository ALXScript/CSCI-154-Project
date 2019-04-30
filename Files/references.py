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

def californiaLength():
    return 1240000

def unitedStatesLength():
    return 4091000

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
    howManySoccer = round((passDiameter / soccerFieldWidth()), 1)
    howManyFootball = round((passDiameter / footballStadiumWidth()), 1)
    howManyBasketball = round((passDiameter / basketballCourtWidth()), 1)

    #building references - American
    howManyStatueOfLiberty = round((passDepth / statueOfLibertyHeight()), 1)
    howManyEmpireState = round((passDepth / empireStateBuildingHeight()), 1)
    howManySpaceNeedle = round((passDepth / spaceNeedleHeight()), 1)
    howManyCalifornia = round((passDepth / californiaLength()), 1)

    #building references - European
    howManyEiffelTowers = round((passDepth / eiffelTowerHeight()), 1)
    howManyBigBen = round((passDepth / bigBenHeight()), 1)

    #building references - Foreign countries
    howManyBurjKahlifa = round((passDepth / burjKhalifaHeight()), 1)
    howManyShanghai = round((passDepth / shanghaiTowerHeight()), 1)

    #field references display
    if(passDiameter > 12.7e6 or passDepth > 12.7e6):
        print("This object would destroy the Earth\n")
    elif (passDiameter > 6.371e6 or passDepth > 6.371e6):
        print("This object would destroy half of the Earth\n")
    elif (passDiameter > unitedStatesLength()):
        print("This object would destroy the entire United States\n")
    elif (passDiameter > californiaLength()):
        print("That is ", howManyCalifornia, " California's wide!\n")
    else:
        if howManySoccer >= 1:
            print("That is ", howManySoccer , " Soccer fields wide!\n")
        
        if howManyFootball >= 1:
            print("That is ", howManyFootball , " Football fields wide!\n")
        
        if howManyBasketball >= 1:
            print("That is ", howManyBasketball , " Basketball courts wide!\n")
        
        #building references display - American
        if howManyStatueOfLiberty >= 1:
            print("That is ", howManyStatueOfLiberty , " Statues of Liberty deep!\n")
    
        if howManyEmpireState >= 1:
            print("That is ", howManyEmpireState , " Empire State Buildings deep!\n")
    
        if howManySpaceNeedle >= 1:
            print("That is ", howManySpaceNeedle , " Space Needles deep!\n")

        if howManyEiffelTowers >= 1:
            print("That is ", howManyEiffelTowers , " Eiffel Towers deep!\n")
    
        if howManyBigBen >= 1:
            print("That is ", howManyBigBen , " Big Bens deep!\n")
    
        if howManyBurjKahlifa >= 1:
            print("That is ", howManyBurjKahlifa , " Burj Khalifas deep!\n")
    
        if howManyShanghai >= 1:
            print("That is ", howManyShanghai , " Shanghai Towers deep!\n")
    
        #print a new line
        print()