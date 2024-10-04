# Função para verificar se um número é par ou ímpar
def verificar_paridade(numero):
    if numero % 2 == 0:
        return f"{numero} é Par"
    else:
        return f"{numero} é Ímpar"

# Solicitar ao usuário que insira um número
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = verificar_paridade(numero)
    print(resultado)
except ValueError:
    print("Por favor, insira um número inteiro válido.")