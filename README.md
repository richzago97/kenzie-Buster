

# Documentação do Projeto de Gerenciamento de Usuários, Filmes e Compras

## Visão Geral
Este projeto visava criar uma aplicação de gerenciamento de usuários, filmes e compras, incorporando autenticação e controle de permissões de acesso a diferentes rotas da aplicação. A aplicação foi desenvolvida em Python, utilizando o framework Django, que oferece uma estrutura sólida para o desenvolvimento web.

## Funcionalidades Principais
O projeto incluiu as seguintes funcionalidades principais:

1. **Autenticação de Usuários**: Os usuários poderiam se cadastrar, fazer login e gerenciar suas contas.

2. **Gestão de Filmes**: A aplicação permitia a adição, edição e remoção de filmes. Informações detalhadas sobre cada filme, como título, gênero, classificação, diretor e data de lançamento, eram armazenadas no banco de dados.

3. **Gestão de Compras**: Os usuários podiam navegar pela lista de filmes disponíveis e fazer compras. O sistema rastreava o histórico de compras de cada usuário.

4. **Controle de Permissões**: Foi implementado um sistema de controle de permissões para diferentes tipos de usuários, com base em funções (por exemplo, administrador, usuário regular, etc.). As rotas e funcionalidades eram restritas com base nas permissões do usuário.

## Executando o Projeto
Para executar o projeto, siga estas etapas:

1. Clone o repositório para o seu ambiente local:
   ```shell
   git clone https://github.com/seuusuario/seuprojeto.git
   ```

2. Navegue até o diretório do projeto:
   ```shell
   cd seuprojeto
   ```

3. Crie um ambiente virtual Python (recomendado) e ative-o:
   ```shell
   python -m venv venv
   source venv/bin/activate
   ```

4. Instale as dependências do projeto usando o `requirements.txt`:
   ```shell
   pip install -r requirements.txt
   ```

5. Aplique as migrações do banco de dados:
   ```shell
   python manage.py migrate
   ```

6. Inicie o servidor de desenvolvimento:
   ```shell
   python manage.py runserver
   ```

7. Acesse a aplicação no seu navegador em [http://localhost:8000](http://localhost:8000).

