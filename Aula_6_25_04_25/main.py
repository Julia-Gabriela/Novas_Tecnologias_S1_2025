from agenda import contato
import datetime


print("""
      
    *******************************
    * Bem vindo ao Sistema agenda *
    *******************************

""")

nome = "Fernanda"
telefone = "61993552745"
datanasc = datetime.date(2000,9,12)
email = "Fernanda.G@gmail.com"

contato1 = contato.Contato(nome, telefone, datanasc, email)

contato2 = contato.Contato()
contato2.nome = "Maria"
contato2.telefone = "61882445965"
contato2.datanasc = datetime.date(2004,7,19)
contato2.email = "Maria.G@gmail.com"