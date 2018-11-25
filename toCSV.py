##changing the json story data to a csv
import json, csv, pandas
filenames = ['story1', 'story2', 'story3']
def initial():
    for file in filenames:
        jsonName = file + ".json"
        csvName = file + ".csv"
        df = pandas.read_json(jsonName)
        df.to_csv(csvName)

if __name__ == '__main__':
    initial()
