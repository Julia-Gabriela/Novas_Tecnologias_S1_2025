#Algoritmo pata coletar informações do usuário

nome = input("Digite se nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura:"))
massa = float(input("Digite seu peso: "))

print(f"Nome: {nome} \nIdade:{idade:x^4d} anos \nIMC: {massa/altura**2:.2f}")
