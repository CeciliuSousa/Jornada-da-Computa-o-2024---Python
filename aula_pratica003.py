# Aula 003

# Esse programa calcula a média de 5 notas usando um laço de repetição 'for'
soma_notas = 0  # Inicializa a soma das notas com 0

# Laço que repete 5 vezes, solicitando uma nota a cada iteração
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))  # Solicita a nota atual
    soma_notas += nota  # Adiciona a nota à soma total

# Calcula a média dividindo a soma das notas pelo número de notas
media = soma_notas / 5
print(f"A média das notas é: {media:.2f}")  # Exibe a média formatada