class Person:
  def __init__(self, name, bday, age, isAthlete, gender, dateWeight, height):
        self.name = name #name person
        self.bday = bday #birth day date
        self.age = age
        self.isAthlete = isAthlete #bool physical condition
        self.gender = gender #gender (man or woman)
        self.dateWeight = dateWeight #date weigh
        # self.weight = weight # weight in kg
        self.height = height #height in mt
        self.imc = 0
        self.interpretation = " "

  def getIMC(self):
    self.imc = (float(self.weight)/(float(self.height)**2))

  def getInterpretation(self):
    if (self.gender == "M"):
      if (self.imc < 20):
        self.interpretation = "BAJO PESO"
      elif (self.imc >= 20 and self.imc <= 24.9):
        self.interpretation = "NORMAL"
      elif  (self.imc >= 25 and self.imc <= 29.9):
        self.interpretation = "OBSESIDAD LEVE"

      elif  (self.imc >= 30 and self.imc <= 40):
        self.interpretation = "OBESIDAD SEVERA"
      elif  (self.imc > 40):
        self.interpretation = "OBESIDAD MUY SEVERA"

    else:
      if (self.imc < 20):
        self.interpretation = "BAJO PESO"
      elif (self.imc >= 20 and self.imc <= 23.9):
        self.interpretation = "NORMAL"
      elif (self.imc >= 24 and self.imc <= 28.9):
        self.interpretation = "OBSESIDAD LEVE"

      elif (self.imc >= 29 and self.imc <= 37):
        self.interpretation = "OBESIDAD SEVERA"
      elif (self.imc > 37):
        self.interpretation = "OBESIDAD MUY SEVERA"


  def __str__(self):
    print("\n\n")
    print("-------- Info --------")
    print("|")
    print("|  Nombre: "+self.name)
    print("|  edad: "+self.age)
    # print("|  Fecha Nacimiento: "+self.bday)
    print("|  ¿Hace ejercicio?: "+self.isAthlete)
    print("|  Genero: "+self.gender)
    # print("|  Peso: "+self.weight + " Kg")
    print("|  Altura: "+self.height + " M")
    # print("|  IMC: "+str(self.imc))
    # print("|  Interpretacion: "+self.interpretation)
    print("|")
    print("|  Fecha Registro: "+self.dateWeight)
    print("|")
    print("----------------------")
    print("\n")
