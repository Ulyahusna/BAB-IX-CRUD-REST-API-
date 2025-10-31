from flask import Flask
import mysql.connector as mysql

app= Flask(__name__)

db = mysql.connect(
    host="localhost",       # ganti jika server database berbeda
    user="root",            # username MySQL kamu
    password="",            # isi password MySQL kamu
    database="flaskmysql" # nama database kamu
)

from app import routes
