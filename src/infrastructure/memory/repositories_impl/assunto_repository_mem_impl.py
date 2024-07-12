from src.domain.models.assunto import Assunto
from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.repositories.assunto_repository import AssuntoRepository


class AssuntoRepositoryMemImpl(AssuntoRepository):

    def obter_por_codigo(self, codigo: int):
        resultado = list(filter(lambda it: it.codigo == codigo))
        if len(resultado) == 0: return None
        if len(resultado) == 1: return resultado[0]
        if len(resultado) > 1:
            raise Exception("Pesquisa retornou mais de um resultado")

    def buscar_por_disciplina(self, disciplina: DisciplinaEnum):
        return list(filter(lambda it: (it.disciplina == disciplina, self.__base)))

    def __init__(self):
        self.__base = [
            Assunto(1, DisciplinaEnum.PORTUGUES, "Leitura e interpretação de texto"),
            Assunto(2, DisciplinaEnum.PORTUGUES, "Ortografia e acentuação"),
            Assunto(3, DisciplinaEnum.PORTUGUES, "Sintaxe"),
            Assunto(4, DisciplinaEnum.MATEMATICA, "Geometria"),
            Assunto(5, DisciplinaEnum.MATEMATICA, "Trigonometria"),
            Assunto(6, DisciplinaEnum.MATEMATICA, "Estatística e probabilidade"),
            Assunto(7, DisciplinaEnum.FISICA, "Mecânica"),
            Assunto(8, DisciplinaEnum.FISICA, "Eletricidade"),
            Assunto(9, DisciplinaEnum.FISICA, "Óptica"),
            Assunto(10, DisciplinaEnum.QUIMICA, "Tabela periódica"),
            Assunto(11, DisciplinaEnum.QUIMICA, "Ligações químicas"),
            Assunto(12, DisciplinaEnum.QUIMICA, "Estado físico da matéria"),
            Assunto(13, DisciplinaEnum.BIOLOGIA, "Genética e biotecnologia"),
            Assunto(14, DisciplinaEnum.BIOLOGIA, "Fisiologia humana"),
            Assunto(15, DisciplinaEnum.BIOLOGIA, "Biologia Celular"),
            Assunto(16, DisciplinaEnum.HISTORIA, "Antiguidade Clássica: Grécia e Roma Antiga"),
            Assunto(17, DisciplinaEnum.HISTORIA, "Feudalismo"),
            Assunto(18, DisciplinaEnum.HISTORIA, "Absolutismo"),
            Assunto(19, DisciplinaEnum.GEOGRAFIA, "Cartografia"),
            Assunto(20, DisciplinaEnum.GEOGRAFIA, "Climatologia"),
            Assunto(21, DisciplinaEnum.GEOGRAFIA, "Hidrografia"),
            Assunto(22, DisciplinaEnum.INGLES, "Pronomes pessoais"),
            Assunto(23, DisciplinaEnum.INGLES, "Verbo to be"),
            Assunto(24, DisciplinaEnum.INGLES, "Verbos auxiliares e de ação"),
            Assunto(25, DisciplinaEnum.INFORMATICA, "Redes de Computadores"),
            Assunto(26, DisciplinaEnum.INFORMATICA, "Engenharia de Software"),
            Assunto(27, DisciplinaEnum.INFORMATICA, "Lógica de Programação"),
            Assunto(28, DisciplinaEnum.DIREITO, "Direito Administrativo"),
            Assunto(29, DisciplinaEnum.DIREITO, "Direito Constitucional"),
            Assunto(30, DisciplinaEnum.DIREITO, "Direito Penal")
        ]
