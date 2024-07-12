from sqlalchemy import Column, String, Integer

from src.domain.models.assunto import Assunto
from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.infrastructure.db.connection import Base


class AssuntoEntity(Base):
    __tablename__ = "assunto"

    id = Column("pk_assunto", Integer, primary_key=True)
    disciplina = Column(String(100))
    descricao = Column(String(200))

    def __init__(self, assunto: Assunto):
        self.id = assunto.codigo
        self.disciplina = assunto.disciplina.name
        self.descricao = assunto.descricao

    def to_model(self) -> Assunto:
        return Assunto(self.id,
                       DisciplinaEnum[self.disciplina],
                       self.descricao)



