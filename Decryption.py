import pyAesCrypt
import os


# ф-ция дешифрования файла
def decryption(file, password):
    # задаем размер буфера, с его помощью и будем шифровать/расшифровывать
    buffer_size = 512 * 1024

    # вызываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # чтобы видеть результат, выводим на печать зашифрованный файл
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' дешифрован]")

    # удаляем исходный файл методом remove
    os.remove(file)


# ф-ция сканирования директорий
def walking_by_dirs(dir, password):
    # перебираем все поддиректоории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        # если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)


password = input("Введите пароль для дешифрования: ")
walking_by_dirs("e:/1En", password)
