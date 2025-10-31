from app import app, db 
from flask import jsonify, render_template

@app.route('/')
@app.route('/api/users')
def api_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

@app.route('/tabel')
def tampil_tabel():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    cursor.close()
    return render_template('table.html', data=data)