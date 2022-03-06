
from flask import request,render_template,session,url_for,flash,redirect
from condominio import app, bcrypt, db
from .modules import Sindico
from .forms import RegisterSindico, LoginSindico



@app.route('/admin')
def admin():
    if 'usuario' not in session:
        flash('SOMENTE ACESSO AUTORIZADO, FAÇA LOGIN PARA ACESSAR!', 'danger')
        return redirect(url_for('loginsindico'))
    return render_template('sindicos/index.html', titile='Admin')


@app.route('/admin/cadastrar', methods=['POST','GET'])    
def registersindico():
    
    form = RegisterSindico(request.form)

    if request.method == 'POST' and form.validate():
        try:
            passwordhash = bcrypt.generate_password_hash(form.password.data)
            sindico = Sindico(
                nome = form.nome.data,
                usuario = form.usuario.data,
                email = form.email.data,
                tel = form.tel.data,
                password = passwordhash
            )
            db.session.add(sindico)
            flash(f'{form.usuario.data} cadastrado com sucesso!', 'success')
            db.session.commit()
            return redirect(url_for('loginsindico'))
        except Exception as e:
            print (e)    
    else:
        flash('Erro ao cadastrar', 'danger')    
    
    return render_template('sindicos/register.html', title='Cadastro Sindico', form=form)    


@app.route('/admin/login', methods=['POST', 'GET'])
def loginsindico():
    form = LoginSindico(request.form)
    if request.method == "POST" and form.validate():
        try:
            sindico = Sindico.query.filter_by(usuario=form.usuario.data).first()
            if sindico and bcrypt.check_password_hash(sindico.password, form.password.data):
                session['usuario'] = form.usuario.data
            
                flash(f'Olá, {sindico.usuario}, seja bem vindo!','success')
                return redirect( url_for('admin'))
        except Exception as e:
            print(e)        
        else:
            flash('Não foi possivel realizar o login!', 'danger')  
    return render_template('sindicos/login.html', form=form,title="Login Sindico") 
            