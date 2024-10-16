# Demando - Gerenciador de Demandas e Tarefas

Bem-vindo ao **Demando**, um aplicativo de gerenciador de tarefas e demandas desenvolvido em Django com Django Rest Framework (DRF) e com a documentação interativa usando `drf_yasg`. Este projeto foi criado para ajudar a organizar tarefas pessoais e colaborativas, permitindo o gerenciamento eficiente de demandas.

## Sumário

1. [Introdução](#introdução)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Funcionalidades](#funcionalidades)
4. [Instalação e Configuração](#instalação-e-configuração)
5. [Como Executar o Projeto](#como-executar-o-projeto)
6. [Documentação da API](#documentação-da-api)
7. [Estrutura do Projeto](#estrutura-do-projeto)
8. [Como Contribuir](#como-contribuir)
9. [Licença](#licença)

## Introdução

O **Demando** é uma aplicação web para gestão de tarefas que permite aos usuários criar, editar e organizar suas demandas. Ele foi desenvolvido com foco em simplicidade e eficiência, visando tanto o uso pessoal quanto a colaboração em equipe.

## Tecnologias Utilizadas

- **Python 3.10**
- **Django 5.1.2**: Framework web utilizado para o desenvolvimento do backend.
- **Django Rest Framework (DRF)**: Utilizado para a criação da API REST.
- **drf_yasg**: Geração da documentação da API usando Swagger e ReDoc.
- **SQLite**: Banco de dados padrão para armazenamento local durante o desenvolvimento.
- **HTMX**: Para interações dinâmicas na interface do usuário.
- **Tailwind CSS**: Utilizado para estilização e criação de uma interface responsiva.

## Funcionalidades

- **Autenticação de Usuário**: Cadastro, login e logout de usuários.
- **CRUD de Demandas**: Criação, edição, exclusão e visualização de demandas.
- **Marcar como Concluído**: Opção de marcar demandas como concluídas.
- **Paginas de Documentação da API**: Visualização interativa da documentação usando Swagger ou ReDoc.
- **Interface Responsiva**: Navegação simples para dispositivos móveis e desktop.

## Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento local:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/demando.git
   cd demando
   ```

2. **Crie e ative um ambiente virtual**:
   ```bash
   python3 -m venv meu_ambiente
   source meu_ambiente/bin/activate  # No Windows: meu_ambiente\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Crie o arquivo `.env`** com as variáveis de ambiente necessárias:
   ```env
   AMBIENTE=desenvolvimento
   SECRET_KEY=sua_chave_secreta_aqui
   DEBUG=True
   ```

5. **Realize as migrações**:
   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário** para acessar a área administrativa:
   ```bash
   python manage.py createsuperuser
   ```

## Como Executar o Projeto

Para iniciar o servidor de desenvolvimento, execute o comando:

```bash
python manage.py runserver
```

Acesse a aplicação em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Documentação da API

A documentação interativa da API está disponível nos seguintes links:

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

Essas páginas oferecem uma interface interativa para testar todos os endpoints da API e verificar suas funcionalidades.

## Estrutura do Projeto

Abaixo, uma breve descrição dos diretórios e arquivos principais:

```
/
|-- demandas/                 # Aplicativo principal
|   |-- migrations/           # Migrações do banco de dados
|   |-- templates/            # Templates HTML
|   |-- urls.py               # Definição das URLs do app demandas
|   |-- views.py              # Lógica das views
|-- demando/
|   |-- settings.py           # Configurações do projeto
|   |-- urls.py               # Definição das URLs principais
|-- requirements.txt          # Dependências do projeto
|-- manage.py                 # Ponto de entrada para comandos do Django
```

## Como Contribuir

Contribuições são bem-vindas! Siga os passos abaixo para contribuir com o projeto:

1. **Faça um fork do repositório**.
2. **Crie uma nova branch** para sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. **Implemente sua funcionalidade**.
4. **Faça o commit de suas alterações**:
   ```bash
   git commit -m "Adiciona minha nova feature"
   ```
5. **Faça push para sua branch**:
   ```bash
   git push origin minha-feature
   ```
6. **Abra um Pull Request** no GitHub.

## Licença

Este projeto é licenciado sob a licença BSD. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
Esperamos que este README ajude a orientar e facilitar o uso e contribuição ao projeto Demando. Em caso de dúvidas, sinta-se à vontade para abrir uma *issue* ou entrar em contato! Feliz codificação! ✌️

