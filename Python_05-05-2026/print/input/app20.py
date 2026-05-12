#----------------------------------------------------------------------------------------->
#Data: 12/05/2026
#Exercício 22 - COMPRA COM TROCO - Um programa que pergunte o valor de um produto e quanto a pessoa entregou para pagar. Depois mostre quanto de troco ela receberá.

valor_produto = float(input("Digite o valor do produto: R$ "))
valor_pago = float(input("Digite o valor pago pelo cliente: R$ "))
troco = valor_pago - valor_produto

if troco > 0:
    print(f"O troco é: R$ {troco:.2f}")
elif troco == 0:
    print("Não há troco.")
else:
    print(f"Valor insuficiente. Faltam: R$ {abs(troco):.2f}")