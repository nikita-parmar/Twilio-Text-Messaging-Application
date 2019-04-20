# Create our database model
#from migrate import db
from app import db

class Numbers(db.Model):
    number = db.Column(db.String(15), primary_key=True)

# class Phone_NumbersSchema(ma.Schema):
# 	number = fields.String(required=True)

class Keywords(db.Model):
	key = db.Column(db.String, primary_key=True)
	correct_resp = db.Column(db.String)
	incorrect_resp = db.Column(db.String)
   

# class KeywordScehma(ma.Schema):
# 	key = fields.String(required=True)
# 	correct_resp = fields.String(required=True)
# 	incorrect_resp = fields.String(required=True)

   
