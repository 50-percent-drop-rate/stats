#Calculate simple stats for each dataset for likes, replies, retweets
#max, average, standard deviation, etc.
import csv, time, numpy, statistics



listOfFilesKhashoggi = ['khashoggi916', 'khashoggi923', 'khashoggi930', 'khashoggi1007', 'khashoggi1014', 'khashoggi1021', 'khashoggi1028']
listOfFilesCanada = ['weed916', 'weed923', 'weed930', 'weed1007', 'weed1014', 'weed1021', 'weed1028']
listOfFilesMichael = ['michael916', 'michael923', 'michael930', 'michael1007', 'michael1014', 'michael1021', 'michael1028']

#Khashoggi
#Output: nameOfFile, numTweets, timeToProcess, maxLikes, avgLikes, medianLikes, stdDevLikes,
#maxReplies, avgReplies, medianReplies, stdDevReplies, maxRetweets, avgRetweets, medianRetweets, stdDevRetweets

def initial():
    #setup finalReport
    headers = ['nameOfFile', 'numTweets', 'timeToProcess', 'maxLikes', 'avgLikes', 'medianLikes', 'stdDevLikes', 'maxReplies',
               'avgReplies', 'medianReplies', 'stdDevReplies', 'maxRetweets', 'avgRetweets', 'medianRetweets', 'stdDevRetweets']
    writeHeaders(headers)
    michaelProcess()
    canadaProcess()
    khashoggiProcess()

def michaelProcess():
    for name in listOfFilesMichael:
        name = name + ".csv"
        t0 = time.time()
        with open(name, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            likes= []
            replies = []
            retweets = []
            for row in reader:
                likes.append(int(row['likes']))
                replies.append(int(row['replies']))
                retweets.append(int(row['retweets']))
            maxLikes = max(likes)
            avgLikes = statistics.mean(likes)
            medianLikes = statistics.median(likes)
            stdDevLikes = statistics.stdev(likes)
            maxReplies = max(replies)
            avgReplies = statistics.mean(replies)
            medianReplies = statistics.median(replies)
            stdDevReplies = statistics.stdev(replies)
            maxRetweets = max(retweets)
            avgRetweets = statistics.mean(retweets)
            medianRetweets = statistics.median(retweets)
            stdDevRetweets = statistics.stdev(retweets)
            count = len(likes)
            t1 = time.time()
            duration = t1-t0
            finalData = [name,count,duration,maxLikes,avgLikes,medianLikes,stdDevLikes,
                     maxReplies,avgReplies,medianReplies,stdDevReplies,maxRetweets,avgRetweets,medianRetweets,stdDevRetweets]
            writeResults(finalData)
def canadaProcess():
    for name in listOfFilesCanada:
        name = name + ".csv"
        t0 = time.time()
        with open(name, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            likes= []
            replies = []
            retweets = []
            for row in reader:
                likes.append(int(row['likes']))
                replies.append(int(row['replies']))
                retweets.append(int(row['retweets']))
            maxLikes = max(likes)
            avgLikes = statistics.mean(likes)
            medianLikes = statistics.median(likes)
            stdDevLikes = statistics.stdev(likes)
            maxReplies = max(replies)
            avgReplies = statistics.mean(replies)
            medianReplies = statistics.median(replies)
            stdDevReplies = statistics.stdev(replies)
            maxRetweets = max(retweets)
            avgRetweets = statistics.mean(retweets)
            medianRetweets = statistics.median(retweets)
            stdDevRetweets = statistics.stdev(retweets)
            count = len(likes)
            t1 = time.time()
            duration = t1-t0
            finalData = [name,count,duration,maxLikes,avgLikes,medianLikes,stdDevLikes,
                     maxReplies,avgReplies,medianReplies,stdDevReplies,maxRetweets,avgRetweets,medianRetweets,stdDevRetweets]
            writeResults(finalData)
def khashoggiProcess():
    for name in listOfFilesKhashoggi:
        name = name + ".csv"
        t0 = time.time()
        with open(name, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            likes= []
            replies = []
            retweets = []
            for row in reader:
                likes.append(int(row['likes']))
                replies.append(int(row['replies']))
                retweets.append(int(row['retweets']))
            maxLikes = max(likes)
            avgLikes = statistics.mean(likes)
            medianLikes = statistics.median(likes)
            stdDevLikes = statistics.stdev(likes)
            maxReplies = max(replies)
            avgReplies = statistics.mean(replies)
            medianReplies = statistics.median(replies)
            stdDevReplies = statistics.stdev(replies)
            maxRetweets = max(retweets)
            avgRetweets = statistics.mean(retweets)
            medianRetweets = statistics.median(retweets)
            stdDevRetweets = statistics.stdev(retweets)
            count = len(likes)
            t1 = time.time()
            duration = t1-t0
            finalData = [name,count,duration,maxLikes,avgLikes,medianLikes,stdDevLikes,
                     maxReplies,avgReplies,medianReplies,stdDevReplies,maxRetweets,avgRetweets,medianRetweets,stdDevRetweets]
            writeResults(finalData)
def writeHeaders(headers):
    with open('results.csv', "w") as myFile:
        #print(finalData)
        for line in headers:
            myFile.write(str(line))
            myFile.write(",")
        myFile.write("\n")
def writeResults(finalData):
    with open('results.csv', "a") as myFile:
        #print(finalData)
        for stat in finalData:
            myFile.write(str(stat))
            myFile.write(",")
        myFile.write("\n")
if __name__ == '__main__':
    initial()
