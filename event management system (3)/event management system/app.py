from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '9865'  # Replace with your actual password
app.config['MYSQL_DB'] = 'event_db'  # Updated database name for events
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/events')
def events():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM eventdetails")  # Fetch all events
    event_info = cur.fetchall()
    cur.close()
    return render_template('events.htm', events=event_info)

@app.route('/search', methods=['POST', 'GET'])
def search():
    search_results = []
    if request.method == "POST":
        search_term = request.form.get('eventid')  # Get event ID from form
        cur = mysql.connection.cursor()
        query = "SELECT * FROM eventdetails WHERE id LIKE %s"
        cur.execute(query, ('%' + search_term + '%',))
        search_results = cur.fetchall()
        cur.close()
        return render_template('events.htm', events=search_results)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        id_data = request.form.get('eventid')  # Get event ID
        name = request.form.get('name')       # Get event name
        date = request.form.get('date')       # Get event date
        location = request.form.get('location')  # Get event location

        # Check if all fields are provided
        if not all([id_data, name, date, location]):
            return render_template('events.htm', error="All fields are required.")

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO eventdetails (id, name, date, location) VALUES (%s, %s, %s, %s)",
                    (id_data, name, date, location))
        mysql.connection.commit()
        return redirect(url_for('events'))

@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM eventdetails WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('events'))

@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form.get('eventid')  # Get event ID
        name = request.form.get('name')       # Get event name
        date = request.form.get('date')       # Get event date
        location = request.form.get('location')  # Get event location

        # Check if all fields are provided
        if not all([id_data, name, date, location]):
            return render_template('events.htm', error="All fields are required for update.")

        cur = mysql.connection.cursor()
        cur.execute("UPDATE eventdetails SET name=%s, date=%s, location=%s WHERE id=%s",
                    (name, date, location, id_data))
        mysql.connection.commit()
        return redirect(url_for('events'))

if __name__ == "__main__":
    app.run(debug=True)
