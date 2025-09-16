import unittest
from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    ###### testes de unidade ######
    def test_entrada_saida_soma(self):
        calc = Calculadora()
        resultado = calc.somar(5,3)
        self.assertEqual(resultado,8)
        self.assertEqual(calc.obter_ultimo_resultado(),8)

    def test_entrada_saida_subtrair(self):
        calc = Calculadora()
        resultado = calc.subtrair(5,3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(),8)
    
    def test_entrada_saida_multiplicar(self):
        calc = Calculadora()
        resultado = calc.multiplicar(5,3)
        self.assertEqual(resultado,8)
        self.assertEqual(calc.obter_ultimo_resultado(),8)

    def test_entrada_saida_dividir(self):
        calc = Calculadora()
        resultado = calc.dividir(5,3)
        self.assertEqual(resultado,8)
        self.assertEqual(calc.obter_ultimo_resultado(),8)
    
    ##### teste adicional de unidade ##########
    def test_entrada_saida_potencia_negativa(self):
        resultado = self.calc.potencia(2, -3)
        self.assertEqual(resultado, 0.125)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 0.125)
    
    ###### testes de tipagem ######
    def test_tipagem_invalida_todas_operacoes(self):
        """
        Verifica se a calculadora levanta um TypeError para argumentos de tipo inválido
        em todas as operações matemáticas.
        """
        # Teste de soma com string
        with self.assertRaises(TypeError):
            self.calc.somar("1", 2)
        with self.assertRaises(TypeError):
            self.calc.somar(1, "2")
        
        # Teste de subtração com lista
        with self.assertRaises(TypeError):
            self.calc.subtrair(5, [1, 2])
        
        # Teste de multiplicação com dicionário
        with self.assertRaises(TypeError):
            self.calc.multiplicar({"a": 1}, 2)
        
        # Teste de divisão com None
        with self.assertRaises(TypeError):
            self.calc.dividir(10, None)
        
        # Teste de potência com booleano
        with self.assertRaises(TypeError):
            self.calc.potencia(2, True)
    
    ###### teste adicional de tipagem ######
    def test_tipagem_invalida_booleano(self):
        """Testa se a calculadora rejeita um argumento booleano."""
        with self.assertRaises(TypeError):
            self.calc.somar(1, True)


    def test_consistencia_historico(self):
        calc = Calculadora()
        calc.somar(2,3)
        calc.multiplicar(4,5)
        self.assertEqual(len(calc.historico),2)
        self.assertIn("2+3=5",calc.historico)
        self.assertIn("4*5=20",calc.historico)

    ###### teste adicional de consistencia ######
    def test_consistencia_historico_decimal(self):
        """Verifica se o histórico armazena corretamente operações com resultados decimais."""
        self.calc.dividir(10, 4)
        self.assertIn("10 / 4 = 2.5", self.calc.historico)
        self.assertEqual(len(self.calc.historico), 1)


    def test_inicializacao(self):
        calc = Calculadora()
        self.assertEqual(calc.resultado,0)
        self.assertEqual(len(calc.historico),0)

    #### teste adicional de inicializacao ####
    def test_inicializacao_apos_uso(self):
        """Verifica se uma nova instância da calculadora é inicializada com dados limpos."""
        self.calc.somar(100, 200)
        nova_calc = Calculadora()
        self.assertEqual(nova_calc.resultado, 0)
        self.assertEqual(len(nova_calc.historico), 0)

    def test_modificacao_historico(self):
        calc = Calculadora()
        calc.somar(1,1)
        self.assertEqual(len(calc.historico),1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico),0)
    
    #### teste adicional de modificacao do historico ######
    def test_modificacao_limpeza_nao_afeta_resultado(self):
        """Verifica se a função limpar_historico não afeta o último resultado."""
        self.calc.multiplicar(5, 5)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 25)
        self.calc.limpar_historico()
        self.assertEqual(self.calc.obter_ultimo_resultado(), 25)

    def test_limite_inferior(self):
        calc = Calculadora()
        # Teste com zero
        resultado = calc.somar(0,5)
        self.assertEqual(resultado,5)
        # Teste com numeros negativos muito pequenos
        resultado = calc.multiplicar(-1e-10,2)
        self.assertEqual(resultado,-2e-10)
    
    #### teste adicional de limite inferior ######
    def test_limite_inferior_divisao_pequeno(self):
        """Testa a divisão que resulta em um número flutuante muito pequeno."""
        resultado = self.calc.dividir(-1, 1e100)
        self.assertAlmostEqual(resultado, -1e-100)

    def test_limite_superior_float(self):
        """
        Verifica o comportamento da calculadora com valores float muito grandes,
        próximos do limite de representação.
        """
        
        # 1. Teste de multiplicação para alcançar o limite
        # Um número muito grande, mas ainda representável
        num_grande = 1e308
        
        # A multiplicação deve resultar em "infinito"
        resultado = self.calc.multiplicar(num_grande, 2)
        self.assertEqual(resultado, float('inf'))

        # 2. Teste de soma para evitar overflow
        # Soma dois números grandes, mas que juntos não ultrapassam o limite
        resultado_soma = self.calc.somar(1e308, 1e308)
        self.assertEqual(resultado_soma, 2e308)
    
    #### teste adicional de limite superior ######
    def test_limite_superior_divisao_por_zero_proximo(self):
        """Testa se a divisão por um número extremamente pequeno resulta em infinito."""
        resultado = self.calc.dividir(10, 1e-320)
        self.assertEqual(resultado, float('inf'))

    def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10,0)

    #### teste adicional de divisao por zero ######        
    def test_potencia_fora_do_intervalo(self):
        """Testa potência com base negativa e expoente fracionário, que não é real."""
        with self.assertRaises(ValueError):
            self.calc.potencia(-1, 0.5)
    
    """Observação: O código-base não trata esse erro.Se o seu teste falhar, isso é um bug a ser corrigido na calculadora, 
    conforme a tarefa 4 do documento. 
    Uma solução seria adicionar
if base < 0 and isinstance(expoente, float): raise ValueError(...) no método potencia"""


    def test_fluxos_divisao(self):
        calc = Calculadora()
        # Caminho normal
        resultado = calc.dividir(10,2)
        self.assertEqual(resultado,5)
        # Caminho de erro
        with self.assertRaises(ValueError):
            calc.dividir(10,0)
        
    #### teste adicional de fluxos ######
    def test_fluxos_divisao_dividendo_zero(self):
        """Verifica o fluxo de divisão com o dividendo igual a zero."""
        resultado = self.calc.dividir(0, 5)
        self.assertEqual(resultado, 0)

    def test_mensagens_erro(self):
        calc = Calculadora()
        try:
            calc.dividir(5,0)
        except ValueError as e:
            self.assertEqual(str(e),"Divisao por zero nao permitida")
    
    ### teste adicional de mensagens de erro ######
    def test_mensagens_erro_divisao_por_zero(self):
        """Verifica se a mensagem de erro de divisão por zero é a esperada."""
        with self.assertRaisesRegex(ValueError, "Divisao por zero nao permitida"):
            self.calc.dividir(10, 0)

