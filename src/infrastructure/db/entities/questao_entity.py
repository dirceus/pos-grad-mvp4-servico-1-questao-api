from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, Boolean, Table, ForeignKey, Text
from sqlalchemy.orm import relationship

from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.enum.origem import OrigemEnum
from src.domain.models.enum.tipo_questao_enum import TipoQuestaoEnum
from src.domain.models.questao import Questao
from src.infrastructure.db.connection import Base
from src.infrastructure.db.entities.alternativa_entity import AlternativaEntity
from src.infrastructure.db.entities.assunto_entity import AssuntoEntity

association_table = Table(
   "questao_assunto",
   Base.metadata,
    Column("questao_id", ForeignKey("questao.pk_questao"), primary_key=True),
   Column("assunto_id", ForeignKey("assunto.pk_assunto"), primary_key=True)
 )


class QuestaoEntity(Base):
    __tablename__ = "questao"

    id = Column("pk_questao", Integer, primary_key=True)
    tipo = Column(String(100))
    disciplina = Column(String(100))
    assuntos = relationship("AssuntoEntity", secondary=association_table, viewonly=True)
    ano = Column(Integer)
    instituicao = Column(String(100))
    origem = Column(String(100))
    origem_descricao = Column(String(200))

    enunciado = Column(Text)
    alternativas = relationship("AlternativaEntity", cascade="all, delete-orphan")

    cadastrador = Column(String(140))
    data_cadastro = Column(DateTime, default=datetime.now())
    ativo = Column(Boolean, default=True)

    def __init__(self, questao: Questao):
        self.tipo = questao.tipo.name
        self.disciplina = questao.disciplina.name
        self.assuntos = list(map(lambda a: AssuntoEntity(a), questao.assuntos))
        self.ano = questao.ano
        self.instituicao = questao.instituicao
        self.origem = questao.origem.name
        self.origem_descricao = questao.origem_descricao
        self.enunciado = questao.enunciado
        self.alternativas = list(map(lambda a: AlternativaEntity(a), questao.alternativas))
        self.cadastrador = questao.cadastrador
        if questao.data_cadastro:
            self.data_cadastro = questao.data_cadastro
        self.ativo = questao.ativo

    def to_model(self) -> Questao:
        return Questao(self.id,
                       TipoQuestaoEnum[self.tipo],
                       self.enunciado,
                       list(map(lambda a: a.to_model(), self.alternativas)),
                       self.instituicao,
                       self.ano,
                       OrigemEnum[self.origem],
                       self.origem_descricao,
                       DisciplinaEnum[self.disciplina],
                       list(map(lambda a: a.to_model(), self.assuntos)),
                       self.cadastrador,
                       self.data_cadastro,
                       self.ativo)
