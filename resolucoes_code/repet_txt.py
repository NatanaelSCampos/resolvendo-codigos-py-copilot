# Solicitar ao usuário que insira uma string e um número inteiro
texto = input("Digite uma string: ")
repeticoes = int(input("Digite o número de repetições: "))

# Repetir a string o número de vezes informado
texto_repetido = (texto + ' ') * repeticoes

# Exibir o texto repetido
print("Texto repetido:")
print(texto_repetido)