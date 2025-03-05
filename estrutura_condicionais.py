MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Autorizado a tirar a habilitação!!!")

if idade < MAIOR_IDADE:
    print("Não autorizado a tirar a habilitação!!!")

if idade >= MAIOR_IDADE:
    print("Autorizado a tirar a habilitação!!!")

else:
    print("Não autorizado a tirar a habilitação!!!")


if idade >= MAIOR_IDADE:
    print("Autorizado a tirar a habilitação!!!")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas não pode fazer aulas práticas")

else:
    print("Não autorizado a tirar a habilitação!!!")
    