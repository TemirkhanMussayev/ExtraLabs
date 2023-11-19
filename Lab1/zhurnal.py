
class UserManagement:
    def __init__(self):
        self.user_list = []

    def add_user(self, user_data):
        email = user_data.get('Username')
        if not self.is_email_unique(email):
            print("Пользователь с таким адресом электронной почты уже существует.")
            return
        self.user_list.append(user_data)
        print("Пользователь успешно добавлен.")

    def is_email_unique(self, email):
        return all(email != user.get('Username') for user in self.user_list)

    def edit_user(self, username):
        for user in self.user_list:
            if user.get('Username') == username:
                print(f"Текущая информация: {user}")
                user.update(self.get_user_data())
                print("Информация успешно обновлена.")
                return
        print("Пользователь не найден.")

    def delete_user(self, username):
        for user in self.user_list:
            if user.get('Username') == username:
                self.user_list.remove(user)
                print("Пользователь успешно удален.")
                return
        print("Пользователь не найден.")

    def view_users(self):
        print("Список пользователей:")
        for user in self.user_list:
            print(user)

    def get_user_data(self):
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        age = input("Введите возраст: ")
        address = input("Введите адрес: ")
        username = input("Введите адрес электронной почты (уникальный): ")
        password = input("Введите пароль (минимум 8 символов): ")
        while len(password) < 8:
            print("Пароль слишком короткий. Минимальная длина - 8 символов.")
            password = input("Введите пароль еще раз: ")

        return {'Name': name, 'Surname': surname, 'Age': age, 'Address': address, 'Username': username, 'Password': password}


if name == "__main__":
    user_management = UserManagement()

    while True:
        print("\n1. Добавить пользователя")
        print("2. Редактировать пользователя")
        print("3. Удалить пользователя")
        print("4. Просмотреть список пользователей")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            user_management.add_user(user_management.get_user_data())
        elif choice == "2":
            username = input("Введите адрес электронной почты пользователя для редактирования: ")
            user_management.edit_user(username)
        elif choice == "3":
            username = input("Введите адрес электронной почты пользователя для удаления: ")
            user_management.delete_user(username)
        elif choice == "4":
            user_management.view_users()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")
class UserManagement:
    def __init__(self):
        self.user_list = []

    def add_user(self, user_data):
        email = user_data.get('Username')
        if not self.is_email_unique(email):
            print("Пользователь с таким адресом электронной почты уже существует.")
            return
        self.user_list.append(user_data)
        print("Пользователь успешно добавлен.")

    def is_email_unique(self, email):
        return all(email != user.get('Username') for user in self.user_list)

    def edit_user(self, username):
        for user in self.user_list:
            if user.get('Username') == username:
                print(f"Текущая информация: {user}")
                user.update(self.get_user_data())
                print("Информация успешно обновлена.")
                return
        print("Пользователь не найден.")

    def delete_user(self, username):
        for user in self.user_list:
            if user.get('Username') == username:
                self.user_list.remove(user)
                print("Пользователь успешно удален.")
                return
        print("Пользователь не найден.")

    def view_users(self):
        print("Список пользователей:")
        for user in self.user_list:
            print(user)

    def get_user_data(self):
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        age = input("Введите возраст: ")
        address = input("Введите адрес: ")
        username = input("Введите адрес электронной почты (уникальный): ")
        password = input("Введите пароль (минимум 8 символов): ")
        while len(password) < 8:
            print("Пароль слишком короткий. Минимальная длина - 8 символов.")
            password = input("Введите пароль еще раз: ")

        return {'Name': name, 'Surname': surname, 'Age': age, 'Address': address, 'Username': username, 'Password': password}


if name == "__main__":
    user_management = UserManagement()

    while True:
        print("\n1. Добавить пользователя")
        print("2. Редактировать пользователя")
        print("3. Удалить пользователя")
        print("4. Просмотреть список пользователей")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            user_management.add_user(user_management.get_user_data())
        elif choice == "2":
            username = input("Введите адрес электронной почты пользователя для редактирования: ")
            user_management.edit_user(username)
        elif choice == "3":
            username = input("Введите адрес электронной почты пользователя для удаления: ")
            user_management.delete_user(username)
        elif choice == "4":
            user_management.view_users()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")