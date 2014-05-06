from app import app
from dataAcquisition import creatDataPoint, inistalizeData

inistalizeData()

creatDataPoint()
app.run(debug = True, host ='0.0.0.0')
