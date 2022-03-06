from turtle import title
from condominio import db,login_manager,bcrypt,app
from flask import render_template, session, request, url_for, flash, redirect
from .modules import Morador
from .forms import RegisterMorador, LoginMorador
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@login_required
def home():   
    return render_template('index.html',title='Home')


@app.route('/morador')
@login_required
def morador(): 
    return render_template('moradores/index.html', title = 'Area do Morador')


@app.route('/morador/cadastrar', methods=['POST', 'GET'])
def moradorregister():
    form = RegisterMorador(request.form)
    if request.method == 'POST' and form.validate():
        try:
            password_hash = bcrypt.generate_password_hash(form.password.data)
            morador = Morador(
             nome = form.nome.data,
             usuario = form.usuario.data,
             email = form.email.data,
             tel = form.tel.data,
             bloco = form.bloco.data,
             apto = form.apto.data,
             password = password_hash   
            )
            db.session.add(morador)
            flash(f'{form.usuario.data} foi cadastrado com sucesso!!', 'success')
            db.session.commit()
            return redirect(url_for('loginmorador'))
        except Exception as e:
            print (e)
        else:
            flash('Erro ao cadastrar morador!', 'danger')
    return render_template('moradores/register.html', title='Cadastro Morador', form=form)     

@app.route('/morador/login', methods=['POST', 'GET'])       
def loginmorador():
    form = LoginMorador()
    if request.method == 'POST':
            morador = Morador.query.filter_by(email=form.email.data).first()
            if morador and bcrypt.check_password_hash(morador.password, form.password.data):
                login_user(morador)  
                flash(f'Bem vindo, {morador.usuario}' ,'success')
                return redirect(url_for('morador'))
                
            else:
                flash('Falha ao realizar o login', 'danger')    
       
    return render_template ('moradores/login.html', title='Login Morador', form=form)               

@app.route('/morador/logout')
def logoutmorador():
    logout_user()
    return redirect(url_for('morador'))    