# Aula 006

# Programa que realiza uma contagem regressiva de 10 até 0
import time  # Importa a biblioteca para controlar o tempo

# Laço que começa em 10 e vai até 0
for i in range(10, -1, -1):
    print(i)  # Exibe o valor atual da contagem
    time.sleep(1)  # Aguarda 1 segundo antes de continuar a contagem

print("Contagem finalizada!")  # Mensagem final após a contagem regressiva