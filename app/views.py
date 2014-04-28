from flask import render_template, flash, redirect, jsonify
from app import app, analyseData
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    timeNow = datetime.now()
    timeNow = timeNow.replace(microsecond=0)
    means = analyseData.returnOurMean()
    Medians = analyseData.returnOurMedian()
    SSD = analyseData.returnOurSSD()
    DS18B201 = {'mean':means[0],'Median':Medians[0],'SD':SSD[0],'TM':timeNow}
    DS18B202 = {'mean':means[1],'Median':Medians[1],'SD':SSD[1],'TM':timeNow}
    MLX90614 = {'mean':means[2],'Median':Medians[2],'SD':SSD[2],'TM':timeNow}
    return render_template("index.html",title = 'Home',DS18B201 = DS18B201,DS18B202=DS18B202,MLX90614=MLX90614 )

@app.route('/settings', methods = ['GET', 'POST'])
def settings():
    return render_template("settings.html",title = 'settings')

@app.route('/DS18B201')
def DS18B201():
    timeNow = datetime.now()
    timeNow = timeNow.replace(microsecond=0)
    mean = analyseData.returnOurMean()
    Medians = analyseData.returnOurMedian()
    SSD = analyseData.returnOurSSD()
    SV = analyseData.returnOurSV()
    MAX = analyseData.returnMaxAndTime()
    MIN = analyseData.returnMinAndTime()
    Num = analyseData.returnLength()
    FirstValue = analyseData.findFirstValue()
    LastValue = analyseData.findLastValue()
    StatsValue = {'TM': timeNow,'mean':mean[2],'Medians':Medians[2], 'SSD':SSD[2],'SV':SV[2],
                  'MAX':MAX[2],'MIN':MIN[2],'Num':Num[2],'FirstValue':FirstValue,'LastValue':LastValue[0],'maxTime':MAX[4],'minTime':MIN[4]}
    return render_template("DS18B201.html",title = 'DS18B201',StatsValue = StatsValue)
@app.route('/DS18B202')
def DS18B202():
    timeNow = datetime.now()
    timeNow = timeNow.replace(microsecond=0)
    mean = analyseData.returnOurMean()
    Medians = analyseData.returnOurMedian()
    SSD = analyseData.returnOurSSD()
    SV = analyseData.returnOurSV()
    MAX = analyseData.returnMaxAndTime()
    MIN = analyseData.returnMinAndTime()
    Num = analyseData.returnLength()
    FirstValue = analyseData.findFirstValue()
    LastValue = analyseData.findLastValue()
    StatsValue = {'TM': timeNow,'mean':mean[2],'Medians':Medians[2], 'SSD':SSD[2],'SV':SV[2],
                  'MAX':MAX[2],'MIN':MIN[2],'Num':Num[2],'FirstValue':FirstValue,'LastValue':LastValue[0],'maxTime':MAX[5],'minTime':MIN[5]}
    return render_template("DS18B202.html",title = 'DS18B202',StatsValue = StatsValue)
@app.route('/MLX90614')
def MLX90614():
    timeNow = datetime.now()
    timeNow = timeNow.replace(microsecond=0)
    mean = analyseData.returnOurMean()
    Medians = analyseData.returnOurMedian()
    SSD = analyseData.returnOurSSD()
    SV = analyseData.returnOurSV()
    MAX = analyseData.returnMaxAndTime()
    MIN = analyseData.returnMinAndTime()
    Num = analyseData.returnLength()
    FirstValue = analyseData.findFirstValue()
    LastValue = analyseData.findLastValue()
    StatsValue = {'TM': timeNow,'mean':mean[2],'Medians':Medians[2], 'SSD':SSD[2],'SV':SV[2],
                  'MAX':MAX[2],'MIN':MIN[2],'Num':Num[2],'FirstValue':FirstValue,'LastValue':LastValue[0],'maxTime':MAX[5],'minTime':MIN[5]}
    return render_template("MLX90614.html",title = 'MLX90614',StatsValue = StatsValue)

@app.route('/liveData',  methods= ['GET'])
def liveData():
    timeNow = datetime.now()
    timeNow = timeNow.replace(microsecond=0)
    return jsonify(timeNow)


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500