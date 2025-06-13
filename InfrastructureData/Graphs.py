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

def plotInfraByState():
    data = AnyInfraByState.csvtodict('InfrastructureData/InfrastructureData_cleaned.csv')
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
    plt.savefig('InfrastructureData/InfrastructureDatabystate.pdf')
    plt.show()

    # print("State counts:", dataSortedbyValue)
    # nodups = list(set(x))  # Remove duplicates from the state list
    # print(len(nodups))

def plotMRFbyState():
    data = MRFbyState.csvtodict('InfrastructureData/MRFdata.csv')
    dataSortedbyValue = {k: v for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True)}

    x = dataSortedbyValue.keys()  # Get the states from the dictionary
    y = dataSortedbyValue.values()  # Get the counts for each state

    f = plt.figure()
    f.set_figwidth(15)

    plt.bar(x, y)
    plt.title('Number of MRFs by State')
    plt.xlabel('State')
    plt.ylabel('# of Sites')
    plt.savefig('InfrastructureData/MRFdatabystate.pdf')
    plt.show()

    # print("State counts:", dataSortedbyValue)
    # nodups = list(set(x))  # Remove duplicates from the state list
    # print(len(nodups))

def plotMostCommonFacilities():
    facilities = MostCommonFacilities.mostCommonFacilities('InfrastructureData/InfrastructureData_cleaned.csv')

    x = facilities.keys() # Get the facilities from the dictionary
    y = facilities.values() # Get the counts for each facility
    f = plt.figure()
    f.set_figwidth(10)

    plt.barh(x, y)
    plt.title('Most Common Facilities')
    plt.ylabel('Facility Type')
    plt.xlabel('# of Sites')
    plt.subplots_adjust(left=.25, bottom=None, right=.883, top=None, wspace=None, hspace=None)
    plt.savefig('InfrastructureData/MostCommonFacilities.pdf')
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
    plt.savefig('InfrastructureData/PopulationDensityvsInfra.pdf')
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
    plt.savefig('InfrastructureData/ResidentPopvsInfra.pdf')
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
    plt.savefig('InfrastructureData/PopulationDensityvsMRF.pdf')
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
    plt.savefig('InfrastructureData/ResidentPopvsMRF.pdf')
    plt.show()

def plotStateRecyclingPercentage():
    recyclingData = GetRecyclingPercentagebyState.get_recycling_percentage_by_state('InfrastructureData/RecyclingPercentageByState.csv')
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
    plt.savefig('InfrastructureData/RecyclingPercentageByState.pdf')
    plt.show()

def plotEmissionsByState():
    emissionsData = GetEmissionsbyYear.get_emissions_by_year('InfrastructureData/LongTermEmissionsData.csv', '2020')
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
    plt.savefig('InfrastructureData/EmissionsByState2020.pdf')
    plt.show()

def plotEmissionsvsinfra():
    popList, infraList = ResidentPopvsInfra.getArrays()
    emissionsData = GetEmissionsbyYear.get_emissions_by_year('InfrastructureData/LongTermEmissionsData.csv', '2020')
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
    plt.savefig('InfrastructureData/EmissionsvsInfra.pdf')
    plt.show()

def plotEmissionsvsMRF():
    popList, MRFList = ResidentPopvsMRF.getArrays()
    emissionsData = GetEmissionsbyYear.get_emissions_by_year('InfrastructureData/LongTermEmissionsData.csv', '2020')
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
    plt.savefig('InfrastructureData/EmissionsvsMRF.pdf')
    plt.show()


#plotInfraByState() 
#plotMRFbyState()
# plotMostCommonFacilities()
# plotDensityvsInfra()
# plotPopvsInfra()
# plotDensityvsMRF()
# plotPopvsMRF()
#plotStateRecyclingPercentage()
#plotEmissionsByState()
#plotEmissionsvsinfra()
plotEmissionsvsMRF()
