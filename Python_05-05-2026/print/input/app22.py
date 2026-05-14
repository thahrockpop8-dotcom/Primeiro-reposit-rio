#Exercícios de Casa (12/05/2026)
#Exercício 2 - Compras na loja: Uma pessoa foi à uma loja e comprou vários produtos. Faça um programa que pergunte ao usuário o valor de cada item abaixo: 
#Camiseta, Calça, Tênis, Boné, Mochila, Cinto.
#Depois o programa deve: calcular o valor total da compra. Mostrar quanto ficaria se a pessoa ganhasse R$ 30,00 de desconto. Mostrar quanto ficaria se 
#a pessoa resolvesse comprar mais uma camiseta. Mostrar todos os resultados na tela.

preco_camiseta = float(input("Digite o valor da camiseta: R$ "))
preco_calca = float(input("Digite o valor da calça: R$ "))
preco_tenis = float(input("Digite o valor do tênis: R$ "))
preco_bone = float(input("Digite o valor do boné: R$ "))
preco_mochila = float(input("Digite o valor da mochila: R$ "))
preco_cinto = float(input("Digite o valor do cinto: R$ "))

total_compra = preco_camiseta + preco_calca + preco_tenis + preco_bone + preco_mochila + preco_cinto
total_desconto = total_compra - 30.00
total_camiseta_adicional = total_compra + preco_camiseta

print(f"Valor total da compra: R$ {total_compra:.2f}")
print(f"Valor com desconto: R$ {total_desconto:.2f}")
print(f"Valor com camiseta adicional: R$ {total_camiseta_adicional:.2f}")

#------------------------------------------------------------------------------------------------------------

#Uso do float pois você está pedindo que o usuário informe o preço, então é um número mutável.

#Quebra de linha: Pode-se utilizar \n e três aspas """. Pode-se também utilizar vários prints, um debaixo do outro.
#Outra opção: end= " "

#String(str): Texto, Nome 
#Booleano: True or False
#Números não ficam dentro das aspas
#Float: Número quebrado/Número decimal

#Uso da vírgula em Python 

#print ("Neidiman", 17)

#Criar múltiplas variáveis 
#nome, idade = "Enzo", 8

#Criar lista de valores (tuplas)
#dados = "Enzo", 8 , True 

#1 - STR (String) Texto 
#Tudo que está entre aspas é texto

#nome = "17"
#print("Neidiman")

#2 INT (Inteiro)
#idade = 17 
#Print (idade)

#--------------------------------------------
#Um programa que pergunte True or False
#resposta = input ("Voce tem carteira de motorista?")
#resultado = resposta.lower() == "sim"
#print (resultado)

