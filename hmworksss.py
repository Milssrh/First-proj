import json
import os

class Person:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        return f"Имя: {self.name}"


class User(Person):
    def __init__(self, name):
        super().__init__(name)
        self.borrowed_books = []

    def borrow_book(self, book_title):
        self.borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)

    def display_info(self):
        return f"Пользователь: {self.name}, Взято книг: {len(self.borrowed_books)}"


class Librarian(Person):
    def display_info(self):
        return f"Библиотекарь: {self.name}"


class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__status = "доступна"

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        if new_status in ["доступна", "выдана"]:
            self.__status = new_status
        else:
            print("Неверный статус")

    def display_info(self):
        return f"Книга: '{self.__title}', Автор: {self.__author}, Статус: {self.__status}"


class LibrarySystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.librarians = []
        self.load_data()

    def load_data(self):
        if os.path.exists("books.txt"):
            with open("books.txt", "r", encoding="utf-8") as f:
                for line in f:
                    data = line.strip().split("|")
                    if len(data) == 3:
                        book = Book(data[0], data[1])
                        book.set_status(data[2])
                        self.books.append(book)

        if os.path.exists("users.txt"):
            with open("users.txt", "r", encoding="utf-8") as f:
                for line in f:
                    data = line.strip().split("|")
                    if len(data) >= 1:
                        user = User(data[0])
                        if len(data) > 1:
                            user.borrowed_books = data[1].split(",") if data[1] else []
                        self.users.append(user)

        if os.path.exists("librarians.txt"):
            with open("librarians.txt", "r", encoding="utf-8") as f:
                for line in f:
                    self.librarians.append(Librarian(line.strip()))

    def save_data(self):
        with open("books.txt", "w", encoding="utf-8") as f:
            for book in self.books:
                f.write(f"{book.get_title()}|{book.get_author()}|{book.get_status()}\n")

        with open("users.txt", "w", encoding="utf-8") as f:
            for user in self.users:
                borrowed = ",".join(user.borrowed_books)
                f.write(f"{user.name}|{borrowed}\n")

        with open("librarians.txt", "w", encoding="utf-8") as f:
            for lib in self.librarians:
                f.write(f"{lib.name}\n")

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Книга '{title}' добавлена.")

    def remove_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                self.books.remove(book)
                print(f"Книга '{title}' удалена.")
                return
        print("Книга не найдена.")

    def register_user(self, name):
        self.users.append(User(name))
        print(f"Пользователь '{name}' зарегистрирован.")

    def view_all_users(self):
        if not self.users:
            print("Нет зарегистрированных пользователей.")
        for user in self.users:
            print(user.display_info())

    def view_all_books(self):
        if not self.books:
            print("В библиотеке нет книг.")
        for book in self.books:
            print(book.display_info())

    def view_available_books(self):
        available = [book for book in self.books if book.get_status() == "доступна"]
        if not available:
            print("Нет доступных книг.")
        for book in available:
            print(book.display_info())

    def borrow_book(self, user_name, book_title):
        user = None
        for u in self.users:
            if u.name == user_name:
                user = u
                break
        if not user:
            print("Пользователь не найден.")
            return

        for book in self.books:
            if book.get_title() == book_title:
                if book.get_status() == "доступна":
                    book.set_status("выдана")
                    user.borrowed_books.append(book_title)
                    print(f"Книга '{book_title}' выдана пользователю {user_name}.")
                else:
                    print(f"Книга '{book_title}' уже выдана.")
                return
        print("Книга не найдена.")

    def return_book(self, user_name, book_title):
        user = None
        for u in self.users:
            if u.name == user_name:
                user = u
                break
        if not user:
            print("Пользователь не найден.")
            return

        if book_title in user.borrowed_books:
            user.borrowed_books.remove(book_title)
            for book in self.books:
                if book.get_title() == book_title:
                    book.set_status("доступна")
                    break
            print(f"Книга '{book_title}' возвращена.")
        else:
            print("У пользователя нет этой книги.")

    def view_borrowed_books(self, user_name):
        for user in self.users:
            if user.name == user_name:
                if user.borrowed_books:
                    print(f"Книги, взятые пользователем {user_name}:")
                    for title in user.borrowed_books:
                        print(f"  - {title}")
                else:
                    print("У пользователя нет взятых книг.")
                return
        print("Пользователь не найден.")


library = LibrarySystem()
print("Добро пожаловать в библиотечную систему!")

if not library.books:
    library.add_book("Война и мир", "Лев Толстой")
    library.add_book("Преступление и наказание", "Фёдор Достоевский")
if not library.users:
    library.register_user("Иван Иванов")
if not library.librarians:
    library.librarians.append(Librarian("Анна Петрова"))

while True:
    print("\n Выберите роль:")
    print("1. Библиотекарь")
    print("2. Пользователь")
    print("3. Выход")
    choice = input("Ваш выбор: ")

    if choice == "1":
        print("\n--- Режим библиотекаря ---")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Зарегистрировать пользователя")
        print("4. Просмотреть всех пользователей")
        print("5. Просмотреть все книги")
        action = input("Выберите действие: ")

        if action == "1":
            title = input("Название книги: ")
            author = input("Автор книги: ")
            library.add_book(title, author)
        elif action == "2":
            title = input("Название книги для удаления: ")
            library.remove_book(title)
        elif action == "3":
            name = input("Имя нового пользователя: ")
            library.register_user(name)
        elif action == "4":
            library.view_all_users()
        elif action == "5":
            library.view_all_books()

    elif choice == "2":
        print("\n--- Режим пользователя ---")
        name = input("Введите ваше имя: ")
        # Проверка регистрации
        user_exists = any(u.name == name for u in library.users)
        if not user_exists:
            print("Вы не зарегистрированы. Обратитесь к библиотекарю.")
            continue

        print("1. Просмотреть доступные книги")
        print("2. Взять книгу")
        print("3. Вернуть книгу")
        print("4. Просмотреть мои книги")
        action = input("Выберите действие: ")

        if action == "1":
            library.view_available_books()
        elif action == "2":
            title = input("Название книги для взятия: ")
            library.borrow_book(name, title)
        elif action == "3":
            title = input("Название книги для возврата: ")
            library.return_book(name, title)
        elif action == "4":
            library.view_borrowed_books(name)

    elif choice == "3":
        library.save_data()
        print("Данные сохранены. До свидания!")
        break
    else:
        print("Неверный выбор.")