from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Crio uma instância do SQLAlchemy para gerenciar o banco de dados.
db = SQLAlchemy()


class Tarefa(db.Model):
    """
    Esta classe representa a tabela de tarefas do sistema.
    Cada objeto criado será armazenado como um registro no banco de dados.
    """

    # Identificador único da tarefa.
    id = db.Column(db.Integer, primary_key=True)

    # Título da tarefa (campo obrigatório).
    titulo = db.Column(db.String(100), nullable=False)

    # Descrição opcional da tarefa.
    descricao = db.Column(db.String(300))

    # Toda tarefa começa como pendente.
    status = db.Column(db.String(20), default="Pendente")

    # Define a prioridade da tarefa.
    prioridade = db.Column(db.String(20), default="Média")
    
    # Armazena automaticamente a data de criação.
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """
        Facilita a identificação da tarefa durante os testes e no terminal.
        """
        return f"<Tarefa {self.titulo}>"