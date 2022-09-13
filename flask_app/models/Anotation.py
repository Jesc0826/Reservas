from flask_app.config.MySqlConnection import mysql

class Anotation:
    def __init__(self, data):
        self.reservation_id = data['reservation_id']
        self.team = data['team']
        self.full_name = data['full_name']

    @classmethod
    def create(cls, data):
        cur = mysql.get_db().cursor()
        cur.execute("INSERT INTO anotations (reservation_id, team, full_name) VALUES (%s,%s,%s)", (data['reservation_id'], data['team'], data['full_name']))
        mysql.get_db().commit()

    @classmethod
    def get(cls):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT * FROM anotations')
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data
    
    @classmethod
    def getByReservation(cls, reservation_id):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT * FROM anotations WHERE reservation_id = %s', (reservation_id))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data
    
    @classmethod
    def getTeamA(cls, reservation_id):
        cur = mysql.get_db().cursor()
        cur.execute("SELECT * FROM anotations WHERE reservation_id = %s AND team = 'A'", (reservation_id))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data

    @classmethod
    def getTeamB(cls, reservation_id):
        cur = mysql.get_db().cursor()
        cur.execute("SELECT * FROM anotations WHERE reservation_id = %s AND team = 'B'", (reservation_id))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data
    
    @classmethod
    def getNA(cls, reservation_id):
        cur = mysql.get_db().cursor()
        cur.execute("SELECT count(*) FROM anotations WHERE reservation_id = %s AND team = 'A'", (reservation_id))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data[0][0]

    @classmethod
    def getNB(cls, reservation_id):
        cur = mysql.get_db().cursor()
        cur.execute("SELECT count(*) FROM anotations WHERE reservation_id = %s AND team = 'B'", (reservation_id))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data[0][0]

    @classmethod
    def find(cls, id):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT * FROM anotations WHERE id = %s', (id))
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data
    
    @classmethod
    def update(cls, id, data):
        cur = mysql.get_db().cursor()
        cur.execute('UPDATE anotations SET reservation_id = %s, team = %s, full_name = %s WHERE id = %s', (data['reservation_id'], data['team'], data['full_name'], id))
        mysql.get_db().commit()
    
    @classmethod
    def delete(cls, id):
        cur = mysql.get_db().cursor()
        cur.execute('DELETE FROM anotations WHERE id = {0}'.format(id))
        mysql.get_db().commit()

    @classmethod
    def count(cls):
        cur = mysql.get_db().cursor()
        cur.execute('SELECT count(*) FROM anotations')
        data = cur.fetchall()
        cur.close()
        mysql.get_db().commit()

        return data[0][0]