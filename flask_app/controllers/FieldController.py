from flask_app import app
from flask_app.models.Field import Field
from flask import Response, session, request, session, render_template, url_for, redirect, jsonify
from flask_bcrypt import Bcrypt
import json
bcrypt = Bcrypt(app)

# Index fields
@app.route('/fields', methods = ['GET'])
def indexfields():
    fields = Field.get()
    return render_template('pages/fields/index.html', fields = fields)

# Show field
@app.route('/fields/<id>', methods=['GET'])
def fieldsShow(id):
    field = (Field.find(id))[0]
    response = {
        'id': field[0],
        'name': field[1],
        'capacity': field[2]
    }
    response = json.dumps(response)
    return Response(response, mimetype="application/json")

# Store field
@app.route('/fields', methods = ['POST'])
def storefields():
    data = { 
        'name': request.form["name"],
        'capacity': request.form["capacity"]
    }
    Field.create(data)
    return redirect(url_for('indexfields'))

# Update field
@app.route('/fields/update/<id>', methods = ['POST'])
def updatefields(id):
    name = request.form["name"]
    capacity = request.form["capacity"]

    if capacity and name and id:        
        data = {
            'name': name,
            'capacity': capacity
        }
        Field.update(id, data)

    return redirect(url_for('indexfields'))

# Delete field
@app.route('/fields/delete/<id>', methods = ['POST'])
def deletefields(id):
    Field.delete(id)
    return redirect(url_for('indexfields'))