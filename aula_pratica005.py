# Aula 005

import random
import string

# Função para gerar uma senha com caracteres aleatórios
def gerar_senha(tamanho):
    # Conjunto de caracteres a serem usados: letras, números e símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Gera uma senha aleatória do tamanho especificado
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha  # Retorna a senha gerada

# Solicita o tamanho da senha ao usuário
tamanho_senha = int(input("Digite o tamanho da senha que deseja gerar: "))

# Chama a função e armazena a senha gerada
senha = gerar_senha(tamanho_senha)

# Exibe a senha gerada
print(f"Sua senha gerada é: {senha}")