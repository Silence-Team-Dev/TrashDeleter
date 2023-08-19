import os
from glob import glob
import ctypes

#Меняем заголовок окна
ctypes.windll.kernel32.SetConsoleTitleW("TrashDeleter")

# Стартовые переменные
name_format: str = "rpyc"
rpycs: list = []
notDeleteds: list = []

# Приветствие программы и ожидание ввода
temp_name: str = input(
"""Добро Пожаловать в программу TrashDeleter

# Если нужно удалить только файлы формата .rpyc - просто нажмите enter

Введите имя формата:"""
    ).replace(
        " ", "",
        99999999999999999
        )

# Если не пусто то используем этот формат
if temp_name != "":
    name_format = temp_name

# Анализируем от корня до уровня 200 подпапок на файл нужного формата
for j in range(0, 200):
    rpycs += glob(f"{'**/'*j}**.{name_format}")

# Пытаемся их удалить
for i in rpycs:
    print("")
    print(f"Try delete {i}")

    try:
        os.remove(i)
        print(f"File {i} deleted succesful")

    except Exception as e:
        notDeleteds.append((i, e))
        print(f"File {i} not deleted")
        rpycs.remove(i)

print("")

# Убираем мусор
os.system('cls' if os.name == 'nt' else 'clear')

print("Deleted:")

# Выводим что удалили
for a in rpycs:
    print(f"- {a}")

# Если мы ничего не удалили
if len(rpycs) == 0:
    print("No")

print("")

print("Not deleted: ")

# Что не удались удалить
for d in notDeleteds:
    print(f"- {d[0]}")

# Если все прошло без ошибок выводим что все хорошо
if len(notDeleteds) == 0:
    print("No")

print("")

# Сколько файлов не удалось удалить
print(f"Errors: {len(notDeleteds)}")

# Выводим ошибки
for k in notDeleteds:
    print(k[1])

print("")

# Ждем реакции пользователя
input("Нажмите Enter чтобы выйти.")
