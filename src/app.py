from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Exibe a página inicial e cadastra novas tarefas.
    """

    # Se o formulário foi enviado
    if request.method == 'POST':

        titulo = request.form['titulo']
        descricao = request.form['descricao']
        prioridade = request.form['prioridade']

        nova_tarefa = Tarefa(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade
        )

        db.session.add(nova_tarefa)
        db.session.commit()

        return redirect('/')

    # Busca todas as tarefas
    tarefas = Tarefa.query.all()

    # Estatísticas
    total_tarefas = len(tarefas)

    tarefas_pendentes = len(
        [t for t in tarefas if t.status == "Pendente"]
    )

    tarefas_concluidas = len(
        [t for t in tarefas if t.status == "Concluída"]
    )

    return render_template(
        'index.html',
        tarefas=tarefas,
        total_tarefas=total_tarefas,
        tarefas_pendentes=tarefas_pendentes,
        tarefas_concluidas=tarefas_concluidas
    )
    
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    """
    Permite editar uma tarefa existente.
    """

    tarefa = Tarefa.query.get_or_404(id)

    if request.method == 'POST':

        tarefa.titulo = request.form['titulo']
        tarefa.descricao = request.form['descricao']
        tarefa.prioridade = request.form['prioridade']

        db.session.commit()

        return redirect('/')

    return render_template(
        'editar.html',
        tarefa=tarefa
    )   

@app.route('/excluir/<int:id>')
def excluir(id):
    """
    Remove uma tarefa do banco de dados.
    """

    # Procura a tarefa pelo ID.
    tarefa = Tarefa.query.get_or_404(id)

    # Remove a tarefa.
    db.session.delete(tarefa)

    # Salva a alteração.
    db.session.commit()

    # Retorna para a página inicial.
    return redirect('/')

@app.route('/concluir/<int:id>')
def concluir(id):
    """
    Altera o status da tarefa para Concluída.
    """

    # Procura a tarefa pelo ID.
    tarefa = Tarefa.query.get_or_404(id)

    # Atualiza o status.
    tarefa.status = "Concluída"

    # Salva no banco.
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)