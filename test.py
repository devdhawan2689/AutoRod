import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from csv import reader
# open file in read mode
user_email = input('Enter your Email ID:- ')
user_password = input('Enter your Password:- ')
with open('test.csv', 'r') as read_obj:
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
        email.set_content(html.substitute({'name': name}),'html')


        with smtplib.SMTP(host='smtp.gmail.com',port='587') as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(user_email,user_password) 
            smtp.send_message(email)
            print('Done!')


    
