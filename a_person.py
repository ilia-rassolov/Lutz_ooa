class Person:  # Комбинирование с классом верхнего уровня

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jons', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.name.split()[-1])
    sue.pay *= 1.1
    print('%.2f' % sue.pay)

print('-'*100)

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self. job = job
        self.pay = pay

    def lastName(self):  # Методы реализации поведения
        return self.name.split()[-1]  # self - подразумеваемый объект

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))   # Потребуется изменять только здесь

    def __repr__(self):   # Добавленный метод
       return '[Person: %s, %s]' %(self.name, self.pay)  # Строка для вывода

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName(), sue.lastName())  # Использовать новые методы вместо жесткого кодирования
    sue.giveRaise(.10)
    print(sue.pay)
    print(sue.__repr__())

print('*'*100)

class Manager(Person):   # Наследование атрибутов Person
    def giveRaise (self, percent, bonus=.10):              # Переопределение с целью настройки
        self.pay = int(self.pay * (1 + percent + bonus))  # Плохой способ: вырезание и вставка
                                                          # затраты на поддержание
class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus) # Хороший способ: расширение исходной версии

# экземпляр.метод (аргументы. . .) == класс .метод (экземпляр, аргументы. . .)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 'mgr', 50000) # Создать экземпляр

    tom.giveRaise(.10)  # Выполняется специальная версия
    print(tom.lastName())  # Выполняется унаследованный метод
    print(tom)   # Выполняется унаследованный__ repr__

if __name__ == '__main__':
    print('--All three—')
    for obj in (bob, sue, tom):  # Обработать объекты обобщенным образом
        obj.giveRaise(.10)  # Выполнить метод giveRaise этого объекта
        print(obj)   # Выполнить общий метод __герг__

print('='*100)

# Добавление настройки конструктора в подклассе
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def __init__(self, name, pay):     # Переопределить конструктор
        Person.__init__(self, name, 'mgr', pay) # Выполнить исходный c 'mgr'

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager ('Tom Jones', 50000)   # Название должности не требуется:
    tom.giveRaise(.10)      # Оно подразумевается устанавливается классом
    print(tom.lastName())
    print(tom)
    # print(dir(tom).__class__.__dict__)

print('/'*100)

print('Перехват встроенных атрибутов в Python З')


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager ('Tom Jones', 50000)   # Название должности не требуется:
    tom.giveRaise(.10)                              # Она устанавливается классом
    print(tom.lastName())
    print(tom)

print('Специальные атрибуты класса')

print(tom)
print(tom.__class__)
print(tom.__class__.__name__)
print(list(tom.__dict__.keys()))  # Атрибуты на самом деле являются ключами словаря Использовать list для получения списка

for key in tom.__dict__:
    print(key, '=>', tom.__dict__[key])   # Ручная индексация
print('.'*100)
for key in bob.__dict__:
    print(key, '=>', getattr(tom, key)) # объект.атрибут, но атрибут - переменная




