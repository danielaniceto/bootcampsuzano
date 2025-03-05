saldo = 5000
saque = 30000

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!!")