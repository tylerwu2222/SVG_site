#call env\Scripts\activate.bat
import os
from os import listdir
from os.path import isfile, join
from posixpath import split

from flask import Flask, render_template,url_for

import pandas as pd

app = Flask(__name__)

## INDEX
@app.route('/')
def index():
    return render_template('index.html')

## BLOG PAGE
@app.route('/events/')
def events():
    event_info = pd.read_excel('static/data/events.xlsx')
    return render_template('events.html',
        event_info = event_info)

@app.route('/team/')
def team():
    member_info = pd.read_excel('static/data/members.xlsx')
    print(member_info)
    return render_template('team.html',
        member_info = member_info)

## DATASETS
@app.route('/join_team/')
def join_team():
    return render_template('join_team.html')

## ABOUT
@app.route('/contact/')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    # app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(debug=True)