print ("telas")
produccionMetros = input("digite las medidas en metros: ")
print ("conversion")
conversion = int(produccionMetros)*float(0.0254)

print ("valor pulgada")
valor = input("digite el valor: ")

print ("costo")
costo = round (conversion*int(valor))
print (f'la ganancia del productor es {costo}')

