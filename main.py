from datetime import datetime
from person import Person
import os
import validation

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))


def clear():
  input("Press Enter to continue...")
  os.system('cls')
  os.system('clear')

def ingresarDatos():
  print("------------- Ingreso de Usuario -------------")
  name = input("|  Ingrese nombre: ")
  nameValidar = validation.validarNombre(name)
  while not nameValidar:
    print("Error nombre invalido, solo se aceptan letras")
    name = input("|  Ingrese nombre: ")
    nameValidar = validation.validarNombre(name)
  isRegistered = list(filter(lambda person: person.name == name, storagePerson))
  if len(isRegistered) == 0:
    bday = input("|  Ingrese Fecha de nacimiento[24/12/1999]: ")
    edad = validation.calcularEdad(bday) # entre 1950 a 2005
    while (edad == "Error") or (not edad[0]):
      if not edad[0]:
        print("      -------- Error --------")
        print("      Debe tener entre 15 a 70 años")
        bday = input("|  Ingrese Fecha de nacimiento[24/12/1999]: ")
        edad = validation.calcularEdad(bday)  # entre 1950 a 2005
      else:
        print("Error Formato ingresado es invalido")
        bday = input("|  Ingrese Fecha de nacimiento[24/12/1999]: ")
        edad = validation.calcularEdad(bday)

    isAthlete = input("|  ¿Hace ejercicio?[Si/No]: ").strip().upper()
    isAthleteValidar = validation.validarIsAthlete(isAthlete)
    while not isAthleteValidar:
      print("\nError: Solo es valido [Si / No]\n")
      isAthlete = input("|  ¿Hace ejercicio?[Si/No]: ").strip().upper()
      isAthleteValidar = validation.validarIsAthlete(isAthlete)

    gender = input("|  Genero [M/F]: ").strip().upper()
    genderValidar = validation.validarGender(gender)
    while not genderValidar:
      print("Error: Solo es valido [M / F]")
      gender = input("|  Genero [M/F]: ").strip().upper()
      genderValidar = validation.validarGender(gender)
    if gender == "M":
      gender = "Masculino"
    else:
      gender = "Femenino"


    height = input("|  Altura[M]: ").strip().replace(",", ".")
    heightValidar = validation.validarheight(height)
    while (not heightValidar) or (height == 0):
      print(height)
      if height == 0:
        print("\nError: no se puede ingresar 0\n")
        height = input("|  Altura[M]: ").strip().replace(",", ".")
        heightValidar = validation.validarheight(height)
      else:
        print("Error: Solo es valido un digito o un digito y hasta 3 decimales")
        height = input("|  Altura[M]: ").strip().replace(",", ".")
        heightValidar = validation.validarheight(height)


    print("|")
    print("----------------------")
    dateNow = datetime.now().strftime("%d/%m/%Y")
    clear()
    prGreen("Usuario ingresado")
    clear()
    return Person(name, bday, str(edad[1]), isAthlete, gender, str(dateNow), height)
  else:
    prRed('|  El usuario ya ha sido registrado.')
    clear()

if __name__ == "__main__":
  storagePerson = []
  ciclo = True
  while ciclo:
    print("------------- APP IMC -------------")
    print("|")
    print("|  | 1 | Ingresar usuario")
    print("|  | 2 | Calcular IMC")
    print("|  | 3 | Salir")
    print("|")
    opcion = input("|  Ingrese la opcion: ")
    print("|")
    print("----------------------")
    print("\n")
    clear()
    if opcion == "1":
      nuevoIngreso = ingresarDatos()
      storagePerson.append(nuevoIngreso)
    elif opcion == "2":
      if len(storagePerson) == 0:
        prRed('|  No hay datos registrados\n')
        clear()
      else:  
        print("|  Lista de ingresos")
        for person in storagePerson:
          print("|  " + person.name)
        nameSearch = input("|  Ingrese nombre para calcular IMC: ")
        nameValidar = validation.validarNombre(nameSearch)
        if not nameValidar:
          print("\nError nombre invalido, solo se aceptan letras\n")
        else:
          isRegistered = list(filter(lambda person: person.name == nameSearch, storagePerson))
          if len(isRegistered) > 0:
            weight = input("|  Peso[Kg]: ").strip().replace(",", ".")
            weightValidar = validation.validarWeight(weight)
            while (not weightValidar) or (weight == 0):

              if weight == 0:
                print("\nError: no se puede ingresar 0\n")
                weight = input("|  Peso[Kg]: ").strip().replace(",", ".")
                weightValidar = validation.validarWeight(weight)
              else:
                print("Error: solo es valido hasta tres digitos o hasta tres digitos y dos decimales")
                weight = input("|  Peso[Kg]: ").strip().replace(",", ".")
                weightValidar = validation.validarWeight(weight)

    elif opcion == "3":
      ciclo = False
    else:
      prRed("  Opcion Invalida")
      clear()