from flask import Flask, render_template, request, redirect
import csv
import os
from werkzeug.utils import secure_filename
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from csv import reader

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>', methods=['POST', 'GET'])
def page(page_name):
    return render_template(page_name)


@app.route('/index.html')
def my_index():
    return render_template('index.html')


@app.route('/signup_page.html')
def my_elements():
    return render_template('signup_page.html')


@app.route('/generic.html')
def my_generic():
    return render_template('generic.html')


@app.route('/new_signup_page.html')
def signup():
    return render_template('new_signup_page.html')


@app.route('/new_login.html')
def login_page():
    return render_template('new_login.html')


@app.route('/new_signup.html')
def signup_page():
    return render_template('new_signup.html')


@app.route('/home_page.html')
def home_page():
    return render_template('home_page.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload_page():
    # try:
    #     os.remove('email_template.csv')
    #     print('file removed')
    # except FileNotFoundError:
    #     print('file not found')
    return render_template("upload_page.html")


def mail_send(email, password):
    # open file in read mode
    user_email = email
    user_password = password
    os.chdir('./')
    with open('email_template.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        email_list = []
        for row in csv_reader:
            email_list.append(row)
            # row variable is a list that represents a row in csv

        del email_list[0]

        print(email_list)

        for i in email_list:
            email_id = i[0]
            name = i[1]
            print(email_id)
            print(name)
            # html = Template(Path('index.html').read_text())
            html = Template(Path('email_template.html').read_text())
            email = EmailMessage()
            email['from'] = user_email
            email['subject'] = 'Intership at Stark Industries'
            email['to'] = email_id
            email.set_content(html.substitute({'name': name}), 'html')

            with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(user_email, user_password)
                smtp.send_message(email)
                print('Done!')


@app.route('/handleUpload', methods=['GET', 'POST'])
def upload_file():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            photo.filename = 'email_template.csv'
            photo.save(os.path.join('', photo.filename))
    return render_template('email_signin.html')


@app.route('/email_login', methods=['GET', 'POST'])
def email_login():
    email = request.form['email_id']
    password = request.form['email_password']
    print(email)
    print(password)
    mail_send(email, password)
    return render_template('home_page.html')
