Relatório de Testes

• Resultado da execução dos testes:
  - Foram executados 23 testes unitários.
  - 6 testes passaram, 5 falharam e 12 apresentaram erros.
  - Testes que passaram: test_divisao_por_zero, test_entrada_saida_soma, test_fluxos_divisao, test_inicializacao, test_limite_inferior, test_modificacao_historico
  - Testes que falharam: test_consistencia_historico, test_entrada_saida_dividir, test_entrada_saida_multiplicar, test_entrada_saida_subtrair, test_mensagens_erro
  - Testes com erro (AttributeError): test_consistencia_historico_decimal, test_entrada_saida_potencia_negativa, test_fluxos_divisao_dividendo_zero, test_inicializacao_apos_uso, test_limite_inferior_divisao_pequeno, test_limite_superior_divisao_por_zero_proximo, test_limite_superior_float, test_mensagens_erro_divisao_por_zero, test_modificacao_limpeza_nao_afeta_resultado, test_potencia_fora_do_intervalo, test_tipagem_invalida_booleano, test_tipagem_invalida_todas_operacoes

• Cobertura de código obtida:
  - src/calculadora.py: 78% (46 linhas, 10 não cobertas)
  - tests/test_integracao.py: 16% (38 linhas, 32 não cobertas)
  - tests/test_unidade.py: 74% (117 linhas, 30 não cobertas)
  - Cobertura total: 64% (201 linhas, 72 não cobertas)

• Problemas encontrados:
  - Muitos testes unitários apresentaram erro de AttributeError por falta de inicialização do atributo 'calc'.
  - Falhas de asserção por divergência entre valores esperados e resultados reais (ex: valores numéricos e acentuação em mensagens).
  - Baixa cobertura nos testes de integração.

• Soluções aplicadas:
  - Ajuste de permissões dos arquivos do ambiente virtual com chmod.
  - Correção do comando de execução dos testes.
  - Recomenda-se adicionar o método setUp nas classes de teste para inicializar corretamente os objetos.
  - Revisar valores esperados nos testes para garantir correspondência com a implementação.

• Lições aprendidas:
  - A inicialização correta dos objetos de teste é fundamental para evitar erros de AttributeError.
  - Testes unitários devem ser precisos nos valores esperados e considerar detalhes de formatação.
  - Testes de integração precisam ser melhorados para aumentar a cobertura.
  - O ambiente virtual deve estar corretamente configurado e os comandos de teste bem definidos.
  - Pequenas diferenças de acentuação ou formatação podem causar falhas inesperadas.
