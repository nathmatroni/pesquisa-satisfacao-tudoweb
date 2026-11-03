# Pesquisa de Satisfação - TudoWeb

## Objetivo
Programa em Python para coletar a opinião de 50 entrevistados sobre o atendimento da empresa TudoWeb.

## Dados solicitados
- Nome
- Idade
- Opinião sobre o atendimento:
  - 1 = EXCELENTE
  - 2 = BOM
  - 3 = RUIM

## Estruturas utilizadas
- `for`: repete a pesquisa para 50 entrevistados.
- `if`, `elif` e `else`: identificam a opinião escolhida.
- `while`: solicita novamente a idade ou opinião quando a entrada é inválida.
- Contadores: registram quantas respostas foram excelentes, boas e ruins.

## Como executar
1. Instale o Python 3.
2. Abra o terminal na pasta do projeto.
3. Execute: `python pesquisa_tudoweb.py`

## Teste de validação com 10 entrevistados
Para testar, execute o programa e informe os dados de 10 pessoas. Para encerrar o teste sem preencher os 50 registros, interrompa a execução após o décimo entrevistado (Ctrl + C).

Exemplo de conjunto de respostas para validar a lógica:
- EXCELENTE: 1, 1, 1, 1
- BOM: 2, 2, 2
- RUIM: 3, 3, 3

Resultado esperado no teste de 10 respostas:
- Quantidade de respostas EXCELENTE: 4
- Quantidade de respostas RUIM: 3

Observação: o programa final permanece configurado para 50 entrevistados, conforme solicitado na atividade.
