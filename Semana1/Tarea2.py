print ("control de regsitro")
produccionLitros = input("digite producido en litros: ")
print ("conversion")
conversion = int(produccionLitros)*float(3.785)

print ("valor galon")
valor = input("digite el valor: ")

print ("ganacias")
ganancia = conversion*int(valor)
print (f'la ganancia del productor es {ganancia}')