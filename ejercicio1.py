print("Bienvenidos al sistema consultorio NBA")

Pacientes=[]

while True:
    paciente=[]
    CitaPrevia = input("¿Tiene cita previa? Si (s) o no (n)")
    if CitaPrevia.lower() == "s":
            print("Paciente pasa a la sala de espera")
    else:
          nombre = input("Ingrese el  nombre del paciente: ")
          

          telefono = input("Ingrese el telefono  del paciente: ")
         

          motivo = input("Ingrese el motivo de visita: ")
         
          fecha=input("Ingrese la fecha de la cita del paciente: ")
          print("")
          print("Datos: ")
          print("Paciente: ",nombre)
          print("Telefono: ",telefono)
          print("Motivo de visita: ",motivo)
          print("Fecha de la cita: ",fecha)
    nuevoregi=input("¿Desea registrar otro paciente? si (s) o no (n)")
    if nuevoregi.lower() == "n":
          print("Saliendo del sistema")
          
          break
