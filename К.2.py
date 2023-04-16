# Об'єктивно-орієнтивне програмування

from abc import ABCMeta, abstractmethod


class Person:
    pass # Пустий блок
p = Person()
print(p)


class Person2:
    def sayHi(self):
        print('Привіт! Як справи?')

p2 = Person2()
p2.sayHi()
Person2().sayHi()


class Person3:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Привіт! Мене звати - ', self.name)

p3 = Person3('Artur')
p3.sayHi()



# objvar.py   (Змінні класа і об'єкта)
class Robot:
    def _init__(self, name):
        self.name = name
        print('Створення {0}'.format(self.name))
        Robot.population += 1
    
    def __del__(self):
        print('Знищення {0}'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{0} був останнім роботом'.format(self.name))
        else:
            print('Залишилось {0:d} роботів'.format(Robot.population))
    
    def sayHi(self):
        print('Вітаю вас, мої творці! Мене звати {0}'.format(self.name))

    def howMany(self):
        print('В нас є {0:d} роботів!'.format(Robot.population))

    howMany = staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C-3PO')
droid2.sayHi()
droid2.howMany()

del droid1
del droid2




#Унаслідування
class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Створений SchoolMember: {0}'.format(self.name))

    def tell(self):
        print('Ім\'я:"{0}" Вік:"{1}"'.format(self.name, self.age), end = ' ')

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Створений Teacher: {0}'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата {0:d}'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, points):
        SchoolMember.__init__(self, name, age)
        self.points = points
        print('Створений Student: {0}'.format(self.name))
 
    def tell(self):
        SchoolMember.tell(self)
        print('Оцінки: {0:d}'.format(self.points))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
print()

members = [t, s]
for member in members:
    member.tell()



# Метакласи
class SchoolMember2(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Створений SchoolMember: {0}'.format(self.name))

    @abstractmethod
    def tell(self):
        print('Ім\'я:"{0}" Вік:"{1}"'.format(self.name, self.age), end =' ')

class Teacher2(SchoolMember2):
    def __init__(self, name, age, salary):
        SchoolMember2.__init__(self, name, age)
        self.salary = salary
        print('Створений Teacher: {0}'.format(self.name))
    
    def tell(self):
        SchoolMember2.tell(self)
        print('Зарплата {0:d}'.format(self.salary))

class Student2(SchoolMember2):
    def __init__(self, name, age, points):
        SchoolMember2.__init__(self, name, age)
        self.points = points
        print('Створений Student: {0}'.format(self.name))
 
    def tell(self):
        SchoolMember2.tell(self)
        print('Оцінки: {0:d}'.format(self.points))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
print()

members = [t, s]
for member in members:
    member.tell()

# end.




# Поділ ООП в Python на теми : 
#   1)
