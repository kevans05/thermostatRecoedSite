import dataset
import numpy

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
    return round(numpy.mean(data[0]),3), round(numpy.mean(data[1]),3), round(numpy.mean(data[2]),3)

def returnOurMedian():
    data = returnDataBaseData()
    return round(numpy.median(data[0]),3), round(numpy.median(data[1]),3), round(numpy.median(data[2]),3)

def returnOurMode():
    data = returnDataBaseData()
    return round(numpy.mode(data[0]),3), round(numpy.mode(data[1]),3), round(numpy.mode(data[2]),3)

def returnOurSSD():
    data = returnDataBaseData()
    return round(numpy.std(data[0]),3), round(numpy.std(data[1]),3), round(numpy.std(data[2]),3)

def returnOurSV():
    data = returnDataBaseData()
    return round(numpy.var(data[0]),3), round(numpy.var(data[1]),3), round(numpy.var(data[2]),3)

def returnMaxAndTime():
    data = returnDataBaseData()
    max_a = max(data[0])
    max_point_a = data[0].index(max_a)

    max_b = max(data[1])
    max_point_b = data[1].index(max_b)

    max_c = max(data[2])
    max_point_c = data[2].index(max_c)

    max_date = data[3]
    return max_a, max_b, max_c, max_date[max_point_a], max_date[max_point_b] ,max_date[max_point_c]

def returnMinAndTime():
    data = returnDataBaseData()
    min_a = min(data[0])
    min_point_a = data[0].index(min_a)

    min_b = min(data[1])
    min_point_b = data[1].index(min_b)

    min_c = min(data[2])
    min_point_c = data[2].index(min_c)

    min_date = data[3]
    return min_a, min_b, min_c, min_date[min_point_a], min_date[min_point_b] ,min_date[min_point_c]

def returnLength():
    data = returnDataBaseData()
    return len(data[0]), len(data[1]),len(data[1])

def findFirstValue():
    data = returnDataBaseData()
    return data[3][0]

def findLastValue():
    data = returnDataBaseData()
    return data[3][-1:]
