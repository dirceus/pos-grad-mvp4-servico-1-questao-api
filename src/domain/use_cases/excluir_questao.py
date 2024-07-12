from src.domain.commons.exceptions import QuestaoNotFoundException
from src.domain.commons.use_case import UseCase
from src.domain.models.dto.questao_completa_response import QuestaoCompletaResponse
from src.domain.models.repositories.questao_repository import QuestaoRepository


class ExcluirQuestao(UseCase):

    def __init__(self, repositorio: QuestaoRepository):
        self.__repositorio = repositorio

    def execute(self, request):
        return self.__repositorio.excluir_questao(request)
