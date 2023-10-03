import os

def stark_normalizar_datos(lista_heroes: list[dict]):
    #La función recibe una lista de diccionarios, si los valores de las keys peso, altura, edad o fuerza no estan en el tipo de dato adecuado los convierte. Imprime un mensaje si la lista que recibe está vacia y otro si normalizó al menos un dato.
    flag = False
    mensaje = "Datos normalizados"
    if not lista_heroes:
        print("Error lista de héroes vacía")
    else:
        for heroe in lista_heroes:
            for key, value in heroe.items():
                if key == "edad" or key == "fuerza" and type(value) != int:
                    value = int(value)  
                    heroe.update({key: value})
                    flag = True
                elif key == "peso" or key == "altura" and type(value) != float:
                    value = float(value)
                    heroe.update({key: value})
                    flag = True
    
    if flag:
        print(mensaje)

def obtener_nombre(heroe: dict) -> str:
    # Recibe:  un heroe de tipo dict, 
    # retorna: un string con el nombre del heroe
    nombre = heroe.get("nombre")
    return f"Nombre: {nombre}"

def imprimir_dato(dato:str):
    #recibe: un string
    #Imprime el dato recibido
    #Retorno: no tiene
    print(dato)

def stark_imprimir_nombres_heroes(lista_heroes:list[dict]):
    #Recibe: lista de diccionarios (heroes)
    #Retorna: -1 si la lista esta vacia
    #Llama a las funciones imprimir dato y obtener nombre para poder listar los nombres de los héroes
    if len(lista_heroes) == 0:
        return -1
    else:
        for heroe in lista_heroes:
            imprimir_dato(obtener_nombre(heroe))

def obtener_nombre_y_dato(heroe:dict, key:str):
    #Recibe: un dict(heroe) y un string
    #Llama a la funcion obtener nombre
    #Retorna: nombre del heroe junto con la key seleccionada con su valor
    return f"{obtener_nombre(heroe)} | {key}: {heroe.get(key)}"

def stark_imprimir_nombres_alturas(lista_heroes:list[dict]):
    #Recibe una list de dict
    #Si la list esta vacia retorna -1. Sino recorre la lista y llama a la funcion obtener_nombre_y_dato para imprimir nombre, y el dato de caa heroe 
    if len(lista_heroes) == 0:
        return -1
    else: 
        for heroe in lista_heroes:
            print(obtener_nombre_y_dato(heroe,"altura"))

def calcular_max(lista_heroes:list[dict], key:str)->dict:
    #Recibe: list de dict y un string que representa el dato a calcular
    #calcula el maximo valor del string ingresado
    #Retorna: nombre del heroe con el maximo valor del dato ingresado como parametro
    heroe_max = None
    valor_max = 0
    for heroe in lista_heroes:
        parametro = heroe.get(key)
        if parametro > valor_max:
            valor_max = parametro
            heroe_max = heroe

    return heroe_max
 
def calcular_min(lista_heroes: list[dict], key:str)->dict:
    #Recibe: list de dict y un string que representa el dato a calcular
    #calcula el minimo valor del string ingresado
    #Retorna: nombre del heroe con el minimo valor del dato ingresado como parametro
    heroe_min = None
    valor_min = 0
    for heroe in lista_heroes:
        parametro = heroe.get(key)
        if valor_min == 0 or parametro < valor_min:
            valor_min = parametro
            heroe_min = heroe
    
    return heroe_min

def calcular_max_min_dato(lista_heroes:list[dict],calculo:str,key:str)->dict:
    #Recibe: list de dict, string calculo que debe ser minimo o maximo, y una key que es el dato a calcular
    #Calcula lo indicado por los parametros calculo y key
    #Retorna el nombre del heroe 
    if calculo == "maximo":
        return calcular_max(lista_heroes,key)
    elif calculo == "minimo":
        return calcular_min(lista_heroes, key)

def stark_calcular_imprimir_heroe(lista_heroes:list[dict],max_o_min:str,key:str):
    #Recibe: lista tipo dict de heroes, un string:debe ser maximo o minimo, y una key que es el parametro a evaluar(ej:peso)
    #Llama a la funcion calcular_max_min_dato para que calcule lo solicitado
    #Hace un print del dato obtenido

    calcular_max_min_dato(lista_heroes,max_o_min,key)
    match max_o_min:
        case "maximo":
            valor = "Mayor"
        case "minimo": 
           valor = "Menor"
        
    print(f"{valor} {key}: {obtener_nombre_y_dato(calcular_max_min_dato(lista_heroes,max_o_min,key), key)}")

def sumar_dato_heroe(lista_heroes:list[dict], key:str):
    acumulador = 0
    for heroe in lista_heroes:
        if type(heroe) == dict and len(heroe) > 0 and (type(heroe.get(key)) == float or type(heroe.get(key)) == int):
            acumulador += heroe.get(key)
    
    
    return acumulador

def dividir(dividendo,divisor):
    resultado =  dividendo/divisor if divisor != 0 else 0
    return resultado

def calcular_promedio(lista_heroes:list[dict], key:str):
    promedio = dividir(sumar_dato_heroe(lista_heroes,key), len(lista_heroes)) 
    return promedio

def stark_calcular_imprimir_promedio_altura(lista_heroes:list[dict]):
    promedio_altura = dividir(sumar_dato_heroe(lista_heroes,"altura"),len(lista_heroes)) if lista_heroes else -1
    imprimir_dato(f"El promedio de altura es: {promedio_altura}")

def stark_imprimir_identidades_bajo_alto(lista_heroes:list[dict]):
    alto = obtener_nombre_y_dato(calcular_max_min_dato(lista_heroes,"maximo","altura"),"identidad")
    bajo = obtener_nombre_y_dato(calcular_max_min_dato(lista_heroes,"minimo","altura"),"identidad")
    print(f"El héroe más alto es: {alto} \nEl héroe mas bajo es: {bajo}")
    

def imprimir_menu():
    menu = """
    1 - Listar nombres de superheroes\n 
    2 - Listar nombre y altura del superheroe\n
    3 - Superheroe mas alto\n 
    4 - Superheroe mas bajo\n 
    5 - Altura promedio de los superheroes\n 
    6 - Identidad de Superheroe mas bajo y mas alto\n 
    7 - Superheroe mas pesado y menos pesado\n
    0 - Salir
    """
    imprimir_dato(menu)

def validar_entero(numero:str):
    return numero.isdigit()

def stark_menu_principal():
    imprimir_menu()
    opcion = input("Por favor elija una opción: ")
    opcion= int(opcion) if validar_entero(opcion) else -1
    return opcion

def limpiar_consola() -> None:
    _ = input("\n Presione una tecla para continuar")
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')