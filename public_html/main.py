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

    totList = []

    cursor.execute("select artikel.id, artikel.rubrik, artikel.ingress, artikel.a_text, artikel.datum from artikel order by artikel.datum desc;")
    artikel = cursor.fetchall()

    forfCount = 0
    for art in artikel:
        cursor.execute("select b.namn, b.lank from ((bilder as b join artikel_foto as p on b.id=p.bild_id) join artikel as a on a.id=p.artikel_id) where a.id= %s", (str(art[0])))
        bilder = cursor.fetchall()

        cursor.execute("select f.namn, f.efternamn from ((forfattare as f join skrivit as s on f.id=s.forfattar_id) join artikel as a on a.id=s.artikel_id) where a.id= %s", (str(art[0])))
        forfattare = cursor.fetchall()

        total = {
            "rubrik": art[1],
            "ingress": art[2],
            "text": art[3],
            "datum": art[4],
            "forfattare": forfattare,
            "bilder": bilder
        }

        totList.append(total)

        #TEST
    for t in totList:
        print("")
        print(t["rubrik"])
        for f in t["forfattare"]:
            print(f)
        for b in t["bilder"]:
            print(b)
        print("")


    return render_template("news.html", totList=totList)

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

    wrong = "Fel användarnamn eller lösenord!"
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
