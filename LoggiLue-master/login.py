import flask
import flask_login
import MySQLdb
from flask import redirect,url_for
from db import *

app = flask.Flask(__name__)
app.secret_key = 'b\x84\x13\xb0\x89\xed\x7f\xc2\x14\xa0A\x9aN\xae3\xd8@\x0b\xa0\x88\xcc`j&\xdd'

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# Denna fungerar "magiskt". Inget vi behöver gå in djupare på
class User(flask_login.UserMixin):
    pass

# Vid varje anrop när man försöker logga in - då körs user_loader
# Tilldelar användaren en email. Fungerar också "magiskt".
@login_manager.user_loader
def user_loader(user_id):
    sql = "SELECT * FROM users WHERE id = '{}'".format(user_id)
    cursor.execute(sql)
    result = cursor.fetchone()
    if result != None:
        user = User()
        user.id = result['id']
        user.email = result['email']
        user.name = result['name']
        user.passw = result['password']
        user.program_id = result['program_id']
        return user
    return

# Skickar en oinloggad användare till funktionen unauthorized.
@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for("unauthorized"))
