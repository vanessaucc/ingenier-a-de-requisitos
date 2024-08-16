print ("primer numero")
primerNumero= input("primer digito :")

print("segundo numero")
segundoNumero= input("segundo digito :")

if primerNumero == segundoNumero:
    print(f'los numeros son iguales')

elif primerNumero >= segundoNumero:
    print(f'{primerNumero} es mayor que {segundoNumero}')

elif segundoNumero >= primerNumero:
    print(f'{primerNumero} es menor que {segundoNumero}')

