from src.domain.models.alternativa import Alternativa


class AlternativaRepositoryMemImpl:

    def __init__(self):
        self.__base = []

    def salvar(self, alternativa: Alternativa):
        self.__base.append(alternativa)

    def total_alternativas(self):
        return len(self.__base)
