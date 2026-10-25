# Sistema de Ponto de Venda (PDV)

## O que o código faz
Este programa simula um sistema de Ponto de Venda (PDV) simplificado que calcula o valor final de compras de forma interativa. Ele aplica descontos progressivos com base na idade do cliente (para maiores ou iguais a 65 anos) e no valor da compra (para valores superiores a R$ 100,00), registrando as transações e exibindo um resumo financeiro detalhado ao final da execução.

## Como ele faz
1. **Entrada de dados**: O programa solicita o valor da compra. Se o valor for negativo, exibe uma mensagem de erro e pede novamente. Se o valor for `0`, o programa encerra o loop de cadastro.
2. **Idade do cliente**: Caso o valor seja válido e diferente de zero, solicita a idade do cliente, validando também para evitar valores negativos.
3. **Aplicação de descontos**: 
   * Verifica se a idade do cliente é maior ou igual a 65 anos; caso seja, aplica um desconto de 20% (multiplica por `0.80`).
   * Em seguida, verifica se o valor atualizado (já com o desconto de idade ou o valor original) é superior a R$ 100,00; caso seja, aplica um desconto adicional de 10% (multiplica por `0.90`).
4. **Armazenamento e Exibição**: Salva os dados calculados (quantidade, total bruto, total de descontos e total final) em uma lista de histórico e imprime o resumo formatado na tela.

## Como rodar
Para executar o programa no seu terminal, utilize o seguinte comando:

```bash
python pdv.py
```

## Tabela de Casos de Teste

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
| :-: | :---: | :---: | :---: | :---: | :---: |
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |