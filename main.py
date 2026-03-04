import flask, sqlite3

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('form.html')


@app.route('/search/', methods=['POST'])
def search():
    formData = flask.request.form

    location = formData['location']

    db = sqlite3.connect('equipment.db')

    cursor = db.execute(''' 
      SELECT SerialNumber, Type
      FROM Device
      WHERE WrittenOff = "FALSE"
      AND Location = ?
    ''', (location,))
    
    data = cursor.fetchall()
    
    db.close()

    return flask.render_template('table.html', data=data, location=location)


### only for running on repl.it
app.run('0.0.0.0', 8080)

### for running on your local machine, use this
#app.run()
