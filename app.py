from flask import Flask, request, render_template, session,redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from database import db, User
from functools import wraps 
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import secrets




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bowling.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'bowling_23&'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)


db.init_app(app)

with app.app_context():
    db.create_all()

def generate_reset_token(user):
    token = secrets.token_urlsafe(32)
    user.reset_token = token
    user.reset_token_expiration = datetime.utcnow() + timedelta(hours=1) #Token is valid for 1 hour
    db.session.commit()
    return token

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    
        #Check if the user exists
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password,password):
            #Login successfull
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            session['logged_in'] = True
            flash(f'Welkom terug, {user.username}!', 'succes')
            return redirect(url_for('home', user=user.username, role=user.role))
        else:
            flash(f'Ingeldige gebruikersnaam of wachtwoord.', 'error')
            return redirect(url_for('login'))
             
    return render_template('login.html')

@app.route('/admin', methods=['GET','POST'])
def admin():

    return render_template('admin.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        selected_value = request.form.get('role') 

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        user = User(name=name, email=email,username=username, password=hashed_password, role=selected_value)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('admin'))

    return render_template('registerLid.html')

@app.route('/statistics', methods=['GET','POST'])
def statistics():

    return render_template('statistics.html')    

@app.route('/request_password_reset', methods=['GET','POST'])
def request_password_reset():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            token = generate_reset_token(user)
            reset_url = url_for('reset_password', token=token, _external=True)
            send_email(user.email, "Password Reset Request", f"Click here to reset your password: {reset_url}")
        flash("If your email is registered, you will recieve a password resel link.")
    return render_template('request_password_reset.html')

if __name__ == '__main__':
    app.run(debug=True)
