from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class calibrate(Form):
    TrueSensorValue = TextField('TrueSensorValue', validators = [Required()])
