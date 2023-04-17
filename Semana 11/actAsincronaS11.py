print("¡BIENVENIDO AL PROGRAMA\n")

#Se solicta el número de datos a ingresar 
num = int(input("Ingrese la cantidad de datos que desea ingresar: "))

#Inician los contadores
pos = 0
neg = 0
nul = 0

#Se solicitan los datos y se verifica si son positivos, negativos o nulos
for i in range(num):
    while True:
        try:
            #Se solicitan los datos
            dat = int(input("Ingrese el dato N° " + str (i + 1) + ": "))
            break
        except ValueError:
            #Si se ingresa un dato incorrecto se muestra un mensaje de error y se pide que ingrese el dato nuevamente
            print("ERROR, ingrese un dato válido")
            
    #Se identifica si los datos ingresados son positivos, negativos o nulos
    if dat > 0:
        pos += 1
    
    elif dat < 0:
        neg += 1
        
    else:
        nul += 1
        
#Mostrar los resultados 
print("\nRESULTADOS:")
print(f"\nLa cantidad de números positivos es: {pos}")
print(f"La cantidad de números negativos es: {neg}")
print(f"La cantidad de números nulos es: {nul}")

print("\n¡FIN DEL PROGRAMA!")

            
    
    