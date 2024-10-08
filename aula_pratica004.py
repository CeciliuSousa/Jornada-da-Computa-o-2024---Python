# Aula 004

# Função que calcula a área de um retângulo a partir da largura e altura
def calcular_area_retangulo(largura, altura):
    return largura * altura  # Retorna a área como produto da largura e altura

# Solicita ao usuário a largura e altura do retângulo
largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

# Chama a função e armazena o resultado da área
area = calcular_area_retangulo(largura, altura)

# Exibe a área do retângulo
print(f"A área do retângulo é: {area:.2f}")