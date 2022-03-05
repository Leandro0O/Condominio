from turtle import title
from condominio import db,login_manager,bcrypt,app
from flask import render_template, session, request, url_for, flash, redirect
from .modules import Morador
from .forms import RegisterMorador, LoginMorador
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/morador')
@login_required
def morador(): 
    return render_template('moradores/index.html', title = 'Area do Morador')


    