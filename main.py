from datetime import datetime

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










# Requirements
# age >= 15 and age <= 70
# imc = weight/height**2

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

  isAthlete = input("|  ¿Hace ejercicio?[S/N]: ")
  gender = input("|  Genero [M/F]: ")
  weight = input("|  Peso[K]: ")
  height = input("|  Altura[M]: ")

  dateNow = datetime.now()

  PruebaUno = Person(name, bday, isAthlete, gender, str(dateNow.date()), weight, height)
  PruebaUno.showInfo()

  # PruebaDos = Person("Daniel", "24/12/1999", "N", "M", "22/08/2021", "50", "2")
  # PruebaDos.showInfo()
