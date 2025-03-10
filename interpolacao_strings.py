nome = "Daniel"
idade = 30
profissao = "Programador"
linguagem = "Python"

data = {"nome": "Daniel", "idade": 30, "saldo": 45.435}

print("Nome: %s Idade: %d" % (nome, 30))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {name} Idade: {age}".format(name=nome, age=idade))
print("Nome: {nome} Idade: {idade} Saldo: {saldo: .2f}".format(**data))
