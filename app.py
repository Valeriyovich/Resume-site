from xml.etree.ElementTree import tostring
from flask import Flask, render_template, url_for, request, flash
import smtplib
import email.message
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

def send_email(data):
    sender = 'pushchykov@gmail.com'
    password = os.getenv("EMAIL_PASS")
    print(password)
     
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    print('connect to smtp')
    server.starttls()
    try:
        server.login(sender, password)
        print('login to mail success')
        print(data)
        # server.sendmail(sender, 'puschikoff@gmail.com', data)
        
        print('send....')
    except Exception as ex:
        return f"{ex} Check data"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', result = '')
    elif request.method == 'POST':
        result = request.form
        data = ''
        for key, value in result.items():
            data += (' ' + value)
        print(data)
        
        # for key, value in result:
        #     arr[key] = result[value]
        
        send_email(data)
        
        
        
        return render_template("index.html",result = request.form)


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)