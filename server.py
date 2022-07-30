import csv

from flask import Flask, render_template,request,redirect
import os
import smtplib
from email.message import EmailMessage
app = Flask(__name__)
os.chdir('D://silbaştan/web_server/siteden_gelenler')
# @app.route("/<username>")
# def hello_world(username=None):
#     return render_template('./index.html',name=username)
# @app.route("/blog")
# def blog():
#     return "<p>Ben blog sayfası açacağım ya da vazgeçtiö</p>"
# @app.route("/favico")
# def fav():
#     return render_template('./favc.html')
# @app.route("/user/<int:id>")
# def user(id=None):
#     return render_template('user.html',numarası=id)
@app.route('/')
def my_home():
    return render_template('index.html')
@app.route('/index.html')
def home():
    return render_template('index.html')
@app.route('/about.html')
def about():
    return render_template('about.html')
@app.route('/works.html')
def work():
    return render_template('works.html')
@app.route('/work.html')
def workes():
    return render_template('work.html')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')
@app.route('/components.html')
def components():
    return render_template('components.html')
def write_csv(data):
    with open('data.csv','a',newline='') as dosya:
        email1=data['email']
        text=data['text']
        texarea=data['textarea']
        csv_writer=csv.writer(dosya,delimiter=',',quotechar="'",quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email1,text,texarea])
@app.route('/sumbit_form', methods=['POST', 'GET'])
def sumbit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        # email_=EmailMessage()
        # email_['from']='hubahuba06@gmail.com'
        # email_['to']=data['email']
        # email_['subject']=data['textarea']
        # email_.set_content('what\'s up')
        # with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
        #     smtp.ehlo()
        #     smtp.starttls()
        #     smtp.login('hubahuba06@gmail.com','Ali.1500')
        #     smtp.sendmail(email_)
        write_csv(data)
        with open('site_mesajları.txt','a')as te:
            te.write(data['email']+' '+data['text']+' '+data['textarea']+'\n')
        
        return render_template('/thank_you.html')
    else:
        return 'wrong'