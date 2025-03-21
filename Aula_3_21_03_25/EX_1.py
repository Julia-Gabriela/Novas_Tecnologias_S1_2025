nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
massa = float(input("Digite seu peso: "))
est_civil = input("Digite seu estado civil:\n" + "S-Solteiro\n" + "V-Viúvo\n" + "D-Divorciado\n" + "C-Casado\n" + "U-União Estável\n")

imc = massa / altura**2

if imc < 18.5:
    pimc = "Abaixo do peso normal."
elif imc >= 18.5 and imc < 25:
    pimc = "Peso normal."
elif imc >= 25 and imc < 30:
    pimc = "Acima do normal."
elif imc >= 30 and imc < 35:
    pimc = "Obesidade 1."
elif imc >= 35 and imc < 40:
    pimc = "Obesidade 2."
elif imc >= 40:
    pimc = "Obesidade 3."

match est_civil:
    case "C":
        pcivil = "Casado"
    case "S":
        pcivil = "Solteiro"
    case "D":
        pcivil = "Divorciado"
    case "V":
        pcivil = "Viúvo"
    case _:
        pcivil = "Estado Civil inexistente"

print(
    f"""
    *************************************************
    *            Formulário de Usuário              *
    *                                               *
    *Nome: {nome}                                   *
    *Idade: {idade}                                 *
    *{"Adulto" if idade >= 18 else "Não adulto"}    *
    *IMC: {imc:.2f}                                 *
    *{pimc}                                         *
    *{pcivil}                                       *
    *************************************************
    """
)
