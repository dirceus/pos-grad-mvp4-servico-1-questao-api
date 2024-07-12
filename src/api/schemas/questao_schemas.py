from typing import Optional, List

from pydantic import BaseModel, Field

from src.domain.models.dto.alternativa_request import AlternativaRequest
from src.domain.models.dto.cadastro_questao_request import CadastroQuestaoRequest
from src.domain.models.dto.filtro_questao_request import FiltroQuestaoRequest
from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.enum.origem import OrigemEnum
from src.domain.models.enum.tipo_questao_enum import TipoQuestaoEnum


class AlternativaSchema(BaseModel):
    codigo: int
    descricao: str
    is_correta: Optional[bool]


class CadastrarQuestaoSchema(BaseModel):
    tipo: TipoQuestaoEnum
    disciplina: DisciplinaEnum
    ano: int
    instituicao: str
    origem: OrigemEnum
    origem_descricao: Optional[str]
    assuntos: List[int] = Field(description="Códigos dos Assuntos")
    enunciado: str
    alternativas: List[AlternativaSchema] = Field(...)

    def to_dto(self) -> CadastroQuestaoRequest:
        return CadastroQuestaoRequest(self.tipo,
                                      self.enunciado,
                                      list(map(lambda a: AlternativaRequest(a.descricao, a.is_correta),
                                               self.alternativas)),
                                      self.instituicao,
                                      self.ano,
                                      self.origem,
                                      self.origem_descricao,
                                      self.disciplina,
                                      self.assuntos)


class QuestaoSchema(BaseModel):
    codigo: int
    tipo: TipoQuestaoEnum
    disciplina: DisciplinaEnum
    ano: int
    instituicao: str
    origem: OrigemEnum
    origem_descricao: str
    enunciado: str
    assuntos: Optional[List[int]]
    alternativas: List[AlternativaSchema]
    cadastrador: str


class QuestaoSimplesSchema(BaseModel):
    codigo: int
    tipo: TipoQuestaoEnum
    disciplina: DisciplinaEnum
    ano: int
    instituicao: str
    origem: OrigemEnum
    origem_descricao: str
    enunciado: str
    cadastrador: str


class QuestaoPath(BaseModel):
    codigo: int


class BuscarAssuntoQueryString(BaseModel):
    disciplina: DisciplinaEnum


class BuscarDisciplina(BaseModel):
    enunciado: str


class AssuntoSchema(BaseModel):
    codigo: int
    disciplina: DisciplinaEnum
    descricao: str


class DisciplinaSchema(BaseModel):
    disciplina: DisciplinaEnum


class FiltroQuestaoSchema(BaseModel):
    tipo: Optional[TipoQuestaoEnum]
    disciplina: Optional[DisciplinaEnum]
    ano: Optional[int]
    instituicao: Optional[str]
    origem: Optional[OrigemEnum]

    def to_dto(self) -> FiltroQuestaoRequest:
        return FiltroQuestaoRequest(
            self.tipo,
            self.instituicao,
            self.ano,
            self.origem,
            self.disciplina,
        )


class ResultadoBooleanoSchema(BaseModel):
    resultado: bool
