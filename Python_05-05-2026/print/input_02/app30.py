#Data: 21/05/2026

# Exercício passado no Google Classroom - 
# Crie um programa que faça o cadastro de uma compra. O programa deve pedir:
# Nome do cliente; Idade do cliente; Valor da compra; Se o cliente pagou o boleto: sim ou não; Se o cliente é cliente VIP: sim ou não
# Depois, o programa deve mostrar: Nome do cliente; idade; valor da compra; se o boleto foi pago; se o cliente é VIP;
# Mensagem final dizendo se a compra foi liberada ou ficou pendente.

#Cadastro do Cliente

nome = input("Por favor, informe o seu nome: ")
idade = int(input("Sua idade: "))
valor_compra = float(input("Por favor, informe o valor da compra: "))


#VIP 

vip = input("Você é cliente VIP? (sim/não): ").lower()
cliente_vip = (vip == "sim")

if cliente_vip:
    print ("Cliente VIP!")
else:
    print ("Cliente ainda não é VIP.")


#Boleto

pagamento_boleto = input("Você pagou o boleto pendente? (sim/não): ").lower()
boleto_pago = (pagamento_boleto == "sim")

if boleto_pago:
    print ("Boleto pago.")
else:
    print ("Boleto não pago/pendente.")


print (f"Olá {nome}. Bem-vindo(a) Central de atendimento. Atualmente, você tem {idade} anos. Você também faz parte de um grupo especial do nosso corpo de cliente: {vip}. \nE o valor da sua compra foi {valor_compra}. Verificamos que seu boleto está {pagamento_boleto}. Sua compra foi liberada.")
