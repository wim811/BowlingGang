from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bowling.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    phone_number = db.Column(db.String(100))
    email = db.Column(db.String(200), unique=True)
    lid_since = db.Column(db.Date, default=datetime.now)

    def __init__(self,name,phone_number,email,lid_since):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.lid_since = lid_since

class Competition(db.Model):
    __tablename__ = 'tournaments'
    id_tournament = db.Column(db.Integer, primary_key=True)
    name_tournament = db.Column(db.String(200))
    year_tournament = db.Column(db.Integer())

    def __init__(self,name_tournament,year_tournament):
        self.name_tournament = name_tournament
        self.year_tournament = year_tournament
       

class CompSession(db.Model):
    __tablename_='comsession'
    id_session_tournament = db.Column(db.Integer, primary_key=True)
    session_tournament = db.Column(db.String(200))
    session_place_tournament = db.Column(db.String(200))
    session_date = db.Column(db.Date, default=datetime.now)

    def __init__(self, session_tournament, session_place_tournament, session_date ):
        self.session_tournament = session_tournament
        self.session_place_tournament = session_place_tournament
        self.session_date = session_date


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/ploeg")
def ploeg():

     players = Member.query.all()

     return render_template('ploeg.html', players = players)

@app.route("/reglement")
def reglement():
    return render_template('reglement.html')
#sub page of Competitie dropdown.
@app.route("/tournooi2025")
def tournooi25():
    return render_template('tournooi2025.html')

@app.route("/statistieken")
def statistieken():
    return render_template('statistieken.html')

@app.route("/adminpage")
def adminpage():

   

    return render_template('adminpage.html')

@app.route('/admin_leden', methods=['Get','POST'])
def admin_leden():
    global members_list
    if request.method == 'POST':
            member_data = request.form

            mem_name = member_data['DName']
            mem_phone = member_data['DPhone']
            mem_mail = member_data['DEmail']
            
            mem_data = Member(name=mem_name, phone_number=mem_phone, email=mem_mail)
            db.session.add(mem_data)
            db.session.commit()

    

            
            return render_template('admin_leden.html')
    members_list = Member.query.all()
    return render_template('admin_leden.html', members_list=members_list)

@app.route('/admin_tournooien', methods=['Get','POST'])
def admin_tournooien():
    return render_template('admin_tournooien.html')

@app.route('/admin_statistieken', methods=['Get','POST'])
def admin_statistieken():
    return render_template('admin_statistieken.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
