from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score


class Avaliador:

    def avaliar(self, modelo, x_test, y_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        predicoes = modelo.predict(x_test)

        # Caso o seu problema tenha mais do que duas classes, altere o parâmetro average
        return (accuracy_score(y_test, predicoes),
                recall_score(y_test, predicoes, average='weighted'),
                precision_score(y_test, predicoes, average='weighted'),
                f1_score(y_test, predicoes, average='weighted'))

