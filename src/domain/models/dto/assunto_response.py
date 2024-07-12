from src.domain.commons.codigo_descricao import CodigoDescricao
from src.domain.models.assunto import Assunto


class AssuntoResponse:

    def __init__(self, assunto: Assunto):
        self.codigo = assunto.codigo
        self.disciplina = CodigoDescricao(assunto.disciplina.name, assunto.disciplina.value)
        self.descricao = assunto.descricao
