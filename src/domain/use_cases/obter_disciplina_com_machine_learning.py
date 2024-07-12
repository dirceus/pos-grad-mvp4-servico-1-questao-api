from src.domain.commons.use_case import UseCase
from src.domain.models.enum.disciplina_enum import DisciplinaEnum
from src.domain.models.modelo import Modelo


class ObterDisciplinaComMachineLearning(UseCase):

    def execute(self, request: str):
        ml_path = 'src/infrastructure/ml_model/nb_modelo_finalizado.joblib'
        allwords_path = 'src/infrastructure/ml_model/allwords.txt'

        allwords = []
        with open(allwords_path) as my_file:
            for line in my_file:
                allwords.append(line.strip())
        modelo = Modelo()
        modelo_carregado = modelo.carrega_modelo_joblib(ml_path)
        resultado = modelo.predicao_disciplina(modelo_carregado, request, allwords)
        return DisciplinaEnum[resultado[0]]
