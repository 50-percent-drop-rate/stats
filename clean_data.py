##cleans the data and removes all tweets with 0 engagement
import csv, time, numpy, statistics, random



listOfFilesKhashoggi = ['khashoggi916', 'khashoggi923', 'khashoggi930', 'khashoggi1007', 'khashoggi1014', 'khashoggi1021', 'khashoggi1028']
listOfFilesCanada = ['weed916', 'weed923', 'weed930', 'weed1007', 'weed1014', 'weed1021', 'weed1028']
listOfFilesMichael = ['michael916', 'michael923', 'michael930', 'michael1007', 'michael1014', 'michael1021', 'michael1028']

global count
global tweet


def initial():
    global count
    global tweet
    tweet = dict()
    count = 0
    #setup finalReport
    headers = ['user', 'tweet-id', 'timestamp', 'url', 'likes', 'replies', 'retweets']
    writeHeaders(headers)
    michaelProcess()
    canadaProcess()
    khashoggiProcess()
    print("Total tweets: " + str(count))

def michaelProcess():
    for name in listOfFilesMichael:
        name = name + ".csv"
        with open(name, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                likes = row['likes']
                replies = row['replies']
                retweets = row['retweets']
                id = row['tweet-id']
                if (int(likes) > 0 or int(replies) > 0 or int(retweets) > 0):
                    global tweet
                    if id not in tweet:
                        tweet[id] = ""
                        user = row['user']
                        stamp = row['timestamp']
                        url = row['url']
                        likes = row['likes']
                        replies = row['replies']
                        retweets = row['retweets']
                        data = [user, id, stamp, url, likes, replies, retweets]
                        writeResults(data)
def canadaProcess():
    for name in listOfFilesCanada:
        name = name + ".csv"
        with open(name, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                likes = row['likes']
                replies = row['replies']
                retweets = row['retweets']
                id = row['tweet-id']
                if (int(likes) > 0 or int(replies) > 0 or int(retweets) > 0):
                    global tweet
                    if id not in tweet:
                        tweet[id] = ""
                        user = row['user']
                        stamp = row['timestamp']
                        url = row['url']
                        likes = row['likes']
                        replies = row['replies']
                        retweets = row['retweets']
                        data = [user, id, stamp, url, likes, replies, retweets]
                        writeResults(data)

def khashoggiProcess():
    for name in listOfFilesKhashoggi:
        name = name + ".csv"
        with open(name, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                likes = row['likes']
                replies = row['replies']
                retweets = row['retweets']
                id = row['tweet-id']
                if (int(likes) > 0 or int(replies) > 0 or int(retweets) > 0):
                    global tweet
                    if id not in tweet:
                        tweet[id] = ""
                        user = row['user']
                        stamp = row['timestamp']
                        url = row['url']
                        likes = row['likes']
                        replies = row['replies']
                        retweets = row['retweets']
                        data = [user, id, stamp, url, likes, replies, retweets]
                        writeResults(data)


def writeHeaders(headers):
    with open('clean_data.csv', "w") as myFile:
        for line in headers:
            myFile.write(str(line))
            myFile.write(",")
        myFile.write("\n")

def writeResults(finalData):
    
    global count
    count = count + 1
    print(count)
    with open('clean_data.csv', "a") as myFile:
        for stat in finalData:
            try:
                myFile.write(stat)
                myFile.write(",")
            except UnicodeEncodeError:
                print("error")
        myFile.write("\n")
     

if __name__ == '__main__':
    initial()
