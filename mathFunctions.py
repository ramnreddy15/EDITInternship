import math

"""Q1 A"""
"""This function return the mean, standard deviation, number of elements in list/vector""" 
def calculateStatistics(listOne, type):
    populationMean = 0.0
    standardDeviation = 0.0
    size = len(listOne)
    
    #Calculates sample mean of list
    populationMean = sum(listOne)/size

    #Calculates sample standard deviation of list
    for i in range(0, size): #First calculates variance
        standardDeviation += pow((listOne[i] - populationMean), 2)
    if(type == "sample")
        standardDeviation = standardDeviation/(size-1)
    else:
        standardDeviation = standardDeviation/(size)
    standardDeviation = math.sqrt(standardDeviation)

    return populationMean, standardDeviation, size

"""Q1 B"""
"""This method return true if the means have a statistically significant differnece"""

def calculateZStat(sampleList, populationList):

    threshold = 4.000 # Number of standard deviations
    p = 0.0001 # In this scenario we are saying that there is more than a 1/10000 change that a certain gene expresses

    sampleMean, sampleStandardDeviation, sampleSize = calculateStatistics(sampleList, "sample")
    populationMean, populationStandardDeviation, populationSize = calculateStatistics(populationList, "population")

    print("Sample Statistics")
    print("Mean: " + str(sampleMean) + " Sample Standard Deviation: " + str(sampleStandardDeviation) + " Size of data: " + str(sampleSize))

    print("Population Statistics")
    print("Mean: " + str(populationMean) + " Sample Standard Deviation: " + str(populationStandardDeviation) + " Size of data: " + str(populationSize))

    #Next calculate Z statistic
    zStat = (sampleMean - populationMean)/(populationStandardDeviation/math.sqrt(populationSize))
    if(abs(zStat) > threshold):
        print("This gene is a bad gene with greater than the change of " + str(p) + " of expressing with a Z statistic of " + str(zStat))
    else:
        print("This gene is a good gene with smaller than the change of " + str(p) + " of expressing with a Z statistic of " + str(zStat))

sampleList = [0, 4.7234714 , 6.29537708, 8.04605971, 4.53169325, 
4.53172609, 8.15842563, 6.53486946, 4.06105123, 6.08512009]
    
populationList = [0, 4.7234714 , 6.29537708, 8.04605971, 4.53169325, 
4.53172609, 8.15842563, 6.53486946, 4.06105123, 6.08512009]

populationMean, populationStandardDeviation, populationSize = calculateStatistics(populationList, "population")

print(populationMean)
print(populationStandardDeviation)
print(populationSize)

# calculateZStat(sampleList, populationList)
