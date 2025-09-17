lista = [25,60,90]

for i,num in enumerate(lista):
    print(f"{i+1}. {num}")

meses = {}
x=1
for meses_agno in ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]:
    meses[x]=meses_agno
    x+=1

lista_meses = [mes for mes in meses.values()]
print(lista_meses)


print(meses)

for i in range (0,19):
    print("Estoy aprendiendo...")
    print("... PYTHON!!!")

print("Eso es todo amigos.")


for i in range(1,10):
    print(i)

edad=int(input("edad: "))

while edad<0 and edad>100:
    print("La edad no es correcta, vuelve a intentar.")
    edad=int(input("edad: "))

print("La edad introducida es " + str(edad))