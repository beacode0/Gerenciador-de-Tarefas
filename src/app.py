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
    Esta rota é responsável por exibir a página inicial
    e cadastrar uma nova tarefa.
    """

    # Se o usuário clicar no botão "Cadastrar"
    if request.method == 'POST':

        # Recebo os dados enviados pelo formulário.
        titulo = request.form['titulo']
        descricao = request.form['descricao']

        # Crio um objeto da classe Tarefa.
        nova_tarefa = Tarefa(
            titulo=titulo,
            descricao=descricao
        )

        # Salvo a tarefa no banco de dados.
        db.session.add(nova_tarefa)
        db.session.commit()

        # Após salvar, volto para a página inicial.
        return redirect('/')

    # Busco todas as tarefas cadastradas.
    tarefas = Tarefa.query.all()

    return render_template(
        'index.html',
        tarefas=tarefas
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