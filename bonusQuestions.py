import sklearn
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
import io
from matplotlib import pyplot as plt
import seaborn as sn
import pandas as pd
import numpy as np

def graphFunction(data):
    labels = data.iloc[:,0]
    data = data.drop(data.columns[0], axis=1)

    for i in range(len(labels)):
        labels[i] = labels[i][-3:]

    model = TSNE(n_components=2, random_state=15)

    tsne_data = model.fit_transform(data)
    tsne_data = np.vstack((tsne_data.T, labels)).T

    tsne_df = pd.DataFrame(data=tsne_data, columns=("Patient", "Expression", "label"))

    patientData = tsne_df.iloc[:,0].to_numpy()
    expressionData = tsne_df.iloc[:,1].to_numpy()
    labelData = tsne_df.iloc[:,2].to_numpy()

    cdict = {"ALL": 'orange', "AML": 'blue'}
    
    fig, ax = plt.subplots()
    for g in np.unique(labelData):
        ix = np.where(labelData == g)
        ax.scatter(patientData[ix], expressionData[ix], c = cdict[g], label = g) # Add labels and title

    ax.legend()
    plt.show()

def classifyData():

data = pd.read_csv(r'/home/romiovictor123/Desktop/EDIT/technical_data/2_a.csv')

graphFunction(data)