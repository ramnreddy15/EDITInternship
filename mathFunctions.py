import math

"""This function return the mean, standard deviation, number of elements in list/vector""" 
def doTheMath(listOne):
    mean = 0.0
    standardDeviation = 0.0
    size = len(listOne)
    
    #Calculates mean of list
    mean = sum(listOne)/size

    #Calculates standard deviation of list
    for i in range(0, size): #First calculates variance
        standardDeviation += pow((listOne[i] - mean), 2)
    standardDeviation = standardDeviation/size
    standardDeviation = math.sqrt(standardDeviation)

    return mean, standardDeviation, size

listOne = [5.99342831, 4.7234714 , 6.29537708, 8.04605971, 4.53169325, 
4.53172609, 8.15842563, 6.53486946, 4.06105123, 6.08512009]

print(doTheMath(listOne))
    



