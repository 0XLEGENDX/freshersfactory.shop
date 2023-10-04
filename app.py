
from flask import Flask,render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("index.html")

@app.route('/register')
def register():
    
    
    return render_template("form1.html")

if __name__ == '__main__':

	app.run()
