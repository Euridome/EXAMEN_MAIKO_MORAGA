import random, os, csv
limpiar = lambda: os.system("cls")
trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
diccionario_trabajadores = {}
total = None
#Definiciones aritmeticas
def salud(sueldo):
    return sueldo * 0.07
def afp(sueldo):
    return sueldo * 0.12
def liquido(sueldo):
    return sueldo * 0.81
#Definiciones principales
def app():
    try:
        while True:
            limpiar()
            menu()
            op = input("Ingrese una opcion: ")
            if op.isdigit():
                op = int(op)
                if op == 1:
                    limpiar()
                    sueldos_aleatorios()
                    esperar()
                elif op == 2:
                    limpiar()
                    clasificar_sueldos(diccionario_trabajadores)
                    impresion()
                    esperar()
                elif op == 3:
                    limpiar()
                    estadisticas()
                    esperar()
                elif op == 4:
                    limpiar()
                    reporte(diccionario_trabajadores)
                    excel()
                    esperar()
                elif op == 5:
                    print("Finalizando programa...\nDesarrollado por Maiko Moraga\nRUT 20.871.562-3")
                    break
                else:
                    print("Ingrese una opcion valida.")
                    esperar()
            else:
                print("Debe ingresar un valor numerico.")
                esperar()
    except ValueError:
        print("Ha ocurrido un error.")
def esperar():
    global tecla
    tecla = input("Presione Enter para continuar.")
def menu():
    print("1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Ver estadisticas\n4. Reporte de sueldos\n5. Salir")
def sueldos_aleatorios():
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        diccionario_trabajadores[trabajador] = {
            "sueldo_base": sueldo,
            "descuento_salud": int(salud(sueldo)),
            "descuento_afp": int(afp(sueldo)),
            "sueldo_liquido": int(liquido(sueldo))
        }
    print("Sueldos aleatorizados exitosamente.")
def clasificar_sueldos(diccionario_trabajadores):
    global total
    rango_sueldo = {
        "Menor a 800.000": [],
        "Entre 800.000 y 2.000.000": [],
        "Mayor que 2.000.000": []
    }
    total = 0
    for trabajador, datos in diccionario_trabajadores.items():
        sueldo = datos["sueldo_base"]
        total += sueldo
        if sueldo < 800000:
            rango_sueldo["Menor a 800.000"].append((trabajador, sueldo))
        elif 800000 <= sueldo < 2000000:
            rango_sueldo["Entre 800.000 y 2.000.000"].append((trabajador, sueldo))
        elif sueldo >= 2000000:
            rango_sueldo["Mayor que 2.000.000"].append((trabajador,sueldo))
    return rango_sueldo
def impresion():
    rangos = clasificar_sueldos(diccionario_trabajadores)
    for rango, lista in rangos.items():
        print(f"Sueldos {rango} TOTAL: {len(lista)}")
        print(f"{"Nombre Empleado":<20}  {"Sueldo":<10}")
        for persona, sueldo in lista:
            print(f"{persona:<20}  ${sueldo:,}".replace(",","."))
        print()
    print(f"TOTAL SUELDOS: ${total:,}".replace(',', '.'))
def estadisticas():
    if not diccionario_trabajadores:
        print("Primero ejecute la opcion de generar sueldos.")
        return None 
    mayor = max(diccionario_trabajadores, key=lambda k: diccionario_trabajadores[k]["sueldo_base"])
    menor = min(diccionario_trabajadores, key=lambda k: diccionario_trabajadores[k]["sueldo_base"])
    prom = int(total/10)
    print(f"El empleado con el sueldo más alto es: {mayor} y su sueldo es: ${diccionario_trabajadores[mayor]["sueldo_base"]:,}".replace(",","."))
    print(f"El empleado con el sueldo más bajo es: {menor} y su sueldo es: ${diccionario_trabajadores[menor]["sueldo_base"]:,}".replace(",","."))
    print(f"El promedio de los sueldos es: ${prom:,}".replace(",","."))
     
def reporte(diccionario_trabajadores):
    print(f"{"Nombre Empleado":<20} {"Sueldo Base":<15}  {"Descuento Salud":<18}  {"Descuento AFP":<18}  {"Sueldo Liquido":<15}")
    for persona, datos in diccionario_trabajadores.items():
        sueldobase = datos["sueldo_base"]
        dsalud = datos["descuento_salud"]
        dafp = datos["descuento_afp"]
        s_liquido = datos["sueldo_liquido"]
        print(f"{persona:<20} ${sueldobase:<15,} ${dsalud:<18,} ${dafp:<18,} ${s_liquido:<15,}".replace(",","."))
def excel():
    with open("archivo.csv","w", newline="") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(["Nombre Empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"])
        for persona, datos in diccionario_trabajadores.items():
            sueldobase = datos["sueldo_base"]
            dsalud = datos["descuento_salud"]
            dafp = datos["descuento_afp"]
            s_liquido = datos["sueldo_liquido"]
            escritor_csv.writerow([persona,sueldobase,dsalud,dafp,s_liquido])
app()