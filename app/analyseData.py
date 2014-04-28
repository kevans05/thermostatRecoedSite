import dataset
import statistics

def connectToDB():
    db = dataset.connect('sqlite:///app.db')
    return db

def returnDataBaseData():
    db = connectToDB()
    temp1 = []
    temp2 = []
    temp3 = []
    dateTimeMessurment = []
    for temps in db['temp']:
        temp1.append(temps['temp1'])
        temp2.append(temps['temp2'])
        temp3.append(temps['temp3'])
        dateTimeMessurment.append(temps['dateAndTime'])
    return temp1,temp2,temp3,dateTimeMessurment

def returnOurMean():
    data = returnDataBaseData()
    return round(statistics.mean(data[0]),3), round(statistics.mean(data[1]),3), round(statistics.mean(data[2]),3)

def returnOurMedian():
    data = returnDataBaseData()
    return round(statistics.median(data[0]),3), round(statistics.median(data[1]),3), round(statistics.median(data[2]),3)

def returnOurMode():
    data = returnDataBaseData()
    return round(statistics.mode(data[0]),3), round(statistics.mode(data[1]),3), round(statistics.mode(data[2]),3)

def returnOurSSD():
    data = returnDataBaseData()
    return round(statistics.stdev(data[0]),3), round(statistics.stdev(data[1]),3), round(statistics.stdev(data[2]),3)

def returnOurSV():
    data = returnDataBaseData()
    return round(statistics.variance(data[0]),3), round(statistics.variance(data[1]),3), round(statistics.variance(data[2]),3)

def returnMaxAndTime():
    data = returnDataBaseData()
    max_point_a = data[0].index(max(data[0]))
    max_point_b = data[1].index(max(data[1]))
    max_point_c = data[2].index(max(data[2]))
    max_date = data[3]
    return round(max(data[0]),3), round(max(data[1]),3), round(max(data[2]),3), max_date[max_point_a], max_date[max_point_c] ,max_date[max_point_c]

def returnMinAndTime():
    data = returnDataBaseData()
    min_point_a = data[0].index(min(data[0]))
    min_point_b = data[1].index(min(data[1]))
    min_point_c = data[2].index(min(data[2]))
    min_date = data[3]
    return round(min(data[0]),3), round(min(data[1]),3), round(min(data[2]),3), min_date[min_point_a], min_date[min_point_b] ,min_date[min_point_c]

def returnLength():
    data = returnDataBaseData()
    return len(data[0]), len(data[1]),len(data[1])

def findFirstValue():
    data = returnDataBaseData()
    return data[3][0]

def findLastValue():
    data = returnDataBaseData()
    return data[3][-1:]
