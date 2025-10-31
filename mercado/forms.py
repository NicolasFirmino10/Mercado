from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from mercado.models import User

class CadastroForm(FlaskForm):
    def validate_usuario(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError('Nome de usuário já existe. Por favor, escolha outro.')
    
    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError('E-mail já existe. Por favor, escolha outro.')
    
    def validate_senha(self, check_senha):
        senha = User.query.filter_by(senha=check_senha.data).first()
        if senha:
            raise ValidationError('Senha já existe. Por favor, escolha outra.')
    
    usuario = StringField('Nome de usuário:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField('E-mail:', validators=[Email(), DataRequired()])
    senha1 = PasswordField('Senha:', validators=[Length(min=6), DataRequired()])
    senha2 = PasswordField('Confirmar senha:', validators=[EqualTo('senha1'), DataRequired()])
    submit = SubmitField('Cadastrar')


class LoginForm(FlaskForm):
    usuario = StringField('Nome de usuário:', validators=[DataRequired()])
    senha = PasswordField('Senha:', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class CompraProdutoForm(FlaskForm):
    submit = SubmitField('Comprar Produto')

class VendaProdutoForm(FlaskForm):
    submit = SubmitField('Vender Produto')