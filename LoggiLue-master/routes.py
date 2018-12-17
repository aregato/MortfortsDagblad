import flask
import MySQLdb
from flask import Flask, render_template, request, redirect, url_for, make_response, send_from_directory
import flask_login
import os
from flask_bcrypt import Bcrypt
from werkzeug import secure_filename
from login import *
from db import *
from week_nr import *

app = flask.Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'b\x84\x13\xb0\x89\xed\x7f\xc2\x14\xa0A\x9aN\xae3\xd8@\x0b\xa0\x88\xcc`j&\xdd'

login_manager.init_app(app)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'pages', 'docx', 'pptx', 'one', 'doc'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']



# Startsidan och loginfunktionaliteten
@app.route('/', methods=['GET', 'POST'])
def login():

    users_sql = "SELECT COUNT(id) FROM users"
    cursor2.execute(users_sql)
    total_users = cursor2.fetchall()

    notes_sql = "SELECT COUNT(note_id) FROM notes"
    cursor2.execute(notes_sql)
    total_notes = cursor2.fetchall()

    ht16_sql = "SELECT COUNT(program_id) FROM users WHERE program_id = 1"
    cursor2.execute(ht16_sql)
    ht16 = cursor2.fetchall()

    ht15_sql = "SELECT COUNT(program_id) FROM users WHERE program_id = 2"
    cursor2.execute(ht15_sql)
    ht15 = cursor2.fetchall()
    
    if flask.request.method == 'GET':
        return render_template("index.html", total_users=total_users, total_notes=total_notes, ht16=ht16, ht15=ht15)

    password = flask.request.form['pw']
    email = flask.request.form['email']

    sql = "SELECT * FROM users WHERE email = '{}'".format(email)
    # Pekare på databasen
    cursor.execute(sql)
    # Hämtar en rad från databasen
    result = cursor.fetchone()

    cursor2.execute("select password from users where email = '{}'".format(email))
    b_losen = cursor2.fetchone()
    if b_losen != None:
        pass_check = bcrypt.check_password_hash(b_losen[0], password)
    else:
        pass

    # Om användaren finns i databasen skickas denna till start
    if result != None and pass_check == True:
        user = User()
        user.id = result['id']
        user.email = result['email']
        flask_login.login_user(user)
        
        resp = set_cookie()
        return resp

    # Om användaren inte finns skickas denna tillbaka till login och en ruta visas med att det är fel uppgifter
    show_box = "show_box"
    text = "Du angav fel inloggningsuppgifter"
    return render_template("index.html", show_box=show_box, text=text, total_users=total_users, total_notes=total_notes, ht16=ht16, ht15=ht15)


# Loggar ut användaren
@app.route('/logout')
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for('login'))

# Visar registrera formulär
@app.route('/register')
def register():
    sql = "SELECT program_id, program_code, program_name FROM programs"

    cursor2.execute (sql)
    result = cursor2.fetchall()
    
    return render_template("register.html", result=result)

# Körs när registreaformuläret skickas
@app.route('/signUp', methods=["POST"])
def signUp():
    username = str(request.form["username"])
    password = str(request.form["psw"])
    email = str(request.form["email"])
    program_id = request.form["prgm"]
    #BCrypt --> Tar password och gör om det till krypt.
    psw_hash = bcrypt.generate_password_hash(password).decode('UTF-8')

    try:
        #Tabell i db där name och email måste vara unika
        cursor.execute("INSERT INTO `users` (name, email,password, program_id)VALUES(%s, %s, %s, %s)", (username, email, psw_hash, program_id))
        db.commit()
        return redirect(url_for("sucess"))
    except:
        #Kopplat till sida istället för felmeddelande. "IdentityError"
        return redirect(url_for("wrong_email"))
    
#Visas om användaren anger en email som redan finns i databasen
@app.route('/wrong_email')
def wrong_email():
    return render_template("wrong_email.html")

# Visas när användaren har lyckats registrera sig i databasen
@app.route('/sucess')
def sucess():
    return render_template("confirmed_login.html")

# Visas om användaren inte är inloggad
@app.route('/unauthorized')
def unauthorized():
    return render_template("unauthorized.html")

# Startsidan när man har loggat in
@app.route('/start')
@flask_login.login_required
def start():

    weeknr= request.cookies.get('weeknr')

    # Hämtar programid på den nuvarande inloggade användaren.
    prog_id = flask_login.current_user.program_id

    # Istället för att ha ett ID på programmet vill vi ju ha dess namn.
    cursor2.execute ("SELECT program_name FROM programs WHERE program_id = %s", [prog_id])
    program_name = str(cursor2.fetchone()[0])


    # Hämtar de olika föreläsningarna från databasen, dag för dag.
    sql = "SELECT bokning_id, start_tid, slut_tid, kurskod, moment FROM lectures WHERE veckonummer = %s AND dagnamn = %s AND program_id = %s ORDER BY datum ASC, start_tid ASC"
    
    cursor2.execute(sql, (weeknr, 'Mån', prog_id))
    man = cursor2.fetchall()

    cursor2.execute(sql, (weeknr, 'Tis', prog_id))
    tis = cursor2.fetchall()

    cursor2.execute(sql, (weeknr, 'Ons', prog_id))
    ons = cursor2.fetchall()

    cursor2.execute(sql, (weeknr, 'Tor', prog_id))
    tor = cursor2.fetchall()

    cursor2.execute(sql, (weeknr, 'Fre', prog_id))
    fre = cursor2.fetchall()

    username = flask_login.current_user.name #BRA grej för att skriva ut username
    
    return render_template("start.html", username=username, weeknr=weeknr, program_name=program_name, man=man, tis=tis, ons=ons, tor=tor, fre=fre)

# Om användaren vill gå till en tidigare vecka körs detta.
@app.route('/prev_week_route')
@flask_login.login_required
def prev_week_route():
    resp = prev_week()
    return resp

# Nästa vecka körs detta.
@app.route('/next_week_route')
@flask_login.login_required
def next_week_route():
    resp = next_week()
    return resp

# Om användaren vill tillbaka snabbt till nuvarande vecka. 
@app.route('/current_week')
@flask_login.login_required
def current_week_route():
    resp = set_cookie()
    return resp

@app.route('/statistics')
@flask_login.login_required
def statistics():
    username = flask_login.current_user.name
    users_sql = "SELECT COUNT(id) FROM users"
    cursor2.execute(users_sql)
    total_users = cursor2.fetchall()

    notes_sql = "SELECT COUNT(note_id) FROM notes"
    cursor2.execute(notes_sql)
    total_notes = cursor2.fetchall()

    ht16_sql = "SELECT COUNT(program_id) FROM users WHERE program_id = 1"
    cursor2.execute(ht16_sql)
    ht16 = cursor2.fetchall()

    ht15_sql = "SELECT COUNT(program_id) FROM users WHERE program_id = 2"
    cursor2.execute(ht15_sql)
    ht15 = cursor2.fetchall()
 
    return render_template("statistics.html", username=username,total_users=total_users, total_notes=total_notes, ht16=ht16, ht15=ht15)

#Visar användarens sida för konto och inställningar
@app.route('/konto')
@flask_login.login_required
def konto():
    u_id = flask_login.current_user.id
    email = flask_login.current_user.email
    name = flask_login.current_user.name
    password = flask_login.current_user.passw
    prog_id = flask_login.current_user.program_id

    
    cursor2.execute ("SELECT program_name FROM programs WHERE program_id = %s", [prog_id])
    program_name = str(cursor2.fetchone()[0])

    sql = "SELECT program_id, program_code, program_name FROM programs"
    cursor2.execute (sql)
    resultat = cursor2.fetchall()

    username = flask_login.current_user.name

    return render_template("konto.html",u_id=u_id, email=email, name=name, password=password ,prog_id=prog_id, program_name=program_name, resultat=resultat, username=username)

# Sida där de olika anteckningarna visas.
@app.route('/note/<bokning_id>')
@flask_login.login_required
def note(bokning_id):

    # Hämtar vilken lektion det var man klickade in på.
    sql_lecture = "SELECT kurskod, moment, datum FROM lectures WHERE bokning_id = %s"
    cursor2.execute (sql_lecture, [bokning_id])
    lecture = cursor2.fetchall()

    # Hämtar alla anteckningar för den nuvarande föreläsningen.
    sql_notes = "SELECT notes.rubrik, notes.text, notes.points, notes.user_id, users.name, notes.note_id, notes.path FROM notes INNER JOIN users ON notes.user_id = users.id WHERE notes.bokning_id = %s ORDER BY points DESC, note_id DESC"
    cursor2.execute (sql_notes, [bokning_id])
    notes = cursor2.fetchall()

    username = flask_login.current_user.name
    
    return render_template("note.html", lecture=lecture, notes=notes, bokning_id=bokning_id, username=username)

# Sida där en anteckning visas
@app.route('/unique_note/<bokning_id>/<note_id>')
@flask_login.login_required
def unique_note(bokning_id, note_id):

    # Hämtar vilken lektion det var man klickade in på.
    sql_lecture = "SELECT kurskod, moment, datum FROM lectures WHERE bokning_id = %s"
    cursor2.execute (sql_lecture, [bokning_id])
    lecture = cursor2.fetchall()

    # Hämtar anteckning för den nuvarande föreläsningen som användaren klickade på.
    sql_notes = "SELECT notes.rubrik, notes.text, notes.points, notes.user_id, users.name, notes.note_id, notes.path FROM notes INNER JOIN users ON notes.user_id = users.id WHERE notes.note_id = %s ORDER BY points DESC, note_id DESC"
    cursor2.execute (sql_notes, [note_id])
    notes = cursor2.fetchall()

    username = flask_login.current_user.name
    
    return render_template("unique_note.html", lecture=lecture, notes=notes, bokning_id=bokning_id, username=username)


#Lägger till en antecknig för föreslänsingen som användaren valde
@app.route('/add_note/<bokning_id>')
@flask_login.login_required
def add_note(bokning_id):

    # Hämtar vilken lektion det var man klickade in på.
    sql_lecture = "SELECT kurskod, moment, datum FROM lectures WHERE bokning_id = %s"
    cursor2.execute (sql_lecture, [bokning_id])
    lecture = cursor2.fetchall()

    username = flask_login.current_user.name
    
    return render_template("add_note.html", bokning_id=bokning_id, username=username, lecture=lecture)

#Lägger till en poäng för anteckningen
@app.route('/add_point/<bokning_id>/<note_id>')
@flask_login.login_required
def add_point(bokning_id, note_id):

    sql = "UPDATE notes INNER JOIN users ON (notes.user_id = users.id) SET notes.points = notes.points +1, users.points = users.points +1 WHERE notes.note_id = %s"

    cursor2.execute (sql, [note_id])
    db.commit()
    return redirect(url_for('note', bokning_id=bokning_id))

#Ta bort en poäng för anteckningen    
@app.route('/remove_point/<bokning_id>/<note_id>')
@flask_login.login_required
def remove_point(bokning_id, note_id):

    sql = "UPDATE notes INNER JOIN users ON (notes.user_id = users.id) SET notes.points = notes.points -1, users.points = users.points -1 WHERE notes.note_id = %s"

    cursor2.execute (sql, [note_id])
    db.commit()
    return redirect(url_for('note', bokning_id=bokning_id))

#Körs när add_note skickas
@app.route('/save_note/<bokning_id>', methods=["POST"])
@flask_login.login_required
def save_note(bokning_id):
    #Hämtar tabellen notes för att kunna mata in värden i den.
    sql = "SELECT bokning_id, user_id, points, rubrik, text FROM notes"
    cursor2.execute (sql)
    result = cursor2.fetchall()
    
    bokning_id = bokning_id
    user_id = flask_login.current_user.id #Hämtar användarID:t för den inloggade användaren så att anteckningen som sparas kopplas till användaren.
    points = '0' 
    rubrik = str(request.form["rubrik"]) 
    text = str(request.form["text"])

    username = flask_login.current_user.name

    # Get the name of the uploaded file
    file = request.files['file']
    # Kollar ifall användaren har bifogat en fil eller inte
    if file.filename != '':
        # Check if the file is one of the allowed types/extensions
        if file and allowed_file(file.filename):
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(file.filename)
            # Move the file form the temporal folder to
            # the upload folder we setup
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #Sparar värdena i tabellen notes
            cursor.execute("INSERT INTO `notes` (bokning_id, user_id, points, text, rubrik, path) VALUES (%s, %s, %s, %s, %s, %s)", (bokning_id, user_id, points, text, rubrik, filename))
            db.commit()
            return redirect(url_for('note', bokning_id=bokning_id))
        else:
            return render_template("wrong_filetype.html", bokning_id=bokning_id, username=username)
    else:
        cursor.execute("INSERT INTO `notes` (bokning_id, user_id, points, text, rubrik) VALUES (%s, %s, %s, %s, %s)", (bokning_id, user_id, points, text, rubrik))
        db.commit()
        return redirect(url_for('note', bokning_id=bokning_id))

@app.route('/show_file/<filename>')
@flask_login.login_required
def show_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/my_notes')
@flask_login.login_required
def my_notes():

    username = flask_login.current_user.name
    u_id = flask_login.current_user.id
    
    sql_notes = "SELECT notes.rubrik, notes.text, notes.points, notes.user_id, users.name, notes.note_id, notes.path FROM notes INNER JOIN users ON notes.user_id = users.id WHERE notes.user_id = %s ORDER BY points DESC, note_id DESC"
    cursor2.execute (sql_notes, [u_id])
    notes = cursor2.fetchall()
    
    return render_template('my_notes.html', notes=notes, username=username)

@app.route('/delete_note/<note_id>')
@flask_login.login_required
def delete_note(note_id):
    #Hämtar path i databasen som sparat namnet på filen
    file_sql = "SELECT path FROM notes WHERE note_id = %s"
    cursor2.execute(file_sql, [note_id])
    file_name = cursor2.fetchone()
    file = file_name[0]

    #Om path inte finns (en användare har inte laddat upp en fil) så händer inget
    if file == "":
        pass
    #Tar bort filen från mappen uploads
    else:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file))

    #Tar bort raden i databasen för antecknningen
    remove = "DELETE FROM notes WHERE note_id = %s"
    cursor2.execute(remove, [note_id])
    db.commit()
    
    return redirect(url_for('my_notes'))
