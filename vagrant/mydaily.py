from flask import Flask,render_template
from data import Day
app = Flask(__name__)

Things = Day()

#login page
@app.route('/')
@app.route('/mydaily')
def logIn():
    return render_template('Home.html')

#show user's calender
@app.route('/mydaily/calendar/')

#create a new day
@app.route('/mydaily/newday/')
def newDay():
    return 'Create a new day.'

#enter specific day
@app.route('/mydaily/<int:date_id>/')
def theDay(date_id):
    return render_template('theDay.html',things=Things,Did=date_id)

#delete a day
@app.route('/mydaily/<int:date_id>/delete/')
def deleteDay():
    return 'Delete the day.'

#add a time
@app.route('/mydaily/<int:date_id>/newtime/')
def addTime():
    return 'Add a time here.'

#edit a time
@app.route('/mydaily/<int:date_id>/<int:time_id>/edit/')
def editTime():
    return 'Eddit time here.'

#delete a time
@app.route('/mydaily/<int:date_id>/<int:time_id>/delete/')
def deleteTime():
    return 'Delete a time here.'


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=5000)
