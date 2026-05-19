"""
Exercício 6 - Crie um programa que: Peça o nome do aluno(a). Peça idade. A nota. Pergunte se ele(a) entregou o trabalho (sim ou não).
Regras: Se a idade for menor que 18, mostrar de que é menor de idade. Se for maior de 18 ou mais, mostrar. Se a idade
for par e ímpar, também mostrar essas informações na tela.
Se a nota for 7 ou mais e entregou o trabalho ("Aprovado"). Senão, ("Reprovado").
Crie uma variável boolenana (True or Flase) para guardar se entregou o trabalho.

"""

 # Exercício 6

nome = input("Qual o seu nome? ")
print("Seu nome é " + nome + ".")

idade = int(input("Informe a sua idade: "))
print(f"Você tem {idade} anos de idade.")

if idade >= 18: 
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Verificação de par ou ímpar deve estar fora do if anterior
if idade % 2 == 0:
    print("Sua idade é par.")
else:
    print("Sua idade é ímpar.")

nota = float(input("Informe a sua nota: "))

# Pergunta sobre o trabalho ANTES de usar a variável
entregou_trabalho = input("Você entregou o trabalho? (sim/não): ").lower()
trabalho_entregue = (entregou_trabalho == "sim")  # variável booleana

if trabalho_entregue:
    print("Trabalho entregue.")
else:
    print("Não entregou o trabalho.")

# Verificação de aprovação #a adição do "and trabalho_entregue" garante que o aluno só será aprovado se tiver nota suficiente E tiver entregue o trabalho.
if nota >= 7 and trabalho_entregue:
    print("Você foi aprovado.")
else:
    print("Você foi reprovado.")

#No código anterior, eu estava perguntando se o aluno havia entregado o trabalho antes de usar a variável booleana, o que poderia causar confusão.
# Agora, a pergunta é feita antes de usar a variável, garantindo que o programa funcione corretamente.
