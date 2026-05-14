#Exercícios de Casa (12/05/2026)
#Exercício 1 - Loja de Roupas: Uma pessoa foi a pessoa à uma loja e comprou: 2 camisetas, cada uma custando R$ 35,00. 1 calça custando R$ 80,00. 1 boné custando R$ 25,00.
#Faça um programa que calcule: O valor total da compra. Quanto a pessoa pagaria se ganhasse R$ 20,00 de desconto. Mostre todas as informaçãos na tela.

camisetas = 2
preco_camiseta = 35.00
calcas = 1
preco_calca = 80.00
bone = 1
preco_bone = 25.00

total_compra = (camisetas * preco_camiseta) + (calcas * preco_calca) + (bone * preco_bone)
total_desconto = total_compra - 20.00

print(f"Valor total da compra: R$ {total_compra:.2f}")
print(f"Valor com desconto: R$ {total_desconto:.2f}")