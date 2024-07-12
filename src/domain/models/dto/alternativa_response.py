from src.domain.models.alternativa import Alternativa


class AlternativaResponse:

    def __init__(self, alternativa : Alternativa):
        self.codigo = alternativa.codigo
        self.descricao = alternativa.descricao
        self.is_correta = alternativa.is_correta

    def to_model(self) -> Alternativa:
        return Alternativa(self.codigo, self.descricao, self.is_correta)


