- install virtualenv on ubuntu system
```bash
sudo apt-get install python3-venv
```
- create virtualenv on system
```sh
python3 -m venv my-project-env
```
- activate the environment
```sh
source my-project-env/bin/activate
```
- deactivate enevironment when work is done
```sh
deactivate
```
- install flask sqlalchamy for database
```sh
pip3 install flask-sqlalchemy
```
```python
from app import db
db.create_all()
```

- Important Links /check sqlite file data online
```
https://inloop.github.io/sqlite-viewer/
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#simple-relationships
```
- heroku deployment
```py
pip install gunicorn
pip freeze >requirements.txt
heroku login
git init
git add .
git commit -m "messsage"
heroku create todo-codewithkeshav
git push heroku master
```