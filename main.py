from datetime import datetime
import re

# Requirements
# age >= 15 and age <= 70
# imc = weight/height**2
class Person:
  def __init__(self, name, bday, isAthlete, gender, dateWeight, weight, height):
        self.name = name #name person
        self.bday = bday #birth day date
        self.isAthlete = isAthlete #bool physical condition
        self.gender = gender #gender (man or woman)
        self.dateWeight = dateWeight #date weigh
        self.weight = weight # weight in kg
        self.height = height #height in mt


  def showInfo(self):
    print("-------- Info --------")
    print("|")
    print("|  "+self.name)
    print("|  "+self.bday)
    print("|  "+self.isAthlete)
    print("|  "+self.gender)
    print("|  "+self.dateWeight)
    print("|  "+self.weight)
    print("|  "+self.height)
    print("|")
    print("----------------------")





def validarNombre(name):

  # Acepta solo letras, espacios y tildes
  regex = re.compile(r"^[a-zA-Z\u00C0-\u017F\s]+$", re.U)
  print(name, regex.match(name) is not None)


def validarIsAthlete(Athlete):
  # Acepta solo si y no
  regex = re.compile(r'^(?:si|no)$', re.U)
  print(Athlete, regex.match(Athlete) is not None)

def validarGender(gender):

  # Acepta solo M y F
  regex = re.compile(r'^(?:m|f)$', re.U)
  print(gender, regex.match(gender) is not None)

def validarNumero(num):
  # Acepta solo numeros
  # regex = re.compile(r'^(\d{1})([.]?[0-9]{0,3})$', re.U)

  # print(num, regex.match(num) is not None)
  pass

def calcularEdad(fecha):
  dateNow = datetime.now()
  objetoFecha = datetime.strptime(fecha, '%d/%m/%Y') # Trasforma la fecha ingresada en objeto dateTime
  edad = dateNow.year - objetoFecha.year - ((dateNow.month, dateNow.day) < (objetoFecha.month, objetoFecha.day)) # Tambien se puede relativedelta

  return True if(edad >= 15 and edad <= 70)else(False)

if __name__ == "__main__":

  print("------------- APP IMC -------------")
  name = input("|  Ingrese nombre: ")

  bday = input("|  Ingrese Fecha de nacimiento[24/12/1999]: ")
  edad = calcularEdad(bday) # entre 1950 a 2005

  while not edad:
    print("      -------- Error --------")
    print("      Debe tener entre 15 a 70 años")
    bday = input("|  Ingrese Fecha de nacimiento[24/12/1999]: ")
    edad = calcularEdad(bday)  # entre 1950 a 2005

  isAthlete = input("|  ¿Hace ejercicio?[Si/No]: ").strip().lower()

  gender = input("|  Genero [M/F]: ").strip().lower()

  weight = input("|  Peso[K]: ").strip().replace(",", ".")
  height = input("|  Altura[M]: ").strip().replace(",", ".")


  dateNow = datetime.now()

  PruebaUno = Person(name, bday, isAthlete, gender, str(dateNow.date()), weight, height)
  PruebaUno.showInfo()

  # PruebaDos = Person("Daniel", "24/12/1999", "N", "M", "22/08/2021", "50", "2")
  # PruebaDos.showInfo()
