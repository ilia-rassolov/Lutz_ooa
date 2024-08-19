# Альтернативная версия Manager, основанная на внедрении
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

# class Manager(Person):  # Его меняем
#     def __init__(self, name, pay):     # Переопределить конструктор
#         Person.__init__(self, name, 'mgr', pay) # Выполнить исходный c ’mgr1
#
#     def giveRaise(self, percent, bonus=.10):
#         Person.giveRaise(self, percent + bonus)

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)  # Внедрить объект Person

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)   # Перехватить и делегировать

    def __getattr__(self, attr):
        return getattr(self.person, attr) # Делегировать все остальные атрибуты

    def __repr__(self):
        return str(self.person)    # Снова должен быть перегружен
#
if __name__== '__main__':
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