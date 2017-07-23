import maiusculas
import pytest

class TestaMaiusculas:
    @pytest.fixture
    def PegaMaiuscula(self, param):
        return maiusculas.Maiusculas.get_maiusculas(self, frase=param)
    def test_capitalize(self):
        assert (self.PegaMaiuscula("Luhan Meireles da Silva") == 'LMS')
    def test_apenas_maiuscula(self):
        assert (self.PegaMaiuscula("LUHAN") == 'LUHAN')
    def test_sem_maiuscula(self):
        assert (self.PegaMaiuscula("luhan") == '')
    def test_primeira_maiscula(self):
        assert (self.PegaMaiuscula("Luhan") == 'L')
    def test_ultima_maiscula(self):
        assert (self.PegaMaiuscula("luhaN") == 'N')