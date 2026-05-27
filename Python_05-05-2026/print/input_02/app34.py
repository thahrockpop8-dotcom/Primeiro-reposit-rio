#DATA: 26/05/2026

#EXERCÍCIOS:

""" 1 - Crie algoritmos que: Solicite ao usuário dois números inteiros. 
O programa deve comparar os dois valores e exibir qual deles é o maior."""

numero1 = int(input("Informe um número inteiro: "))
numero2 = int(input("Informe outro número inteiro: "))

if numero1 > numero2:
    print(f"O maior número é o primeiro, que vale {numero1}")
elif numero2 > numero1:
    print(f"O maior número é o segundo, que vale {numero2}")
else:
    print("Os dois números são iguais.")

#---------------------------------------------------------------->
# 2 - Solicite ao usuário 1 número e informe se este é par ou ímpar.

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print (f"O número {numero} é par.")
else:
    print (f"O número {numero} é impar.")

#------------------------------------------------------------------>
""" 3 - Solicite ao usuário o nome do estudante e 3 notas, retorne
a média ponderada das notas (com pesos 1,1 e 2), o nome do estudante e se reprovado (media 6 aprovado)."""

nome = input ("Por favor, informe o seu nome: ")
nota1 = float(input("Informe sua nota em português: "))
nota2 = float(input("Informe sua nota em matématica: "))
nota3 = float(input("Informe sua nota em Inglês: "))

if nota1 == 0 or nota2 == 0 or nota3 == 0:
    print("Infelizmente, você foi reprovado.")
else:
    media_ponderada = (nota1 * 1 + nota2 * 1 + nota3 * 2) / 4
    print(f"{nome}, sua média ponderada é: {media_ponderada:.2f}")
    if media_ponderada >= 6:
        print("Parabéns, você foi aprovado!")
    else:
        print("Infelizmente, você foi reprovado.")
#----------------------------------------------------------------------->
""" 4 - Leia o ano de nascimento de uma pessoa e o ano atual. Com base nisso, calcule a idade da pessoa 
e informe se ela é maior de idade (18 anos ou mais) ou menor de idade."""

nome_pessoa = input("Qual o seu nome? ")
ano_nascimento = int(input("Informe o ano de nascimento: "))
ano_atual = int(input("Informe o ano atual: "))
idade_atual = ano_atual - ano_nascimento

if idade_atual >= 18:
    print(f"{nome_pessoa}, você é maior de idade.")
else:
    print(f"{nome_pessoa}, você é menor de idade.")


#--------------------------------------------------------------------------------->
""" 5 - Leia o salário atual de um funcionário e o percentual dereajuste. 
Calcule e exiba o valor do aumento e o novo salário
 após o reajuste."""

salario_atual = float(input("Informe o seu salário atual: "))
percentual_reajuste = float(input("Informe o percentual de reajuste: "))
valor_aumento = salario_atual * (percentual_reajuste / 100)
novo_salario = salario_atual + valor_aumento

print(f"O valor do aumento é: R$ {valor_aumento:.2f}")
print(f"O novo salário é: R$ {novo_salario:.2f}")

#--------------------------------------------------------------------------------->
# 6 - Leia a idade de duas pessoas e calcule a diferença absoluta de idade entre elas (sem exibir valores negativos).

idade_pessoa1 = float(input("Informe a idade da primeira pessoa: "))
idade_pessoa2 = float(input("Informe a idade da segunda pessoa: "))
diferenca_idade = abs(idade_pessoa1 - idade_pessoa2)
print(f"A diferença absoluta de idade entre as duas pessoas é: {diferenca_idade} anos.")

#--------------------------------------------------------------------------------->
""" 7 -  Leia o valor de um produto. Se o valor for maior que R$ 100,00, aplique um desconto de 10%. Caso contrário, aplique um desconto de apenas 5%. 
# Exiba o valor do desconto calculado e o preço final que o cliente irá pagar."""

valor_produto = float(input("Informe o valor do produto em R$: "))

if valor_produto > 100:
    desconto = valor_produto * 0.10
else:
    desconto = valor_produto * 0.05

print(f"O valor do desconto é: R$ {desconto:.2f}")
print(f"O preço final é: R$ {valor_produto - desconto:.2f}")

#--------------------------------------------------------------------------------->
""" 8  - Solicite ao usuário que digite um nome de usuário e uma senha. O sistema deve verificar se o usuário é exatamente "admin" e 
# se a senha é "1234". Se ambos estiverem corretos, exiba "Acesso liberado". Caso contrário, exiba "Acesso negado"."""

nome_usuario = input("Por favor, digite aqui o seu nome de usuário: ")
senha_usuario = input("Por favor, digite aqui a sua senha: ")
if nome_usuario =="admin" and senha_usuario == "1234":
    print("Acesso liberado.")
else:
    print("Acesso negado.")

#--------------------------------------------------------------------------------->
""" 9 - Solicite a distância total percorrida por um carro (em km) e o total de combustível gasto (em litros). Calcule o consumo médio do veículo (km/l). 
 Se o consumo for menor que 10 km/l, exiba a mensagem "Situação: Consumo alto". Caso contrário, exiba "Situação: Consumo dentro do esperado "."""

distancia_percorrida = float(input("A distância total percorrida pelo carro (em km) foi: "))
combustivel_gasto = float(input("O total de combustível gasto (em litros) foi: "))

if combustivel_gasto > 0:
    consumo_medio = distancia_percorrida / combustivel_gasto
    print(f"O consumo médio do veículo é: {consumo_medio:.2f} km/l.")
    if consumo_medio < 10:
        print("Situação: Consumo alto")
    else:
        print("Situação: Consumo dentro do esperado")
else:
    print("O total de combustível gasto deve ser maior que zero para calcular o consumo médio.")

#--------------------------------------------------------------------------------->
""" 10 - Escreva um programa que receba do usuário uma distância em quilômetros (km). O programa deve calcular e exibir essa mesma 
distância convertida para duas unidades do sistema americano: jardas (yd) e milhas (mi).
Utilize as seguintes fórmulas para o cálculo: Jardas (yd): Jardas = km X 1093.61 Milhas (mi): Milhas = km / 1.60934
O programa deve calcular e exibir o valor convertido com duas casas decimais."""

distancia_km = float(input("Informe a distância em quilômetros (km): "))
distancia_yd = distancia_km * 1093.61
distancia_mi = distancia_km / 1.60934
print(f"A distância convertida para jardas (yd) é: {distancia_yd:.2f} yd.")
print(f"A distância convertida para milhas (mi) é: {distancia_mi:.2f} mi.")

        






