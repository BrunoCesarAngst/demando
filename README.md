# Demando

> **Status: projeto independente histórico, sem manutenção ativa.** Esta é a implementação preservada do estudo de gestão de demandas. Não é anunciado como serviço disponível, produto finalizado ou aplicação segura para uso em produção.

**O que pode ser avaliado:** [modelo de demandas](demandas/models.py), [fluxos de autenticação, listagem e operações](demandas/views.py) e [rotas da aplicação](demandas/urls.py). Há pendências de testes e autorização documentadas abaixo; não é necessário executar o sistema para compreender o escopo desenvolvido.

Aplicação web para gestão de demandas e tarefas, construída com Django e uma API REST documentada.

O projeto concentra-se em um problema recorrente de sistemas de trabalho: registrar responsabilidades, acompanhar o estado das demandas e oferecer diferentes superfícies de uso sem duplicar a lógica central.

## Em um minuto: problema, solução e evidências

- **Problema:** gerir demandas por interface web e API sem duplicar a lógica de domínio.
- **Escopo do projeto:** aplicação pública de estudo aplicado; sem alegações de adoção comercial.
- **Solução documentada:** aplicação Django com autenticação, operações de demandas, API REST e documentação interativa.
- **Tecnologias:** Python, Django, Django REST Framework, HTMX, SQLite e Swagger/ReDoc.
- **Resultado verificável:** estrutura de aplicação, dependências em [requirements.txt](requirements.txt) e rotas de documentação descritas neste README. Não há resultado operacional quantificado.

**Como verificar:** examine `demandas/`, `demando/` e inicie o servidor local conforme os passos abaixo.

## Evidências no código (inspeção de outubro de 2026)

| Funcionalidade encontrada | Onde conferir | Limite da evidência |
| --- | --- | --- |
| Modelo de demanda com título, descrição, datas, usuário proprietário e indicador de conclusão | [models.py](demandas/models.py) | Persistência modelada; sem volume real de registros |
| Listagem com paginação de dez itens por página e resposta parcial para requisições HTMX | [views.py](demandas/views.py) | Paginação configurada; sem medição de performance |
| Cadastro, autenticação e criação de demandas vinculadas ao usuário autenticado | [views.py](demandas/views.py) | Os fluxos foram identificados no código; autorização por objeto exige revisão |
| Estrutura de testes Django | [tests.py](demandas/tests.py) | **Ainda não há casos de teste implementados nesse arquivo** |

**Resultado demonstrável:** aplicação de gestão de demandas com modelo, views e interface/API documentadas. **Atenção técnica:** revisar proteção CSRF e controles de autorização antes de qualquer uso real.

## Visão do sistema

Demando combina:

- interface web para operação cotidiana;
- autenticação de usuários;
- criação, edição e conclusão de demandas;
- API REST para integração;
- documentação interativa dos endpoints;
- área administrativa fornecida pelo ecossistema Django.

## Arquitetura

```mermaid
flowchart LR
    U[Usuário] --> H[Interface HTML / HTMX]
    C[Cliente externo] --> A[API REST]
    H --> D[Django]
    A --> R[Django REST Framework]
    D --> M[Modelo de demandas]
    R --> M
    M --> B[(Banco de dados)]
    A --> S[Swagger / ReDoc]
```

## Stack

**Aplicação**  
`Python 3.10` · `Django 5.1` · templates Django · `HTMX`

**API**  
`Django REST Framework` · `drf-yasg` · Swagger · ReDoc

**Persistência e configuração**  
`SQLite` · `python-dotenv`

## Funcionalidades presentes ou descritas no código

- cadastro, login e logout;
- criação e edição de demandas;
- conclusão e exclusão de tarefas;
- visualização organizada dos registros;
- API REST para acesso programático;
- documentação navegável da API;
- administração do sistema;
- interface adaptável para desktop e dispositivos móveis.

## Estrutura

```text
/
├── demandas/
│   ├── migrations/       # evolução do schema
│   ├── templates/        # interface web
│   ├── urls.py           # rotas do domínio
│   └── views.py          # comportamento da aplicação
├── demando/
│   ├── settings.py       # configuração
│   └── urls.py           # composição das rotas
├── requirements.txt
└── manage.py
```

## Execução local

```bash
git clone https://github.com/BrunoCesarAngst/demando.git
cd demando
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Crie um arquivo `.env`:

```env
AMBIENTE=desenvolvimento
SECRET_KEY=defina-uma-chave-local
DEBUG=True
```

Prepare o banco e inicie a aplicação:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Aplicação: `http://127.0.0.1:8000/`

## Documentação da API

- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

A documentação interativa permite inspecionar contratos e testar endpoints durante o desenvolvimento.

## Decisões de engenharia demonstradas

- uma camada de domínio atendendo interface e API;
- rotas separadas por responsabilidade;
- migrações versionadas para evolução dos dados;
- configuração sensível fora do código;
- documentação gerada a partir da API;
- uso da administração do Django como ferramenta operacional;
- possibilidade de evolução gradual do front-end sem substituir o back-end.

## Possíveis evoluções

- substituir SQLite por PostgreSQL em ambientes compartilhados;
- introduzir testes automatizados de domínio e API;
- adicionar filtros, prioridades e responsáveis;
- criar trilha de auditoria para mudanças de estado;
- modelar permissões mais granulares;
- preparar execução conteinerizada.

## Estado do projeto

Projeto independente interrompido e preservado como registro de aprendizado e implementação. Demonstra modelagem, views, API e uso integrado do ecossistema Django, mas não foi validado aqui como produto pronto para produção.

---

[Perfil de Bruno César Angst](https://github.com/BrunoCesarAngst) · [Site](https://brunoangst.com.br/)
