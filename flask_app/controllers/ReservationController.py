from flask_app import app
from flask_app.models.Field import Field
from flask_app.models.User import User
from flask_app.models.Reservation import Reservation
from flask import Response, session, request, session, render_template, url_for, redirect, jsonify
from flask_bcrypt import Bcrypt
import json
bcrypt = Bcrypt(app)

# Index reservations
@app.route('/reservations', methods = ['GET'])
def indexreservations():
    users = User.get()
    fields = Field.get()
    reservations = Reservation.get()
    return render_template('pages/reservations/index.html', reservations = reservations, users = users, fields = fields)

# Show reservation
@app.route('/reservations/<id>', methods=['GET'])
def reservationsShow(id):
    reservation = (reservation.find(id))[0]
    response = {
        'id': reservation[0],
        'user_id': reservation[1],
        'field_id': reservation[2],
        'start_at': reservation[3],
        'end_at': reservation[4]
    }
    response = json.dumps(response)
    return Response(response, mimetype="application/json")

# Store reservation
@app.route('/reservations', methods = ['POST'])
def storereservations():
    user =  request.form["user"]
    field = request.form["field"]
    start_at = request.form["start_at"]
    end_at =  request.form["end_at"]
    if user and field and start_at and end_at:
        print(Reservation.betweenDates(start_at, end_at, field))
        if Reservation.betweenDates(start_at, end_at, field) > 0:
            print(False)
            print(Reservation.betweenDates(start_at, end_at, field))
        else:
            data = {
                'user_id': request.form["user"],
                'field_id': request.form["field"],
                'start_at': request.form["start_at"],
                'end_at': request.form["end_at"]
            }
            Reservation.create(data)
    return redirect(request.referrer)

# Update reservation
@app.route('/reservations/update/<id>', methods = ['POST'])
def updatereservations(id):
    user =  request.form["user"]
    field = request.form["field"]
    start_at = request.form["start_at"]
    end_at =  request.form["end_at"]

    if user and field and start_at and end_at and id:
        data = {
            'user_id': user,
            'field_id': field,
            'start_at': start_at,
            'end_at': end_at
        }
        Reservation.update(id, data)

    return redirect(request.referrer)

# Delete reservation
@app.route('/reservations/delete/<id>', methods = ['POST'])
def deletereservations(id):
    Reservation.delete(id)
    return redirect(request.referrer)