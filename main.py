# Bismillah

from flask import Flask, render_template, request, redirect, url_for, session
import fetcher
import secrets
import db_connectivity

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route('/', methods=['GET', 'POST']) # homepage handling
def home():
        username = session.get('username')
        if request.method == 'POST':
               articles = fetcher.fetchmain(request.form['topic'])
               return render_template('index.html', articles=articles, username=username)

        articles = fetcher.fetchmain()
        return render_template('index.html', articles=articles, username=username)



@app.route('/login', methods=['GET', 'POST']) # loginpage handling
def login():
        if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']

                userStatus = db_connectivity.user_connect(username, password)

                if userStatus:
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

if __name__ == "__main__":
       app.run(host='0.0.0.0', port=8000)
