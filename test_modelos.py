from sklearn.feature_extraction.text import CountVectorizer

from src.domain.models.avaliador import Avaliador
from src.domain.models.carregador import Carregador
from src.domain.models.modelo import Modelo

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Modelo()
avaliador = Avaliador()

# Parâmetros
url_dados = "src/infrastructure/db/csv/dataset_enunciados_test.csv"

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, ['enunciado', 'disciplina'])

# tratando texto em linguagem natural
lista_enunciados_tratados = []
for enunciado in dataset.enunciado:
    enunciado_tratado = modelo.tratar_texto_linguagem_natural(enunciado)
    lista_enunciados_tratados.append(enunciado_tratado)

# convertendo texto para array de valores com 10.000 colunas
cou_vec = CountVectorizer(max_features=10000)
sparce_matrix = cou_vec.fit_transform(lista_enunciados_tratados).toarray()

y = dataset.iloc[:, 1].values
x = sparce_matrix


# Método para testar o modelo de Naive Bayes a partir do arquivo correspondente
def test_modelo_nb():
    # Importando o modelo
    nb_path = 'src/infrastructure/ml_model/nb_modelo_finalizado.joblib'
    modelo_nb = modelo.carrega_modelo_joblib(nb_path)

    # Obtendo as métricas
    acuracia, recall, precisao, f1 = avaliador.avaliar(modelo_nb, x, y)

    # Testando as métricas
    assert acuracia >= 0.75
    assert recall >= 0.5
    assert precisao >= 0.5
    assert f1 >= 0.5

