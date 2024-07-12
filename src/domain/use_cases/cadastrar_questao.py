from datetime import datetime

from src.domain.commons.use_case import UseCase
from src.domain.commons.usuario_logado import obter_usuario_logado
from src.domain.models.dto.cadastro_questao_request import CadastroQuestaoRequest
from src.domain.models.dto.questao_completa_response import QuestaoCompletaResponse
from src.domain.models.repositories.assunto_repository import AssuntoRepository
from src.domain.models.repositories.questao_repository import QuestaoRepository


class CadastrarQuestao(UseCase):

    def __init__(self, repositorio: QuestaoRepository, assunto_repository: AssuntoRepository):
        self.__repositorio = repositorio
        self.__assunto_repositorio = assunto_repository

    def execute(self, request: CadastroQuestaoRequest):
        nome_cadastrador = obter_usuario_logado()
        assuntos = list(map(lambda a: self.__assunto_repositorio.obter_por_codigo(a), request.assuntos))
        questao = request.to_model(assuntos)
        questao.cadastrador = nome_cadastrador
        questao.data_cadastro = datetime.now()
        return QuestaoCompletaResponse(self.__repositorio.salvar(questao))
