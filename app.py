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
@app.route('/content/')
def blog():
    # blog_posts = pd.read_excel('static/data/blog_posts.xlsx')
    return render_template('content.html')
        # posts = blog_posts)

@app.route('/team/')
def team():
    pp_wd = 'static/images/profile_pics'
    profile_pics = os.listdir(pp_wd)
    return render_template('team.html',
        profile_pics = profile_pics)

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