# Bismillah
import os

from flask import Flask, render_template, request, redirect, url_for, session
import Handlers.fetcher as fetcher
import secrets
import Handlers.db_connectivity as db_connectivity

app = Flask(__name__, static_folder="uploads/")
app.secret_key = secrets.token_hex(16)


@app.route('/', methods=['GET', 'POST']) # homepage handling
def home():
        username = session.get('username')
        if request.method == 'POST':
               articles = fetcher.fetchmain(request.form['topic'])
               return render_template('index.html', articles=articles, username=username)

        articles = fetcher.fetchmain()
        return render_template('index.html', articles=articles, username=username)



@app.route('/login', methods=['GET', 'POST']) # login page handling
def login():
        if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']

                userStatus = db_connectivity.user_connect(username, password)

                if userStatus:
                        session['username'] = username
                        return redirect(url_for('home'))
                else:
                        return redirect(url_for('login'))
        else:
                return render_template('login.html')
        

@app.route('/signup', methods=['GET', 'POST']) # handles user signup
def signup():
       '''
       - pull data of the form and push to backend
       - add data to database (no need for checking for duplicates)
       - add username to cookie and redirect to homepage
       '''

       if request.method == 'POST':
              name = request.form['name']
              username = request.form['username']
              password = request.form['password']
              confirm_password = request.form['repassword']
              bio = request.form['bio']
              user_pfp = request.files['user_pfp']

              user_pfp.filename = user_pfp.filename.replace(' ', '_')
              user_pfp.save('uploads/pfps/' + user_pfp.filename)
              picture_name = user_pfp.filename

              if password and confirm_password != '' or None:
                     new_user_status = db_connectivity.add_user(username=username, password=password, name=name, pfp=picture_name, bio=bio)

                     if new_user_status:
                            session['username'] = username
                            return redirect(url_for('home'))
                     
                     else:
                            os.remove(f'uploads/pfps/{picture_name}')
                            return redirect(url_for('signup'))

       else:
              return render_template('signup.html')


@app.route('/logout') # logout handling
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/profile', methods=['GET']) # profile page handling
def profile():
       username = session.get('username')

       if username:
              user_written_articles = db_connectivity.retrive_user_articles(username=username)

              user_profile_data = db_connectivity.serve_profile_data(username=username)
              user_full_name, user_bio, user_pic = user_profile_data

              return render_template('profile.html', username=username, articles=user_written_articles, userFullName=user_full_name, userBio=user_bio, profilePic=user_pic)
       else:
              return redirect(url_for('login'))



@app.route('/submit_article', methods=['POST']) # handling user articles
def submit_article():
       username = session.get('username')
       if username:
              article_picture = request.files['article_picture']
              article_title = request.form['article_title']
              article_description = request.form['article_description']

              # saving article picture to uploads
              article_picture.filename = article_picture.filename.replace(' ', '_')
              article_picture.save('uploads/' + article_picture.filename)
              picture_name = article_picture.filename

              # Sending data to database
              db_connectivity.add_article(article_picture=picture_name, article_title=article_title, article_description=article_description, username=username)
              return redirect(url_for('profile'))

       else:
              return redirect(url_for('login'))


if __name__ == "__main__":
       app.debug = True
       app.run(host='0.0.0.0', port=8000)
