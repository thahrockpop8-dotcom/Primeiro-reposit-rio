#DATA: 26/05/2026

#EXERCÍCIOS:

# 1 - Crie algoritmos que: Solicite ao usuário dois números inteiros. 
# O programa deve comparar os dois valores e exibir qual deles é o maior.

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

# 3 - Solicite ao usuário o nome do estudante e 3 notas, retorne
# a média ponderada das notas (com pesos 1,1 e 2), o nome do estudante e se reprovado (media 6 aprovado).

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

        






