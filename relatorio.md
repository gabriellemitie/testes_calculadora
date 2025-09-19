Relatório de Testes

• Resultado da execução dos testes:
  - Foram executados 23 testes unitários.
  - 6 testes passaram, 5 falharam e 12 apresentaram erros.

• Cobertura de código obtida:
<img width="358" height="94" alt="Captura de Tela 2025-09-19 às 19 58 31" src="https://github.com/user-attachments/assets/52ea673e-b2ba-4bb7-9620-15557fa89ddf" />


• Problemas encontrados:
  - Muitos testes unitários apresentaram erro de AttributeError por falta de inicialização do atributo 'calc'.
  - Erro no assertion por divergência entre valores esperados e resultados reais 
  - Baixa cobertura nos testes de integração.

• Soluções aplicadas:
  - Recomenda-se adicionar o método setUp nas classes de teste para inicializar corretamente os objetos.
  - Revisar valores esperados nos testes para garantir correspondência com a implementação.

• Lições aprendidas:
  - A inicialização correta dos objetos de teste é fundamental para evitar erros de AttributeError.
  - Testes unitários devem ser precisos nos valores esperados e considerar detalhes de formatação.
  - Testes de integração precisam ser melhorados para aumentar a cobertura.
  - Pequenas diferenças de acentuação ou formatação podem causar falhas inesperadas.
