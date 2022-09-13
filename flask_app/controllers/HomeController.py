from flask_app import app
from flask import render_template, url_for, redirect, session
from flask_app.models.Reservation import Reservation
from flask_app.models.Field import Field
from flask_app.models.User import User

@app.route('/')
def index():
    if "user" in session:
        if session['user'][1] == 'admin':
            nUsers = User.count()
            nFields = Field.count()
            nReservations = Reservation.count()
            return render_template('pages/home/admin/index.html', nUsers = nUsers, nFields = nFields ,nReservations = nReservations, reservations = Reservation.getAll())
        if session['user'][1] == 'user':
            fields = Field.get()
            return render_template('pages/home/user/index.html', reservations = Reservation.getByUser(session['user'][0]), fields = fields)
    else:
        return redirect(url_for("login"))