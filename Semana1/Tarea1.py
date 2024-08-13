print ("area del rectangulo")
baseRectangulo = input("digite la base: ")
alturaRectangulo = input("digite la altura: ")
areaRectangulo = int(baseRectangulo)*int(alturaRectangulo)
print (f'la area del rectangulo es {areaRectangulo}')

print ("area del triangulo")
baseTriangulo = input("digite la base: ")
alturaTriangulo = input("digite la altura: ")
areaTriangulo = int(baseTriangulo)*int(alturaTriangulo)/2
print (f'la area del triangulo es {areaTriangulo}')

print ("area del terreno")
area_terreno = areaRectangulo+areaTriangulo
print (f'la area del terreno es {area_terreno}')