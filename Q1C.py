import pandas as pd
import math

class TestGenes:

    def calculateZStat(self, sampleList, populationList):
            sampleMean = 0.0
            sampleSize = len(sampleList)
            populationMean = 0.0
            populationStandardDeviation = 0.0
            populationSize = len(populationList)

            #Calculates sample mean of list
            sampleMean = sum(sampleList)/sampleSize

            #Calculates population mean of list
            populationMean = sum(populationList)/populationSize

            #Calculates sample standard deviation of list
            for i in range(0, populationSize): #First calculates variance
                populationStandardDeviation += pow((populationList[i] - populationMean), 2)
            populationStandardDeviation = populationStandardDeviation/(populationSize)
            populationStandardDeviation = math.sqrt(populationStandardDeviation)

            #Next calculate Z statistic
            zStat = (sampleMean - populationMean)/(populationStandardDeviation/math.sqrt(populationSize))
            return zStat

    def runTests(self):
            df = self.data
            threshold = 4.000 # Number of standard deviations
            p = 0.0001 # In this scenario we are saying that there is more than a 1/10000 change that a certain gene expresses
            zStat = 0
            rows = len(df)
            columns = len(df.columns)
            count1 = 0
            count2 = 0
            name = ""
            sampleNumber = "sample_"
            sampleList = []
            populationList = []

            for i in range(0, rows):
                temp = df[i:i+1].values.tolist() # Getting the data ready
                populationList = temp[0][1:columns]
                name = temp[0][0]

                for x in range(1, columns):
                    sampleList = temp[0][x:x+1]
                    zStat = self.calculateZStat(sampleList, populationList) # Going through every sample and gene
                    if(abs(zStat) > threshold):
                        print(name + " of " + sampleNumber + " " + str(x-1) + " " + "is a bad gene with greater than the change of " + str(p) + " of expressing with a Z statistic of " + str(zStat))
                        count1+=1
                    else:
                        print(name + " of " + sampleNumber + " " + str(x-1) + " " + "is a good gene with smaller than the change of " + str(p) + " of expressing with a Z statistic of " + str(zStat))
                        count2+=1
            print(f"Number of bad genes is {count1}")
            print(f"Number of good genes is {count2}")

    def __init__(self):
        self.data = pd.read_csv(r'/home/romiovictor123/Desktop/EDIT/EDITInternship/technical_data/1_c_d.csv')

test = TestGenes()

test.runTests()