import os

# --- IMPORTANTE ---
# 1. Copie a URL do seu Vercel Postgres (do painel Vercel)
# 2. Cole a URL e a sua Secret Key aqui embaixo:
# ------------------
# ESTAS LINHAS DEVEM VIR ANTES DE "from mercado import app"
os.environ['POSTGRES_URL'] = "postgres://3d4f3b48666bc31618fd8ea9dcdebac6c4099cadd445253cec27a907e65f0987:sk_llfLB62ZYpEkbh34GZ38F@db.prisma.io:5432/postgres?sslmode=require"
os.environ['SECRET_KEY'] = '1afb86cf05c9bcf0de4be1de'
# ------------------


# Agora que as variáveis de ambiente estão setadas, podemos importar o app.
# O __init__.py vai ler as variáveis que acabamos de setar.
from mercado import app, db

# O __init__.py já configurou o app,
# mas vamos imprimir para confirmar a conexão.
db_uri_display = "Variável POSTGRES_URL não foi colada no script"
if os.environ.get('POSTGRES_URL') != 'postgres://...':
    db_uri_display = os.environ.get('POSTGRES_URL').replace("postgres://", "postgresql://", 1)

print(f"Tentando conectar ao banco: {db_uri_display}")

# Usa o contexto do app para se conectar ao banco e criar as tabelas
with app.app_context():
    print("Criando tabelas (User, Item)...")
    db.create_all()
    print("Tabelas criadas com sucesso no banco PostgreSQL!")

