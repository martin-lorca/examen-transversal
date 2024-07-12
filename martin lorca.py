import csv,random

sueldos = []

trabajadores = [{'nombre': 'Juan Perez'}, {'nombre': 'Maria Garcia'},{'nombre': 'Carlos Lopez'},{'nombre': 'Ana Martinez'}, {'nombre': 'Pedro Rodriguez'},{'nombre': 'Laura Hernandez'},{'nombre': 'Miguel Sanchez'},{'nombre': 'Isabel Gomez'},{'nombre': 'Francisco Diaz'},{'nombre': 'Elena Fernandez'}]

def asignar_sueldo():
    for trabajador in trabajadores:
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    print(sueldos)

def clasificacion():
    print('Clasificación de sueldo')
    print('Sueldo bajo:')
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 300000:
            print(f"Nombre: {trabajador['nombre']}, Sueldo: ${sueldo}")
    print('Sueldo entre $300.000 y $2.500.000:')
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if 300000 <= sueldo <= 2500000:
            print(f"Nombre: {trabajador['nombre']}, Sueldo: ${sueldo}")
    print('Sueldo superior a $2.500.000:')
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo > 300000:
            print(f"Nombre: {trabajador['nombre']}, Sueldo: ${sueldo}")

def ver_estadisticas():
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    print(f'Sueldo máximo: {sueldo_max}')
    print(f'Sueldo mínimo: {sueldo_min}')
    print(f'Promedio de sueldo: {sueldo_promedio}')
    

def reporte_sueldo():
    with open('archivo_trabajador.csv', 'w', newline='') as archivo_trabajador:
        escritor = csv.writer(archivo_trabajador)
        encabezado = ['Nombre trabajador',  'Sueldo Base', 'Desc Salud', 'Desc AFP', 'Sueldo Bruto']
        escritor.writerow(encabezado)
        for trabajador, sueldo in zip(trabajadores, sueldos):
            desc_salud = (sueldo * 7) / 100
            desc_afp = (sueldo * 12) / 100
            sueldo_liquido = sueldo - desc_salud - desc_afp
            escritor.writerow([trabajador['nombre'], sueldo, int(desc_salud), int(desc_afp), int(sueldo_liquido)])
        print(f"Nombre:{trabajador['nombre']}, Sueldo: ${sueldo}, Salud: {desc_salud},AFP: {desc_afp}, Sueldo Total: {sueldo_liquido}")

def salir_programa():
    print('Finalizar programa')
    print('Finalizando programa...')
    print('Desarrollado por [martin lorca]')
    print('RUT [21.688.436-1]')

def menu():
    while True:
        print('1) Asignar sueldo')
        print('2) Clasificación de sueldo')
        print('3) Estadísticas')
        print('4) Reporte de sueldo')
        print('5) Salir')
        opc = int(input('Seleccione una opción: '))
        if opc == 1:
            asignar_sueldo()
        elif opc == 2:
            clasificacion()
        elif opc == 3:
            ver_estadisticas()
        elif opc == 4:
            reporte_sueldo()
        elif opc == 5:
            salir_programa()
            break
        else:
            print('Opción inválida')

if __name__ == "__main__":
    menu()
