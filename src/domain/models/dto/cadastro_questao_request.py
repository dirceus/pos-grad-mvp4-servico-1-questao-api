from typing import List

from src.domain.models.assunto import Assunto
from src.domain.models.dto.alternativa_request import AlternativaRequest
from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.enum.origem import OrigemEnum
from src.domain.models.enum.tipo_questao_enum import TipoQuestaoEnum
from src.domain.models.questao import Questao


class CadastroQuestaoRequest:

    def __init__(self,
                 tipo: TipoQuestaoEnum,
                 enunciado: str,
                 alternativas: List[AlternativaRequest],
                 instituicao: str,
                 ano: int,
                 origem: OrigemEnum,
                 origem_descricao: str,
                 disciplina: DisciplinaEnum,
                 assuntos: List[int]):
        self.tipo = tipo
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.instituicao = instituicao
        self.ano = ano
        self.origem = origem
        self.origem_descricao = origem_descricao
        self.disciplina = disciplina
        self.assuntos = assuntos

    def to_model(self, assuntos: List[Assunto]) -> Questao:
        return Questao(None,
                       self.tipo,
                       self.enunciado,
                       list(map(lambda it: it.to_model(), self.alternativas)),
                       self.instituicao,
                       self.ano,
                       self.origem,
                       self.origem_descricao,
                       self.disciplina,
                       assuntos,
                       None
                       )
