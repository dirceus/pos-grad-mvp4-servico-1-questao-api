from flask import redirect, make_response
from flask_cors import CORS
from flask_openapi3 import Tag, Info, OpenAPI

from src.domain.use_cases.buscar_questoes_por_filtro import BuscarQuestoesPorFiltro
from src.domain.use_cases.cadastrar_questao import CadastrarQuestao
from src.domain.use_cases.exibir_questao import ExibirQuestao
from src.domain.use_cases.proxima_questao import ProximaQuestao
from src.domain.use_cases.excluir_questao import ExcluirQuestao
from src.domain.use_cases.listar_assuntos_por_disciplina import ListarAssuntosPorDisciplina
from src.domain.use_cases.listar_questoes import ListarQuestoes
from src.domain.use_cases.obter_disciplina_com_machine_learning import ObterDisciplinaComMachineLearning
from src.infrastructure.db.repositories_impl.assunto_repository_db_impl import AssuntoRepositoryDbImpl
from src.infrastructure.db.repositories_impl.questao_repository_db_impl import QuestaoRepositoryDbImpl
from src.api.schemas.error import ErrorSchema
from src.api.schemas.questao_schemas import QuestaoPath, QuestaoSchema, CadastrarQuestaoSchema, \
    QuestaoSimplesSchema, FiltroQuestaoSchema, BuscarAssuntoQueryString, AssuntoSchema, ResultadoBooleanoSchema, \
    BuscarDisciplina, DisciplinaSchema
from src.api.utils.handle_errors import handle_errors
from src.api.utils.serializer import serializa_dto

info = Info(title="Base de Questões API", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)

# instanciando repositórios
questao_repository = QuestaoRepositoryDbImpl()
assunto_repository = AssuntoRepositoryDbImpl()

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
questao_tag = Tag(name="Questão", description="Adição, consulta, visualização e desativação de questões na base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.get('/api/questao/listar', tags=[questao_tag],
         responses={"200": QuestaoSimplesSchema, "500": ErrorSchema})
def listar_todas():
    """ Obtêm todas as questões cadastradas em uma representação minimalista, ou seja, apenas os atributos básico da questão

    Retorna todas as questões ativas.
    """
    try:
        use_case_listar_questoes = ListarQuestoes(questao_repository)
        resultado = use_case_listar_questoes.execute(None)
        return make_response(serializa_dto(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)


@app.get('/api/questao/exibir/<int:codigo>', tags=[questao_tag],
         responses={"200": QuestaoSchema, "400": ErrorSchema, "500": ErrorSchema})
def exibir(path: QuestaoPath):
    """Obtêm uma questão a partir de seu código

    :param path: Identificador da questão
    :return: Retorna uma representação de questão completa(com todos os atributos) de acordo com código.
    """
    try:
        use_case_exibir_questao = ExibirQuestao(questao_repository)
        resultado = use_case_exibir_questao.execute(path.codigo)
        return make_response(serializa_dto(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)

@app.get('/api/questao/proxima/<int:codigo>', tags=[questao_tag],
         responses={"200": QuestaoSchema, "400": ErrorSchema, "500": ErrorSchema})
def exibir_proxima(path: QuestaoPath):
    """Obtêm a próxima questão de multipla escolha cujo id é maior que o informado

    :param path: Identificador da última questão
    :return: Retorna uma representação de questão completa(com todos os atributos) do tipo de multipla escolha.
    """
    try:
        use_case_proxima_questao = ProximaQuestao(questao_repository)
        resultado = use_case_proxima_questao.execute(path.codigo)
        return make_response(serializa_dto(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)


@app.post('/api/questao/cadastrar', tags=[questao_tag],
          responses={"200": QuestaoSchema, "500": ErrorSchema}, )
def cadastrar(body: CadastrarQuestaoSchema):
    """Adiciona uma nova questão na base de dados

    Retorna a representação da questão cadastrada.
    """
    try:
        cadastro_questao_request = body.to_dto()
        use_case_cadastrar_questao = CadastrarQuestao(questao_repository, assunto_repository)
        resultado = use_case_cadastrar_questao.execute(cadastro_questao_request)

        return make_response(serializa_dto(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)


@app.get('/api/questao/buscar', tags=[questao_tag],
         responses={"200": QuestaoSimplesSchema, "400": ErrorSchema, "500": ErrorSchema})
def buscar(query: FiltroQuestaoSchema):
    """Faz uma busca de acordo com filtro de pesquisa.
       Retorna as questões em uma representação minimalista atendendo aos critérios de busca.
    """
    try:
        filtro_request = query.to_dto()
        use_case_buscar_questoes_por_filtro = BuscarQuestoesPorFiltro(questao_repository)
        resultado = use_case_buscar_questoes_por_filtro.execute(filtro_request)
        return make_response(serializa_dto(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)


@app.get('/api/questao/assuntos', tags=[questao_tag],
         responses={"200": AssuntoSchema, "404": ErrorSchema, "500": ErrorSchema})
def listar_assuntos(query: BuscarAssuntoQueryString):
    """
    Obtêm todos os assuntos associados a uma disciplina.
    :param query: identificador da disciplina
    :return: lista dos assuntos associados a uma disciplina
    """
    try:
        use_case_listar_assuntos = ListarAssuntosPorDisciplina(assunto_repository)
        resultado = use_case_listar_assuntos.execute(query.disciplina)
        return make_response(serializa_dto(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)


@app.delete('/api/questao/excluir/<int:codigo>', tags=[questao_tag],
            responses={"200": ResultadoBooleanoSchema, "400": ErrorSchema, "404": ErrorSchema, "500": ErrorSchema})
def excluir(path: QuestaoPath):
    """Exclui logicamente uma questão da base de dados

    :param path: Identificador da questão
    """
    try:
        use_case_excluir_questao = ExcluirQuestao(questao_repository)
        resultado = use_case_excluir_questao.execute(path.codigo)
        return make_response(serializa_dto({"resultado": resultado}), 200)
    except Exception as ex:
        return handle_errors(ex)


@app.get('/api/questao/predicao_disciplina', tags=[questao_tag],
         responses={"200": DisciplinaSchema, "404": ErrorSchema, "500": ErrorSchema})
def obter_disciplina(query: BuscarDisciplina):
    """
    Obtêm disciplina através predição a partir do conteúdo do enunciado.
    :param query: Enunciado
    :return: DisciplinaEnum
    """
    try:
        use_case_obter_disciplina_com_machine_learning = ObterDisciplinaComMachineLearning()
        resultado = use_case_obter_disciplina_com_machine_learning.execute(query.enunciado)
        return make_response(serializa_dto(resultado), 200)
    except Exception as ex:
        return handle_errors(ex)
