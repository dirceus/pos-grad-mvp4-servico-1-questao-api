from typing import List

from src.domain.commons.exceptions import InvalidInputException
from src.domain.models.assunto import Assunto
from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.repositories.assunto_repository import AssuntoRepository
from src.infrastructure.db.connection import Session
from src.infrastructure.db.entities.assunto_entity import AssuntoEntity


class AssuntoRepositoryDbImpl(AssuntoRepository):

    def buscar_por_disciplina(self, disciplina: DisciplinaEnum) -> List[Assunto]:
        session = Session()
        assuntos = session.query(AssuntoEntity).filter(AssuntoEntity.disciplina == disciplina.name)
        return list(map(lambda q: q.to_model(), assuntos))

    def obter_por_codigo(self, codigo: int) -> Assunto:
        session = Session()
        assunto = session.query(AssuntoEntity).filter(AssuntoEntity.id == codigo).first()
        if assunto:
            return assunto.to_model()
        raise InvalidInputException("Codigo de Assunto inválido: "+str(codigo))