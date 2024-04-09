menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

==>
'''

saldo = 0
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
dp_total = 0

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        print("Depósito")
        valor_deposito = float(input("Digite o valor a ser depositado: "))  
        if valor_deposito <= 0:
            print("Deposito com valor não autorizado")    
        else:
            saldo += valor_deposito
            print(f"Foram depositados {valor_deposito} reais com sucesso!!")   
            dp_total += 1
            
    elif opcao == "2":
        print("Saque")
        valor_sacado = float(input("Digite o valor a ser sacado: "))

        if valor_sacado <= 0 or valor_sacado > 500.00:
            print("Valor não autorizado.")
        elif numero_saques >= 3:
            print("Limite de saques diários atingidos.")
        else:
            saldo -= valor_sacado
            numero_saques += 1
            print(f"Foram sacados com sucesso {valor_sacado} Reais")
                                
    elif opcao == "3":
        print("Extrato")
        print(f"O valor do seu saldo atual é: {saldo}")
        print(f"Foram feitos {numero_saques} saques")
        print(f"Foram feitos {dp_total} depositos")
    
    elif opcao == "4":
        print("Saindo...")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")