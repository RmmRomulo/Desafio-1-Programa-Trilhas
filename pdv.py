while True:
    valorCompra = float(input("Digite o valor da compra:"))
    while valorCompra < 0:
        valorCompra = float(input("valor invalido, por favor digite novamente:"))
    if valorCompra == 0:
        break
    idadeCliente = int(input("Digite a idade do cliente:"))
    while idadeCliente < 0:
        idadeCliente = int(input("valor invalido de idade, por favor digite novamente:"))


    historico = []
    qtdCompras = 0
    totalFinal = 0
    totalBruto = 0
    totalDescontos = 0

    totalBruto += valorCompra

    if idadeCliente >= 65:
        valorCompra = valorCompra * 0.80

    if valorCompra > 100:
        valorCompra = valorCompra * 0.90

    totalFinal += valorCompra

    totalDescontos = totalBruto - totalFinal 
    qtdCompras += 1

historico.append((qtdCompras,totalBruto,totalDescontos,totalFinal)) 
print(f"Quantidade de compras registradas: {historico[0][0]}, Total bruto (soma dos valores originais): {historico[0][1]}, Total de descontos concedidos: {historico[0][2]}, Total final (soma dos valores com desconto): R${historico[0][3]:.2f}")