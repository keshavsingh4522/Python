from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,Float,String
import os
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager,jwt_required,create_access_token
from flask_mail import Mail,Message

app=Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,"planets.db")
app.config['JWT_SECRET_KEY']='super secret' # chenge this in real life

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = ''
# app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = ''
# app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
mail=Mail(app)

# Start
@app.cli.command("db_create")
def db_create():
	db.create_all()
	print("databse created")

@app.cli.command("db_drop")
def db_drop():
	db.drop_all()
	print("databse droped")

'''
seeding databse
'''
@app.cli.command("db_seed")
def db_seed():
	mercury = Planet(
		planet_name='Mercury',
		planet_type='Class D',
		home_star='Sol',
		mass=2.258e23,
		radius=1516,
		distance=35.98e6)
	venus = Planet(
		planet_name='Venus',
		planet_type='Class K',
		home_star='Sol',
		mass=4.867e24,
		radius=3760,
		distance=67.24e6)
	earth = Planet(
		planet_name='Earth',
		planet_type='Class M',
		home_star='Sol',
		mass=5.972e24,
		radius=3959,
		distance=92.96e6)
	db.session.add(mercury)
	db.session.add(venus)
	db.session.add(earth)

	test_user = User(first_name='William',
                     last_name='Herschel',
                     email='test@test.com',
                     password='P@ssw0rd')
	db.session.add(test_user)
	db.session.commit()
	print("databse seeded!")

# End



@app.route("/",methods=["GET"])
def hello_world():
	return jsonify( message ="hi this is looking awesome"),200

@app.route("/<int:id>",methods=["GET"])
def hello(id):
	return jsonify(message=f"hi you entered the number is {id}"),400


@app.route("/parameters")
def parameters():
	name=request.args.get("name")
	age=int(request.args.get("age"))
	if age<18:
		return jsonify(message="hi "+name+ ', you are not old,hence you are not able to accesss this page'),401
	# by default status code is 200 or ok 
	return jsonify(message="hello "+name+" you are old.")


@app.route("/url_parameter/<string:name>/<int:age>")
# def url_parameter(name,age):  same work as below
def url_parameter(name:str,age:int):
	if age<18:
		return jsonify(message="hi "+name+ ', you are not old,hence you are not able to accesss this page'),401
	# by default status code is 200 or ok 
	return jsonify(message="hello "+name+" you are old.")



##
@app.route("/planets",methods=["GET"])
def planets():
	planet_list=Planet.query.all()
	result = planets_schema.dump(planet_list)
	return jsonify(result)
	# return jsonify(data=planet_list)

@app.route("/register",methods=["POST"])
def register():
	email=request.form['email']
	test=User.query.filter_by(email=email).first()
	if test:
		return jsonify(message="email is already exist!"),409

	first_name=request.form['first_name']
	last_name=request.form['last_name']
	password=request.form['password']
	db.session.add(User(first_name=first_name,last_name=last_name,email=email,password=password))
	db.session.commit()
	return jsonify(message="user Created Successfully!"),201


@app.route("/login",methods=["POST"])
def login():
	# api==json, or form
	if request.is_json:
		# if user is trying to login via api
		email=request.json['email']
		password=request.json['password']
	else:
		# if user is logging via form
		email=request.form['email']
		password=request.form['password']
	test=User.query.filter_by(email=email,password=password).first()
	if test:
		# create token
		access_token=create_access_token(identity=email)
		return jsonify(message="login Successfully!",access_token=access_token)
	else:
		return jsonify(message="bad password or email"),401


@app.route("/retrieve_password/<string:email>",methods=["GET"])
def retrieve_password(email:str):
	user = User.query.filter_by(email=email).first()
	if user:
		msg = Message(
			"Your planetry api password is "+user.password,
			sender="admin@planatry-api.com",
			recipients=[email])
		mail.send(msg)
		return jsonify(message="password sent to "+email)
	else:
		return jsonify(message=email+" email doesn't exist!"),401


@app.route("/planet_details/<int:planet_id>",methods=["GET"])
def planet_details(planet_id:int):
	planet = Planet.query.filter_by(planet_id=planet_id).first()
	if planet:
		result = planet_schema.dump(planet)
		return jsonify(result)
	else:
		return jsonify(message="that planet does not exist!"),404


@app.route("/add_planet",methods=["POST"])
@jwt_required()
def add_planet():
	planet_name= request.form['planet_name']
	planet = Planet.query.filter_by(planet_name=planet_name).first()
	if planet:
		return jsonify(message="the planet is exists already!"),409
	else:
		planet_type=request.form['planet_type']
		home_star=request.form['home_star']
		mass=request.form['mass']
		radius=request.form["radius"]
		distance=request.form["distance"]
		db.session.add(Planet(planet_name=planet_name,planet_type=planet_type,home_star=home_star,mass=mass,radius=radius,distance=distance))
		db.session.commit()
		return jsonify(message="You added a planet Successfully!"),201


@app.route("/update_planet",methods=["PUT"])
@jwt_required()
def update_planet():
	planet_id= request.form['planet_id']
	planet = Planet.query.filter_by(planet_id=planet_id).first()
	if planet:
		planet.planet_name=request.form['planet_name']
		planet.planet_type=request.form['planet_type']
		planet.home_star=request.form['home_star']
		planet.mass=request.form['mass']
		planet.radius=request.form["radius"]
		planet.distance=request.form["distance"]
		db.session.commit()
		return jsonify(message="You updated a planet Successfully!"),202
	else:
		return jsonify(message="the planet does not exists!"),404



@app.route("/remove_planet/<int:planet_id>",methods=["DELETE"])
@jwt_required()
def remove_planet(planet_id:int):
	planet = Planet.query.filter_by(planet_id=planet_id).first()
	if planet:
		db.session.delete(planet)
		db.session.commit()
		return jsonify(message="You deleted a planet Successfully!"),202
	else:
		return jsonify(message="the planet does not exists!"),404

# Databse Models
class User(db.Model):
	__tablename__="User"
	id=Column(Integer,primary_key=True)
	first_name=Column(String)
	last_name=Column(String)
	email=Column(String,unique=True)
	password=Column(String)

class Planet(db.Model):
	planet_id = Column(Integer,primary_key=True)
	planet_type=Column(String)
	planet_name=Column(String)
	home_star=Column(String)
	mass=Column(Float)
	radius=Column(Float)
	distance=Column(Float)

class UserSchema(ma.Schema):
	class Meta:
		fields=("id","first_name","last_name","email","password")

class PlanetSchema(ma.Schema):
	class Meta:
		fields=("planet_id","planet_type","planet_name","home_star","mass","radius","distance")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)





if __name__=="__main__":
	app.run(debug=True)