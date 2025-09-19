import unittest
from src.calculadora import Calculadora

def test_operacoes_sequenciais(self):
    calc = Calculadora()
    # Sequencia : 2 + 3 = 5 , depois 5 * 4 = 20 , depois 20 / 2 = 10
    calc.somar(2,3)
    resultado1 = calc.obter_ultimo_resultado()
    calc.multiplicar(resultado1,4)

    resultado2 = calc.obter_ultimo_resultado()
    calc.dividir(resultado2,2)
    resultado_final = calc.obter_ultimo_resultado()
    self.assertEqual(resultado_final,10)
    self.assertEqual(len(calc.historico),3)

def test_integracao_historico_resultado(self):
    calc = Calculadora()
    calc.potencia(2,3) # 2^3 = 8
    calc.somar(calc.obter_ultimo_resultado(),2) # 8 + 2 = 10
    self.assertEqual(calc.obter_ultimo_resultado(),10)
    self.assertEqual(len(calc.historico),2)
    self.assertIn("2^3=8",calc.historico)
    self.assertIn("8+2=10",calc.historico)

#### testes adicionais ######
def test_operacoes_sequenciais_alternativo(self):
    calc = Calculadora()
    # Sequência: 10 - 4 = 6, depois 6 ^ 2 = 36, depois 36 / 6 = 6
    calc.subtrair(10, 4)
    resultado1 = calc.obter_ultimo_resultado()

    calc.potencia(resultado1, 2)
    resultado2 = calc.obter_ultimo_resultado()

    calc.dividir(resultado2, 6)
    resultado_final = calc.obter_ultimo_resultado()

    self.assertEqual(resultado_final, 6)
    self.assertEqual(len(calc.historico), 3)

def test_integracao_historico_resultado_alternativo(self):
    calc = Calculadora()
    calc.multiplicar(3, 5)  # 3 * 5 = 15
    calc.subtrair(calc.obter_ultimo_resultado(), 4)  # 15 - 4 = 11

    self.assertEqual(calc.obter_ultimo_resultado(), 11)
    self.assertEqual(len(calc.historico), 2)
    self.assertIn("3*5=15", calc.historico)
    self.assertIn("15-4=11", calc.historico)
