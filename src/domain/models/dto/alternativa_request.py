from src.domain.models.alternativa import Alternativa


class AlternativaRequest:

    def __init__(self, descricao: str,  is_correta: bool):
                self.descricao = descricao
                self.is_correta = is_correta

    def to_model(self) -> Alternativa:
        return Alternativa(None, self.descricao, self.is_correta)