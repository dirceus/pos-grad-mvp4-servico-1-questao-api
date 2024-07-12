from typing import List, Optional

from src.domain.models.dto.filtro_questao_request import FiltroQuestaoRequest
from src.domain.models.questao import Questao
from src.domain.models.repositories.questao_repository import QuestaoRepository
from src.infrastructure.memory.repositories_impl.alternativa_repository_mem_impl import AlternativaRepositoryMemImpl


class QuestaoRepositoryMemImpl(QuestaoRepository):

    def __init__(self, alternativa_repository: AlternativaRepositoryMemImpl):
        self.__base = []
        self.__alternativa_repository = alternativa_repository

    def obter_por_filtro(self, filtro: FiltroQuestaoRequest) -> List[Questao]:
        pass

    def obter_por_codigo(self, codigo: int) -> Optional[Questao]:
        resultado = list(filter(lambda it: it.codigo == codigo, self.__base))
        if len(resultado) == 1:
            return resultado[0]
        return None

    def obter_proxima_questao(self, codigo: int) -> Optional[Questao]:
        return None

    def obter_todos(self) -> List[Questao]:
        return list(filter(lambda it: it.ativo, self.__base))

    def salvar(self, questao: Questao) -> Questao:
        questao.codigo = self.total_questoes() + 1
        for alternativa in questao.alternativas:
            alternativa.codigo = self.__alternativa_repository.total_alternativas() + 1
            self.__alternativa_repository.salvar(alternativa)
        self.__base.append(questao)
        return questao

    def total_questoes(self):
        return len(self.__base)

    def excluir_questao(self, codigo: int) -> bool:
        pass
