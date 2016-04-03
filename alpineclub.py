# -*- coding: utf-8 -*-
import re
import sqlite3
import time

from flask import g, render_template, flash, Flask, session, redirect, url_for, \
    escape, request
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

DATABASE = 'alpineclub.db'
DEBUG = True
SECRET_KEY = 'SeriouslySecretKey'

app.config.from_object(__name__)


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def init_db():
    with app.app_context():
        db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def put_db(table, values):
    query = "INSERT INTO " + table + " VALUES ("
    for value in values:
        query += "?, "
    query = query[:-2] + ")"
    db = get_db()
    db.execute(query, values)
    db.commit()


def initsampledata():
    put_db("users", ["haraldfw@gmail.com", "90977322",
                     generate_password_hash("asdfQWE123"),
                     time.strftime('YYYY-MM-DD')])


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def checkcredentials(email, pw):
    user = query_db('SELECT * FROM users WHERE email = ?', [email],
                    one=True)
    if user is None:
        return False
    else:
        return check_password_hash(user['password_hash'], pw)


@app.route('/myprofile', methods=['GET', 'POST'])
def myprofile():
    if request.method == 'GET':
        user = query_db("SELECT * FROM users WHERE email= ?",
                        [session['email']], one=True)
        entries = {}
        entries['email'] = user[0]
        entries['phone'] = user[1]
        entries['joined'] = user[3]
        return render_template('profile.html', entries=entries)
    else:
        if "submitdeluser" in request.form:
            return render_template('deluser.html')
        elif 'submitchangepw' in request.form:
            oldpw = request.form['oldpw']
            newpw = request.form['newpw']
            repeatpw = request.form['repeatpw']

            if not checkcredentials(session['email'], oldpw):
                flash('Nåværende passord er ikke riktig')
            elif newpw != repeatpw:
                flash('Passordene er ikke like')
            else:
                db = get_db()
                db.execute('UPDATE users SET password_hash = ? WHERE email = ?',
                           [generate_password_hash(newpw), session['email']])
                db.commit()
                flash('Passord endret')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def registeruser():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        repeatpw = request.form['repeatpw']
        phone = request.form['phone']

        user = query_db('SELECT * FROM users WHERE email = ?', [email],
                        one=True)
        if user is not None:
            flash('E-post er allerede i bruk')
        elif not re.match('^\+?\d+$', phone):
            flash('Ugyldig telefonnummer. Bare tast inn tall.')
        elif password != repeatpw:
            flash('Passordene er ikke like')
        elif re.search('[a-z][A-Z][0-9]', password):
            flash('passordet må ha minst én stor og liten '
                  'bokstav samt ett tall')
        elif len(password) < 8:
            flash('Passord må være lengre enn 8 karakterer.')
        else:
            pwhash = generate_password_hash(password)
            db = get_db()
            db.execute('INSERT INTO users VALUES(?, ?, ?, ?)',
                       [email, phone, pwhash, time.strftime('YYYY-MM-DD')])
            db.commit()

            session['logged_in'] = True
            session['email'] = request.form['email']
            return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if checkcredentials(request.form['email'], request.form['password']):
            session['email'] = request.form['email']
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('Feil e-post eller passord.')
    return render_template('login.html')


@app.route('/logout')
def logout():
    # Remove the username from the session if it's there
    session.pop('email', None)
    session.pop('logged_in', None)
    return redirect(url_for('index'))


@app.route('/deluser', methods=['GET', 'POST'])
def deluser():
    if request.method == 'GET':
        return render_template('deluser.html')
    else:
        if checkcredentials(session['email'], request.form['password']):
            db = get_db()
            db.execute('DELETE FROM users WHERE email = ?', [session['email']])
            db.commit()
            return 'lek'
        return 'kek'
    return 'sek'


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/add', methods=['POST'])
def add_entry():
    tittel = request.form['tittel']
    nyhet = request.form['nyhet']
    forfatter = request.form['forfatter']
    dato = time.strftime('%Y-%m-%d')
    # sjekker at alle felter er fyllt ut
    if str(tittel).strip() and str(nyhet).strip() and str(forfatter).strip():
        db = get_db()
        db.execute(
                'INSERT INTO nyheter (tittel, nyhet, forfatter, dato) VALUES (?, ?, ?, ?)',
                [tittel, nyhet, forfatter, dato])
        db.commit()
        flash('Innlegget ble sendt og lagret i databasen')
    else:
        flash('Nyhet ikke lagt til. Fyll alle feltene.')
    return redirect(url_for('index'))


@app.route('/nyheter')
def shownewsonly():
    db = get_db()
    cur = db.execute('SELECT * FROM nyheter ORDER BY id DESC')
    entries = cur.fetchall()
    return render_template('news.html', entries=entries)


if __name__ == '__main__':
    app.run()
    init_db()
    initsampledata()
