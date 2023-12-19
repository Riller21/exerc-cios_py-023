# Inicializando variáveis
total_colaboradores = 0
total_gasto_abonos = 0
total_minimo_pago = 0
maior_valor_abono = 0

# Loop para receber os salários
while True:
    salario = float(input("Salário (digite 0 para encerrar): "))

    # Verifica se o usuário deseja encerrar
    if salario == 0:
        break

    # Calcula o abono de acordo com as regras
    abono = max(salario * 0.2, 100)

    # Atualiza as variáveis
    total_colaboradores += 1
    total_gasto_abonos += abono
    if abono == 100:
        total_minimo_pago += 1
    if abono > maior_valor_abono:
        maior_valor_abono = abono

    # Exibe o salário e o abono
    print(f"R$ {salario:.2f} - R$ {abono:.2f}")

# Exibe os resultados finais
print("\nForam processados", total_colaboradores, "colaboradores")
print("Total gasto com abonos: R$", total_gasto_abonos)
print("Valor mínimo pago a", total_minimo_pago, "colaboradores")
print("Maior valor de abono pago: R$", maior_valor_abono)
