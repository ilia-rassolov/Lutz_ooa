from f_person_nested import Person, Manager


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager ('Tom Jones', 50000)   # Название должности не требуется:
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)

print('0'*100)

import shelve


db = shelve.open('h_persondb')  # Имя файла, в котором хранятся объекты
for obj in (bob, sue, tom):   # Использовать атрибут паше объекта в качестве ключа
    db[obj.name] = obj        # Сохранить объект в shelve по ключу
db.close ()                   # Закрыть после внесения изменений


db = shelve.open('h_persondb')   # Повторно открыть хранилище shelve
print(len(db))                   # Сохранены три 'записи'
print(list(db.keys()))

print(db['Bob Smith'])        # Извлечь объект bob по ключу
print(bob.lastName()  )        # Выполняет lastName из Person)
print(db)
for key in db:                  # Проходf извлечение, вывод
    print (key, '=>' , db[key])
print('0'*50)
for key in sorted(db):         # Проход по сортированным ключам
    print(key, '=>', db[key])











