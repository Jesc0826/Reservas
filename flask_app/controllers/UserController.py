from flask_app import app
from flask_app.models.User import User
from flask import Response, session, request, session, render_template, url_for, redirect, jsonify
from flask_bcrypt import Bcrypt
import json
bcrypt = Bcrypt(app)

# Index users
@app.route('/users', methods = ['GET'])
def indexUsers():
    users = User.get()
    return render_template('pages/users/index.html', users = users)

# Show user
@app.route('/users/<id>', methods=['GET'])
def usersShow(id):
    user = (User.find(id))[0]
    response = {
        'id': user[0],
        'role': user[1],
        'first_name': user[2],
        'lastname': user[3],
        'email': user[4],
    }
    response = json.dumps(response)
    return Response(response, mimetype="application/json")

# Store user
@app.route('/users', methods = ['POST'])
def storeUsers():
    data = { 
        'first_name': request.form["first_name"],
        'role': request.form["role"],
        'lastname': request.form["lastname"],
        'email': request.form["email"],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    User.create(data)
    return redirect(url_for('indexUsers'))

# Update user
@app.route('/users/update/<id>', methods = ['POST'])
def updateUsers(id):
    first_name = request.form["first_name"]
    role = request.form["role"]
    lastname = request.form["lastname"]
    email = request.form["email"]
    password = request.form['password']

    if role and first_name and lastname and email:
        if password:
            hashed_password = bcrypt.generate_password_hash(request.form['password'])
        else:
            user = (User.find(id))[0]
            hashed_password = user[5]
        data = {
            'first_name': first_name,
            'role': role,
            'lastname': lastname,
            'email': email,
            'password': hashed_password
        }
        User.update(id, data)

    return redirect(url_for('indexUsers'))

# Delete user
@app.route('/users/delete/<id>', methods = ['POST'])
def deleteUsers(id):
    User.delete(id)
    return redirect(url_for('indexUsers'))