from xml.etree.ElementTree import tostring


nombre=input ("dime tu nombre >> ")
print(nombre.upper)
numletras=len(nombre)
print("\nTu nombre tiene "+str(numletras)+" letras")

for i in range (numletras): 
    print("\n"+ nombre)