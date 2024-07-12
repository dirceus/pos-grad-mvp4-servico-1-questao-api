from typing import List


from datetime import datetime

from src.domain.models.alternativa import Alternativa
from src.domain.models.assunto import Assunto
from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.enum.origem import OrigemEnum
from src.domain.models.enum.tipo_questao_enum import TipoQuestaoEnum


class Questao:

    def __init__(self, codigo: int,
                 tipo: TipoQuestaoEnum,
                 enunciado: str,
                 alternativas: List[Alternativa],
                 instituicao: str,
                 ano: int,
                 origem: OrigemEnum,
                 origem_descricao: str,
                 disciplina: DisciplinaEnum,
                 assuntos: List[Assunto],
                 cadastrador: str,
                 data_cadastro: datetime = None,
                 ativo: bool = True
                 ):
        self.codigo = codigo
        self.tipo = tipo
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.instituicao = instituicao
        self.ano = ano
        self.origem = origem
        self.origem_descricao = origem_descricao
        self.disciplina = disciplina
        self.assuntos = assuntos
        self.cadastrador = cadastrador
        self.data_cadastro = data_cadastro
        self.ativo = ativo
