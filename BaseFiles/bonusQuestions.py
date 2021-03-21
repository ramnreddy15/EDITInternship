import sklearn
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
import io
from matplotlib import pyplot as plt
import seaborn as sn
import pandas as pd
import numpy as np

def graphFunction(data):
    labels = data.iloc[:,0]
    data = data.drop(data.columns[0], axis=1)

    for i in range(len(labels)): # Removes index from row
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

    plt.xlabel("Patient")
    plt.ylabel("Expression")
    plt.title("Patient vs Expression")

    ax.legend()
    plt.show()

def classifyData(data):
    # Prep for model
    labels = data.iloc[:,0]    
    for i in range(len(labels)): # Removes index from row
        labels[i] = labels[i][-3:]
    data = data.drop(data.columns[0], axis=1)
    x_train,x_test,y_train,y_test=train_test_split(data,labels,test_size=0.2, random_state=15)

    trainReady = scale(x_train)
    testReady = scale(x_test)
    
    # Creating model
    clustering = KMeans(n_clusters=2,random_state=15)
    model = clustering.fit(trainReady)
    
    #Verifying model
    # 0 is ALL
    # 1 is AML
    prediction = model.predict(x_test)
    correct = 0      

    correctLabels = y_test.values.tolist()
    for i in range(len(correctLabels)):
        if(correctLabels[i] == "ALL"):
            correctLabels[i] = 0
        else:
            correctLabels[i] = 1

    for i in range(len(prediction)):
        if(prediction[i] == correctLabels[i]):
            correct = correct + 1
    return (correct/len(y_test))

data = pd.read_csv(r'/home/romiovictor123/Desktop/EDIT/technical_data/2_a.csv', header=None)

graphFunction(data)
print(classifyData(data))