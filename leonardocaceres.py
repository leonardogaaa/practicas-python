x1=int(input("¿Que coordenada inicial es en x?"))
y1=int(input("¿Que coordenada inicial es en y?"))
z1=int(input("¿Que coordenada inicial es en z?"))
x2=int(input("¿Que coordenada final es en x?"))
y2=int(input("¿Que coordenada final es en y?"))
z2=int(input("¿Que coordenada final es en z?"))
a=(x2-x1)**2
b=(y2-y1)**2
c=(z2-z1)**2
d=(1/2)
print((a+b+c)**d)

lado1=float(input("¿Cual es el valor del cateto1"))
lado2=float(input("¿Cual es el valor del cateto2?"))
lado3=float(input("¿Cual es el valor del hipotenusa?"))
print((lado1**2)+(lado2**2)==lado3**2)  #true

puntox1=float(input("¿Por que punto paso en x1?"))
puntoy1=float(input("¿Por que punto paso en y1?"))
puntox2=float(input("¿Por que punto paso en x2?"))
puntoy2=float(input("¿Por que punto paso en y2?"))
print((puntoy2-puntoy1)/(puntox2-puntox1))

segundos=float(input("¿Cuantos segundos?"))
min=(segundos//60)
seg=(segundos%60)
horas=(min//60)
minu=(min%60)
print(horas,minu,seg)   #Horas/Minutos/Segundos