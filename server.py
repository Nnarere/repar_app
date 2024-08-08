#pip install Flask
#pipenv install flask pymysql flask-bcrypt
#py server.py

from flask_app import app
from flask_app.controllers import user_controller
from flask_app.controllers import vehicle_controller


if __name__== "__main__":
    app.run(debug=True)