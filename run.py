from app import app
from dataAcquisition import creatDataPoint, inistalizeData

streams = inistalizeData()

creatDataPoint(streams[0],streams[1],streams[2],streams[3])
app.run(debug = True, host ='0.0.0.0')
