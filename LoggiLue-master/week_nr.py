import datetime
from flask import make_response, redirect, url_for, request


# Körs när man loggar in på sidan och sätter veckonummret till dagens veckonummer.
def current_week():
    date = datetime.datetime.now()
    weeknr = date.isocalendar()[1]
    return weeknr

# Ökar veckonumret som finns i cookien med 1.
def next_week():
    weeknr = request.cookies.get('weeknr')
    new_weeknr = int(weeknr) + 1
    resp = make_response(redirect(url_for('start')))
    resp.set_cookie('weeknr', str(new_weeknr))
    return resp

# Minskar veckonumret som finns i cookien med 1.
def prev_week():
    weeknr = request.cookies.get('weeknr')
    new_weeknr = int(weeknr) - 1
    resp = make_response(redirect(url_for('start')))
    resp.set_cookie('weeknr', str(new_weeknr))
    return resp

# Sparar veckonumret i en cookie.
def set_cookie():
    weeknr = str(current_week())
    resp = make_response(redirect(url_for('start')))
    resp.set_cookie('weeknr', weeknr)
    return resp
