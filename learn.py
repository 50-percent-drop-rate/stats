##Use KNN from Scikit-learn to train our scoring of sample.csv
import numpy as np
import pandas as pd
import csv
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
##load data


def initial():
    tweet = dict()
    count = 0
    #setup finalReport
    headers = ['user', 'tweet-id', 'timestamp', 'url', 'likes', 'replies', 'retweets', 'score']
    writeHeaders('scored.csv', headers)
    writeHeaders('scored_scaled.csv', headers)
    learn()
    scaling()

def scaling():
    data = pd.read_csv('scored.csv')
    scoredData = data.loc[:, "score"]
    min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 100))
    scaledData = min_max_scaler.fit_transform(scoredData[:, np.newaxis])
    with open('scored.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0
        for row in reader:
            user = row['user']
            id = row['tweet-id']
            stamp = row['timestamp']
            url = row['url']
            likes = row['likes']
            replies = row['replies']
            retweets = row['retweets']
            prediction = scaledData[i][0] * 100
            results = [user,id, stamp, url, likes, replies, retweets, str(prediction)]
            i = i + 1
            writeResults('scored_scaled.csv',results)
def learn():
    data = pd.read_csv('sample.csv')
    x_data = data.loc[:, ["likes", "replies", "retweets"]]
    y_data = data.loc[:, "tscore"]
    #using knn
    #parameters = {'n_neighbors': range(1,30)}
    #neigh = KNeighborsClassifier()
    #clf = GridSearchCV(neigh, parameters, cv= 5)
    #clf.fit(x_data, y_data)
    #print ("best score", clf.best_score_)
    #print("best params", clf.best_params_)
    #tunedNeigh = KNeighborsClassifier(n_neighbors=2)
    #neigh.fit(x_data, y_data)
    #process(neigh)

    #using regression
    reg = LinearRegression(normalize=True).fit(x_data, y_data)
    process(reg)
    

def process(neigh):
    with open('clean_data.csv', encoding="utf8") as csvfile:
         reader = csv.DictReader(csvfile)
         i = 0
         for row in reader:
             user = row['user']
             id = row['tweet-id']
             stamp = row['timestamp']
             url = row['url']
             likes = row['likes']
             replies = row['replies']
             retweets = row['retweets']
             prediction = neigh.predict([[int(likes), int(replies), int(retweets)]])
             results = [user,id, stamp, url, likes, replies, retweets, str(prediction[0])]
             writeResults('scored.csv', results)

def writeResults(filename, finalData):  
    with open(filename, "a") as myFile:
        for stat in finalData:
            try:
                myFile.write(stat)
                myFile.write(",")
            except UnicodeEncodeError:
                print("error")
        myFile.write("\n")

def writeHeaders(filename, headers):
    with open(filename, "w") as myFile:
        for line in headers:
            myFile.write(str(line))
            myFile.write(",")
        myFile.write("\n")

if __name__ == '__main__':
    initial()
