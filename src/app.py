from flask import Flask, render_template

# Importo o banco de dados e a classe Tarefa criados no models.py
from models import db, Tarefa

app = Flask(__name__)

# Configuração do banco de dados SQLite
# O arquivo database.db será criado automaticamente dentro da pasta src.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Desabilita um aviso do SQLAlchemy.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados na aplicação Flask.
db.init_app(app)

# Cria as tabelas do banco de dados caso elas ainda não existam.
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)