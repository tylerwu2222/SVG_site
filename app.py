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
    base_path = 'static/images/front_page_pics'
    images = ['../' + base_path + '/' + img for img in os.listdir(base_path)]
    return render_template('index.html',
    images = images)

## BLOG PAGE
@app.route('/events/')
def events():
    event_info = pd.read_excel('static/data/events.xlsx')
    base_path = 'static/images/event_pics'
    image_base_dir = os.listdir(base_path)
    df_list = []
    for image_folder in image_base_dir:
        images = os.listdir(os.path.join(base_path,image_folder))
        for img in images:
            path = '../' + os.path.normpath(os.path.join(base_path,image_folder,img)).replace('\\','/')
            row = [image_folder,img, path]
            df_list.append(row)
    img_df=pd.DataFrame(df_list,columns=['folder','img','path'])
    print(img_df)
    return render_template('events.html',
        image_df = img_df,
        event_info = event_info)

@app.route('/team/')
def team():
    member_info = pd.read_excel('static/data/members.xlsx')
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