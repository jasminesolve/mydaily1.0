from flask import Flask
app = Flask(__name__)


#login page
@app.route('/')
@app.route('/mydaily')
def logIn():
    return 'Login here.'

#show user's calender
@app.route('/mydaily/calendar/')

#create a new day
@app.route('/mydaily/newday/')
def newDay():
    print('Create a new day.')
    return

#enter specific day
@app.route('/mydaily/<int:date_id>/')
def theDay():
    print('This is the day.')
    return

#delete a day
@app.route('/mydaily/<int:date_id>/delete/')
def deleteDay():
    print('Delete the day.')
    return

#add a time
@app.route('/mydaily/<int:date_id>/newtime/')
def addTime():
    print('Add a time here.')
    return

#edit a time
@app.route('/mydaily/<int:date_id>/<int:time_id>/edit/')
def editTime():
    print('Eddit time here.')
    return

#delete a time
@app.route('/mydaily/<int:date_id>/<int:time_id>/delete/')
def deleteTime():
    print('Delete a time here.')
    return


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=5000)
