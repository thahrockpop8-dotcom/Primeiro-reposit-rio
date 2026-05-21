"""Criem um jogo chamado A Ilha dos Códigos Perdidos.

O jogo precisa ter:

Nome do jogador;
Idade;
Vida inicial de 100;
Energia inicial de 50;
Pelo menos 5 fases;
Escolhas com if/elif/else;
Pelo menos 1 while;
Pelo menos 1 for;
Uso de operadores matemáticos;
Uso de operadores relacionais;
Uso de and, or ou not;
final de vitória ou derrota.

"""

nome_do_jogador = input ("Escolha um nome para o seu personagem: ")
idade = int(input("A idade do seu personagem: "))
vida_inicial = 100
energia_inicial = 50 
fase = 1


print ("========== Fase 1 ==========")
print (f"Olá, {nome_do_jogador}")
print ("========== Status ==========")
print (f"Vida: {vida_inicial}\nEnergia: {energia_inicial}")
print ("====================")

print ("Você encontrou um orc!")
atacar = input("Atacar?[S/N] ").upper().strip()

while True:
    if vida_inicial <= 0:
        print ("Você está morto!")
        break
    else:
        if atacar == "S":
            print ("É muita coragem a sua, enfrentá-lo! Que pena! Dano: -30.")
            vida_inicial = vida_inicial - 30
            atacar = input("Atacar?[S/N] ").upper().strip()
        else:
            print("Nada acontece!")
            break 
    

print (f"========== Fase 2 ==========")
print (f"Olá, {nome_do_jogador}")
print ("========== Status ==========")
print (f"Vida: {vida_inicial}\nEnergia: {energia_inicial}")
print ("====================")


print (f"========== Fase 3 ==========")
print ("Você chegou numa encruzilhada. As opções são: Floresta Sombria ou Montanha de Fogo.\nFaça a sua escolha com sabedoria.")
caminho1 = "Floresta Sombria"
caminho2 = 

caminho = input("")


if caminho1 == "floresta Sombria"
print ("Você escolheu a Floresta Sombria. Seus")










