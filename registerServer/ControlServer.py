from flask import Flask, redirect, render_template, request, session, url_for
import os

from registerServer import Configuration
from registerServer.Database import Database

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index2', methods=['GET', 'POST'])
def loginpage():

    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/index3', methods=['GET', 'POST'])
def registerpage():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('registerPage.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if Database(request.form['name'], request.form['password'], request.form['email']).checkuserReg() is True:
        if Configuration.Configuration.emailUserCount == True:
            Configuration.Configuration.emailUserCount = False
            return render_template('userEmailExists.html')
        return render_template('userExists.html')
    else:
        if Database(request.form['name'], request.form['password'], request.form['email']).addUser() is True:
            return render_template('awaitingConfirmation.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.form['password'] == '12shroot' and request.form['name'] == 'administrator':
        session['logged_in'] = True
        return render_template('admin.html')
    else:
        if Database(request.form['name'], request.form['password'], "").checkForUserPassword() is True:
            session['logged_in'] = True
            return render_template('downloadPage.html')
        else:
            return render_template('userDoesNotExist.html')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":

    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
