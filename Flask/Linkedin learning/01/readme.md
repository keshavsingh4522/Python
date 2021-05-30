- Configuring the flask
```text
- create a project folder
- create a virtual environment
- install flask to virtual environment
- setup environment vairiables
- install the flask wrf-extension
- create requirements.txt file to track all dependencies

```

- create folder enrollment
- create virtual environmen and activate it
- install the package here in this environment
```bash
pip3 install Flask
pip3 install flask-wtf
```
- .flaskenv file in your project folder for storing environment variable
- to use .env and .flaskenv file install below package
```bash
pip3 install python-dotenv
```
- install all package from file
```bash
pip3 install -r requirements.txt
```
- to run we have below two methods
```sh
python3 main.py

    OR

flask run
```

- include
```text
- this adds pages to another pages

{% include "/includes/footer.html" %}
```

- {{url_for()}}
```text
- it can be for files
  <link rel="stylesheet" type="text/css" href="{{url_for('static',filename='css/main.css')}}">
- it can be point to routes function name 
      <li><a href="{{url_for('courses')}}">Courses</a></li>
```
- inherit the page using extends jinja syntax
```js
{% extends "_Layout.html" %}
```
- we can block content, see below
```html
{% block content %}
  
{% endblock %}

{{ self.content() }}

```
- request and  response
```py
# args
request.args.get('<field name>')
request.args['<field name>']

# forms
request.form.get('<field name>')
request.form['<field name>']
```