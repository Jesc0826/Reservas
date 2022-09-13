from flask_app import app
from flaskext.mysql import MySQL

# Mysql Settings
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Jesc1997.'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1' # localhost
app.config['MYSQL_DATABASE_DB'] = 'reservas'

# MySQL Connection
mysql = MySQL()
mysql.init_app(app)