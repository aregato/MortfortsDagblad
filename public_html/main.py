from flask import Flask, render_template,request,redirect,url_for
import flask
import flask_login
import psycopg2

app = flask.Flask(__name__)
app.secret_key = 'randomNyckel'

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

conn = psycopg2.connect(dbname="ag6946", user="ag6946", password="jnblid5q", host="pgserver.mah.se")

cursor = conn.cursor()

# Denna fungerar "magiskt". Inget vi behöver gå in djupare på
class User(flask_login.UserMixin):
    pass

#ROUTES
@app.route('/', methods=["GET","POST"])
def start():
    return render_template("index.html")

@app.route('/loggedIn')
def loggedIn():
    return render_template("loggedIn.html")

@app.route('/news')
def news():
    return render_template("news.html")

@app.route('/imgages')
def images():
    return render_template("images.html")

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/settings')
def settings():
    return render_template("setting.html")


#METHODS
@app.route('/logIn', methods=["POST"])
def logIn():
    
    #Från Form
    username = str(request.form["username"])
    password = str(request.form["psw"])
    #Databas username
    cursor.execute("select username from users;")
    name = cursor.fetchall()
    #Databas Password
    cursor.execute("select password from users;")
    word = cursor.fetchall()
    
    username_db = loopList(username, name)
    password_db = loopList(password ,word)

    right = "Du loggas nu in!"
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
