import MRFbyState
import matplotlib.pyplot as plt
import AnyInfraByState
import MostCommonFacilities
import AllInfravsPopDensity
import ResidentPopvsInfra
import DensityvsMRF
import ResidentPopvsMRF
import GetRecyclingPercentagebyState
import GetEmissionsbyYear
import numpy as np
import GetTotalEmissions
import TextilesVsArtReg
import RegvsRecyclingRate
import GetRatesbyStatePETBottles
import GetRatesbyStateTextiles
import GetRatesbyStateAluminum
import GetRatesbyStateGlass
import GetRatesbyStatePaper
import LandfillTippingFees
import BottleBills
import GetRatesbyStateWood
import GetRatesbyStateElectronics

def plotInfraByState():
    data = AnyInfraByState.csvtodict('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    dataSortedbyKey = {k: v for k, v in sorted(data.items(), key=lambda x: x[0])}

    print("State counts:", dataSortedbyKey)
    dataSortedbyValue = {k: v for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True)}

    x = dataSortedbyValue.keys()  # Get the states from the dictionary
    y = dataSortedbyValue.values()  # Get the counts for each state

    f = plt.figure()
    f.set_figwidth(15)

    plt.title('Number of Recyling Centers by State')
    plt.xlabel('State')
    plt.ylabel('# of Sites') 
    plt.bar(x, y)
    plt.savefig('InfrastructureData/Graphs/InfrastructureDatabystate.png')
    plt.show()

    # print("State counts:", dataSortedbyValue)
    # nodups = list(set(x))  # Remove duplicates from the state list
    # print(len(nodups))

def plotMRFbyState():
    data = MRFbyState.csvtodict('InfrastructureData/CSVData/MRFdata.csv')
    dataSortedbyValue = {k: v for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True)}

    x = dataSortedbyValue.keys()  # Get the states from the dictionary
    y = dataSortedbyValue.values()  # Get the counts for each state

    f = plt.figure()
    f.set_figwidth(15)

    plt.bar(x, y)
    plt.title('Number of MRFs by State')
    plt.xlabel('State')
    plt.ylabel('# of Sites')
    plt.savefig('InfrastructureData/Graphs/MRFdatabystate.png')
    plt.show()

    # print("State counts:", dataSortedbyValue)
    # nodups = list(set(x))  # Remove duplicates from the state list
    # print(len(nodups))

def plotMostCommonFacilities():
    facilities = MostCommonFacilities.mostCommonFacilities('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')

    x = facilities.keys() # Get the facilities from the dictionary
    y = facilities.values() # Get the counts for each facility
    f = plt.figure()
    f.set_figwidth(10)

    plt.barh(x, y)
    plt.title('Most Common Facilities')
    plt.ylabel('Facility Type')
    plt.xlabel('# of Sites')
    plt.subplots_adjust(left=.25, bottom=None, right=.883, top=None, wspace=None, hspace=None)
    plt.savefig('InfrastructureData/Graphs/MostCommonFacilities.png')
    plt.show()

def plotDensityvsInfra():
    densityList, infraList = AllInfravsPopDensity.getArrays()
    z = np.polyfit(densityList, infraList, 1)
    p = np.poly1d(z)
    plt.scatter(densityList, infraList)
    plt.plot(densityList, p(densityList), "r--")
    plt.title('Population Density vs. Number of Recycling Centers')
    plt.xlabel('Population Density (people per square mile)')
    plt.ylabel('Number of Recycling Centers')
    plt.savefig('InfrastructureData/Graphs/PopulationDensityvsInfra.png')
    plt.show()

def plotPopvsInfra():
    popList, infraList = ResidentPopvsInfra.getArrays()
    z = np.polyfit(popList, infraList, 1)
    p = np.poly1d(z)
    plt.scatter(popList, infraList)
    plt.plot(popList, p(popList), "r--")
    plt.title('Resident Population vs. Number of Recycling Centers')
    plt.xlabel('Resident Population')
    plt.ylabel('Number of Recycling Centers')
    plt.savefig('InfrastructureData/Graphs/ResidentPopvsInfra.png')
    plt.show()

def plotDensityvsMRF():
    densityList, MRFList = DensityvsMRF.getArrays()
    z = np.polyfit(densityList, MRFList, 1)
    p = np.poly1d(z)
    plt.scatter(densityList, MRFList)
    plt.plot(densityList, p(densityList), "r--")
    plt.title('Population Density vs. Number of MRFs')
    plt.xlabel('Population Density (people per square mile)')
    plt.ylabel('Number of MRFs')
    plt.savefig('InfrastructureData/Graphs/PopulationDensityvsMRF.png')
    plt.show()

def plotPopvsMRF():
    popList, MRFList = ResidentPopvsMRF.getArrays()
    z = np.polyfit(popList, MRFList, 1)
    p = np.poly1d(z)
    plt.scatter(popList, MRFList)
    plt.plot(popList, p(popList), "r--")
    plt.title('Resident Population vs. Number of MRFs')
    plt.xlabel('Resident Population')
    plt.ylabel('Number of MRFs')
    plt.savefig('InfrastructureData/Graphs/ResidentPopvsMRF.png')
    plt.show()

def plotStateRecyclingPercentage():
    recyclingData = GetRecyclingPercentagebyState.get_recycling_percentage_by_state('InfrastructureData/CSVData/RecyclingPercentageByState.csv')
    recyclingDataSortedbyValue = {k: v for k, v in sorted(recyclingData.items(), key=lambda x: x[1], reverse=True)}

    x = recyclingDataSortedbyValue.keys()  # Get the states from the dictionary
    y = recyclingDataSortedbyValue.values()  # Get the recycling percentages for each state

    f = plt.figure()
    f.set_figwidth(15)
    f.set_figheight(8)

    plt.bar(x, y)
    plt.title('Recycling Percentage by State')
    plt.xlabel('State')
    plt.ylabel('Recycling Percentage (%)')
    plt.gca().set_ybound(upper=100)
    plt.savefig('InfrastructureData/Graphs/RecyclingPercentageByState.png')
    plt.show()

def plotEmissionsByState():
    emissionsData = GetEmissionsbyYear.get_emissions_by_year('InfrastructureData/CSVData/LongTermEmissionsData.csv', '2020')
    emissionsDataSortedbyValue = {k: v for k, v in sorted(emissionsData.items(), key=lambda x: x[1], reverse=True)}

    print("Emissions Data Sorted by Value:", emissionsDataSortedbyValue)
    x = emissionsDataSortedbyValue.keys()  # Get the states from the dictionary
    y = emissionsDataSortedbyValue.values()  # Get the emissions for each state

    f = plt.figure()
    f.set_figwidth(15)
    f.set_figheight(8)

    plt.bar(x, y)
    plt.title('Emissions by State in 2020')
    plt.xlabel('State')
    plt.ylabel('Emissions (million metric tons)')
    plt.savefig('InfrastructureData/Graphs/EmissionsByState2020.png')
    plt.show()

def plotEmissionsvsinfra():
    popList, infraList = ResidentPopvsInfra.getArrays()
    emissionsData = GetEmissionsbyYear.get_emissions_by_year('InfrastructureData/CSVData/LongTermEmissionsData.csv', '2020')
    emissionsDataSortedbyKey = {k: v for k, v in sorted(emissionsData.items(), key=lambda x: x[0])}
    emissionsList = list(emissionsDataSortedbyKey.values())

    # print("Emissions Data Sorted by Key:", emissionsDataSortedbyKey)
    # print("\nInfra List:", infraList)

    z = np.polyfit(infraList, emissionsList, 1)
    p = np.poly1d(z)

    plt.scatter(infraList, emissionsList)
    plt.plot(infraList, p(infraList), "r--")
    plt.title('2020 Emissions vs. Number of Recycling Centers')
    plt.xlabel('Number of Recycling Centers')
    plt.ylabel('Emissions (million metric tons)')
    plt.savefig('InfrastructureData/Graphs/EmissionsvsInfra.png')
    plt.show()

def plotEmissionsvsMRF():
    popList, MRFList = ResidentPopvsMRF.getArrays()
    emissionsData = GetEmissionsbyYear.get_emissions_by_year('InfrastructureData/CSVData/LongTermEmissionsData.csv', '2020')
    emissionsDataSortedbyKey = {k: v for k, v in sorted(emissionsData.items(), key=lambda x: x[0])}
    emissionsList = list(emissionsDataSortedbyKey.values())

    # print("Emissions Data Sorted by Key:", emissionsDataSortedbyKey)
    # print("\nMRF List:", MRFList)
    z = np.polyfit(MRFList, emissionsList, 1)
    p = np.poly1d(z)

    plt.scatter(MRFList, emissionsList)
    plt.plot(MRFList, p(MRFList), "r--")
    plt.title('2020 Emissions vs. Number of MRFs')
    plt.xlabel('Number of MRFs')
    plt.ylabel('Emissions (million metric tons)')
    plt.savefig('InfrastructureData/Graphs/EmissionsvsMRF.png')
    plt.show()

def plotYearlyEmissions():
    data = GetTotalEmissions.getTotalYearlyEmissions('InfrastructureData/CSVData/LongTermEmissionsData.csv')
    
    x = data.keys()  # Get the years from the dictionary
    y = data.values()  # Get the emissions for each year

    f = plt.figure()
    f.set_figwidth(30)
    f.set_figheight(8)
    f.subplots_adjust(left=.05, bottom=None, right=.95, top=None, wspace=None, hspace=None)
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title('Total Yearly Emissions')
    plt.xlabel('Year')
    plt.ylabel('Emissions (million metric tons)')
    plt.savefig('InfrastructureData/Graphs/TotalYearlyEmissions.png')
    plt.show()

def plotRecyclingPercentagevsInfra():
    recyclingData = GetRecyclingPercentagebyState.get_recycling_percentage_by_state('InfrastructureData/CSVData/RecyclingPercentageByState.csv')
    infraData = AnyInfraByState.csvtodict('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')

    recyclingDataNoOutliers = {}
    infraDataNoOutliers = {}
    for key in infraData:
        if infraData[key] < 100:
            infraDataNoOutliers[key] = infraData[key]
            recyclingDataNoOutliers[key] = recyclingData[key]

    recyclingDataSortedbyKey = {k: v for k, v in sorted(recyclingDataNoOutliers.items(), key=lambda x: x[0])}
    recyclingList = list(recyclingDataSortedbyKey.values())

    infraDataSortedbyKey = {k: v for k, v in sorted(infraDataNoOutliers.items(), key=lambda x: x[0])}
    infraList = list(infraDataSortedbyKey.values())

    z = np.polyfit(infraList, recyclingList, 1)
    p = np.poly1d(z)

    # print("Recycling Data Sorted by Key:", recyclingDataSortedbyKey)
    # print("\n\nInfra Data Sorted by Key:", infraDataSortedbyKey)

    plt.scatter(infraList, recyclingList)
    plt.plot(infraList, p(infraList), "r--")
    plt.title('Recycling Percentage vs. Number of Recycling Centers')
    plt.xlabel('Number of Recycling Centers')
    plt.ylabel('Recycling Percentage (%)')
    plt.savefig('InfrastructureData/Graphs/RecyclingPercentagevsInfra.png')
    plt.show()

def plotRecyclingPercentagevsMRF():
    recyclingData = GetRecyclingPercentagebyState.get_recycling_percentage_by_state('InfrastructureData/CSVData/RecyclingPercentageByState.csv')
    MRFData = MRFbyState.csvtodict('InfrastructureData/CSVData/MRFdata.csv')

    recyclingDataNoOutliers = {}
    MRFDataNoOutliers = {}

    for key in MRFData:
        if MRFData[key] < 30:
            MRFDataNoOutliers[key] = MRFData[key]
            recyclingDataNoOutliers[key] = recyclingData[key]

    MRFDataSortedbyKey = {k: v for k, v in sorted(MRFDataNoOutliers.items(), key=lambda x: x[0])}
    MRFList = list(MRFDataSortedbyKey.values())

    recyclingDataSortedbyKey = {k: v for k, v in sorted(recyclingDataNoOutliers.items(), key=lambda x: x[0])}
    recyclingList = list(recyclingDataSortedbyKey.values())

    z = np.polyfit(MRFList, recyclingList, 1)
    p = np.poly1d(z)

    print("Recycling Data Sorted by Key:", recyclingDataSortedbyKey)
    print("\n\nMRF Data Sorted by Key:", MRFDataSortedbyKey)

    plt.scatter(MRFList, recyclingList)
    plt.plot(MRFList, p(MRFList), "r--")
    plt.title('Recycling Percentage vs. Number of MRFs')
    plt.xlabel('Number of MRFs')
    plt.ylabel('Recycling Percentage (%)')
    plt.savefig('InfrastructureData/Graphs/RecyclingPercentagevsMRF.png')
    plt.show()

def plotTextilesByState():
    data = TextilesVsArtReg.csvtodict('InfrastructureData/CSVData/TextileData.csv')
    dataSortedbyValue = {k: v for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True)}
    x = dataSortedbyValue.keys()  # Get the states from the dictionary
    y = dataSortedbyValue.values()  # Get the counts for each state
    f = plt.figure()
    f.set_figwidth(15)
    plt.yticks(np.arange(0,20,2))
    plt.bar(x, y)
    plt.title('Number of Textile Recycling Centers by State')
    plt.xlabel('State')
    plt.ylabel('# of Textile Recycling Centers')
    plt.savefig('InfrastructureData/Graphs/TextileRecyclingCentersByState.png')
    plt.show()

def plotRegvsRecyclingRate():
    regData = RegvsRecyclingRate.getAvgPercentageByReg()
    regDataSortedbyValue = {k: v for k, v in sorted(regData.items(), key=lambda x: x[1], reverse=True)}

    x = regDataSortedbyValue.keys()  # Get the regulations from the dictionary
    y = regDataSortedbyValue.values()  # Get the average recycling percentages for each regulation

    f = plt.figure()
    f.set_figwidth(15)
    f.set_figheight(8)

    plt.bar(x, y)
    plt.title('Average Recycling Percentage by Regulation')
    plt.xlabel('Regulation')
    plt.ylabel('Average Recycling Percentage (%)')
    plt.gca().set_ybound(upper=100)
    plt.savefig('InfrastructureData/Graphs/AvgRecyclingPercentageByRegulation.png')
    plt.show()

def plotPetRatesbyState():
    rates = GetRatesbyStatePETBottles.getRates('RecyclingData/CSVData/PETBottlesbyZip_cleaned.csv')
    ratesSortedbyValue = {k: v for k, v in sorted(rates.items(), key=lambda x: x[1], reverse=True)}

    x = ratesSortedbyValue.keys()
    y = ratesSortedbyValue.values()

    f = plt.figure()
    f.set_figwidth(15)

    plt.bar(x,y)
    plt.title('PET Bottle Recycling Rates for 50 States')
    plt.xlabel('State')
    plt.ylabel('PET Bottle Recycling Rate')
    plt.savefig('InfrastructureData/Graphs/PETBottleRecyclingRatesbyState')
    plt.show()

def plotTextileRatesbyState():
    rates = GetRatesbyStateTextiles.getRates('RecyclingData/CSVData/TextileRecyclingbyZip_cleaned.csv')
    ratesSortedbyValue = {k: v for k, v in sorted(rates.items(), key=lambda x: x[1], reverse=True)}

    x = ratesSortedbyValue.keys()
    y = ratesSortedbyValue.values()

    f = plt.figure()
    f.set_figwidth(15)

    plt.bar(x,y)
    plt.title('Textile Recycling Rates for US States')
    plt.xlabel('State')
    plt.ylabel('Textile Recycling Rate')
    plt.savefig('InfrastructureData/Graphs/TextileRecyclingRatesbyState')
    plt.show()

def plotPETsitesbyState():
    petData = GetRatesbyStatePETBottles.getRates('RecyclingData/CSVData/PETBottlesbyZip_cleaned.csv')
    petDataSortedbyValue = {k: v for k, v in sorted(petData.items(), key=lambda x: x[1], reverse=True)}
    x = petDataSortedbyValue.keys()  # Get the states from the dictionary
    y = petDataSortedbyValue.values()  # Get the counts for each state

    f = plt.figure()
    f.set_figwidth(15)
    plt.bar(x, y)
    plt.title('Number of PET Bottle Recycling Sites by State')
    plt.xlabel('State')
    plt.ylabel('# of PET Bottle Recycling Sites')
    plt.savefig('InfrastructureData/Graphs/PETBottleRecyclingSitesByState.png')
    plt.show()


def plotPETvsRecyclingRate():
    petData = GetRatesbyStatePETBottles.getRates('RecyclingData/CSVData/PETBottlesbyZip_cleaned.csv')
    plasticSites = GetRatesbyStatePETBottles.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')

    petDataSortedbyKey = {k: v for k, v in sorted(petData.items(), key=lambda x: x[0])}
    plasticSitesSortedbyKey = {k: v for k, v in sorted(plasticSites.items(), key=lambda x: x[0])}

    petDataList = list(petDataSortedbyKey.values())
    plasticSitesList = list(plasticSitesSortedbyKey.values())

    z = np.polyfit(plasticSitesList, petDataList, 1)
    p = np.poly1d(z)
    plt.scatter(plasticSitesList, petDataList)
    plt.plot(plasticSitesList, p(plasticSitesList), "r--")
    plt.title('PET Bottle Recycling Rate vs. Number of Plastic Recycling Sites')
    plt.xlabel('Number of Plastic Recycling Sites')
    plt.ylabel('PET Bottle Recycling Rate (%)')
    plt.savefig('InfrastructureData/Graphs/PETBottleRecyclingRatevsSites.png')
    plt.show()

def plotTextilesvsRecyclingRate():
    textileData = GetRatesbyStateTextiles.getRates('RecyclingData/CSVData/TextileRecyclingbyZip_cleaned.csv')
    textileSites = GetRatesbyStateTextiles.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    textileSitesCleaned = {}

    for key in textileSites:
        if key in textileData:
            textileSitesCleaned[key] = textileSites[key]

    textileDataSortedbyKey = {k: v for k, v in sorted(textileData.items(), key=lambda x: x[0])}
    textileSitesSortedbyKey = {k: v for k, v in sorted(textileSitesCleaned.items(), key=lambda x: x[0])}

    textileDataList = list(textileDataSortedbyKey.values())
    textileSitesList = list(textileSitesSortedbyKey.values())

    z = np.polyfit(textileSitesList, textileDataList, 1)
    p = np.poly1d(z)
    plt.scatter(textileSitesList, textileDataList)
    plt.plot(textileSitesList, p(textileSitesList), "r--")
    plt.title('Textile Recycling Rate vs. Number of Textile Recycling Sites')
    plt.xlabel('Number of Textile Recycling Sites')
    plt.ylabel('Textile Recycling Rate (%)')
    plt.savefig('InfrastructureData/Graphs/TextileRecyclingRatevsSites.png')
    plt.show()

def plotAluminumRatesbyState():
    aluminumData = GetRatesbyStateAluminum.getRates('RecyclingData/CSVData/AluminumRecyclingbyZip_cleaned.csv')
    aluminumDataSortedbyValue = {k: v for k, v in sorted(aluminumData.items(), key=lambda x: x[1], reverse=True)}
    
    x = aluminumDataSortedbyValue.keys()  # Get the states from the dictionary
    y = aluminumDataSortedbyValue.values()  # Get the recycling rates for each state
    f = plt.figure()
    f.set_figwidth(15)
    plt.bar(x, y)
    plt.title('Aluminum Recycling Rates by State')
    plt.xlabel('State')
    plt.ylabel('Aluminum Recycling Rate (%)')
    plt.gca().set_ybound(upper=100)
    plt.savefig('InfrastructureData/Graphs/AluminumRecyclingRatesbyState.png')
    plt.show()

def plotAluminumRatesvsMRFS():
    aluminumData = GetRatesbyStateAluminum.getRates('RecyclingData/CSVData/AluminumRecyclingbyZip_cleaned.csv')
    MRFData = MRFbyState.csvtodict('InfrastructureData/CSVData/MRFdata.csv')
    MRFDataCleaned = {}

    for key in MRFData:
        if key in aluminumData:
            MRFDataCleaned[key] = MRFData[key]

    aluminumDataSortedbyKey = {k: v for k, v in sorted(aluminumData.items(), key=lambda x: x[0])}
    MRFDataSortedbyKey = {k: v for k, v in sorted(MRFDataCleaned.items(), key=lambda x: x[0])}
    aluminumDataList = list(aluminumDataSortedbyKey.values())
    MRFDataList = list(MRFDataSortedbyKey.values())

    z = np.polyfit(MRFDataList, aluminumDataList, 1)
    p = np.poly1d(z)
    plt.scatter(MRFDataList, aluminumDataList)
    plt.plot(MRFDataList, p(MRFDataList), "r--")
    plt.title('Aluminum Recycling Rate vs. Number of MRFs')
    plt.xlabel('Number of MRFs')
    plt.ylabel('Aluminum Recycling Rate (%)')
    plt.savefig('InfrastructureData/Graphs/AluminumRecyclingRatevsMRFs.png')
    plt.show()

def plotGlassSitesbyState():
    glassData = GetRatesbyStateGlass.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    glassDataSortedbyValue = {k: v for k, v in sorted(glassData.items(), key=lambda x: x[1], reverse=True)}
    x = glassDataSortedbyValue.keys()  # Get the states from the dictionary
    y = glassDataSortedbyValue.values()  # Get the counts for each state
    f = plt.figure()
    f.set_figwidth(15)
    plt.bar(x, y)
    plt.title('Number of Glass Recycling Sites by State')
    plt.xlabel('State')
    plt.ylabel('# of Glass Recycling Sites')
    plt.savefig('InfrastructureData/Graphs/GlassRecyclingSitesByState.png')
    plt.show()

def plotGlassRatesbyState():
    glassData = GetRatesbyStateGlass.getRates('RecyclingData/CSVData/GlassRecyclingbyZip_cleaned.csv')
    glassDataSortedbyValue = {k: v for k, v in sorted(glassData.items(), key=lambda x: x[1], reverse=True)}
    x = glassDataSortedbyValue.keys()  # Get the states from the dictionary
    y = glassDataSortedbyValue.values()  # Get the recycling rates for each state
    f = plt.figure()
    f.set_figwidth(15)
    plt.bar(x, y)
    plt.title('Glass Recycling Rates by State')
    plt.xlabel('State')
    plt.ylabel('Glass Recycling Rate (%)')
    plt.gca().set_ybound(upper=100)
    plt.savefig('InfrastructureData/Graphs/GlassRecyclingRatesbyState.png')
    plt.show()
    
def plotGlassvsRecyclingRate():
    glassData = GetRatesbyStateGlass.getRates('RecyclingData/CSVData/GlassRecyclingbyZip_cleaned.csv')
    glassSites = GetRatesbyStateGlass.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    glassSitesCleaned = {}

    for key in glassSites:
        if key in glassData:
            glassSitesCleaned[key] = glassSites[key]

    glassDataSortedbyKey = {k: v for k, v in sorted(glassData.items(), key=lambda x: x[0])}
    glassSitesSortedbyKey = {k: v for k, v in sorted(glassSitesCleaned.items(), key=lambda x: x[0])}

    glassDataList = list(glassDataSortedbyKey.values())
    glassSitesList = list(glassSitesSortedbyKey.values())

    z = np.polyfit(glassSitesList, glassDataList, 1)
    p = np.poly1d(z)
    plt.scatter(glassSitesList, glassDataList)
    plt.plot(glassSitesList, p(glassSitesList), "r--")
    plt.title('Glass Recycling Rate vs. Number of Glass Recycling Sites')
    plt.xlabel('Number of Glass Recycling Sites')
    plt.ylabel('Glass Recycling Rate (%)')
    plt.savefig('InfrastructureData/Graphs/GlassRecyclingRatevsSites.png')
    plt.show()
    
def plotPaperSitesbyState():
    paperData = GetRatesbyStatePaper.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    paperDataSortedbyValue = {k: v for k, v in sorted(paperData.items(), key=lambda x: x[1], reverse=True)}
    x = paperDataSortedbyValue.keys()  # Get the states from the dictionary
    y = paperDataSortedbyValue.values()  # Get the counts for each state

    f = plt.figure()
    f.set_figwidth(15)
    plt.bar(x, y)
    plt.title('Number of Paper Recycling Sites by State')
    plt.xlabel('State')
    plt.ylabel('# of Paper Recycling Sites')
    plt.savefig('InfrastructureData/Graphs/PaperRecyclingSitesByState.png')
    plt.show()

def plotPaperRatesbyState():
    paperData = GetRatesbyStatePaper.getRates('RecyclingData/CSVData/PaperRecyclingbyZip_cleaned.csv')
    paperDataSortedbyValue = {k: v for k, v in sorted(paperData.items(), key=lambda x: x[1], reverse=True)}
    x = paperDataSortedbyValue.keys()  # Get the states from the dictionary
    y = paperDataSortedbyValue.values()  # Get the recycling rates for each state
    f = plt.figure()
    f.set_figwidth(15)
    plt.bar(x, y)
    plt.title('Paper Recycling Rates by State')
    plt.xlabel('State')
    plt.ylabel('Paper Recycling Rate (%)')
    plt.gca().set_ybound(upper=100)
    plt.savefig('InfrastructureData/Graphs/PaperRecyclingRatesbyState.png')
    plt.show()

def plotPapervsRecyclingRate():
    paperData = GetRatesbyStatePaper.getRates('RecyclingData/CSVData/PaperRecyclingbyZip_cleaned.csv')
    paperSites = GetRatesbyStatePaper.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    paperSitesCleaned = {}
    for key in paperSites:
        if key in paperData:
            paperSitesCleaned[key] = paperSites[key]
    paperDataSortedbyKey = {k: v for k, v in sorted(paperData.items(), key=lambda x: x[0])}
    paperSitesSortedbyKey = {k: v for k, v in sorted(paperSitesCleaned.items(), key=lambda x: x[0])}
    paperDataList = list(paperDataSortedbyKey.values())
    paperSitesList = list(paperSitesSortedbyKey.values())
    z = np.polyfit(paperSitesList, paperDataList, 1)
    p = np.poly1d(z)
    plt.scatter(paperSitesList, paperDataList)
    plt.plot(paperSitesList, p(paperSitesList), "r--")
    plt.title('Paper Recycling Rate vs. Number of Paper Recycling Sites')
    plt.xlabel('Number of Paper Recycling Sites')
    plt.ylabel('Paper Recycling Rate (%)')
    plt.savefig('InfrastructureData/Graphs/PaperRecyclingRatevsSites.png')
    plt.show()

def plotTippingFeesByState():
    tippingFees = LandfillTippingFees.getTippingFees('RecyclingMarketFactors/CSVData/LandfillTippingFees_cleaned.csv')
    tippingFeesSortedbyValue = {k: v for k, v in sorted(tippingFees.items(), key=lambda x: x[1], reverse=True)} 
    x = tippingFeesSortedbyValue.keys()  # Get the states from the dictionary
    y = tippingFeesSortedbyValue.values()  # Get the tipping fees for each state
    f = plt.figure()
    f.set_figwidth(15)
    plt.bar(x, y)
    plt.title('Landfill Tipping Fees by State')
    plt.xlabel('State')
    plt.ylabel('Average Tipping Fee (USD per ton)')
    plt.savefig('InfrastructureData/Graphs/LandfillTippingFeesByState.png')
    plt.show()

def plotRegvsTippingFees():
    data = LandfillTippingFees.regvsTippingFees()
    dataSortedbyValue = {k: v for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True)}
    x = dataSortedbyValue.keys()  # Get the regulations from the dictionary
    y = dataSortedbyValue.values()  # Get the average tipping fees for each regulation
    f = plt.figure()
    f.set_figwidth(15)
    f.set_figheight(8)
    plt.bar(x, y)
    plt.title('Average Tipping Fees by Regulation')
    plt.xlabel('Regulation')
    plt.ylabel('Average Tipping Fee (USD per ton)')
    plt.gca().set_ybound(upper=100)
    plt.savefig('InfrastructureData/Graphs/AvgTippingFeesByRegulation.png')
    plt.show()
    
def plotTippingFeesvsRecyclingRate():
    tippingFees = LandfillTippingFees.getTippingFees('RecyclingMarketFactors/CSVData/LandfillTippingFees_cleaned.csv')
    recyclingData = GetRecyclingPercentagebyState.get_recycling_percentage_by_state('InfrastructureData/CSVData/RecyclingPercentageByState.csv')

    tippingFeessortedbyKey = {k: v for k, v in sorted(tippingFees.items(), key=lambda x: x[0])}
    recyclingDataSortedbyKey = {k: v for k, v in sorted(recyclingData.items(), key=lambda x: x[0])}
    tippingFeesList = list(tippingFeessortedbyKey.values())
    recyclingList = list(recyclingDataSortedbyKey.values())
    z = np.polyfit(tippingFeesList, recyclingList, 1)
    p = np.poly1d(z)
    plt.scatter(tippingFeesList, recyclingList)
    plt.plot(tippingFeesList, p(tippingFeesList), "r--")
    plt.title('Recycling Rate vs. Landfill Tipping Fees')
    plt.xlabel('Landfill Tipping Fees (USD per ton)')
    plt.ylabel('Recycling Rate (%)')
    plt.savefig('InfrastructureData/Graphs/RecyclingRatevsTippingFees.png')
    plt.show()

def plotBottleBillsvsTippingFee():
    data = BottleBills.bottleBillvsTippingFees()
    dataSortedbyValue = {k: v for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True)}
    x = dataSortedbyValue.keys()  # Get the states from the dictionary
    y = dataSortedbyValue.values()  # Get the bottle bill amounts for each state
    f = plt.figure()
    f.set_figwidth(15)
    plt.bar(x, y)
    plt.title('Tipping Fees vs. Presence of Bottle Bills by State')
    plt.xlabel('Presence of Bottle Bill')
    plt.ylabel('Average Tipping Fee (USD per ton)')
    plt.savefig('InfrastructureData/Graphs/TippingFeesvsBottleBills.png')
    plt.show()

def plotWoodSitesbyState():
    woodData = GetRatesbyStateWood.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    woodDataSortedbyValue = {k: v for k, v in sorted(woodData.items(), key=lambda x: x[1], reverse=True)}
    x = woodDataSortedbyValue.keys()  # Get the states from the dictionary
    y = woodDataSortedbyValue.values()  # Get the counts for each state
    f = plt.figure()
    f.set_figwidth(15)
    plt.bar(x, y)
    plt.title('Number of Wood Recycling Sites by State')
    plt.xlabel('State')
    plt.ylabel('# of Wood Recycling Sites')
    plt.savefig('InfrastructureData/Graphs/WoodRecyclingSitesByState.png')
    plt.show()


def plotWoodvsRecyclingRate():
    woodData = GetRatesbyStateWood.getRates('RecyclingData/CSVData/WoodRecyclingbyZip_cleaned.csv')
    woodSites = GetRatesbyStateWood.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')

    woodSitesCleaned = {}
    for key in woodSites:
        if key in woodData:
            woodSitesCleaned[key] = woodSites[key]
    woodDataSortedbyKey = {k: v for k, v in sorted(woodData.items(), key=lambda x: x[0])}
    woodSitesSortedbyKey = {k: v for k, v in sorted(woodSitesCleaned.items(), key=lambda x: x[0])}
    woodDataList = list(woodDataSortedbyKey.values())
    woodSitesList = list(woodSitesSortedbyKey.values())

    z = np.polyfit(woodSitesList, woodDataList, 1)
    p = np.poly1d(z)
    plt.scatter(woodSitesList, woodDataList)
    plt.plot(woodSitesList, p(woodSitesList), "r--")
    plt.title('Wood Recycling Rate vs. Number of Wood Recycling Sites')
    plt.xlabel('Number of Wood Recycling Sites')
    plt.ylabel('Wood Recycling Rate (%)')
    plt.savefig('InfrastructureData/Graphs/WoodRecyclingRatevsSites.png')
    plt.show()

def plotElectronicsSitesbyState():
    electronicsData = GetRatesbyStateElectronics.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    electronicsDataSortedbyValue = {k: v for k, v in sorted(electronicsData.items(), key=lambda x: x[1], reverse=True)}
    x = electronicsDataSortedbyValue.keys()  # Get the states from the dictionary
    y = electronicsDataSortedbyValue.values()  # Get the counts for each state
    f = plt.figure()
    f.set_figwidth(15)
    plt.bar(x, y)
    plt.title('Number of Electronics Recycling Sites by State')
    plt.xlabel('State')
    plt.ylabel('# of Electronics Recycling Sites')
    plt.savefig('InfrastructureData/Graphs/ElectronicsRecyclingSitesByState.png')
    plt.show()

def plotElectronicsvsRecyclingRate():
    electronicsData = GetRatesbyStateElectronics.getRates('RecyclingData/CSVData/ElectronicRecyclingbyZip_cleaned.csv')
    electronicsSites = GetRatesbyStateElectronics.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    electronicsSitesCleaned = {}
    for key in electronicsSites:
        if key in electronicsData:
            electronicsSitesCleaned[key] = electronicsSites[key]
    electronicsDataSortedbyKey = {k: v for k, v in sorted(electronicsData.items(), key=lambda x: x[0])}
    electronicsSitesSortedbyKey = {k: v for k, v in sorted(electronicsSitesCleaned.items(), key=lambda x: x[0])}
    electronicsDataList = list(electronicsDataSortedbyKey.values())
    electronicsSitesList = list(electronicsSitesSortedbyKey.values())
    z = np.polyfit(electronicsSitesList, electronicsDataList, 1)
    p = np.poly1d(z)
    plt.scatter(electronicsSitesList, electronicsDataList)
    plt.plot(electronicsSitesList, p(electronicsSitesList), "r--")
    plt.title('Electronics Recycling Rate vs. Number of Electronics Recycling Sites')
    plt.xlabel('Number of Electronics Recycling Sites')
    plt.ylabel('Electronics Recycling Rate (%)')
    plt.savefig('InfrastructureData/Graphs/ElectronicsRecyclingRatevsSites.png')
    plt.show()

def plotTextilevsMRFs():
    MRFdata = MRFbyState.csvtodict('InfrastructureData/CSVData/MRFdata.csv')
    textileSites = GetRatesbyStateTextiles.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    MRFdataCleaned = {}
    for key in MRFdata:
        if key in textileSites:
            MRFdataCleaned[key] = MRFdata[key]

    MRFdataSortedbyKey = {k: v for k, v in sorted(MRFdataCleaned.items(), key=lambda x: x[0])}
    textileSitesSortedbyKey = {k: v for k, v in sorted(textileSites.items(), key=lambda x: x[0])}

    MRFdataList = list(MRFdataSortedbyKey.values())
    textileSitesList = list(textileSitesSortedbyKey.values())
    z = np.polyfit(textileSitesList, MRFdataList, 1)
    p = np.poly1d(z)
    plt.scatter(textileSitesList, MRFdataList)
    plt.plot(textileSitesList, p(textileSitesList), "r--")
    plt.title('Textile Recycling Sites vs. Number of MRFs')
    plt.xlabel('Number of Textile Recycling Sites')
    plt.ylabel('Number of MRFs')
    plt.savefig('InfrastructureData/Graphs/TextileRecyclingSitesvsMRFs.png')
    plt.show()

def plotPlasticvsMRF():
    MRFdata = MRFbyState.csvtodict('InfrastructureData/CSVData/MRFdata.csv')
    plasticSites = GetRatesbyStatePETBottles.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    MRFdataCleaned = {}
    for key in MRFdata:
        if key in plasticSites:
            MRFdataCleaned[key] = MRFdata[key]

    MRFdataSortedbyKey = {k: v for k, v in sorted(MRFdataCleaned.items(), key=lambda x: x[0])}
    plasticSitesSortedbyKey = {k: v for k, v in sorted(plasticSites.items(), key=lambda x: x[0])}
    MRFdataList = list(MRFdataSortedbyKey.values())
    plasticSitesList = list(plasticSitesSortedbyKey.values())

    z = np.polyfit(plasticSitesList, MRFdataList, 1)
    p = np.poly1d(z)
    plt.scatter(plasticSitesList, MRFdataList)
    plt.plot(plasticSitesList, p(plasticSitesList), "r--")
    plt.title('Plastic Recycling Sites vs. Number of MRFs')
    plt.xlabel('Number of Plastic Recycling Sites')
    plt.ylabel('Number of MRFs')
    plt.savefig('InfrastructureData/Graphs/PlasticRecyclingSitesvsMRFs.png')
    plt.show()

def plotGlassvsMRFs():
    MRFdata = MRFbyState.csvtodict('InfrastructureData/CSVData/MRFdata.csv')
    glassSites = GetRatesbyStateGlass.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    MRFdataCleaned = {}
    for key in MRFdata:
        if key in glassSites:
            MRFdataCleaned[key] = MRFdata[key]

    MRFdataSortedbyKey = {k: v for k, v in sorted(MRFdataCleaned.items(), key=lambda x: x[0])}
    glassSitesSortedbyKey = {k: v for k, v in sorted(glassSites.items(), key=lambda x: x[0])}
    MRFdataList = list(MRFdataSortedbyKey.values())
    glassSitesList = list(glassSitesSortedbyKey.values())

    z = np.polyfit(glassSitesList, MRFdataList, 1)
    p = np.poly1d(z)
    plt.scatter(glassSitesList, MRFdataList)
    plt.plot(glassSitesList, p(glassSitesList), "r--")
    plt.title('Glass Recycling Sites vs. Number of MRFs')
    plt.xlabel('Number of Glass Recycling Sites')
    plt.ylabel('Number of MRFs')
    plt.savefig('InfrastructureData/Graphs/GlassRecyclingSitesvsMRFs.png')
    plt.show()

def plotPapervsMRFs():
    MRFdata = MRFbyState.csvtodict('InfrastructureData/CSVData/MRFdata.csv')
    paperSites = GetRatesbyStatePaper.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    MRFdataCleaned = {}
    for key in MRFdata:
        if key in paperSites:
            MRFdataCleaned[key] = MRFdata[key]

    MRFdataSortedbyKey = {k: v for k, v in sorted(MRFdataCleaned.items(), key=lambda x: x[0])}
    paperSitesSortedbyKey = {k: v for k, v in sorted(paperSites.items(), key=lambda x: x[0])}
    MRFdataList = list(MRFdataSortedbyKey.values())
    paperSitesList = list(paperSitesSortedbyKey.values())

    z = np.polyfit(paperSitesList, MRFdataList, 1)
    p = np.poly1d(z)
    plt.scatter(paperSitesList, MRFdataList)
    plt.plot(paperSitesList, p(paperSitesList), "r--")
    plt.title('Paper Recycling Sites vs. Number of MRFs')
    plt.xlabel('Number of Paper Recycling Sites')
    plt.ylabel('Number of MRFs')
    plt.savefig('InfrastructureData/Graphs/PaperRecyclingSitesvsMRFs.png')
    plt.show()

def plotWoodvsMRFs():
    MRFdata = MRFbyState.csvtodict('InfrastructureData/CSVData/MRFdata.csv')
    woodSites = GetRatesbyStateWood.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    MRFdataCleaned = {}
    for key in MRFdata:
        if key in woodSites:
            MRFdataCleaned[key] = MRFdata[key]

    MRFdataSortedbyKey = {k: v for k, v in sorted(MRFdataCleaned.items(), key=lambda x: x[0])}
    woodSitesSortedbyKey = {k: v for k, v in sorted(woodSites.items(), key=lambda x: x[0])}
    MRFdataList = list(MRFdataSortedbyKey.values())
    woodSitesList = list(woodSitesSortedbyKey.values())

    z = np.polyfit(woodSitesList, MRFdataList, 1)
    p = np.poly1d(z)
    plt.scatter(woodSitesList, MRFdataList)
    plt.plot(woodSitesList, p(woodSitesList), "r--")
    plt.title('Wood Recycling Sites vs. Number of MRFs')
    plt.xlabel('Number of Wood Recycling Sites')
    plt.ylabel('Number of MRFs')
    plt.savefig('InfrastructureData/Graphs/WoodRecyclingSitesvsMRFs.png')
    plt.show()

def plotElectronicsvsMRF():
    MRFdata = MRFbyState.csvtodict('InfrastructureData/CSVData/MRFdata.csv')
    electronicsSites = GetRatesbyStateElectronics.getNumberofCentersperState('InfrastructureData/CSVData/InfrastructureData_cleaned.csv')
    MRFdataCleaned = {}
    for key in MRFdata:
        if key in electronicsSites:
            MRFdataCleaned[key] = MRFdata[key]
    MRFdataSortedbyKey = {k: v for k, v in sorted(MRFdataCleaned.items(), key=lambda x: x[0])}
    electronicsSitesSortedbyKey = {k: v for k, v in sorted(electronicsSites.items(), key=lambda x: x[0])}
    MRFdataList = list(MRFdataSortedbyKey.values())
    electronicsSitesList = list(electronicsSitesSortedbyKey.values())
    z = np.polyfit(electronicsSitesList, MRFdataList, 1)
    p = np.poly1d(z)
    plt.scatter(electronicsSitesList, MRFdataList)
    plt.plot(electronicsSitesList, p(electronicsSitesList), "r--")
    plt.title('Electronics Recycling Sites vs. Number of MRFs')
    plt.xlabel('Number of Electronics Recycling Sites')
    plt.ylabel('Number of MRFs')
    plt.savefig('InfrastructureData/Graphs/ElectronicsRecyclingSitesvsMRFs.png')
    plt.show()


plotMRFbyState()
plotMostCommonFacilities()
plotDensityvsInfra()
plotPopvsInfra()
plotDensityvsMRF()
plotPopvsMRF()
plotStateRecyclingPercentage()
plotEmissionsByState()
plotEmissionsvsinfra()
plotEmissionsvsMRF()
plotYearlyEmissions()
plotRecyclingPercentagevsInfra()
plotRecyclingPercentagevsMRF()
plotTextilesByState()
plotRegvsRecyclingRate()
plotPetRatesbyState()
plotTextileRatesbyState()
plotPETsitesbyState()
plotPETvsRecyclingRate()
plotTextilesvsRecyclingRate()
plotAluminumRatesbyState()
plotAluminumRatesvsMRFS()
plotGlassSitesbyState()
plotGlassRatesbyState()
plotGlassvsRecyclingRate()
plotPaperSitesbyState()
plotPaperRatesbyState()
plotPapervsRecyclingRate()
plotTippingFeesByState()
plotRegvsTippingFees()
plotTippingFeesvsRecyclingRate()
plotBottleBillsvsTippingFee()
plotWoodSitesbyState()
plotWoodvsRecyclingRate()
plotTextilevsMRFs()
plotPlasticvsMRF()
plotGlassvsMRFs()
plotPapervsMRFs()
plotWoodvsMRFs()
plotElectronicsSitesbyState()
plotElectronicsvsRecyclingRate()
plotElectronicsvsMRF()