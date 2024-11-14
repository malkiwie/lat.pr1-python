import os
import json
import zipfile
import psutil
import xml.etree.ElementTree as ET
import win32api


def main():
    while True:
        print("\nГлавное меню:")
        print("1. Работа с текстовыми файлами")
        print("2. Работа с JSON файлами")
        print("3. Работа с XML файлами")
        print("4. Работа с ZIP архивами")
        print("5. Информация о логических дисках")
        print("6. Выход")
        choice = input("Выберите действие: ")

        menu_actions = {
            "1": text_file_menu,
            "2": json_file_menu,
            "3": xml_file_menu,
            "4": zip_file_menu,
            "5": display_drive_info,
            "6": exit
        }

        action = menu_actions.get(choice)
        if action:
            action()
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


def text_file_menu():
    while True:
        print("\nМеню работы с текстовыми файлами:")
        print("1. Создать текстовый файл")
        print("2. Записать в текстовый файл")
        print("3. Прочитать текстовый файл")
        print("4. Удалить текстовый файл")
        print("5. Вернуться в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            create_file_with_extension_check(".txt")
        elif choice == "2":
            write_to_file(".txt")
        elif choice == "3":
            read_file(".txt")
        elif choice == "4":
            delete_file(".txt")
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def json_file_menu():
    while True:
        print("\nМеню работы с JSON файлами:")
        print("1. Создать JSON файл")
        print("2. Записать новый объект в JSON файл")
        print("3. Прочитать JSON файл")
        print("4. Удалить JSON файл")
        print("5. Вернуться в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            create_file_with_extension_check(".json")
        elif choice == "2":
            write_object_to_json()
        elif choice == "3":
            read_file(".json")
        elif choice == "4":
            delete_file(".json")
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def xml_file_menu():
    while True:
        print("\nМеню работы с XML файлами:")
        print("1. Создать XML файл")
        print("2. Записать данные в XML файл")
        print("3. Прочитать XML файл")
        print("4. Удалить XML файл")
        print("5. Вернуться в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            create_file_with_extension_check(".xml")
        elif choice == "2":
            write_object_to_xml()
        elif choice == "3":
            read_file(".xml")
        elif choice == "4":
            delete_file(".xml")
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def zip_file_menu():
    while True:
        print("\nМеню работы с ZIP архивами:")
        print("1. Создать ZIP архив")
        print("2. Добавить файл в ZIP архив")
        print("3. Извлечь файлы из ZIP архива")
        print("4. Удалить ZIP архив")
        print("5. Вернуться в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            create_file_with_extension_check(".zip")
        elif choice == "2":
            add_to_zip_archive()
        elif choice == "3":
            extract_from_zip_archive()
        elif choice == "4":
            delete_file(".zip")
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def create_file_with_extension_check(extension):
    file_name = input(f"Введите имя файла с расширением {extension}: ")
    if not file_name.endswith(extension):
        print(f"Ошибка: файл должен иметь расширение {extension}.")
        return
    with open(file_name, 'w') as file:
        print(f"Файл {file_name} успешно создан.")


def write_to_file(extension):
    file_name = input(f"Введите имя файла с расширением {extension}: ")
    if not os.path.exists(file_name):
        print("Файл не найден.")
        return
    data = input("Введите текст для записи в файл: ")
    with open(file_name, 'w') as file:
        file.write(data)
        print("Данные успешно записаны.")


def read_file(extension):
    file_name = input(f"Введите имя файла с расширением {extension}: ")
    if not os.path.exists(file_name):
        print("Файл не найден.")
        return
    with open(file_name, 'r') as file:
        print(file.read())


def delete_file(extension):
    file_name = input(f"Введите имя файла с расширением {extension}: ")
    if os.path.exists(file_name):
        os.remove(file_name)
        print("Файл успешно удален.")
    else:
        print("Файл не найден.")


def write_object_to_json():
    file_name = input("Введите имя JSON файла: ")
    message = input("Введите сообщение: ")
    data = {"message": message}
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    print("Данные успешно записаны в JSON файл.")


def write_object_to_xml():
    file_name = input("Введите имя XML файла: ")
    message = input("Введите сообщение: ")
    root = ET.Element("MessageData")
    ET.SubElement(root, "Message").text = message
    tree = ET.ElementTree(root)
    tree.write(file_name, encoding='utf-8', xml_declaration=True)
    print("Данные успешно записаны в XML файл.")


def add_to_zip_archive():
    zip_name = input("Введите имя ZIP архива: ")
    file_name = input("Введите имя файла для добавления: ")
    with zipfile.ZipFile(zip_name, 'a') as zipf:
        zipf.write(file_name)
        print("Файл добавлен в архив.")


def extract_from_zip_archive():
    zip_name = input("Введите имя ZIP архива: ")
    extract_path = input("Введите путь для извлечения: ")
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_path)
        print("Файлы успешно извлечены.")


def display_drive_info():
    print("Информация о логических дисках:")
    partitions = psutil.disk_partitions()

    for partition in partitions:
        try:
            volume_label = win32api.GetVolumeInformation(partition.mountpoint)[0]
            print(f"\nИмя диска: {partition.device}")
            print(f"Метка тома: {volume_label if volume_label else 'Без метки'}")
            print(f"Тип файловой системы: {partition.fstype}")

            usage = psutil.disk_usage(partition.mountpoint)
            print(f"Свободное место: {convert_bytes(usage.free)}")
            print(f"Общий размер: {convert_bytes(usage.total)}")
            print(f"Использовано: {convert_bytes(usage.used)} ({usage.percent}%)")

        except PermissionError:
            print(f"Нет доступа к информации по диску: {partition.device}")


def convert_bytes(bytes):
    sizes = ["B", "KB", "MB", "GB", "TB"]
    len_bytes = bytes
    order = 0
    while len_bytes >= 1024 and order < len(sizes) - 1:
        order += 1
        len_bytes /= 1024
    return f"{len_bytes:.2f} {sizes[order]}"


if __name__ == "__main__":
    main()
