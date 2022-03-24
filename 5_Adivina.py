from random import random
num1= randint(2,10)
num2=randint(2,10)
multiplicacion=num1*num2
res=int(input("Adivina la multiplicacion(4- 100)>> "))

if res==multiplicacion:
    print ("tomaaa! Exacto, el resultado es ", multiplicacion)
else:
    print ("ooohhhh!! que mal, el resultado era ", multiplicacion)