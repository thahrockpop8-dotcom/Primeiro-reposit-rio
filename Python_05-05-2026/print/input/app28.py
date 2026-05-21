# Data: 19/05/2026
# Exercício 1 - Maior de idade: peça a idade de pessoa. Mostre se ele(a) é maior ou menor de idade.

idade = int(input("Por favor, informe sua idade: "))
if idade >= 18:
    print ("Infelizmente, você se tornou um adulto. Meus pêsames...")
else:
    print ("Calma, brotinho. Ainda há um longo caminho até lá. Aproveite sua juventude, e não apresse o tempo.")

#------------------------------------------------------------------------->

# Exercício 2 - Número positivo ou negativo: Peça um número. Se for maior que zero, mostre "número positivo". Se não, mostre "número negativo ou zero."

numero = int(input("Por favor, digite um número: ")) #também poderia utilizar o float.
if numero >= 0:
    print ("O número que você digitou é positivo.")
else:
    print ("O número que você digitou é um número negativo ou zero.")

#-------------------------------------------------------------------------------->

# Exercício 3 - Senha simples: Crie uma senha fixa (1234). Peça ao usuário que ele(a) digite uma senha. Se estiver correta, mostre "Acesso Permitido". Senão, "Senha Incorreta".

senha = int(input("Digite a senha: "))
if senha >= 1234:
    print ("Acesso Permitido.")
else:
    print ("Senha Incorreta.")

#----------------------------------------------------------------------------------->

# Exercício 4 - Nota do aluno: Peça ao aluno, sua nota. Se for 10, mostre "Nota máxima!". Se for 7 ou mais "Aprovado". Senão, "Reprovado".

nota = float(input("Por favor, informe a sua nota para o sistema: "))
if nota >= 10:
    print  ("Parabéns, você atingiu a nota máxima!")
elif nota >= 7:
    print ("Você foi aprovado.")
elif nota >= 5:
    print ("Você está em recuperação.")
else:
    print ("Você foi reprovado.")


#----------------------------------------------------------------------------------------------->
# Exercício 5 - Par ou Ímpar: Peça um número inteiro. Se ele for divisível por 2, mostre "número par". Senão, "número ímpar".

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("número par")
else:
    print("número ímpar")

#--------------------------------------------------------------------------------------------->
