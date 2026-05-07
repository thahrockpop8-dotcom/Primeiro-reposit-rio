#Data: 07/05/2026
#Exercício 10 - DINHEIRO - Um programa que pergunte quanto dinheiro a pessoa tem e mostre quanto ela teria se ganhasse R$ 50,00.

# Pergunta quanto dinheiro a pessoa tem
dinheiro_atual = float(input("Quanto dinheiro você tem? R$ "))

# Adiciona R$ 50,00
novo_total = dinheiro_atual + 50.00

# Mostra o resultado formatado
print(f"Se você ganhasse R$ 50,00, você teria: R$ {novo_total:.2f}")

