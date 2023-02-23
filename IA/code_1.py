#Validacion de Cadena SI y No
si = ['Si', 'SI', 'SÍ', 'Sí', 'si', 'sí', 'sÍ', 'sI']
no = ['No', 'NO', 'NÓ', 'Nó', 'no', 'nó', 'nÓ', 'nO']


#Valida si es un numero entero o no 
def ValidacionNum(numero):
    try:
        int(numero)
        return False
    except:
        return True


#Todas las validaciones de las entradas de datos
def Validaciones(ID):
    if(ID == 1):
        resp = input('¿Agregar Nodo de caminos? \n' + '1.SI \n' + "2.NO \n")
        while(len(list(filter(lambda x: x == resp, si))) == 0 and len(list(filter(lambda x: x == resp, no))) == 0 ):
            resp = input('EL VALOR INGRESADO NO ES VALIDO')
        if(len(list(filter(lambda x: x == resp, si))) != 0):  
            return True
        else:
            return False
    elif(ID == 2):
        t = input('Ingresa la cantidad de nodos: ')
        while(ValidacionNum(t)):
            t= input('ERROR! Ingrese un valor valido porfavor! \n')
        return int(t)
    elif (ID== 3):
        ni = input('Ingrese el nodo inicial del recorrido: ')
        while (ni == ''):
            ni = input('ERROR! Ingrese un valor valido! \n')
        return ni
    elif (ID== 4):
        nf = input('Digite el nodo final del recorrido: ')
        while(nf==''):
            nf= input('ERROR! Ingrese un valor valido \n')
        return nf
    elif(ID == 5):
        usuario = input('Ingrese nombre de Usuario: ')
        while(usuario==''):
            usuario = input('ERROR INGRESE UN NOMBRE VALIDO \n')
        return usuario
    elif(ID==6):
        opcion = input('Elija una opcion: ')
        return int(opcion)
    elif(ID==7):
        opcion = input("Digite el ID que desea buscar: ")
        while(ValidacionNum(opcion)):
            opcion=input('Valor invalido, ingrese un valor numerico: ')
        return int(opcion)
    elif (ID == 8):
        resp2 = input('¿Desea eliminar un nodo? \n' + '1.SI \n' + "2.NO \n")
        while(len(list(filter(lambda x: x == resp2, si))) == 0 and len(list(filter(lambda x: x == resp2, no))) == 0 ):
            resp2 = input('EL VALOR INGRESADO NO ES VALIDO')
        if(len(list(filter(lambda x: x == resp2, si))) != 0):  
            return True
        else:
            return False


       



