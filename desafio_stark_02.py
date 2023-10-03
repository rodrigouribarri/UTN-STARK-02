from biblioteca_stark_02 import(stark_menu_principal,stark_imprimir_nombres_heroes,stark_imprimir_nombres_alturas,stark_calcular_imprimir_heroe,stark_calcular_imprimir_promedio_altura,stark_imprimir_identidades_bajo_alto, stark_normalizar_datos, limpiar_consola)


def stark_marvel_app(lista_heroes:list[dict]):
    stark_normalizar_datos(lista_heroes)
    while True:
        opcion_elegida = stark_menu_principal()
        match opcion_elegida:
            case 0:
                break
            case 1:
                stark_imprimir_nombres_heroes(lista_heroes)
            case 2:
                stark_imprimir_nombres_alturas(lista_heroes)
            case 3:
                stark_calcular_imprimir_heroe(lista_heroes,"maximo","altura")
            case 4:
                stark_calcular_imprimir_heroe(lista_heroes,"minimo","altura")
            case 5:
                stark_calcular_imprimir_promedio_altura(lista_heroes)
            case 6:
                stark_imprimir_identidades_bajo_alto(lista_heroes)
            case 7:
                stark_calcular_imprimir_heroe(lista_heroes,"maximo","peso")
                stark_calcular_imprimir_heroe(lista_heroes,"minimo","peso")
            case _: 
                print("Opción incorrecta.\nElija otra por favor")
        limpiar_consola()
                

