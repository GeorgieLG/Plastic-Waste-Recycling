import MRFbyState
import matplotlib.pyplot as plt
import AnyInfraByState
import MostCommonFacilities
import AllInfravsPopDensity
import ResidentPopvsInfra

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

    plt.scatter(densityList, infraList)
    plt.title('Population Density vs. Number of Recycling Centers')
    plt.xlabel('Population Density (people per square mile)')
    plt.ylabel('Number of Recycling Centers')
    plt.savefig('InfrastructureData/PopulationDensityvsInfra.pdf')
    plt.show()

def plotPopvsInfra():
    popList, infraList = ResidentPopvsInfra.getArrays()
    plt.scatter(popList, infraList)
    plt.title('Resident Population vs. Number of Recycling Centers')
    plt.xlabel('Resident Population')
    plt.ylabel('Number of Recycling Centers')
    plt.savefig('InfrastructureData/ResidentPopvsInfra.pdf')
    plt.show()

#plotInfraByState() 
#plotMRFbyState()
#plotMostCommonFacilities()
#plotDensityvsInfra()
plotPopvsInfra()