#First import everything needed to use.
from flask import Flask, render_template, request

#Initialise the web app.
app = Flask(__name__)


#Create the routes of the website.
@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)