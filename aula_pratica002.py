# Aula 002

# Esse programa calcula um desconto baseado no valor da compra
compra = float(input("Digite o valor da compra: "))  # Solicita o valor da compra

# Verifica se o valor da compra é maior que 100 para aplicar o desconto
if compra > 100:
    desconto = compra * 0.1  # 10% de desconto
    print(f"Você ganhou um desconto de R$ {desconto:.2f}")  # Exibe o desconto formatado
else:
    print("Você não tem desconto.")  # Caso o valor seja menor ou igual a 100, sem desconto