from flask_app.config.MySqlConnection import mysql

class User:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.role = data['role']
        self.lastname = data['lastname']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def create(cls, data):
        cur = mysql.get_db().cursor()
        cur.execute("INSERT INTO users (first_name, role, lastname, email, password) VALUES (%s,%s,%s,%s,%s)", (data['first_name'], data['role'], data['lastname'], data['email'], data['password']))
        mysql.get_db().commit()

    @classmethod
    def getByEmail(cls, email):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT * FROM users WHERE email = %s', (email))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data

    @classmethod
    def get(cls):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT * FROM users')
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data
    
    @classmethod
    def count(cls):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT count(*) FROM users')
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data[0][0]

    @classmethod
    def find(cls, id):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT * FROM users WHERE id = %s', (id))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data
    
    @classmethod
    def update(cls, id, data):
        cur = mysql.get_db().cursor()
        cur.execute('UPDATE users SET role = %s, first_name = %s, lastname = %s, email = %s, password = %s WHERE id = %s', (data['role'], data['first_name'], data['lastname'], data['email'], data['password'], id))
        mysql.get_db().commit()
    
    @classmethod
    def delete(cls, id):
        cur = mysql.get_db().cursor()
        cur.execute('DELETE FROM users WHERE id = {0}'.format(id))
        mysql.get_db().commit()