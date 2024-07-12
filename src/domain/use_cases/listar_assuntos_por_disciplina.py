from src.domain.commons.use_case import UseCase
from src.domain.models.dto.assunto_response import AssuntoResponse
from src.domain.models.repositories.assunto_repository import AssuntoRepository


class ListarAssuntosPorDisciplina(UseCase):

    def __init__(self, repositorio: AssuntoRepository):
        self.__repositorio = repositorio

    def execute(self, request):
        return list(map(lambda it: AssuntoResponse(it), self.__repositorio.buscar_por_disciplina(request)))