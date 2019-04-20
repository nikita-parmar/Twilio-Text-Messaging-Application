from app import app
from flask import render_template, flash, redirect,request
from app.forms import Keyword
from app.forms import Broadcast
from app.forms import IndividualMsg
from app import db
from app.config import Config
from app.models import Keywords,Numbers
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse


@app.route('/',methods=['GET', 'POST'])
@app.route('/index',methods=['GET', 'POST'])
def index():
	form = Keyword()
	if form.validate_on_submit():
		#Delete all previous keywords
		allrows = Keywords.query.all()
		for arow in allrows:
			db.session.delete(arow)

		#Insert new keyword
		row = Keywords(key=form.keyword.data, correct_resp=form.true_response.data, incorrect_resp=form.false_response.data)   
		
		db.session.add(row)
		db.session.commit()

		print('Keyword {}, resp1={}, resp2 = {}'.format(form.keyword.data, form.true_response.data, form.false_response.data))
		flash('Keyword {}, resp1={}, resp2 = {}'.format(form.keyword.data, form.true_response.data, form.false_response.data))
		return render_template('index.html', title='Keyword Updated', form=form)

	return render_template('index.html', title='', form=form)


@app.route('/broadcast',methods=['GET', 'POST'])
def broadcast():
	form = Broadcast()
	conf = Config()
	if form.validate_on_submit():
		flash('Broadcast Msg {}'.format(form.broadcast_msg.data))

		allnum = Numbers.query.all()
		for anum in allnum:
			print(anum.number)
			client = Client(conf.ACCOUNT_KEY, conf.AUTH_TOKEN)
			message = client.messages \
				.create(
				     body=form.broadcast_msg.data,
				     from_=conf.TWILIO_NUMBER,
				     to=anum.number
				 )
		return render_template('broadcast.html', title='Broadcast Sent', form=form)

	return render_template('broadcast.html', title='', form=form)




@app.route('/amessage',methods=['GET', 'POST'])
def amessage():
	form = IndividualMsg()
	if form.validate_on_submit():
		row = Numbers.query.filter_by(number=form.individual_number.data).first()
		if row is not None:
			conf = Config()
			client = Client(conf.ACCOUNT_KEY, conf.AUTH_TOKEN)
			message = client.messages \
					.create(
					body=form.individual_msg.data,
					from_=conf.TWILIO_NUMBER,
					to=form.individual_number.data 
					)
			return render_template('amessage.html', title='Individual Message Sent', form=form)
		else:
			print("User is not registered")
			return render_template('amessage.html', title='Individual Message Sent', form=form)

	return render_template('amessage.html', title='', form=form)


@app.route('/temp')
def temp():
	return "Hello, World!"


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
	body = request.values.get('Body', None)
	print(request.values)
	print(request.values.get('From', None))

	allkeywords = Keywords.query.all()
	resp = MessagingResponse()
	
	for akeyword in allkeywords:
		if akeyword.key == body:
			#Send correct response message
			flag = 0
			allnum = Numbers.query.all()
			#if user is already registered
			for anum in allnum:
				if anum.number == request.values.get('From', None):
					resp.message(akeyword.correct_resp)
					flag = 1
					break
			#if it is a new user
			if flag == 0:
				row = Numbers(number=request.values.get('From', None))   
				db.session.add(row)
				db.session.commit()
				resp.message(akeyword.correct_resp)
		#incorrect keyword
		else:			
			resp.message(akeyword.incorrect_resp)

	return str(resp)
	

