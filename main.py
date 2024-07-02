import os

# Функция для отображения всех записей
def display_contacts(contacts):
    if contacts:
        print("\nКонтакты:")
        for contact in contacts:
            print(contact)
    else:
        print("\nКонтактов нет.")

# Функция для загрузки данных из файла
def load_contacts(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                contacts.append(line.strip())
    return contacts

# Функция для сохранения данных в файл
def save_contacts(filename, contacts):
    with open(filename, 'w', encoding='utf-8') as file:
        for contact in contacts:
            file.write(contact + '\n')

# Функция для поиска записей по критерию
def search_contacts(contacts, query):
    results = []
    for contact in contacts:
        if query.lower() in contact.lower():
            results.append(contact)
    return results

# Функция для добавления нового контакта
def add_contact(contacts):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    contact = f"{surname} {name} {patronymic} {phone}"
    contacts.append(contact)

# Функция для изменения контакта
def edit_contact(contacts, query):
    results = search_contacts(contacts, query)
    if not results:
        print("Контакт не найден.")
        return
    print("Найденные контакты:")
    for i, result in enumerate(results):
        print(f"{i+1}. {result}")
    choice = int(input("Выберите номер контакта для редактирования: ")) - 1
    if 0 <= choice < len(results):
        contact = results[choice]
        index = contacts.index(contact)
        surname = input("Введите новую фамилию (или нажмите Enter, чтобы оставить без изменений): ")
        name = input("Введите новое имя (или нажмите Enter, чтобы оставить без изменений): ")
        patronymic = input("Введите новое отчество (или нажмите Enter, чтобы оставить без изменений): ")
        phone = input("Введите новый номер телефона (или нажмите Enter, чтобы оставить без изменений): ")
        new_contact = contact.split()
        if surname:
            new_contact[0] = surname
        if name:
            new_contact[1] = name
        if patronymic:
            new_contact[2] = patronymic
        if phone:
            new_contact[3] = phone
        contacts[index] = " ".join(new_contact)
    else:
        print("Неверный выбор.")

# Функция для удаления контакта
def delete_contact(contacts, query):
    results = search_contacts(contacts, query)
    if not results:
        print("Контакт не найден.")
        return
    print("Найденные контакты:")
    for i, result in enumerate(results):
        print(f"{i+1}. {result}")
    choice = int(input("Выберите номер контакта для удаления: ")) - 1
    if 0 <= choice < len(results):
        contact = results[choice]
        contacts.remove(contact)
        print("Контакт удален.")
    else:
        print("Неверный выбор.")

# Основная функция
def main():
    filename = 'contacts.txt'
    contacts = load_contacts(filename)

    while True:
        print("\nТелефонный справочник")
        print("1. Показать все контакты")
        print("2. Добавить новый контакт")
        print("3. Найти контакт")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            display_contacts(contacts)
            input("Нажмите Enter, чтобы продолжить...")
        elif choice == '2':
            add_contact(contacts)
            save_contacts(filename, contacts)
            print("Контакт добавлен.")
            input("Нажмите Enter, чтобы продолжить...")
        elif choice == '3':
            query = input("Введите фамилию или имя для поиска: ")
            results = search_contacts(contacts, query)
            if results:
                print("\nНайденные контакты:")
                for result in results:
                    print(result)
            else:
                print("Контакты не найдены.")
            input("Нажмите Enter, чтобы продолжить...")
        elif choice == '4':
            query = input("Введите фамилию или имя для поиска: ")
            edit_contact(contacts, query)
            save_contacts(filename, contacts)
            input("Нажмите Enter, чтобы продолжить...")
        elif choice == '5':
            query = input("Введите фамилию или имя для поиска: ")
            delete_contact(contacts, query)
            save_contacts(filename, contacts)
            input("Нажмите Enter, чтобы продолжить...")
        elif choice == '6':
            break
        else:
            print("Неверный выбор, попробуйте снова.")
            input("Нажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()