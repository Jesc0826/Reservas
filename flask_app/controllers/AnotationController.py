from __future__ import annotations
from flask_app import app
from flask_app.models.Anotation import Anotation
from flask_app.models.Reservation import Reservation
from flask import Response, session, request, session, render_template, url_for, redirect, jsonify

@app.route('/anotations/<reservation_id>', methods = ['GET'])
def indexaAnotations(reservation_id):
    reservation = Reservation.withField(reservation_id)
    anotationsTeamA = Anotation.getTeamA(reservation_id)
    anotationsTeamB = Anotation.getTeamB(reservation_id)
    nA = Anotation.getNA(reservation_id)
    nB = Anotation.getNB(reservation_id)
    print(nA)
    print(nB)
    return render_template('pages/home/user/anotations/index.html', anotationsTeamA = anotationsTeamA, anotationsTeamB = anotationsTeamB, nA = nA, nB = nB, reservation = reservation)

@app.route('/anotations', methods = ['POST'])
def storeAnotations():
    data = {
        "reservation_id": request.form['reservation_id'],
        "team": request.form['team'],
        "full_name": request.form['full_name']
    }
    Anotation.create(data)
    return redirect(request.referrer)





@app.route('/anotations/update/<id>', methods = ['POST'])
def updateAnotations(id):
    data = {
        "anotation_status": request.form['anotation_status'],
        "title": request.form['title'],
        "date_end": request.form['date_end']
    }
    Anotation.update(id, data)

    return redirect(url_for('indexanotations'))

@app.route('/anotations/delete/<id>', methods = ['GET'])
def deleteAnotations(id):
    Anotation.delete(id)
    return redirect(request.referrer)