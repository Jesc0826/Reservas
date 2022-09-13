from flask_app import app
from flask import Response, session, request, session, render_template, url_for, redirect, jsonify
from flask_app.models.User import User
from flask_bcrypt import Bcrypt
import json
bcrypt = Bcrypt(app)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        if "user_id" in session:
            return redirect(url_for('index'))
        return render_template('login.html')
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        auxUser = User.getByEmail(email)
        user = auxUser[0]
        print (user)

        if user:
            if bcrypt.check_password_hash(user[5], password):
                session["user"] = user
                session["user_id"] = user[0]
                return redirect(url_for('index'))
            else:
                message = 'Contraseña incorrecta'
                return render_template('login.html', message = message)
        else:
            message = 'Usuario no registrado'
            return render_template('login.html', message = message)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == "GET":
        if "user_id" in session:
            return redirect(url_for('index'))
        return render_template('register.html')

    if request.method == "POST":
        if request.form["password"] == request.form["password_confirm"]:
            if len(request.form['password']) < 8:
                message = 'La contraseña debe tener mìnimo 8 caracteres'
                return render_template('register.html', message = message, type = "danger")
            data = {
                'first_name': request.form["first_name"],
                'role': 'user',
                'lastname': request.form["lastname"],
                'email': request.form["email"],
                'password': bcrypt.generate_password_hash(request.form['password'])
            }
            User.create(data)
            message = 'Usuario registrado satisfactoriamente'
            return render_template('register.html', message = message, type = "success")
        else:
            message = 'Las contraseñas no coinciden'
            return render_template('register.html', message = message, type = "warning")

@app.route('/logout', methods=['GET'])
def logout():
    if "user_id" in session:
        session.pop("user_id", None)
        return redirect(url_for('login'))
    return redirect(url_for('index'))