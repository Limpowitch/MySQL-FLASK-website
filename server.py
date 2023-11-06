from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__, static_url_path='/static')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '#Arbetare42'
app.config['MYSQL_DB'] = 'my_database'

mysql = MySQL(app)

@app.route('/users')
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return render_template('users.html', users=users)

@app.route("/")
def Mainpage():
    return render_template('home.html', url='/home')

@app.route('/about')
def about():
    return render_template('about.html', url='/about')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')