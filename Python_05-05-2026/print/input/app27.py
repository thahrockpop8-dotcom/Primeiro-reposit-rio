# Data: 19/05/2026

# Aula sobre If, Else e Ilif
# If: Se
# Else: Se não 
# Ilif: 

idade = 18
if idade >= 18:
    print ("Você é maior de idade.")

else:
    print ("Você é menor de idade.")


#------------------------------------------------------------>
#Exemplo

nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")

#-------------------------------------------------------------->

#Exemplo 1 

idade = int(input("Quantos anos você tem? "))
if idade >= 18:
    print ("Você pode tirar carteira de motorista.")

else: 
    print ("Você não pode tirar carteira de motorista.")

#--------------------------------------------------------------->

#Exemplo 2 
resposta = input ("Python é uma linguagem de programação? ")
if resposta == "sim":
    print ("Correto!")
else:
    print ("Incorreto.")

#------------------------------------------------------------------>

#Exemplo 3
pets = input("Você possui algum animal de estimação? ").lower()

if pets == "sim":
    print("Que legal! Adoraria saber mais sobre seu animalzinho.")
    nome_pet = input("Qual o nome do seu animalzinho? ")
    print(f"O nome dele(a) é {nome_pet}.")

elif pets == "não":
    print("Isso é uma pena. Você sabia que existem estudos que comprovam que animais de estimação ajudam na saúde mental? \nSe você sempre quis ter um e sempre hesitou, não perca tempo! \nEles são os melhores companheiros que alguém poderia ter.")

#---------------------------------------------------------------------->
