"""Crie um programa que peça ao usuário para digitar uma frase e conte
quantas vogais (a, e, i, o, u) aparecem na frase. Considere que a contagem
deve ser case-insensitive (ou seja, não diferencie maiúsculas de
minúsculas)."""

frase = input("Digite uma frase: ").upper()

print(f"Na frase {frase} ""tem:\n",
      f"QTD de A: {frase.count("A")}\n",
      f"QTD de E: {frase.count("E")}\n",
      f"QTD de I: {frase.count("I")}\n",
      f"QTD de O: {frase.count("O")}\n",
      f"QTD de U: {frase.count("U")}\n")