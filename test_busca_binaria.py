import pytest
import busca_binaria as binaria

class TestaBuscaBinaria:
    def test_busca_simples(self):
        assert (binaria.busca([0,1,2,3,4,5,6,7,8,9], 7) == 7)

    def test_sem_resultado(self):
        assert (binaria.busca([0,1,2,3,4,5,6,7,8,9], 10) == False)