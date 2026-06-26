from flask_sqlalchemy import SQLAlchemy

# Crio uma instância do SQLAlchemy para gerenciar o banco de dados.
# Ela será utilizada em toda a aplicação.
db = SQLAlchemy()


class Tarefa(db.Model):
    """
    Esta classe representa a tabela 'tarefa' no banco de dados.
    Cada objeto criado será uma tarefa cadastrada pelo usuário.
    """

    # Identificador único da tarefa.
    id = db.Column(db.Integer, primary_key=True)

    # Título da tarefa.
    titulo = db.Column(db.String(100), nullable=False)

    # Descrição da tarefa.
    descricao = db.Column(db.String(300))

    # Status inicial da tarefa.
    # Todas começam como "Pendente".
    status = db.Column(db.String(20), default="Pendente")