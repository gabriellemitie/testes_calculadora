# testes_calculadora
Atividade 5 da disciplina de Testes de Software.

<!--
Relatório de Testes - 19/09/2025

• Resultado da execução dos testes:
	- Foram executados 23 testes unitários.
	- 5 testes falharam (FAIL) e 12 apresentaram erros (ERROR).
	- Principais erros: AttributeError devido à ausência de inicialização do atributo 'calc' na classe de teste, e falhas de asserção por valores esperados divergentes dos resultados reais.

• Cobertura de código obtida:
	- O comando de cobertura foi executado, mas não foi possível gerar o relatório HTML devido à ausência do pacote coverage instalado corretamente ou problemas de permissão.
	- Recomenda-se garantir que o pacote coverage esteja instalado e que os arquivos estejam acessíveis.

• Problemas encontrados e soluções aplicadas:
	- Problema de permissão ao executar scripts do ambiente virtual (.venv/bin): resolvido ajustando permissões com chmod.
	- Erro de comando ao executar testes: corrigido utilizando o comando correto `.venv/bin/python -m unittest discover tests -v`.
	- Erros de inicialização do atributo 'calc' nas classes de teste: necessário adicionar o método setUp para instanciar o objeto calculadora.
	- Falhas de asserção por diferenças de valores e acentuação: revisar os valores esperados nos testes para corresponder ao resultado real da calculadora.

• Lições aprendidas sobre cada tipo de teste:
	- Testes unitários exigem inicialização correta dos objetos e atenção aos valores esperados.
	- Testes de integração podem revelar problemas de dependências e permissões no ambiente.
	- É importante garantir que os comandos de teste e cobertura estejam corretos e que o ambiente virtual esteja configurado adequadamente.
	- Pequenas diferenças de formatação ou acentuação podem causar falhas em testes de comparação de strings.

-->
