from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rohak@123'
app.config['MYSQL_DB'] = 'sentiment_analysis'
mysql = MySQL(app)

from app import routes
