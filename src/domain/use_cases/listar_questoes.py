from src.domain.commons.use_case import UseCase
from src.domain.models.dto.questao_simples_response import QuestaoSimplesResponse
from src.domain.models.repositories.questao_repository import QuestaoRepository


class ListarQuestoes(UseCase):

    def __init__(self, repositorio: QuestaoRepository):
        self.__repositorio = repositorio

    def execute(self, request):
        return list(map(lambda it: QuestaoSimplesResponse(it), self.__repositorio.obter_todos()))
