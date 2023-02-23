from code_1 import Validaciones
import json
graph={}
fileJson = "datos.json"
with open (fileJson, 'r') as file:
    info = json.load(file)


# MENU PRINCIPAL
def menu():
    print("------ MENU PRINCIPAL -------")
    print ('1. INICIAR PROGRAMA')
    print ('2. CONSULTAR DATOS')
    print ('3. SALIR')
    respuesta = Validaciones(6)
    while (respuesta!=0):
        if(respuesta == 1):
            inicio()
            menu()
            return
            
        elif(respuesta==2):
            consultadatos()
            return
        elif(respuesta==3):
            print("Saliendo...")
            return


# MENU CONSULTA DE DATOS
def consultadatos():
    print(" CONSULTA DE DATOS")
    print(" 1. Ver todos datos")
    print(" 2. Buscar id")
    print(" 3. Atras")

    resp = Validaciones(6)
    while(resp != 0):
        if(resp ==1 ):
            print("")
            print('DATOS ENCONTRADOS: ')
            print(info)
            menu()
            break
        elif (resp == 2):
            id_usuario()
            break
        elif ( resp == 3):
            menu()
            break
            
#Escribir JSON y dar formato
def insert_json(datos):
    fileJson = 'datos.json'
    with open(fileJson,'w') as file:
        json.dump(datos,file, indent= 4)


#Buscar id Usuario
def id_usuario():
    id = Validaciones(7)
    for i in info["_id"]:
        if id == i["_id"]:
            print(i)
            return
    
    print("NO EXISTE!")



#Llenar Nodos - Unir Nodos - Crear ramificaciones o Nodos Caminos - Eliminar Nodos
def llenar_nodos():

    conex_nodo=[]

    d = Validaciones(2)
    for i in range(d):
        valor = input(f"Digite el nombre del nodo {i + 1} : ").upper()
        while (valor ==''):
            valor = input (f'No existe \n')
            continue
        nodo = valor
        respuesta = Validaciones(1)
        if(respuesta==1):
            estado=True
            while(estado==True):
                print(("Digite el nombre del nodo a agregar   "))
                nodo_unir=input()
                if(nodo_unir ==''):
                    print('Ingrese un valor valido.\n')
                    continue
                else:
                    conex_nodo.append(nodo_unir)
                    print(conex_nodo)   if nodo_unir not in conex_nodo else print('Nodo existente')
                    rpta=Validaciones(1)
                if(rpta==True):
                    estado=True
                else:
                    estado=False
        else:
            print("No se agregan mas nodos")

        eliminar=Validaciones(8)
        while eliminar:
            print(f'NODOS: \n {conex_nodo}')
            nodo_eliminar=input("INGRESE EL NODO A ELIMINAR\n").upper()
            conex_nodo.remove(nodo_eliminar) if nodo_eliminar in conex_nodo else print("Nodo no encontrado!")
            eliminar = Validaciones(8)

        graph.update({nodo: set(conex_nodo)})
        conex_nodo.clear()
        print(graph)
    return d


# Return all graphs from start to goal 
def dfs_paths(graph, start, goal):
    # Define stack variable
    stack = [[start]]
    # Do the process while there are paths to follow
    while stack:
        path = stack.pop()
        node = path[-1]
        for next in graph[node] - set(path):
            # If a correct path is founded, then return the path with the generator
            # else write a new path and follow iterating.
            if next == goal:
                yield path + [next]
            else:
                stack.append(path + [next])


# Print paths
def inicio():
    usuario = Validaciones(5)
    cantidad_nodos = llenar_nodos()
    vi=Validaciones(3)
    vf=Validaciones(4)
    rutas = list(dfs_paths(graph, vi, vf))

    menor=[]
    mayor=[]
    rutas_ig=[]
    for ruta in rutas:
        if len(ruta)> len(mayor) or mayor==[]:
            mayor = ruta
        if len(ruta) < len (menor) or menor == []:
            menor = ruta
        if len(ruta) == len(rutas_ig):
            rutas_ig=ruta



# Imprime Json en formato 'Key' : 'value' 
    info.append({
      "id": len(info)+1,
      "usuario" : usuario,
      "cantidad_de_nodos" : cantidad_nodos,
      "cantidad_de_rutas" : len(rutas),
      "nodo_inicial" : vi, 
      "nodo_final" : vf,
      "rutas": rutas,
      "ruta_mayor": mayor,
      "ruta_menor": menor,
      "ruta_igual": rutas_ig
      })
    with open(fileJson, 'w') as file:
        json.dump(info, file)
    print("<-------------------------------------->")
    print("REGISTRO INGRESADO EXITOSAMENTE!")
    print("<------------------------------------->")




menu()



