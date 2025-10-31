from mercado import app, db
from mercado.models import User, Item

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso!")