from condominio import db, login_manager,bcrypt,app
from flask import render_template, redirect, flash, session, url_for,request
from .modules import Mensagem, Chamados , Sugestoes
from .forms import AbreMensagem, AbreChamados , AbreSugestoes
from condominio.morador.modules import Morador
from condominio.morador.forms import LoginMorador
from condominio.admin.forms import LoginSindico
from flask_login import login_required, current_user




@app.route('/chamados', methods=['POST','GET'])
@login_required
def moradorchamados():
    form = AbreChamados(request.form)
    morador = Morador.query.filter_by(id=current_user.id).first()
    if request.method == 'POST' and current_user.is_authenticated:
        morador_id = current_user.id
        try:
            chamado = Chamados(
               nome = form.nome.data,
               bloco = form.bloco.data,
               apto = form.apto.data,
               descricao = form.descricao.data,
               morador_id = morador_id 
            )
            db.session.add(chamado)  
            flash('Chamado aberto com sucesso', 'success') 
            db.session.commit()
            return redirect(url_for('morador'))
        except Exception as e:
            print(e)
    
    return render_template('/moradores/chamados.html', title='Home', form=form, morador=morador)    


@app.route('/sugestoes', methods=['POST','GET'])
@login_required
def moradorsugestoes():
    form = AbreSugestoes(request.form)
    if request.method == 'POST' and current_user.is_authenticated:
        morador_id = current_user.id
        try:
            chamado = Sugestoes(
               nome = form.nome.data,
               bloco = form.bloco.data,
               apto = form.apto.data,
               descricao = form.descricao.data,
               morador_id = morador_id 
            )
            db.session.add(chamado)
            db.session.commit()
            flash('Sugestão enviada com sucesso', 'success')
           
            return redirect(url_for('morador'))
        except Exception as e:
            print(e)
   
    return render_template('/moradores/sugestoes.html', title='Home', form=form)      


@app.route('/mensagem', methods=['POST','GET'])
@login_required
def moradormensagem():
    form = AbreMensagem(request.form)
    if request.method == 'POST' and current_user.is_authenticated:
        morador_id = current_user.id
        try:
            chamado = Mensagem(
               nome = form.nome.data,
               bloco = form.bloco.data,
               apto = form.apto.data,
               descricao = form.descricao.data,
               morador_id = morador_id 
            )
            db.session.add(chamado)
            db.session.commit()
            flash('Mensagem enviada com sucesso', 'success') 
            
            return redirect(url_for('morador'))
        except Exception as e:
            print(e)
    
    return render_template('/moradores/mensagem.html', title='Home', form=form)                    



