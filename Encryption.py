import pyAesCrypt
import os


# ф-ция шифрования файла
def encryption(file, password):
    # задаем размер буфера, с его помощью и будем шифровать/расшифровывать
    buffer_size = 512 * 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # чтобы видеть результат, выводим на печать зашифрованный файл
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    # удаляем исходный файл методом remove
    os.remove(file)


# ф-ция сканирования директорий
def walking_by_dirs(dir, password):
    # перебираем все поддиректоории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        # если находим файл, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)


password = input("Введите пароль для шифрования: ")
walking_by_dirs("e:/1En", password) #указать путь к папке шифрования
