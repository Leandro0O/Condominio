from flask import request,render_template,session,url_for,flash,redirect
from main import app, bcrypt, login_sindico, db

@app.route('/admin')
def admin():
    if 'usuario' not in session:
        flash('SOMENTE ACESSO AUTORIZADO, FAÇA LOGIN PARA ACESSAR!', 'danger')
        return redirect(url_for('loginsindico'))
    return render_template('sindico/index.html', titile='Admin')

    
