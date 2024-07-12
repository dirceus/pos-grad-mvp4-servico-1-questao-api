from src.domain.models.enum.disciplina_enum import DisciplinaEnum


class Assunto:

    def __init__(self, codigo: int, disciplina: DisciplinaEnum, descricao: str):
        self.codigo = codigo
        self.disciplina = disciplina
        self.descricao = descricao
