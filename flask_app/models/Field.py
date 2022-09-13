from flask_app.config.MySqlConnection import mysql

class Field:
    def __init__(self, data):
        self.name = data['name']
        self.capacity = data['capacity']

    @classmethod
    def create(cls, data):
        cur = mysql.get_db().cursor()
        cur.execute("INSERT INTO fields (name, capacity) VALUES (%s,%s)", (data['name'], data['capacity']))
        mysql.get_db().commit()

    @classmethod
    def get(cls):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT * FROM fields')
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data
    
    @classmethod
    def getByUser(cls, user_id):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT * FROM fields WHERE user_id = %s', (user_id))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data

    @classmethod
    def find(cls, id):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT * FROM fields WHERE id = %s', (id))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data
    
    @classmethod
    def update(cls, id, data):
        cur = mysql.get_db().cursor()
        cur.execute('UPDATE fields SET name = %s, capacity = %s WHERE id = %s', (data['name'], data['capacity'], id))
        mysql.get_db().commit()
    
    @classmethod
    def delete(cls, id):
        cur = mysql.get_db().cursor()
        cur.execute('DELETE FROM fields WHERE id = {0}'.format(id))
        mysql.get_db().commit()
    
    @classmethod
    def count(cls):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT count(*) FROM fields')
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data[0][0]