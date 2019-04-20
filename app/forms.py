from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class Keyword(FlaskForm):
	keyword = StringField('Keyword', validators=[DataRequired()])
	true_response = StringField('Correct Response', validators=[DataRequired()])
	false_response = StringField('Incorrect Response', validators=[DataRequired()])
	submit1 = SubmitField('Submit Keyword')

class Broadcast(FlaskForm):
	broadcast_msg = StringField('Broadcast message:', validators=[DataRequired()])
	submit2 = SubmitField('Submit Broadcast')
	
class IndividualMsg(FlaskForm):
	individual_number = StringField('Individual number:', validators=[DataRequired()])    
	individual_msg = StringField('Individual message:', validators=[DataRequired()])
	submit3 = SubmitField('Submit Individual Message')
