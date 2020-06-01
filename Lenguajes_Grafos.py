import os

class Grafo():
    Estados = 0
    Abecedario = ""

    def impresion_tabla(self,Tabla, Estados, Letras):
        for i in range(0,Estados+1):
            for j in range(0,len(Letras)+1):
                print(Tabla[i][j], end = "  ")
            print()
 
    def Contar_letras(self,Abecedario, Letras):
        for i in range(0,len(Abecedario)):
            if Abecedario[i] != " " and Abecedario[i] != ",":
                Letras.append(Abecedario[i])
        return Letras

    def Formar_Tabla(self, Tabla, Estados,Letras):
        for i in range(0,Estados+1):
            Tabla.append([])
            for j in range (0,len(Letras)+1):
                Tabla[i].append([])
        return Tabla

    def Llenar_tabla_Fase_0(self, Tabla, Letras, Estados):
        for i in range (1,Estados+1):
            for j in range(1,len(Letras)+1):
                Tabla[i][j] = 0

        for i in range (0,len(Letras)+1):
            if i == 0:
                Tabla[0][0] = ("¬") 
            else:
                Tabla[0][i] = Letras[i-1]
            for j in range (1,Estados+1):
                Tabla[j][0] = j
        return Tabla

    def Formar_Enlaces(self,Tabla,Estados,Letras):
        self.Enlace = 0
        for i in range (1,Estados+1):
            print("\nEstá en el estado", i, ":")
            for j in range(0,len(Letras)):
                self.Enlace = validar_enlace("  Enlace de la letra (" + Letras[j] + ") hacía el estado: ",Estados)
                Tabla[i][j+1]= self.Enlace
        return Tabla

def validar_enlace(Texto,Estados):
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input(Texto))
            if num <= Estados and num >= 0:
                correcto=True
            else:
                print("Teclea un numero mayor a cero y menor a la cantidad de estados")
                ValueError
        except ValueError:
            print("Error, introduce un numero entero")
    return num

def validar(parte):
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input(parte))
            if num > 0:
                correcto=True
            else:
                print("Teclea un numero mayor a cero")
                ValueError
        except ValueError:
            print("Error, introduce un numero entero")
    return num

def Generar_Grafo(Automata,Tabla, Letras):

    os.system("cls")
    print("\t.:Proyecto Automatas y Lenguajes Formales:.\n\n")

    Automata.Estados = validar("Cantidad de estados del autómata: ")
    Automata.Abecedario = input("Ingrese el alfabeto a usar: ")    
    Letras = Automata.Contar_letras(Automata.Abecedario , Letras)
    Tabla = Automata.Formar_Tabla(Tabla, Automata.Estados,Letras)
    Tabla = Automata.Llenar_tabla_Fase_0(Tabla,Letras, Automata.Estados)
    Tabla = Automata.Formar_Enlaces(Tabla, Automata.Estados, Letras)
    
    os.system("pause")
    menu(Automata, Tabla, Letras, Estados_Aceptacion)

def Agregar_Estados_Aceptacion(Automata, Estados,Estados_Aceptacion):

    Estados_Aceptacion = []

    os.system("cls")
    print("\t.:Proyecto Automatas y Lenguajes Formales:.\n\n")
    n_estados = validar_enlace("Cantidad de estados de aceptación que hay: ", Estados)
    
    for i in range(0,n_estados):
        e_a = validar_enlace("Estado: ", Estados)
        Estados_Aceptacion.append(e_a)
    
    os.system("pause")
    menu(Automata, Tabla, Letras, Estados_Aceptacion)

def Verificar_palabras(Automata, Tabla, Letras, Estados_Aceptacion):
    Estado_actual = 1
    contar_letra = 0
    Letras_aux = []

    palabra = input("\nIngrese la palabra a verificar: ")
    palabra_aux = ""    
    Letras_aux = Automata.Contar_letras(palabra , Letras_aux)

    for i in range (0,len(Letras_aux)):
        if Letras_aux[i] not in Letras:
            print("\n\tPalabra no válida\n")
            break

    comprobar = True

    while comprobar == True:
        for i in range(0,len(Letras) + 1):
            if contar_letra < len(palabra):
                if Tabla[0][i] == palabra[contar_letra]:

                    Estado_actual = Tabla[Estado_actual][i]
                    palabra_aux = palabra_aux + palabra[contar_letra]
                    contar_letra += 1

                    if palabra_aux == palabra and Estado_actual in Estados_Aceptacion:
                        print("\n\tPalabra válida\n")
                        comprobar = False
                        break
                    elif Estado_actual == 0:
                        print("\n\tPalabra no válida\n") 
                        comprobar = False
                        break
            else:
                print("\n\tPalabra no válida\n") 
                comprobar = False
                break

    os.system("pause")
    menu(Automata,Tabla,Letras,Estados_Aceptacion)            

def imprimir(Automata,Tabla, Letras, Estados_Aceptacion):
    print()
    Automata.impresion_tabla(Tabla, Automata.Estados, Letras)
    print()
    os.system("pause")
    menu(Automata,Tabla,Letras,Estados_Aceptacion) 

def menu(Automata,Tabla,Letras, Estados_Aceptacion):

    os.system("cls")
    print("\t.:Proyecto Automatas y Lenguajes Formales:.\n")
    print("1. Generar Grafo del Automata")
    print("2. Agregar estados de aceptación")
    print("3. Verificar palabras")
    print("4. Mostrar tabla de adyacencia")
    print("5. Salir\n")

    opc = validar("Opcion: ")

    while opc > 5:
        print("\n\tIntroduce una opción válida")
        opc = validar("\nOpcion: ")
        
    if opc == 1:
        Generar_Grafo(Automata, Tabla, Letras)
    elif opc == 2:
        Automata.Estados_Aceptacion = Agregar_Estados_Aceptacion(Automata, Automata.Estados, Estados_Aceptacion)
    elif opc == 3:
        Verificar_palabras(Automata,Tabla, Letras, Estados_Aceptacion)
    elif opc == 4:
        imprimir(Automata,Tabla, Letras, Estados_Aceptacion)
    else:
        os.system("cls")
        os.system("exit ()")

if __name__ == "__main__":
    Automata = Grafo()
    Tabla = []
    Letras = []
    Estados_Aceptacion = []
    menu(Automata, Tabla, Letras, Estados_Aceptacion)
