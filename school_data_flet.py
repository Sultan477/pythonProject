import flet as ft
from openpyxl import load_workbook

# Класс для хранения информации о студенте
class Student:
    def __init__(self, name, surname, class_name, address, school_info, student_phone, school_phone, requirements):
        self.name = name
        self.surname = surname
        self.class_name = class_name
        self.address = address
        self.school_info = school_info
        self.student_phone = student_phone
        self.school_phone = school_phone
        self.requirements = requirements

# Класс для управления базой данных учащихся
class SchoolData:
    def __init__(self):
        # Загрузка электронной таблицы Excel
        self.wb = load_workbook('students.xlsx')
        self.ws = self.wb['Sheet1']

    def add_student(self, student):
        # Добавление нового студента в электронную таблицу
        row_index = self.ws.max_row
        self.ws.cell(row=row_index + 1, column=1).value = student.name
        self.ws.cell(row=row_index + 1, column=2).value = student.surname
        self.ws.cell(row=row_index + 1, column=3).value = student.class_name
        self.ws.cell(row=row_index + 1, column=4).value = student.address
        self.ws.cell(row=row_index + 1, column=5).value = student.school_info
        self.ws.cell(row=row_index + 1, column=6).value = student.student_phone
        self.ws.cell(row=row_index + 1, column=7).value = student.school_phone
        self.ws.cell(row=row_index + 1, column=8).value = student.requirements

    def search_by_class(self, class_name):
        # Поиск студентов по классу
        results = []
        for row in range(2, self.ws.max_row + 1):
            if self.ws.cell(row=row, column=3).value == class_name:
                results.append(self.ws.cell(row=row, column=1).value)
        return results

    def search_by_name(self, name):
        # Поиск студентов по имени
        results = []
        for row in range(2, self.ws.max_row + 1):
            if self.ws.cell(row=row, column=1).value == name:
                results.append(self.ws.cell(row=row, column=1).value)
        return results

sd = SchoolData()

# Функция для отображения окна приложения
def show_app():
    app = ft.App(title='Управление базой данных учащихся', size=(500, 600))
    with app:
        # Кнопка для добавления учащихся
        btn_add = ft.Button(label='Добавить учащегося', on_click=lambda: add_student())
        # Кнопки для поиска учащихся
        btn_search_by_class = ft.Button(label='Поиск по классу', on_click=lambda: search_by_class())
        btn_search_by_name = ft.Button(label='Поиск по имени', on_click=lambda: search_by_name())
        # Отображение кнопок
        ft.Grid().add(btn_add, row=0, col=0)
        ft.Grid().add(btn_search_by_class, row=1, col=0)
        ft.Grid().add(btn_search_by_name, row=2, col=0)

# Функция для добавления учащегося
def add_student():
    # Диалоговое окно для ввода данных учащегося
    dialog = ft.Dialog(title='Добавление учащегося')
    with dialog:
        name = ft.InputText(label='Имя')
        surname = ft.InputText(label='Фамилия')
        class_name = ft.InputText(label='Класс')
        address = ft.InputText(label='Адрес')
        school_info = ft.InputText(label='Школьная информация')
        student_phone = ft.InputText(label='Студенческий телефон')
        school_phone = ft.InputText(label='Школьный телефон')
        requirements = ft.InputText(label='Требования')
        # Отображение полей ввода
        ft.Grid().add(name, row=0, col=0)
        ft.Grid().add(surname, row=1, col=0)
        ft.Grid().add(class_name, row=2, col=0)
        ft.Grid().add(address, row=3, col=0)
        ft.Grid().add(school_info, row=4, col=0)
        ft.Grid().add(student_phone, row=5, col=0)
        ft.Grid().add(school_phone, row=6, col=0)
        ft.Grid().add(requirements, row=7, col=0)

        # Проверка введенных данных и добавление учащегося
        if dialog.wait():
            data = {'name': name.value, 'surname': surname.value, 'class_name': class_name.value,
                    'address': address.value, 'school_info': school_info.value,
                    'student_phone': student_phone.value, 'school_phone': school_phone.value,
                    'requirements': requirements.value}
            sd = SchoolData()
            sd.add_student(Student(**data))

# Функция для поиска учащихся по классу
def search_by_class():
    # Диалоговое окно для ввода класса
    dialog = ft.Dialog(title='Поиск по классу')
    with dialog:
        class_name = ft.InputText(label='Класс')
        # Отображение поля ввода
        ft.Grid().add(class_name, row=0, col=0)
        # Проверка введенного класса и вывод результатов
        if dialog.wait():
            sd = SchoolData()
            results = sd.search_by_class(class_name.value)
            if len(results) > 0:
                ft.Alert(title='Результаты поиска', message=f'Студенты из класса "{class_name.value}":\n{", ".join(results)}').show()
            else:
                ft.Alert(title='Нет результатов', message='Не найдено студентов из класса "{}"'.format(class_name.value)).show()

# Функция для поиска учащихся по имени
def search_by_name():
    # Диалоговое окно для ввода имени
    dialog = ft.Dialog(title='Поиск по имени')
    with dialog:
        name = ft.InputText(label='Имя')
        # Отображение поля ввода
        ft.Grid().add(name, row=0, col=0)
        # Проверка введенного имени и вывод результатов
        if dialog.wait():
            sd = SchoolData()
            results = sd.search_by_name(name.value)
            if len(results) > 0:
                ft.Alert(title='Результаты поиска', message=f'Студенты с именем "{name.value}":\n{", ".join(results)}').show()
            else:
                ft.Alert(title='Нет результатов', message='Не найдено студентов с именем "{}"'.format(name.value)).show()

# Запуск приложения
show_app()