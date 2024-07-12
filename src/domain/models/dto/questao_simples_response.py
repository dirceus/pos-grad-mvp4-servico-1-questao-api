from src.domain.commons.codigo_descricao import CodigoDescricao
from src.domain.models.questao import Questao


class QuestaoSimplesResponse:

    def __init__(self, questao: Questao):
        self.codigo = questao.codigo
        self.tipo = CodigoDescricao(questao.tipo.name, questao.tipo.value)
        self.enunciado = questao.enunciado
        self.instituicao = questao.instituicao
        self.ano = questao.ano
        self.origem = CodigoDescricao(questao.origem.name, questao.origem.value)
        self.origem_descricao = questao.origem_descricao
        self.disciplina = CodigoDescricao(questao.disciplina.name, questao.disciplina.value)
        self.cadastrador = questao.cadastrador
        self.data_cadastro = questao.data_cadastro
        self.ativo = True