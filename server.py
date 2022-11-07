from flask import Flask, render_template, request, redirect
#import smtplib
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['MAIL_SERVER']='mail.alojafacil.cl'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'contacto_desde_pagina@alojafacil.cl'
app.config['MAIL_PASSWORD'] = '{O~+_e%}m,Qu'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/concon')
def concon():
    return render_template('concon.html')

@app.route('/vina')
def vina():
    return render_template('vina_del_mar.html')

@app.route('/renaca')
def renaca():
    return render_template('renaca.html')

@app.route('/papudo')
def papudo():
    return render_template('papudo.html')


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():

    nombre = request.form.get("nombre")
    email = request.form.get("email")
    asunto = request.form.get("asunto")
    mensaje = request.form.get("mensaje")
    datos = 'nombre: '+nombre +'\n email:'+email +'\n asunto:'+asunto + '\n mensaje:'+mensaje
    msg = Message(asunto, sender ='contacto_desde_pagina@alojafacil.cl', recipients = ['alojafacil@gmail.com'])
    msg.body = datos
    mail.send(msg)
    return redirect('/contacto')

@app.route('/rentabiliza')
def rentabiliza():
    return render_template('rentabiliza.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

if __name__=="__main__":
    app.run(debug=True) 