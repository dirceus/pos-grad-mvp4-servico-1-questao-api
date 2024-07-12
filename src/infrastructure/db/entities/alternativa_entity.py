from sqlalchemy import Column, Integer, Boolean, ForeignKey, Text

from src.domain.models.alternativa import Alternativa
from src.infrastructure.db.connection import Base


class AlternativaEntity(Base):
    __tablename__ = 'alternativa'

    id = Column("pk_alternativa", Integer, primary_key=True)
    descricao = Column(Text)
    is_correta = Column(Boolean)
    questao = Column(Integer, ForeignKey("questao.pk_questao"), nullable=False)

    def __init__(self, alternativa: Alternativa):
        self.descricao = alternativa.descricao
        self.is_correta = alternativa.is_correta

    def to_model(self) -> Alternativa:
        return Alternativa(self.id, self.descricao, self.is_correta)

