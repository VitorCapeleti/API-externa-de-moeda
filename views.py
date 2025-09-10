from app import app
import sys
sys.path.append('/home/vitor/Documentos/Projetos/Consumir API py')
from controller.listInfos import *
from flask import render_template, redirect, request, session, flash
from flask import send_file, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField, SubmitField
@app.route('/', methods=['GET', 'POST'])
def index():
    data = list_infos()
    return render_template('index.html', data=data)