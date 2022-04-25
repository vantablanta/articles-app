from flask import render_template
from app import app 

@app.route('/')

def index():
    title = "Hello World"
    return render_template('index.html', title = title)