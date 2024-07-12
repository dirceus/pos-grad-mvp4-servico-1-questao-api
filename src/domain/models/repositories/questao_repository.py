from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.models.dto.filtro_questao_request import FiltroQuestaoRequest
from src.domain.models.questao import Questao


class QuestaoRepository(ABC):

    @abstractmethod
    def obter_por_filtro(self, filtro: FiltroQuestaoRequest) -> List[Questao]:
        pass

    @abstractmethod
    def obter_por_codigo(self, codigo: int) -> Optional[Questao]:
        pass

    def obter_proxima_questao(self, codigo: int) -> Optional[Questao]:
        pass

    @abstractmethod
    def obter_todos(self) -> List[Questao]:
        pass

    @abstractmethod
    def salvar(self, questao: Questao) -> Questao:
        pass

    @abstractmethod
    def excluir_questao(self, codigo: int) -> bool:
        pass
