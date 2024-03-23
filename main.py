# bismillah

import sqlalchemy as db
from flask import Flask, render_template, request, redirect, url_for, session
import fetcher
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route('/', methods=['GET', 'POST'])
def home():
        if request.method == 'POST':
               username = session.get('username')
               articles = fetcher.fetchmain(request.form['topic'])
               return render_template('index.html', articles=articles, username=username)


        username = session.get('username')
        articles = fetcher.fetchmain()
        return render_template('index.html', articles=articles, username=username)



@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']

                if username == 'admin' and password == 'password':
                        session['username'] = username
                        return redirect(url_for('home'))
                else:
                        return 'Invalid username or password <a herf="/login">Try Again !!</a>'
        else:
                return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))
