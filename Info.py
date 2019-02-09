

variable1 = 1
variable2 = 'str'
varibale3 = list([1])
varibale4 = 'c'
variable5 = 6.5
variable6 = {}
varibale7 = []
varibal = ()

# Сохранить Имя, фамилию, год рождения и месяц рождения
name = "alex"
surname = "gr"
year = 2013
month = 12
print(name)

person = list()
person = []
person.append(2013)  #0
person.append("alex")#1
person.append("gr")  #2
person.append(12)    #3
print(person[0])


person = {} # map, словарь
person["month"] = "12"
person["name"] = "alex"
person["surname"] = "gr"
person["year"] = "2013"
print(person["name"])

class Person:
    def __init__(self, name, surname, year, month):
        self.surname = surname
        self.name = name
        self.year = year
        self.month = month
        if month > 12 or month < 1:
            raise Exception('Месяц неверный')

    def print_name_surname(self):
        print("name: " + self.name + " " +  "\nsurname: " + self.surname)

    def age(self):
        return 2019 - self.year

personAlex = Person("alex", "gr", 2013, 12)
personDmitry = Person("dmitry", "pe", 2016, 10)
personSlava = Person("slava", "sk", 2020, 12)
personAlex.print_name_surname()
personDmitry.print_name_surname()
personSlava.print_name_surname()


l =  [1 ,2 ,3, 4, 6, 5]
class ArrayWork:
    def __init__(self, array):
        self.array = array

    def min(self):
        return min(self.array)

    def max(self):
        return max(self.array)

    def mean(self):
        return sum(self.array) / len(self.array)

a = ArrayWork(l)
print(a.mean())
