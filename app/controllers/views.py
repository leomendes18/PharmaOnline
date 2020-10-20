from flask import render_template, redirect, url_for, session, request
from flask_login import login_user, logout_user, login_required, current_user
from app import pharmaonline, db, login_manager
from app.models.tables import *
from app.models.forms import *

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(id):
	return User.select().filter(id=id)


@pharmaonline.route('/')
@pharmaonline.route('/index')
def index():
    return render_template('index.html')

@pharmaonline.route('/pharma')
def pharma():
    return render_template('pharma.html')

@pharmaonline.route('/medpaguemenos')
def medpaguemenos():
    return render_template('medpaguemenos.html')

@pharmaonline.route('/medsantamaria')
def medsantamaria():
    return render_template('medsantamaria.html')

@pharmaonline.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@pharmaonline.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()
    print("Aki")
    #print(fr)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # print(User.usuario)
        # usuario = User()
        # usuario.name = form.name.data
        # usuario.password =form.password.data
        # usuario.email = form.email.data
        # usuario.usuario = form.usuario.data
        # usuario.endereco = form.endereco.data
        # usuario.telefone = form.telefone.data
        # print(usuario)
        # usuario.save()
        usuario = User.create(name = form.name.data, email = form.email.data, password = form.password.data, usuario = form.usuario.data, endereco=form.endereco.data, telefone=form.telefone.data)
        #login_user(usuario)
        return redirect(url_for('pagamento'))
    else:
        print(form.errors)
    return render_template("cadastro.html", form=form)


@pharmaonline.route('/pagamento', methods=['GET', 'POST'])
@login_required
def pagamento():
    return render_template('pagamento.html')

@pharmaonline.route('/finalização')
@login_required
def finalizacao():
    return render_template('finalização.html')

