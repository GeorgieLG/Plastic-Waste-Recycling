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
    plt.savefig('InfrastructureData/Graphs/InfrastructureDatabystate.pdf')
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
    plt.savefig('InfrastructureData/Graphs/MRFdatabystate.pdf')
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
    plt.savefig('InfrastructureData/Graphs/MostCommonFacilities.pdf')
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
    plt.savefig('InfrastructureData/Graphs/PopulationDensityvsInfra.pdf')
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
    plt.savefig('InfrastructureData/Graphs/ResidentPopvsInfra.pdf')
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
    plt.savefig('InfrastructureData/Graphs/PopulationDensityvsMRF.pdf')
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
    plt.savefig('InfrastructureData/Graphs/ResidentPopvsMRF.pdf')
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
    plt.savefig('InfrastructureData/Graphs/RecyclingPercentageByState.pdf')
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
    plt.savefig('InfrastructureData/Graphs/EmissionsByState2020.pdf')
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
    plt.savefig('InfrastructureData/Graphs/EmissionsvsInfra.pdf')
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
    plt.savefig('InfrastructureData/Graphs/EmissionsvsMRF.pdf')
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
    plt.savefig('InfrastructureData/Graphs/TotalYearlyEmissions.pdf')
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
    plt.savefig('InfrastructureData/Graphs/RecyclingPercentagevsInfra.pdf')
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
    plt.savefig('InfrastructureData/Graphs/RecyclingPercentagevsMRF.pdf')
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
    plt.savefig('InfrastructureData/Graphs/TextileRecyclingCentersByState.pdf')
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
    plt.savefig('InfrastructureData/Graphs/AvgRecyclingPercentageByRegulation.pdf')
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

# plotInfraByState()
# plotMRFbyState()
# plotMostCommonFacilities()
# plotDensityvsInfra()
# plotPopvsInfra()
# plotDensityvsMRF()
# plotPopvsMRF()
# plotStateRecyclingPercentage()
# plotEmissionsByState()
# plotEmissionsvsinfra()
# plotEmissionsvsMRF()
# plotYearlyEmissions()
# plotRecyclingPercentagevsInfra()
# plotRecyclingPercentagevsMRF()
# plotTextilesByState()
# plotRegvsRecyclingRate()
# plotPetRatesbyState()
# plotTextileRatesbyState()
