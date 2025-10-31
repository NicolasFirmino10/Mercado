from  mercado import db, login_manager
from mercado import bcrypt
from flask_login import UserMixin

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable = False, unique = True)
    cod_barra = db.Column(db.String(50), nullable = False, unique = True)
    preco = db.Column(db.Float, nullable = False)
    descricao = db.Column(db.String(100), nullable = False)
    dono = db.Column(db.Integer, db.ForeignKey('user.id'))

    def compra(self, usuario):
        self.dono = usuario.id
        usuario.valor -= self.preco
        db.session.commit()
    
    def venda(self, usuario):
        self.dono = None
        usuario.valor += self.preco
        db.session.commit()
    
    @property
    def formataPreco(self):
        return f'R$ {self.preco:.2f}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String(50), nullable = False, unique = True)
    senha = db.Column(db.String(100), nullable = False)
    valor = db.Column(db.Float, nullable = False, default = 5000.00)
    itens = db.relationship('Item', backref = 'dono_user', lazy = True)


    @property
    def formataValor(self):
        return f'R$ {self.valor:.2f}'

    @property 
    def senhacrip(self):
        return self.senha   # Retorna a senha já criptografada

    @senhacrip.setter
    def senhacrip(self, senha_texto):
        self.senha = bcrypt.generate_password_hash(senha_texto).decode('utf-8') # Criptografa automaticamente ao definir
    
    def converte_senha(self, senha_texto_claro):
        return bcrypt.check_password_hash(self.senha, senha_texto_claro) # Aqui vai servir para o login. Quando preencher o campo ele vai verificar se a senha inserida é igual a senha salva e descriptografada.

    def compra_disponivel(self, produto_obj):
        return self.valor >= produto_obj.preco
    
    def venda_disponivel(self, produto_obj):
        return produto_obj in self.itens
