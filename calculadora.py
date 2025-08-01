print("\n******************* Calculadora em Python *******************")

print("selecione o numero da operação desejada: ")

print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisao")


operação = input("digite a operação (1/2/3/4): ")

primeiroNUmero = int(input("digite o primeiro numero: "))

segundoNumero = int(input("digite o segundo numero: "))

if operação == "1":
    resultado = primeiroNUmero + segundoNumero 
    print(f"Resultado: {primeiroNUmero} + {segundoNumero} = {resultado: }")	

elif operação == "2":
    resultado = primeiroNUmero - segundoNumero 
    print(f"Resultado: {primeiroNUmero} - {segundoNumero} = {resultado: }")

elif operação == "3":
    resultado = primeiroNUmero * segundoNumero 
    print(f"Resultado: {primeiroNUmero} x {segundoNumero} = {resultado: }")

elif operação == "4":
    if segundoNumero != 0:
        resultado = primeiroNUmero / segundoNumero 
        print(f"Resultado: {primeiroNUmero} / {segundoNumero} = {resultado:.2f}")
    else:
        print("Não é possivel dividir por zero!")

else:
    print("Operação inválida! Escolha de 1 a 4")
