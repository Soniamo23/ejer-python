def leer_colaboradores(archivo):
    try:
        with open(archivo, 'r') as file:
            colaboradores = [line.strip() for line in file.readlines()]
        return colaboradores
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
        return []
def escribir_colaboradores(archivo, colaboradores):
    with open(archivo, 'w') as file:
        for colaborador in colaboradores:
            file.write(colaborador + '\n')
def mostrar_colaboradores(colaboradores, cantidad=5):
    for colaborador in colaboradores[:cantidad]:
        print(colaborador)

def agregar_colaborador(archivo, nuevo_colaborador):
    colaboradores = leer_colaboradores(archivo)
    if len(colaboradores) < 15:
        colaboradores.append(nuevo_colaborador)
        escribir_colaboradores(archivo, colaboradores)
        print(f"{nuevo_colaborador} ha sido agregado.")
    else:
        print("No se pueden agregar más colaboradores. El límite es de 15.")

def main():
    archivo = 'colaboradores.txt'
    
    colaboradores = leer_colaboradores(archivo)
    
    print("Mostrando los primeros 5 colaboradores:")
    mostrar_colaboradores(colaboradores)
    
    opcion = input("¿Desea agregar un nuevo colaborador? (s/n): ").strip().lower()
    if opcion == 's':
        nuevo_colaborador = input("Ingrese el nombre del nuevo colaborador: ").strip().upper()
        agregar_colaborador(archivo, nuevo_colaborador)
    
    opcion = input("¿Desea mostrar un número específico de colaboradores? (s/n): ").strip().lower()
    if opcion == 's':
        cantidad = int(input("Ingrese la cantidad de colaboradores a mostrar: "))
        mostrar_colaboradores(colaboradores, cantidad)

if __name__ == "__main__":
    main()
