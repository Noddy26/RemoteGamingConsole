from flask import Flask, redirect, render_template, request, session, url_for
import os

from Configuration import Configuration
from Database import Database
from Methods.FileMethods import FileMethods

app = Flask(__name__)

@app.route('/')
def home():
    FileMethods.returnHTMLpageBack(Configuration.adminhtml, Configuration.adminhtmlbcakup)
    return render_template('index.html')


@app.route('/index2', methods=['GET', 'POST'])
def loginpage():
    FileMethods.returnHTMLpageBack(Configuration.adminhtml, Configuration.adminhtmlbcakup)
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/index3', methods=['GET', 'POST'])
def registerpage():
    FileMethods.returnHTMLpageBack(Configuration.adminhtml, Configuration.adminhtmlbcakup)
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('registerPage.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    FileMethods.returnHTMLpageBack(Configuration.adminhtml, Configuration.adminhtmlbcakup)
    if Database(request.form['name'], request.form['password'], request.form['email']).checkuserReg() is True:
        if Configuration.emailUserCount == True:
            Configuration.emailUserCount = False
            return render_template('userEmailExists.html')
        return render_template('userExists.html')
    else:
        if Database(request.form['name'], request.form['password'], request.form['email']).addUser() is True:
            return render_template('awaitingConfirmation.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    FileMethods.returnHTMLpageBack(Configuration.adminhtml, Configuration.adminhtmlbcakup)
    if request.form['password'] == Configuration.adminpassword and request.form['name'] == Configuration.adminusername:
        session['logged_in'] = True
        data = FileMethods.readfile(Configuration.userfilepath)
        newdata = FileMethods.replaceHTML(Configuration.adminhtml, data, " ")
        return render_template('admin.html', data=newdata)
    else:
        if Database(request.form['name'], request.form['password'], "").checkForUserPassword() is True:
            session['logged_in'] = True
            return render_template('downloadPage.html')
        else:
            return render_template('userDoesNotExist.html')


@app.route("/admin", methods=['GET', 'POST'])
def adminpage():
    count = 0
    data = FileMethods.readfile(Configuration.userfilepath)
    newdata = data.split("\n")
    for each in newdata:
        count = count + 1
    if count < count + 1:
        count += 1
        if request.method == 'POST':
            print(request.method)

@app.route("/logout")
def logout():
    FileMethods.returnHTMLpageBack(Configuration.adminhtml, Configuration.adminhtmlbcakup)
    session['logged_in'] = False
    return home()


if __name__ == '__main__':
    FileMethods.returnHTMLpageBack(Configuration.adminhtml, Configuration.adminhtmlbcakup)
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='192.168.0.103', port=3000)
