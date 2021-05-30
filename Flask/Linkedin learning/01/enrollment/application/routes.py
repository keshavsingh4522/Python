from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
	return render_template("index.html",index=True)


@app.route("/courses")
def courses():
	data=[{'id':1,'title':'html','description':'html for frontend','credits':'html rtr','term':'fr'},
	{'id':2,'title':'css','description':'css for frontend','credits':'css ffd','term':'ffff'},
	{'id':3,'title':'javascript','description':'its javascript not java','credits':'javascrtip gfh','term':'trtr'},
	{'id':4,'title':'python','description':'python very easy to learn','credits':'python tt','term':'ghf'}]s
	return render_template("courses.html",courses=True,courseData=data)


@app.route("/login")
def login():
	return render_template("login.html",login=True)

@app.route("/register")
def register():
	return render_template("register.html",register=True)