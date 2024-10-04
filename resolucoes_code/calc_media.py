# Função para calcular a média de três notas
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

# Solicitar ao usuário que insira as três notas
try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Calcular e exibir a média
    media = calcular_media(nota1, nota2, nota3)
    print(f"A média das três notas é: {media:.2f}")
except ValueError:
    print("Por favor, insira valores numéricos válidos para as notas."