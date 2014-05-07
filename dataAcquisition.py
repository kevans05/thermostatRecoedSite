__author__ = 'Kyle'
import random
import dataset
import plotly
import json
import  threading
import collectDS18B20
import collectMLX90614
from datetime import datetime
from time import sleep


def creatStreamingGraph(fileName, ConfigGile,chanID):
    with open(ConfigGile) as config_file:
        plotly_user_config = json.load(config_file)
    username = plotly_user_config['plotly_username']
    api_key = plotly_user_config['plotly_api_key']
    stream_token = plotly_user_config['plotly_streaming_tokens'][chanID]
    stream_server = 'http://stream.plot.ly'

    p = plotly.plotly(username, api_key)
    layout = {'autosize': True, 'showlegend':True,'legend': {"x" : 1, "y" : 1},"xaxis": {"title":"Time"},"yaxis": {"title":"Temp (C)"}}
    p.plot([{'x': [],'y': [],"name":fileName,'type': 'scatter', 'mode': 'lines+markers','stream': {'token': stream_token,'maxpoints': 60}}],filename=fileName, fileopt='overwrite',layout = layout, world_readable=True)
    s = plotly.stream(stream_token)
    return s
def generateThreeTrace(ConfigGile):
    with open(ConfigGile) as config_file:
        plotly_user_config = json.load(config_file)
    username = plotly_user_config['plotly_username']
    api_key = plotly_user_config['plotly_api_key']
    stream_tokenA = plotly_user_config['plotly_streaming_tokens'][3]
    stream_tokenB = plotly_user_config['plotly_streaming_tokens'][4]
    stream_tokenC = plotly_user_config['plotly_streaming_tokens'][5]
    stream_server = 'http://stream.plot.ly'
    layout = {'autosize': True, 'showlegend':True,'legend': {"x" : 1, "y" : 1},"xaxis": {"title":"Time"},"yaxis": {"title":"Temp (C)"}}
    data = [
        {'x': [], 'y': [],"name":"DS18B20 1", 'type': 'scatter', 'mode': 'lines+markers', 'line': {'color': 'rgba(106, 45, 172, 1)'},
         'stream': {'token': stream_tokenA, 'maxpoints': 60}},
        {'x': [], 'y': [],"name":"DS18B20 2", 'type': 'scatter', 'mode': 'lines+markers', 'line': {'color':  'rgba(215, 40, 44, 1)'},
            'stream': {'token': stream_tokenB, 'maxpoints': 60}},
        {'x': [], 'y': [],"name":"MLX90614 1", 'type': 'scatter', 'mode': 'lines+markers', 'line': {'color': 'rgba(106, 240, 44, 1)'},
            'stream': {'token': stream_tokenC, 'maxpoints': 60}}]
    p = plotly.plotly(username, api_key)
    p.plot(data, fileopt='overwrite',layout = {'autosize': True, 'showlegend':True,'legend': {"x" : 1, "y" : 1}})
    s4 = plotly.stream(stream_tokenA)
    s5 = plotly.stream(stream_tokenB)
    s6 = plotly.stream(stream_tokenC)
    return s4, s5, s6

def addPointToLargeStreamingGraph(stream_ID,dateTime, temp1, temp2, temp3):
    stream_ID[0].write({'x': str(dateTime), 'y':temp1})
    stream_ID[1].write({'x': str(dateTime), 'y':temp2})
    stream_ID[2].write({'x': str(dateTime), 'y':temp3})


def addPointToStreamingGraph(dateTime, sensor_data, s):
    s.write({'x': str(dateTime), 'y': sensor_data})

def placeInDB(temps1,temps2,temps3, timeOfMessurment):
    db = dataset.connect('sqlite:///app.db')
    table = db['temp']
    temp1 = temps1
    temp2 = temps2
    temp3 = temps3
    table.insert(dict(temp1=temp1, temp2=temp2, temp3=temp3, dateAndTime=timeOfMessurment))

def inistalizeData():
    global largePotGeneation
    global stream_A
    global stream_B
    global stream_C
    global serialID

    serialID = collectMLX90614.open_serial_port()
    largePotGeneation = generateThreeTrace('./config.json')
    stream_A = creatStreamingGraph("DS18B20 1", './config.json',0)
    stream_B = creatStreamingGraph("DS18B20 2", './config.json',1)
    stream_C = creatStreamingGraph("MLX90614", './config.json',2)
    return largePotGeneation, stream_A,stream_B,stream_C

def creatDataPoint():
    #instad of calling random int i will use the functions the cody makes

    sensorName_a = "/sys/bus/w1/devices/28-0000055fd19b/w1_slave"
    sensorName_b = "/sys/bus/w1/devices/28-0000058955a2/w1_slave"
    temp1 = collectDS18B20.read_temperature(sensorName_a)
    temp2 = collectDS18B20.read_temperature(sensorName_b)
    temp3 = collectMLX90614.read_temperature(serialID)

    timeOfMessurment = datetime.now()
    timeOfMessurment = timeOfMessurment.replace(microsecond=0)
    placeInDB(temp1,temp2,temp3,timeOfMessurment)
    addPointToStreamingGraph(timeOfMessurment, temp1, stream_A)
    addPointToStreamingGraph(timeOfMessurment, temp2, stream_B)
    addPointToStreamingGraph(timeOfMessurment, temp3, stream_C)
    addPointToLargeStreamingGraph(largePotGeneation,timeOfMessurment,temp1,temp2,temp3)
    threading.Timer(10, creatDataPoint).start()
