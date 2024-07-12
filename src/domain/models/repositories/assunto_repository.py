from abc import ABC, abstractmethod
from typing import Optional, List

from src.domain.models.assunto import Assunto
from src.domain.models.enum.disciplina_enum import DisciplinaEnum


class AssuntoRepository(ABC):

    @abstractmethod
    def buscar_por_disciplina(self, disciplina: DisciplinaEnum) -> List[Assunto]:
        pass

    @abstractmethod
    def obter_por_codigo(self, codigo: int) -> Assunto:
        pass

