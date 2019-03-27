# -*- coding: utf-8 -*-
from flask import Flask, render_template,request,redirect,url_for
import flask
import flask_login
import psycopg2
import datetime

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
    cursor.execute("select artikel.id, artikel.rubrik, artikel.ingress, artikel.datum from artikel order by artikel.datum desc limit 6;")
    artikel = cursor.fetchall()

    totList = []

    for art in artikel:
        try:
            cursor.execute("select b.lank, p.bildnamn from ((bilder as b join artikel_foto as p on b.id=p.bild_id) join artikel as a on a.id=p.artikel_id) where a.id= %s", (str(art[0])))
            bild = cursor.fetchone()
        except:
            print("Finns ingen bild")
            bild = ("Ingen")

        mid =  "#modal" + str(art[0])
        modalId = "modal" + str(art[0])
        lank = "/artikel/" + str(art[0])


        try:
            cursor.execute("select p.bildnamn, b.lank from ((bilder as b join artikel_foto as p on b.id=p.bild_id) join artikel as a on a.id=p.artikel_id) where a.id= %s", (str(art[0])))
            bilder = cursor.fetchall()
        except:
            bilder = ("Ingen")

        try:
            cursor.execute("select f.namn, f.efternamn from ((forfattare as f join skrivit as s on f.id=s.forfattar_id) join artikel as a on a.id=s.artikel_id) where a.id= %s", (str(art[0])))
            forfattare = cursor.fetchall()

        except:
            forfattare = ["Ingen", "Forfattare"]


        total = {
            "rubrik": art[1],
            "ingress": art[2],
            "datum": art[3],
            "bilden": bild,
            "bilder": bilder,
            "mId": mid,
            "modalId":modalId,
            "forfattare": forfattare,
            "lank": lank
        }
        totList.append(total)

    return render_template("index.html", artikel=artikel, totList=totList)

@app.route('/loggedIn')
def loggedIn():
    return render_template("loggedIn.html")

@app.route('/news')
def news():

    totList = []

    cursor.execute("select artikel.id, artikel.rubrik, artikel.ingress, artikel.a_text, artikel.datum from artikel order by artikel.datum desc;")
    artikel = cursor.fetchall()

    for art in artikel:
        #Lägg till , p.bildtext efter selecten
        try:
            cursor.execute("select p.bildnamn, b.lank from ((bilder as b join artikel_foto as p on b.id=p.bild_id) join artikel as a on a.id=p.artikel_id) where a.id= %s", (str(art[0])))
            bilder = cursor.fetchall()
        except:
            bilder = ("Ingen")
        try:
            cursor.execute("select f.namn, f.efternamn from ((forfattare as f join skrivit as s on f.id=s.forfattar_id) join artikel as a on a.id=s.artikel_id) where a.id= %s", (str(art[0])))
            forfattare = cursor.fetchall()

        except:
            forfattare = ["Ingen", "Forfattare"]
        total = {
            "rubrik": art[1],
            "ingress": art[2],
            "text": art[3],
            "datum": art[4],
            "forfattare": forfattare,
            "bilder": bilder
        }
        totList.append(total)

    return render_template("news.html", totList=totList)

@app.route('/images')
def images():
    cursor.execute("select lank from bilder;")
    images = cursor.fetchall()
    return render_template("images.html", images=images)

@app.route('/add')
def add():
    cursor.execute("select namn, efternamn, id from forfattare;")
    forfattare = cursor.fetchall()

    cursor.execute("select lank, bnamn, id from bilder;")
    bilder = cursor.fetchall()

    cursor.execute("select id, rubrik from artikel;")
    artikel = cursor.fetchall()

    return render_template("add.html", forfattare=forfattare, bilder=bilder, artikel=artikel)

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
        if password_db == True:
            print("Rätt lösenord!")
            return render_template("loggedIn.html", username=username)
        else:
            print("Fel lösenord!")
            return render_template("index.html", wrong=wrong)
    else:
        print("Fel användarnamn!")
        return render_template("index.html", wrong=wrong)

@app.route('/addArticle', methods=["POST"])
def addArticle():
    rubrik = str(request.form["rubrik"])
    ingress = str(request.form["ingress"])
    a_text = str(request.form["a_text"])
    datum = str(request.form["date"])

    try:
        cursor.execute("INSERT INTO artikel (rubrik, ingress, a_text, datum)VALUES(%s, %s, %s, %s)", (rubrik, ingress, a_text, datum))
        conn.commit()
    except:
        print("Error till db!")

    totList = []

    cursor.execute("select artikel.id, artikel.rubrik, artikel.ingress, artikel.a_text, artikel.datum from artikel order by artikel.datum desc;")
    artikel = cursor.fetchall()

    for art in artikel:
        #Lägg till , p.bildtext efter selecten
        try:
            cursor.execute("select p.bildnamn, b.lank from ((bilder as b join artikel_foto as p on b.id=p.bild_id) join artikel as a on a.id=p.artikel_id) where a.id= %s", (str(art[0])))
            bilder = cursor.fetchall()
        except:
            bilder = ("Ingen")
        try:
            cursor.execute("select f.namn, f.efternamn from ((forfattare as f join skrivit as s on f.id=s.forfattar_id) join artikel as a on a.id=s.artikel_id) where a.id= %s", (str(art[0])))
            forfattare = cursor.fetchall()

        except:
            forfattare = ["Ingen", "Forfattare"]

        total = {
            "rubrik": art[1],
            "ingress": art[2],
            "text": art[3],
            "datum": art[4],
            "forfattare": forfattare,
            "bilder": bilder
        }
        totList.append(total)

    return render_template("news.html", totList=totList)


@app.route('/addImage', methods=["POST"])
def addImage():
    bnamn = str(request.form["bnamn"])
    lank = str(request.form["bild"])

    try:
        cursor.execute("INSERT INTO bilder (bnamn, lank) VALUES(%s, %s)", (bnamn, lank))
        conn.commit()
    except:
        print("Error till db!")

    cursor.execute("select lank from bilder;")
    images = cursor.fetchall()

    return render_template("images.html",images=images)

@app.route('/addAuthor', methods=["POST"])
def addAuthor():
    anv_namn = str(request.form["email"])
    losenord = str(request.form["losenord"])
    namn = str(request.form["namn"])
    efternamn = str(request.form["efternamn"])
    telefon = str(request.form["telefon"])


    try:
        cursor.execute("INSERT INTO forfattare (anv_namn, losenord, namn, efternamn, telefon)VALUES(%s, %s, %s, %s, %s)", (anv_namn, losenord, namn, efternamn, telefon))
        conn.commit()
    except:
        print("Error till db!")

    cursor.execute("select namn, efternamn, id from forfattare;")
    forfattare = cursor.fetchall()

    cursor.execute("select bnamn, lank, id from bilder;")
    bilder = cursor.fetchall()

    cursor.execute("select id, rubrik from artikel;")
    artikel = cursor.fetchall()

    return render_template("add.html", forfattare=forfattare, bilder=bilder, artikel=artikel)

@app.route('/connectForf', methods=["POST"])
def connectForf():
    art_id = request.form["art_id"]
    forf_id = request.form["forf_id"]

    try:
        cursor.execute("INSERT INTO skrivit (artikel_id, forfattar_id)VALUES(%s, %s)", (art_id, forf_id))
        conn.commit()
    except:
        print("Error till db!")


    totList = []

    cursor.execute("select artikel.id, artikel.rubrik, artikel.ingress, artikel.a_text, artikel.datum from artikel order by artikel.datum desc;")
    artikel = cursor.fetchall()

    for art in artikel:
        #Lägg till , p.bildtext efter selecten
        try:
            cursor.execute("select p.bildnamn, b.lank from ((bilder as b join artikel_foto as p on b.id=p.bild_id) join artikel as a on a.id=p.artikel_id) where a.id= %s", (str(art[0])))
            bilder = cursor.fetchall()
        except:
            bilder = ("Ingen")
        try:
            cursor.execute("select f.namn, f.efternamn from ((forfattare as f join skrivit as s on f.id=s.forfattar_id) join artikel as a on a.id=s.artikel_id) where a.id= %s", (str(art[0])))
            forfattare = cursor.fetchall()

        except:
            forfattare = ["Ingen", "Forfattare"]
        total = {
            "rubrik": art[1],
            "ingress": art[2],
            "text": art[3],
            "datum": art[4],
            "forfattare": forfattare,
            "bilder": bilder
        }
        totList.append(total)

    return render_template("news.html", totList=totList)


@app.route('/connectImage', methods=["POST"])
def connectImage():
    art_id = request.form["artbild"]
    bild_id = request.form["bildart"]
    bildnamn = request.form["bildnamn"]

    try:
        cursor.execute("INSERT INTO artikel_foto (artikel_id, bild_id, bildnamn)VALUES(%s, %s, %s)", (art_id, bild_id, bildnamn))
        conn.commit()
    except:
        print("Error till db!")

    totList = []

    cursor.execute("select artikel.id, artikel.rubrik, artikel.ingress, artikel.a_text, artikel.datum from artikel order by artikel.datum desc;")
    artikel = cursor.fetchall()

    for art in artikel:
        #Lägg till , p.bildtext efter selecten
        try:
            cursor.execute("select p.bildnamn, b.lank from ((bilder as b join artikel_foto as p on b.id=p.bild_id) join artikel as a on a.id=p.artikel_id) where a.id= %s", (str(art[0])))
            bilder = cursor.fetchall()
        except:
            bilder = ("Ingen")
        try:
            cursor.execute("select f.namn, f.efternamn from ((forfattare as f join skrivit as s on f.id=s.forfattar_id) join artikel as a on a.id=s.artikel_id) where a.id= %s", (str(art[0])))
            forfattare = cursor.fetchall()

        except:
            forfattare = ["Ingen", "Forfattare"]

        total = {
            "rubrik": art[1],
            "ingress": art[2],
            "text": art[3],
            "datum": art[4],
            "forfattare": forfattare,
            "bilder": bilder
        }
        totList.append(total)

    return render_template("news.html", totList=totList)



# Sida där de olika anteckningarna visas.
@app.route('/artikel/<artikel_id>')
def artikel(artikel_id):
    # Hämtar vilken lektion det var man klickade in på.
    #sql_lecture = "SELECT artikel, moment, datum FROM artikel WHERE id = %s"
    #cursor.execute (sql_lecture, [artikel_id])

    totList = []

    cursor.execute("select artikel.id, artikel.rubrik, artikel.ingress, artikel.a_text, artikel.datum from artikel where id= %s;", (str(artikel_id)))
    art = cursor.fetchone()

    try:
        cursor.execute("select p.bildnamn, b.lank from ((bilder as b join artikel_foto as p on b.id=p.bild_id) join artikel as a on a.id=p.artikel_id) where a.id= %s", (str(art[0])))
        bilder = cursor.fetchall()
    except:
        bilder = ("Ingen")
    try:
        cursor.execute("select f.namn, f.efternamn from ((forfattare as f join skrivit as s on f.id=s.forfattar_id) join artikel as a on a.id=s.artikel_id) where a.id= %s", (str(art[0])))
        forfattare = cursor.fetchall()
    except:
        forfattare = ["Ingen", "Forfattare"]


    cursor.execute("select knamn, text, kommentar_id, datum from kommentar where artikel_id=%s order by datum desc", (str(art[0])))
    kommentarer = cursor.fetchall()

    print(kommentarer)

    total = {
        "rubrik": art[1],
        "ingress": art[2],
        "text": art[3],
        "datum": art[4],
        "forfattare": forfattare,
        "bilder": bilder
        }

    totList.append(total)

    return render_template("article.html", totList=totList, artikel=artikel, kommentarer=kommentarer,artikel_id=artikel_id)

@app.route('/addComment', methods=["POST"])
def addComment():

    namn = request.form["knamn"]
    kommentar = request.form["kommentar"]
    art_id = request.form["art_id"]
    now = datetime.datetime.now()

    datum = str(now)
    print(datum)
    

    try:
        cursor.execute("INSERT INTO kommentar (knamn, text, artikel_id, datum)VALUES(%s, %s, %s, %s)", (namn, kommentar, art_id, datum))
        conn.commit()
    except:
        print("Error till db!")

    cursor.execute("select artikel.id, artikel.rubrik, artikel.ingress, artikel.datum from artikel order by artikel.datum desc limit 6;")
    artikel = cursor.fetchall()

    totList = []

    for art in artikel:
        try:
            cursor.execute("select b.lank, p.bildnamn from ((bilder as b join artikel_foto as p on b.id=p.bild_id) join artikel as a on a.id=p.artikel_id) where a.id= %s", (str(art[0])))
            bild = cursor.fetchone()
        except:
            print("Finns ingen bild")
            bild = ("Ingen")

        mid =  "#modal" + str(art[0])
        modalId = "modal" + str(art[0])
        lank = "/artikel/" + str(art[0])

        try:
            cursor.execute("select p.bildnamn, b.lank from ((bilder as b join artikel_foto as p on b.id=p.bild_id) join artikel as a on a.id=p.artikel_id) where a.id= %s", (str(art[0])))
            bilder = cursor.fetchall()
        except:
            bilder = ("Ingen")

        try:
            cursor.execute("select f.namn, f.efternamn from ((forfattare as f join skrivit as s on f.id=s.forfattar_id) join artikel as a on a.id=s.artikel_id) where a.id= %s", (str(art[0])))
            forfattare = cursor.fetchall()

        except:
            forfattare = ["Ingen", "Forfattare"]


        total = {
            "rubrik": art[1],
            "ingress": art[2],
            "datum": art[3],
            "bilden": bild,
            "bilder": bilder,
            "mId": mid,
            "modalId":modalId,
            "forfattare": forfattare,
            "lank": lank
        }
        totList.append(total)

    return render_template("index.html", artikel=artikel, totList=totList)

@app.route('/deleteComment/<kommentar_id>')
def delete_note(kommentar_id):

    delete = str(kommentar_id)

    remove = "DELETE FROM kommentar WHERE kommentar_id = %s"
    cursor.execute(remove, [delete])
    conn.commit()

    cursor.execute("select artikel.id, artikel.rubrik, artikel.ingress, artikel.datum from artikel order by artikel.datum desc limit 6;")
    artikel = cursor.fetchall()

    totList = []

    for art in artikel:
        try:
            cursor.execute("select b.lank, p.bildnamn from ((bilder as b join artikel_foto as p on b.id=p.bild_id) join artikel as a on a.id=p.artikel_id) where a.id= %s", (str(art[0])))
            bild = cursor.fetchone()
        except:
            print("Finns ingen bild")
            bild = ("Ingen")

        mid =  "#modal" + str(art[0])
        modalId = "modal" + str(art[0])
        lank = "/artikel/" + str(art[0])

        try:
            cursor.execute("select p.bildnamn, b.lank from ((bilder as b join artikel_foto as p on b.id=p.bild_id) join artikel as a on a.id=p.artikel_id) where a.id= %s", (str(art[0])))
            bilder = cursor.fetchall()
        except:
            bilder = ("Ingen")

        try:
            cursor.execute("select f.namn, f.efternamn from ((forfattare as f join skrivit as s on f.id=s.forfattar_id) join artikel as a on a.id=s.artikel_id) where a.id= %s", (str(art[0])))
            forfattare = cursor.fetchall()

        except:
            forfattare = ["Ingen", "Forfattare"]


        total = {
            "rubrik": art[1],
            "ingress": art[2],
            "datum": art[3],
            "bilden": bild,
            "bilder": bilder,
            "mId": mid,
            "modalId":modalId,
            "forfattare": forfattare,
            "lank": lank
        }
        totList.append(total)

    return render_template("index.html", artikel=artikel, totList=totList)






#FUNCTIONS
def loopList(key, words):
    for word in words:
        for i in word:
            if key == i:
                return True
            else:
                return False






app.run()
