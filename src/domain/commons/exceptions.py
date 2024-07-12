class QuestaoNotFoundException(Exception):
    """Questão não encontrada"""

    def __init__(self, codigo: int):
        self.message = "Não encontrada questão com código: {}".format(codigo)
        super().__init__(self.message)


class BusinessException(Exception):
    pass


class InvalidInputException(Exception):
    pass


class InternalErrorException(Exception):
    pass


class InvalidStateException(Exception):
    pass
