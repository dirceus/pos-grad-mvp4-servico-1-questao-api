from src.domain.models.dto.assunto_response import AssuntoResponse
from src.domain.models.dto.questao_simples_response import QuestaoSimplesResponse
from src.domain.models.questao import Questao


class QuestaoCompletaResponse(QuestaoSimplesResponse):

    def __init__(self, questao: Questao):
        super().__init__(questao)
        self.alternativas = questao.alternativas
        self.assuntos = list(map(lambda a: AssuntoResponse(a), questao.assuntos))
        self.ativo = questao.ativo
