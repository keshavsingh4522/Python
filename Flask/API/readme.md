```python
from flask import Flask,jsonify,request
```
- return result as in form of json
```py
return jsonify(message="great work",name="_name_here_")
```
- by default status code is 200 ok, above code will work same as below
```py
return jsonify(message="great work",name="_name_here_"),200
```
- catch the data wwhich is passed along with url
```py
app.route("/parameters")
def parameters():
	name=request.args.get("name")
	age=int(request.args.get("age"))
	if age<18:
		return jsonify(message="hi "+name+ ', you are not old,hence you are not able to accesss this page'),401
	# by default status code is 200 or ok 
	return jsonify(message="hello "+name+" you are old.")
```
- url parameters
```py
@app.route("/url_parameter/<string:name>/<int:age>")
# def url_parameter(name,age):  same work as below
def url_parameter(name:str,age:int):
	if age<18:
		return jsonify(message="hi "+name+ ', you are not old,hence you are not able to accesss this page'),401
	# by default status code is 200 or ok 
	return jsonify(message="hello "+name+" you are old.")
```
- [Flask + marshmallow for beautiful APIs(if jsonify will not work then use one more this)](https://flask-marshmallow.readthedocs.io/en/latest/)
```py

```

## Securing your web api with JWT(JSON Web Tokens)
```py
- pip3 install Flask-Login
- pip3 install Flask-User # role based

--- i used below
pip3 install flask-jwt-extended

```
-- for mail
```py
pip3 install Flask-Mail

```