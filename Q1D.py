import pandas as pd
import matplotlib.pyplot as plt

def makeGraphs(data1, data2):
    labels = [data1[0][0], data2[0][0]]
    data1 = data1[0][1:]
    data2 = data2[0][1:]

    plt.scatter(data1, data2, color='orange') #2 vs 5 is one
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(labels[0] + " vs. " + labels[1])
    plt.show()

data1 = pd.read_csv(r'/home/romiovictor123/Desktop/EDIT/EDITInternship/technical_data/1_c_d.csv')
data2 = pd.read_csv(r'/home/romiovictor123/Desktop/EDIT/EDITInternship/technical_data/1_c_d.csv')

print("Select which genes you want to see in a graph.")
print("Selectable genes: gene_0, gene_1, gene_2, gene_3, gene_4, gene_5, gene_6, gene_7")
geneList = list(input("Input two genes like '07' with no space in between. No other method will be accepted."))

if((len(geneList) > 2) or (int(geneList[0]) > 7) or (int(geneList[1]) > 7)):
    print("Please input correctly.")
else:
    data1 = data1[int(geneList[0]):int(geneList[0])+1].values.tolist()
    data2 = data2[int(geneList[1]):int(geneList[1])+1].values.tolist()

    makeGraphs(data1, data2)


