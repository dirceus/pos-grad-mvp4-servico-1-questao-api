from src.domain.commons.exceptions import QuestaoNotFoundException
from src.domain.commons.use_case import UseCase
from src.domain.models.dto.questao_completa_response import QuestaoCompletaResponse
from src.domain.models.repositories.questao_repository import QuestaoRepository


class ProximaQuestao(UseCase):

    def __init__(self, repositorio: QuestaoRepository):
        self.__repositorio = repositorio

    def execute(self, request):
        questao = self.__repositorio.obter_proxima_questao(request)
        if questao is None:
            raise QuestaoNotFoundException(request)
        else:
            return QuestaoCompletaResponse(questao)
