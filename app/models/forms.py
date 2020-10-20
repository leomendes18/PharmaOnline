from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class CadastroForm(FlaskForm):
    

    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    usuario = StringField("usuario", validators=[DataRequired()])
    endereco = StringField("endereço", validators=[DataRequired()])
    telefone = StringField("telefone", validators=[DataRequired()])

class LoginForm(FlaskForm):
    

    password = PasswordField("Password", validators=[DataRequired()])
    usuario = StringField("usuario", validators=[DataRequired()])
    
