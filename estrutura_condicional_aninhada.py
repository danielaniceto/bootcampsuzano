conta_corrente = True
saldo_cc = 5000
saque_cc = 65000
cheque_especial_cc = 3000

conta_estudante = False
saldo_ce = 500
saque_ce = 650

if conta_corrente:
    if saque_cc <= saldo_cc:
        print("CONTA CORRENTE: Saque realizado com sucesso!!!")

    elif saque_cc <= (saldo_cc + cheque_especial_cc):
        print("CONTA CORRENTE: Saque AUTORIZADO, usando cheque especial !!!")
        
    else:
        print("CONTA CORRENTE: Saque não autorizado!!!")

elif conta_estudante:
    if saldo_ce >= saque_ce:
        print("CONTA ESTUDANTE: Saque realizado com sucesso!!!")

    else:
        print("CONTA ESTUDANTE: Saque não autorizado, saldo insuficiente!!!")
        
else:
    print("Nosso sistema não reconheceu seu tipo de conta, entre em contato com seu gerente para saber mais")
