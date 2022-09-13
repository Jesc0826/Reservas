from flask_app.config.MySqlConnection import mysql

class Reservation:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.field_id = data['field_id']
        self.start_at = data['start_at']
        self.end_at = data['end_at']

    @classmethod
    def create(cls, data):
        cur = mysql.get_db().cursor()
        cur.execute("INSERT INTO reservations (user_id, field_id, start_at, end_at) VALUES (%s,%s,%s,%s)", (data['user_id'], data['field_id'], data['start_at'], data['end_at']))
        mysql.get_db().commit()

    @classmethod
    def get(cls):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT * FROM reservations')
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data
    
    @classmethod
    def getAll(cls):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT reservations.id, fields.name, reservations.start_at, reservations.end_at, fields.capacity FROM reservations JOIN fields ON fields.id = reservations.field_id')
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data

    @classmethod
    def find(cls, id):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT * FROM reservations WHERE id = %s', (id))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data
    
    @classmethod
    def update(cls, id, data):
        cur = mysql.get_db().cursor()
        cur.execute('UPDATE reservations SET user_id = %s, field_id = %s, start_at = %s, end_at = %s WHERE id = %s', (data['user_id'], data['field_id'], data['start_at'], data['end_at'], id))
        mysql.get_db().commit()
    
    @classmethod
    def delete(cls, id):
        cur = mysql.get_db().cursor()
        cur.execute('DELETE FROM reservations WHERE id = {0}'.format(id))
        mysql.get_db().commit()
    
    @classmethod
    def betweenDates(cls, start_at, end_at, field):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT count(*) FROM reservations WHERE field_id = %s AND start_at >= %s AND end_at < %s', (field, start_at, end_at))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data[0][0]
    
    @classmethod
    def getByUser(cls, user_id):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT reservations.id, fields.name, reservations.start_at, reservations.end_at, fields.capacity FROM reservations JOIN fields ON fields.id = reservations.field_id  WHERE user_id = %s', (user_id))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data
    
    @classmethod
    def withField(cls, reservation_id):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT reservations.id, fields.name, fields.capacity FROM reservations JOIN fields ON fields.id = reservations.field_id WHERE reservations.id = %s', (reservation_id))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data[0]

    @classmethod
    def count(cls):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT count(*) FROM reservations')
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data[0][0]