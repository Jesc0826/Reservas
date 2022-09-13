from flask_app import app

from flask_app.controllers import AuthController
from flask_app.controllers import HomeController
from flask_app.controllers import UserController
from flask_app.controllers import FieldController
from flask_app.controllers import ReservationController
from flask_app.controllers import AnotationController

if __name__ == "__main__":
    app.run(debug = True)