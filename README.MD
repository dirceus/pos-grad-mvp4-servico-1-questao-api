# Base de Questão API

É uma api para implementação dos MVPs do curso de pós-graduação em Engenharia de Software da PUC-RIO.

No primeiro MVP da disciplina **Desenvolvimento Full Stack Básico** foi desenvolvida uma API para cadastrar e consultar
questões dos tipos: múltipla-escolha e verdadeiro-ou-falso, utilizando um banco de dados SQLite e com a API documentada
utilizando o OpenAPI.

Já no segundo MVP da disciplina **Qualidade de Software, Segurança e Sistemas Inteligentes** foi integrado a API um modelo
de machine learning para predição da disciplina de uma questão a partir de seu enunciado. 

---
## Arquitetura da API

A aplicação foi construída base na arquitetura de clean architecture, composto pelas camadas:

- **Domínio** - onde está concentrada a lógica de negócio, essa camada não possui dependência de frameworks.
- **Infraestrutura** - onde estão as tecnologias utilizadas como, por exemplo, banco de dados, log...  
- **API** - camada que interage com os meios externos, sem conter nenhuma regra de negócio.

Estrutura de Pacotes:

- Domain
  - Models
    - DTO
    - Enum
    - Repositories
  - User Cases
- Infrastructure
  - DB
    - Connection
    - Entities
    - Repositories (Implementation)
  - Memory
    - Repositories (Implementation)
  - Machine Learning Model
- API
  - Rest API
  - Schemas


---
## Tecnologias utilizadas

- Python
- Flask
- OpenAPI
- Pydantic
- SQLAlchemy
- SQLite3

## Como executar

1. Baixe ou clone este repositório usando git clone https://github.com/dirceus/pos-grad-mvp1-backend.git;

2. Crie um ambiente virtual do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

3. No ambiente virtual, instale as dependências através do comando:
```
(env)$ pip install -r requirements.txt
```
4. Execute a API através do comando
```
(env)$ flask run --host 0.0.0.0 --port 5000
```
5. Com a aplicação rodando, abra no navegador a url: [http://localhost:5000/#/](http://localhost:5000/#/)
