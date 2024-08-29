class Super:
    def hello(self):
        self.data1 = 'spam'

class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'

X = Sub()
print(X.__dict__)   # Словарь пространства имен экземпляра
print(X.__class__.__name__)
print(Sub.__bases__)  # Суперкласс класса
print(Super.__bases__)  # Пустой кортеж ()

print('*'*49)

Y = Sub()
print(X.hello())
print(X.__dict__)
X.hola()
print(X.__dict__)
print(X.hello)
# print(dir(X))
print(list (Sub.__dict__.keys()))
print(list (Super.__dict__.keys()))
print(Y.__dict__)

