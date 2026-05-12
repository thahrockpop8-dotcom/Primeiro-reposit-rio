#Data: 12/05/2026
#Exercício 19 - COMPRA DE CAMISETAS: Um programa que pergunte quantas camisetas a pessoa comprou e o valor de cada camiseta. Depois mostre o valor total da compra.

nome = input("Nome: ")
quantas_camisetas = input("Quantas camisetas você comprou? ")
camiseta_azul =  float(input("Qual o valor da camiseta azul? "))
camiseta_verde = float(input("Qual o valor da camiseta verde? "))

total = camiseta_azul + camiseta_verde

print (f"Olá, {nome}. Sua mãe disse que você foi à C&A hoj, onde está havendo boas promoções. Ela me disse que você comrpou {quantas_camisetas} camisetas. E que uma foi R$ {camiseta_azul} e a outra foi R$ {camiseta_verde}! No total, você desembolsou {total}. Foi uma boa compra.")
