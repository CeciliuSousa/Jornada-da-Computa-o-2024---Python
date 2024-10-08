# Aula 001

# Esse programa implementa uma calculadora simples para duas operações (soma e multiplicação)
print("Calculadora simples")  # Exibe uma mensagem inicial

# Solicita ao usuário dois números e converte para float (números decimais)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza a soma e a multiplicação dos números
soma = num1 + num2
multiplicacao = num1 * num2

# Exibe os resultados formatados
print(f"A soma de {num1} e {num2} é {soma}")
print(f"A multiplicação de {num1} por {num2} é {multiplicacao}")