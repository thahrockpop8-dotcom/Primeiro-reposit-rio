# Solicitando os dados para o usuário
nome = input("Nome do cliente: ")
idade = int(input("Idade do cliente: "))
valor_compra = float(input("Valor da compra (R$): "))

# Usando .strip().lower() para garantir que respostas com letras maiúsculas/minúsculas funcionem
boleto_pago = input("Pagou o boleto? (Sim ou Não): ").strip().lower()
vip = input("É cliente VIP? (Sim ou Não): ").strip().lower()

print("\n--- RESUMO DO CADASTRO ---")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Boleto pago: {boleto_pago.capitalize()}")
print(f"É VIP: {vip.capitalize()}")

# Condição para liberar ou pendenciar
if boleto_pago == "sim" or vip == "sim":
    print("\nSTATUS: Compra LIBERADA! 🚀")
else:
    print("\nSTATUS: Compra PENDENTE. ⏳")
