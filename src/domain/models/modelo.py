from sklearn.feature_extraction.text import CountVectorizer

import re
import joblib
import nltk
import pandas as pd

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


class Modelo:

    def carrega_modelo_joblib(self, path):
        return joblib.load(path)

    def predicao_disciplina(self, modelo, enunciado, allwords):
        """Realiza a predição com base no enunciado da questão"""
        cou_vec_test = CountVectorizer(vocabulary=allwords)
        texto = self.tratar_texto_linguagem_natural(enunciado)
        x_novos_dados = cou_vec_test.fit_transform([texto])
        entrada = pd.DataFrame(x_novos_dados.toarray(), columns=allwords)
        array_entrada = entrada.values
        x_entrada = array_entrada[:, 0:10000].astype(float)
        return modelo.predict(x_entrada)

    def tratar_texto_linguagem_natural(self, texto_original):
        texto_lowercase = texto_original.lower()
        texto_sem_caracter_especial = re.sub("[^a-zA-Z \\\]", " ", texto_lowercase)
        return self.remover_stopwords(texto_sem_caracter_especial)

    def remover_stopwords(self, texto):
        stop_words = set(nltk.corpus.stopwords.words('portuguese'))
        stopwords_contexto_app = ["correto", "afirmativa", "questao", "afirmativas", "incorreto", "incorretas", "nao",
                                  "seguintes", "opcoes", "opcao",
                                  "assinale", "em", "um", "referese", "os", "as", "seu", "seus", "tem", "sao", "leia",
                                  "observe", "qual", "das", "de", "dos",
                                  "assinalar", "se", "no", "na", "do", "da", "para", "uma", "um", "verdadeiro", "falso",
                                  "ii", "iii", "iv",
                                  "preciso", "precisa", "atraves", "utilizam", "leia", "durante", "exemplo", "figura",
                                  "alternativas", "abaixo",
                                  "refere", "ao", "contexto", "muito", "importante", "pois", "seguinte", "dentro",
                                  "fora", "antes", "depois",
                                  "imagem", "oriundo", "oriundos", "aberto", "fechado", "abertos", "dispoe", "sobre",
                                  "sob", "abaixo", "acima",
                                  "como", "novo", "nova", "por", "quer", "queria", "pratica", "qual", "condicao",
                                  "condicoes", "suponha",
                                  "nesse", "nesses", "nessa", "nessas", "neste", "nestes", "nestas", "nesta", "essa",
                                  "esse", "essas", "esses", "pode",
                                  "podem", "por", "para", "possui", "possuem", "geral", "geralmente", "normal",
                                  "normalmente", "eventual", "eventualmente",
                                  "momento", "proximo", "longe", "cujo", "cujos", "cujas", "cuja", "que", "quem",
                                  "quais", "apresenta", "apresentou",
                                  "especial", "especiais", "mulher", "homem", "mulheres", "meninos", "meninas",
                                  "homens", "menino", "menina", "praticamente",
                                  "com", "contra", "mesmo", "mesma", "tendo", "cada", "ate", "bem", "mal", "bom",
                                  "entre", "significa"]

        palavras = nltk.word_tokenize(texto)

        enunciado_sem_stopwords = [palavra for palavra in palavras if not palavra in stopwords_contexto_app]
        enunciado_sem_stopwords = [palavra for palavra in enunciado_sem_stopwords if not palavra in stop_words]
        return " ".join(enunciado_sem_stopwords)
