import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

	ACCOUNT_KEY = os.environ.get('ACCOUNT_KEY') or 'ACf08c75f84fbdb276fe8189c5a7f61695'

	AUTH_TOKEN = os.environ.get('AUTH_TOKEN') or '30760298b870cf45f4d5c0d0272ebbc7'

	TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER') or '+12133400467'
	                 
	MY_TEST_NUMBER = os.environ.get('MY_TEST_NUMBER') or '+13235401388'

	SQLALCHEMY_DATABASE_URI = 'postgresql://nikitaparmar:@localhost:5432/testdb'

	SQLALCHEMY_TRACK_MODIFICATIONS = True

	#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True