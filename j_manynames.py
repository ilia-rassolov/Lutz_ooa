X = 11          # Глобальное имя/атрибут модуля (X или manynames.X)
def f():
    print(X)    # Доступ к глобальному имени X (11)
def g():
    X = 22      # Локальная переменная в функции (X, скрывает X в модуле)
    print(X)


class C:
    X = 33      # Атрибут класса (С.Х)
    def __init__(self):
        self.X = 99
    def m(self):
        X = 44         # Локальная переменная в методе (X)
        self.X = 55    # Атрибут экземпляра (экземпляр.X)

print(X)
f()
g()
print(C.X)
ins = C()
print(ins.X)
ins.m()
print(ins.X)
print(C.X)


