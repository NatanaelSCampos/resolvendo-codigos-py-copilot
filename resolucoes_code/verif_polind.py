# Função para verificar se uma palavra é palíndromo
def verificar_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")  # Converter para minúsculas e remover espaços
    return palavra == palavra[::-1]  # Verifica se a palavra é igual à sua versão invertida

# Solicitar ao usuário que insira uma palavra
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

# Verificar e exibir o resultado
if verificar_palindromo(palavra):
    print(f'"{palavra}" é um palíndromo!')
else:
    print(f'"{palavra}" não é um palíndromo.')