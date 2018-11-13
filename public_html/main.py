# -*- coding: utf-8 -*-
from flask import Flask, render_template,request,redirect,url_for
import flask
import flask_login
import psycopg2

app = flask.Flask(__name__)
app.secret_key = 'randomNyckel'

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

conn = psycopg2.connect(dbname="ag6946_mfdbv3", user="ag6946", password="jnblid5q", host="pgserver.mah.se")

cursor = conn.cursor()

# Denna fungerar "magiskt". Inget vi behöver gå in djupare på
class User(flask_login.UserMixin):
    pass

#ROUTES
@app.route('/', methods=["GET","POST"])
def start():
    #Databas username
    cursor.execute("select artikel.rubrik, artikel.ingress, artikel.datum from artikel order by artikel.datum desc limit 6;")
    artikel = cursor.fetchall()
    print(artikel)
    print(type(artikel))

    return render_template("index.html", artikel=artikel)

@app.route('/loggedIn')
def loggedIn():
    return render_template("loggedIn.html")

@app.route('/news')
def news():


    cursor.execute("select artikel.rubrik, artikel.ingress,  artikel.a_text, artikel.datum from artikel order by artikel.datum desc;")
    artikel = cursor.fetchall()

    cursor.execute("select * from artikel;")
    art = cursor.fetchall()

    cursor.execute("select * from skrivit;")
    skrivit = cursor.fetchall()

    cursor.execute("select * from forfattare;")
    forfattare = cursor.fetchall()

    cursor.execute("select * from bilder;")
    bilder = cursor.fetchall()

    forfCount = 0
    for a in art:
        for s in skrivit:
            if a[0] == s[0]:

                forfCount = forfCount + 1

                #cursor.execute("select forfattare.namn from forfattare where id=%s".format(s[1]))
                #forfs = cursor.fetchall()

                print("Artikel: " + a[1] + " Författare:" )
            else:
                pass
    print("Antal kopplingar: " + str(forfCount))


    return render_template("news.html", artikel=artikel)

@app.route('/images')
def images():
    cursor.execute("select namn, lank from bilder;")
    images = cursor.fetchall()
    return render_template("images.html", images=images)

@app.route('/add')
def add():

    return render_template("add.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")


#METHODS
@app.route('/logIn', methods=["POST"])
def logIn():

    #Från Form
    username = str(request.form["username"])
    password = str(request.form["psw"])
    #Databas username
    cursor.execute("select anv_namn from forfattare;")
    name = cursor.fetchall()
    #Databas Password
    cursor.execute("select losenord from forfattare;")
    word = cursor.fetchall()

    username_db = loopList(username, name)
    password_db = loopList(password ,word)

    right = "Du loggas nu in!"
    wrong = "Fel användarnamn eller lösenord!"
    print(username_db)
    print(password_db)

    if username_db == True:
        print(right)
        if password_db == True:
            print("Rätt lösenord!")
            return render_template("loggedIn.html", username=username)
        else:
            print("Fel lösenord!")
            return render_template("index.html", wrong=wrong)
    else:
        print("Fel användarnamn!")
        return render_template("index.html", wrong=wrong)

#FUNCTIONS
def loopList(key, words):
    for word in words:
        for i in word:
            if key == i:
                return True
            else:
                return False






app.run()
