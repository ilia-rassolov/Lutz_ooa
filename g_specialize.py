class Super:

    def method(self):
        print('in Super.method')

class Sub(Super):
    def method(self):                        # Переопределить метод
        print('starting Sub.method')       # Добавить здесь нужные действия
        Super.method (self)                 # Запустить стандартное действие
        print('ending Sub.method')


x = Super()       # Создать экземпляр Super
print(x.method())

x = Sub()         # Создать экземпляр Sub
print(x.method())  # Выполняется Sub.method,

print('-'*99)


class Super:

    def method(self):               # Стандартное поведение
        print('in Super.method')

    def delegate(self):          # Ожидается определение метода
        self.action()


class Inheritor(Super):           # Буквальное наследование метода
    pass


class Replacer(Super):
    def method(self):                 # Полное замещение метода в Replacer .method
        print('in Replacer.method')


class Extender(Super):
    def method(self):
        print('starting Extender.method')       # начало Extender.method
        Super.method(self)                        # Расширение поведения метода
        print('ending Extender.method')          # конец Extender.method


class Provider(Super):            # Заполнение обязательного метода
    def action(self):
        print('in Provider.action')         # в Provider.method


if __name__ == '__main__':
    for klass in (Super, Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + ' ...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    print(x.method())
    x.delegate()
    print(x.method())

print(('+'*99))

from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta) :
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass

# X = Super()

# class Sub(Super): pass
# X = Sub()

class Sub(Super):
    def action(self): print('spam')

X = Sub()
X.delegate()