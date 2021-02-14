import pandas as pd
import math

class TestGenes:

    def calculateZStat(self, sampleList, populationList):
            sampleMean = 0.0
            sampleStandardDeviation = 0.0
            sampleSize = len(sampleList)
            populationMean = 0.0
            populationStandardDeviation = 0.0
            populationSize = len(populationList)

            #Calculates sample mean of list
            sampleMean = sum(sampleList)/sampleSize

            #Calculates sample standard deviation of list
            if(sampleSize > 1):
                for i in range(0, sampleSize): #First calculates variance
                    sampleStandardDeviation += pow((sampleList[i] - sampleMean), 2)
                sampleStandardDeviation = sampleStandardDeviation/(sampleSize-1)
                sampleStandardDeviation = math.sqrt(sampleStandardDeviation)
            else:
                 sampleStandardDeviation = 0

            #Calculates sample mean of list
            populationMean = sum(populationList)/populationSize

            #Calculates sample standard deviation of list
            for i in range(0, populationSize): #First calculates variance
                populationStandardDeviation += pow((populationList[i] - populationMean), 2)
            populationStandardDeviation = populationStandardDeviation/(populationSize)
            populationStandardDeviation = math.sqrt(populationStandardDeviation)

            print("Sample Statistics")
            print("Mean: " + str(sampleMean) + " Sample Standard Deviation: " + str(sampleStandardDeviation) + " Size of data: " + str(sampleSize))

            print("Population Statistics")
            print("Mean: " + str(populationMean) + " Sample Standard Deviation: " + str(populationStandardDeviation) + " Size of data: " + str(populationSize))

            #Next calculate Z statistic
            zStat = (sampleMean - populationMean)/(populationStandardDeviation/math.sqrt(populationSize))
            return zStat

    def runTests(self):
            df = self.data
            threshold = 4.000 # Number of standard deviations
            p = 0.0001 # In this scenario we are saying that there is more than a 1/10000 change that a certain gene expresses
            rows = len(df)
            count1 = 0
            count2 = 0
            columns = len(df.columns)
            name = ""
            zStat = 0
            sampleNumber = "sample_"
            sampleList = []
            populationList = []
            for i in range(0, rows):
                ab = df[i:i+1]
                bac = ab.values.tolist()
                populationList = bac[0][1:columns]
                name = bac[0][0]

                for x in range(1, columns):
                    sampleList = bac[0][x:x+1]
                    zStat = self.calculateZStat(sampleList, populationList)
                    if(abs(zStat) < p):
                        print(name + " of " + sampleNumber + " " + str(x-1) + " " + "is a bad gene with smaller than the change of 1/10000 of expressing with a Z statistic of " + str(zStat))
                        count1+=1
                    else:
                        print(name + " of " + sampleNumber + " " + str(x-1) + " " + "is a good gene with greater than the change of 1/10000 of expressing with a Z statistic of " + str(zStat))
                        count2+=1
            print(count1)
            print(count2)

    def __init__(self):
        self.data = pd.read_csv(r'/home/romiovictor123/Desktop/EDIT/EDITInternship/technical_data/1_c_d.csv')

test = TestGenes()

test.runTests()