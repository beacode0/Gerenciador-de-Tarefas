# Gerenciador de Tarefas

## Descrição

O Gerenciador de Tarefas é uma aplicação web desenvolvida em Python utilizando o framework Flask. O sistema permite o gerenciamento de tarefas por meio de operações básicas de cadastro, visualização, edição e exclusão.

## Objetivo

O objetivo do projeto é aplicar conceitos de Engenharia de Software, versionamento com Git e GitHub, metodologias ágeis, testes automatizados e integração contínua.

## Tecnologias Utilizadas

* Python
* Flask
* HTML5
* CSS3
* SQLite
* Pytest
* GitHub Actions

## Estrutura Inicial

Nesta primeira etapa foi criada a estrutura base do projeto, incluindo:

* Organização de diretórios
* Ambiente virtual Python
* Configuração inicial do Flask
* Arquivos de documentação
* Configuração do Git


## Desenvolvimento

### Etapa 1 – Configuração Inicial

Nesta etapa foi realizada a configuração do ambiente de desenvolvimento para iniciar o projeto. As seguintes atividades foram concluídas:

* Criação do ambiente virtual (venv) para isolamento das dependências do projeto;
* Instalação das bibliotecas necessárias, como Flask, Flask-SQLAlchemy e Pytest;
* Geração do arquivo `requirements.txt`, contendo todas as dependências utilizadas;
* Organização da estrutura inicial de diretórios (`src`, `templates`, `static`, `tests`, `docs` e `.github`);
* Criação do arquivo principal da aplicação (`app.py`);
* Desenvolvimento da primeira página HTML (`index.html`);
* Criação do arquivo de estilos (`style.css`);
* Configuração inicial do repositório para utilização do Git.

Com essa estrutura preparada, o projeto está pronto para iniciar o desenvolvimento das funcionalidades do sistema, começando pela modelagem do banco de dados e implementação do cadastro de tarefas.


### Etapa 2 – Configuração do Banco de Dados

Nesta etapa foi realizada a configuração do banco de dados utilizando SQLite em conjunto com o Flask-SQLAlchemy.

Também foi criada a classe `Tarefa`, responsável por representar as informações de cada tarefa cadastrada no sistema. Inicialmente, foram definidos os campos de identificação, título, descrição e status.

Além disso, foi configurada a criação automática do banco de dados e das tabelas sempre que a aplicação for executada pela primeira vez, permitindo que o sistema esteja preparado para armazenar as informações dos usuários.


### Etapa 3 – Cadastro e Listagem de Tarefas

Nesta etapa foi implementada a principal funcionalidade do sistema: o cadastro de tarefas.

Foi desenvolvido um formulário para que o usuário possa informar o título e a descrição da tarefa. Após o envio, as informações são armazenadas no banco de dados SQLite utilizando o Flask-SQLAlchemy.

Além disso, foi criada a listagem dinâmica das tarefas cadastradas na página inicial, permitindo visualizar todas as informações registradas no sistema de forma organizada.

Também foi realizada a estilização da interface utilizando CSS, proporcionando uma experiência visual mais agradável e intuitiva para o usuário.


## Etapa 4 – Edição de Tarefas

Nesta etapa foi implementada a funcionalidade de edição das tarefas cadastradas.

Foi criada uma rota específica para localizar a tarefa pelo seu identificador, permitindo alterar o título e a descrição. Após a atualização, as alterações são gravadas no banco de dados e exibidas imediatamente na página inicial.

Também foi realizada uma melhoria na interface, adicionando um botão de edição com estilo compatível com a identidade visual do sistema Organiza+.

## Etapa 5 – Conclusão de Tarefas

Nesta etapa foi implementada a funcionalidade de conclusão de tarefas.

Foi criada uma rota responsável por alterar o status de uma tarefa para "Concluída". A interface foi atualizada para exibir o status por meio de selos coloridos, facilitando a identificação visual das tarefas pendentes e concluídas.

Também foi adicionado um botão para marcar tarefas como concluídas, tornando o gerenciamento mais prático e intuitivo para o usuário.
 
## Etapa 6 – Dashboard do Sistema

Nesta etapa foi desenvolvido um painel de informações para fornecer uma visão geral das tarefas cadastradas no sistema.

Foram implementados três indicadores principais:

- Total de tarefas cadastradas;
- Quantidade de tarefas pendentes;
- Quantidade de tarefas concluídas.

Esses dados são calculados automaticamente sempre que uma tarefa é criada, concluída ou removida, permitindo ao usuário acompanhar rapidamente o andamento das suas atividades.

Além da implementação do dashboard, também foram realizadas melhorias na interface do Organiza+, tornando a aplicação mais organizada, agradável e intuitiva para o usuário.

## Etapa 7 – Implementação da Prioridade das Tarefas

Nesta etapa foi iniciada a implementação da funcionalidade de prioridade das tarefas.

Agora, ao cadastrar uma nova tarefa, o usuário pode escolher entre três níveis de prioridade:

- 🟢 Baixa
- 🟡 Média
- 🔴 Alta

Essa funcionalidade foi adicionada após o escopo inicial do projeto, simulando uma nova solicitação do cliente e demonstrando a adaptação do sistema a novos requisitos durante o desenvolvimento.

## Etapa 8 – Edição da Prioridade

Foi adicionada a possibilidade de alterar a prioridade de uma tarefa já cadastrada.

Com isso, o usuário pode modificar o título, a descrição e também a prioridade da tarefa, mantendo as informações sempre atualizadas.

## Etapa 9 – Estrutura para Testes Automatizados

Nesta etapa foram implementados testes automatizados utilizando o framework Pytest.

Foi criado um teste para verificar se a página inicial da aplicação responde corretamente (status HTTP 200), garantindo que o sistema esteja acessível e funcionando corretamente.

A utilização de testes automatizados contribui para a qualidade do software, permitindo identificar problemas rapidamente sempre que novas alterações forem realizadas.

## Etapa 10 – Integração Contínua (GitHub Actions)

Foi configurado um workflow utilizando o GitHub Actions para automatizar a execução dos testes da aplicação.

Sempre que um novo código é enviado ao repositório (push) ou um Pull Request é criado, o GitHub instala automaticamente as dependências do projeto e executa os testes implementados com Pytest.

Essa prática auxilia na identificação rápida de erros e garante maior qualidade durante o desenvolvimento.


## Etapa 11 – Modelagem UML

Foram elaborados dois diagramas UML para representar a estrutura e o funcionamento do sistema:

- **Diagrama de Casos de Uso:** apresenta as principais funcionalidades disponíveis ao usuário, como cadastrar, visualizar, editar, excluir e concluir tarefas.

- **Diagrama de Classes:** representa a estrutura da classe `Tarefa`, seus atributos e as principais operações realizadas pelo sistema.

A modelagem UML contribuiu para a organização do projeto e facilitou a compreensão da arquitetura da aplicação antes e durante o desenvolvimento.
## Autor

Beatriz Alves Santos
