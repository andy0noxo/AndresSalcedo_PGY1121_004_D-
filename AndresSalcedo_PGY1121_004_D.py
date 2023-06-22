
import numpy as np

tipos=[]
patentes=[]
marcas=[]
precios=[]
multas_montos=[]
multas_fechas=[]
fechas_registros=[]
nombres_duenos=[]


def mostrar_menu():
    print("----MENÚ----")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Salir")


def grabar_vehiculo():
    tipo=input("Ingrese el tipo de vehiculo: ")
    patente=input("Ingrese la patente: ")
    marca=input("Ingrese la marca: ")
    precio=int(input("Ingrese el precio: "))
    multas_monto=int(input("Ingrese el monto de las multas: "))
    multas_fecha=input("Ingrese la fecha de las multas: ")
    fecha_registro=input("Ingrese la fecha de registro: ")
    nombre_dueno=input("Ingrese el nombre del dueño: ")

    if len(patente)!=6:
        print("La patente debe tener 6 caracteres.")
        return
    if len(marca)<2 or len(marca)>15:
        print("La marca debe tener entre 2 y 15 caracteres.")
        return
    if precio<=5000000:
        print("El precio debe ser mayor a $5.000.000.")
        return
    
    tipos.append(tipo)
    patentes.append(patente)
    marcas.append(marca)
    precios.append(precio)
    multas_montos.append(multas_monto)
    multas_fechas.append(multas_fecha)
    fechas_registros.append(fecha_registro)
    nombres_duenos.append(nombre_dueno)

    print("Vehículo grabado exitosamente.");


def buscar_vehiculo():
    patente=input("Ingrese la patente del vehiculo a buscar: ")
    for i in range(len(patentes)):
        if patentes[i]==patente:
            print("----Información del vehículo----")
            print("Tipo: ",tipos[i])
            print("Patente: ",patentes[i])
            print("Marca: ",marcas[i])
            print("Precio: ",precios[i])
            print("Monto de multas: ",multas_montos[i])
            print("Fecha de multas: ",multas_fechas[i])
            print("Fecha de registro: ",fechas_registros[i])
            print("Dueño: ",nombres_duenos[i])
            return
        else:
            print("No se encontró un vehículo con esa patente.")


def imprimir_certificados():
    patente=input("Ingrese la patente del vehiculo a buscar: ")
    for i in range(len(patentes)):
        if patentes[i]==patente:
            certificado_emision=np.random.uniform(1500,3500)
            certificado_anotaciones=np.random.uniform(1500,3500)
            certificado_multas=np.random.uniform(1500,3500)
            print("---- Certificados del vehículo ",patentes[i]," ----")
            print("Certificado de Emisión de Contaminantes: ",certificado_emision)
            print("Certificado de Anotaciones Vigentes: ",certificado_anotaciones)
            print("Certificado de Multas: ",certificado_multas)
            print("Dueño: ",nombres_duenos[i])
            print()
        else:
            print("No se encontró un vehículo con esa patente.")


def salir():
    print("Gracias por utilizar Auto Seguro.")
    print("Nombre: Andrés Salcedo Morales ")
    print("Versión del programa: 1.0")


def main():
    while True:
        mostrar_menu()
        opcion=input("Ingrese la opción deseada (1-4): ")
        if opcion=="1":
            grabar_vehiculo()
        elif opcion=="2":
            buscar_vehiculo()
        elif opcion=="3":
            imprimir_certificados()
        elif opcion=="4":
            salir()
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__=="__main__":
    main()