# Sistema de Mercado Flask

Sistema web de compra e venda de produtos desenvolvido em Flask com autenticação de usuários.

## Funcionalidades

- **Cadastro e Login**: Criação de conta e autenticação segura
- **Comprar Produtos**: Visualizar e comprar produtos disponíveis
- **Vender Produtos**: Vender produtos que você possui
- **Carteira Virtual**: Cada usuário inicia com R$ 5.000(para testes)


## Como Funciona

### 1. Cadastro/Login
- Usuários se cadastram com nome, email e senha
- Sistema criptografa senhas automaticamente
- Login necessário para acessar o mercado

### 2. Compra de Produtos
- Produtos disponíveis aparecem na tabela principal
- Usuário clica em "Comprar esse produto"
- Sistema verifica se há dinheiro suficiente
- Produto é transferido para o usuário e valor é debitado

### 3. Venda de Produtos
- Produtos do usuário aparecem na seção "Produtos adicionados"
- Usuário clica em "Vender esse produto"
- Produto volta para o mercado e valor é creditado

### 4. Sistema de Carteira
- Cada usuário tem saldo inicial de R$ 5.000
- Compras debitam o valor
- Vendas creditam o valor
- Saldo é exibido formatado (ex: R$ 1.500)

## Estrutura do Banco de Dados

### Tabela Users
- `id`: Identificador único
- `usuario`: Nome de usuário (único)
- `email`: Email (único)
- `senha`: Senha criptografada
- `valor`: Saldo da carteira (padrão: 5000)

### Tabela Items
- `id`: Identificador único
- `nome`: Nome do produto (único)
- `cod_barra`: Código de barras (único)
- `preco`: Preço do produto
- `descricao`: Descrição do produto
- `dono`: ID do usuário proprietário (null = disponível)


## Tecnologias e Libs Utilizadas

- **Flask**: Framework web Python
- **SQLAlchemy**: ORM para banco de dados
- **Flask-Login**: Sistema de autenticação
- **Flask-WTF**: Formulários web seguros
- **Bcrypt**: Criptografia de senhas
- **Bootstrap**: Interface responsiva
- **SQLite**: Banco de dados

## Instalação e Execução

1. Clone o repositório
2. Instale as dependências: `pip install flask flask-sqlalchemy flask-login flask-wtf bcrypt`
3. Execute: `python app.py`
4. Acesse: `http://localhost:5000`

## Estrutura de Arquivos

```
mercado/
├── __init__.py          # Configuração da aplicação
├── models.py            # Modelos do banco de dados
├── routes.py            # Rotas e lógica de negócio
├── forms.py             # Formulários WTF
└── templates/           # Templates HTML
    ├── base.html        # Template base
    ├── home.html        # Página inicial
    ├── login.html       # Página de login
    ├── cadastro.html    # Página de cadastro
    ├── produtos.html    # Página principal do mercado
    └── includes/        # Componentes reutilizáveis
```

## Fluxo de Uso

1. **Primeiro Acesso**: Usuário se cadastra
2. **Login**: Acessa com credenciais
3. **Produtos**: Visualiza produtos disponíveis
4. **Compra**: Seleciona e compra produtos
5. **Venda**: Vende produtos de volta ao mercado

## Segurança

- Senhas criptografadas com Bcrypt
- Proteção CSRF nos formulários
- Autenticação obrigatória para acessar o mercado
- Validação de dados de entrada
- Controle de permissões para área admin