# Solicitar ao usuário que insira dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicitar ao usuário que escolha uma operação
print("Escolha a operação que deseja realizar:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

operacao = input("Digite o número da operação (1/2/3/.4): ")

# Realizar a operação com base na escolha do usuário
if operacao == '1':
    resultado = numero1 + numero2
    print(f"Resultado da soma: {resultado}")
elif operacao == '2':
    resultado = numero1 - numero2
    print(f"Resultado da subtração: {resultado}")
elif operacao == '3':
    resultado = numero1 * numero2
    print(f"Resultado da multiplicação: {resultado}")
elif operacao == '4':
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"Resultado da divisão: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")
