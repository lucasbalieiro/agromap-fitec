# AgroMap - Teste Tecnico para Dev Backend Python @ FITec

## Indice de Perguntas do Teste
 1. Descreva as etapas para executar configuração Inicial do Projeto
 2. Defina e escolha e Configuração do ORM
 3. Como versionar e organizar as migrações de Banco de Dados
 4. Defina a tecnologia e a forma de uso a Autenticação e Autorização
 5. Informe os métodos e ferramentas para gerar a Documentação da API
 6. Se necessário como deve ser tratada a integração com Outros Serviços
 7. Como corrigir e evitar erros de Configuração de Ambiente
 8. Quais os principais casos de problemas de Serialização/Deserialização
 9. Defina os critérios para criar uma consulta eficiente
 10. Como tratar o retorno de falhas de Transação
 11. Explique o formato correto de manipulação de Conexões de Dados
 12. Como evitar e tratar os Problemas de Concurrency
 13. Como deve ser feito o despejo e configuração de logs
 14. Defina a Modularização e Organização do Código
 15. Utilização de Dependências e Middleware para Reutilização de Código


### Introducao.
Para o desenvolvimento deste projeto nao temos muito informacoes alem de ser algo voltado pro 'Agronegocio e GEO'. Entao, algumas decisoes vao ser tomadas a partir das 'vozes da minha cabeca', vulgo experiencia.
Estou assumindo que o ambiente de desenvolvimento, homologacao e producao estao rodando num ambeinte debian com docker instalados. O framework ASGI utilizado vai ser o [FastAPI](https://fastapi.tiangolo.com/)

### 1 Descreva as etapas para executar configuração Inicial do Projeto

 - Passo 1: Iniciar as configuracoes de versionamento: `git`, `git remote` e `.gitignore`
 - Passo 2: Iniciar o gerenciador de pacotes com os primeiros pacotes essenciais. Vou usar o proprio `pip` junto com [`requirements.txt`](./requirements.txt) e [requirements-dev.txt](./requirements-dev.txt) por questoes de simplicidade.
- Passo 3: Criar um `venv` local para o projeto (Algumas pessoas utilizando o conda). Mas eu prefiro sempre comecar pela solucao mais simples: `python3 -m venv .venv` depois so instalar os pacotes nesse ambiente.
- Passo 4: Iniciar as configuracoes de Docker. Crio um [Dockerfile](./Dockerfile) com a imagem para o backend, outra para o [banco de dados](./db/Dockerfile), que vou utilizar o postgresql. E faco o orquestramento deles via [docker compose](./docker-compose.yml)

### 2 Defina e escolha e Configuração do ORM
Meu ORM de escolha eh o `SQLAlchemy` pela facilidade de utilizacao, documentacao abrangente, junto com um bom suporte da comunidade.
Para a configuracao do ORM vou precisar de dois pacotes `sqlalchemy==2.0.32` e `psycopg2-binary==2.9.9`. O `psycopg2-binary` vai ser o driver o que `sqlalchemy` vai utilizar pra conectar e gerenciar as conexoes e transacoes do nosso querido postgres.
Depois disso, resolvo criar uma funcao de conexao e retorno de uma sessao do banco em [database.py](./app/config/database.py). Isso vai me permitir que eu reutilize com mais facilidade essa funcao de conexao e vai se adequar melhor com a injecao de dependencias do FastAPI

###  3 Como versionar e organizar as migrações de Banco de Dados

Como estou utilizando o SQLAlchemy, nada mais natural do que usar o `alembic` para versionar o banco de dados.

Como nao ha necessidades especificas, as configuracoes inicias do `alembic` podem ser alcancadas atraves do comando 
```bash
alembic init alembic
```

Ele vai gerar uma nova pasta chamada alembic que vai ser a pasta responsavel por armazenas as versoes do banco e algumas configuracoes do alembic. Outro arquivo importante, gerado com esse comando, na raiz do diretorio, é o `alembic.ini`

Para questoes de configuracoes do projeto, vamos mudar a configuracao 
`sqlalchemy.url` (linha 63 de [alembic.ini](./alembic.ini)) para, em vez de receber a url do banco diretamente, agora vai receber atraves da variavel de ambiente configurada em [.env]

E tambem, vou precisar adicionar as linhas 12 e 13 de [alembic/env.py](./alembic/env.py). Para fazer o replace do valor da variavel de ambiente no arquivo `alembic.ini`