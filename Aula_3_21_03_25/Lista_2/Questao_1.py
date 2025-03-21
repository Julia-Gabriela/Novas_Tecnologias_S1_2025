"""
Crie um programa que some todos os números pares entre 1 e N , onde N é fornecido pelo
usuário
"""

n = int(input("Digite um número: "))

soma = 0

for num in range(0, n+1, 2):
    soma+=num

print(f"De um ate {n}, a soma é {soma}") 