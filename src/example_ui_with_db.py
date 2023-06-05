# -*- coding: utf-8 -*-

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QListWidget
import sqlite3

# З'єднання з базою даних SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Створення таблиці, якщо її ще не існує
cursor.execute("CREATE TABLE IF NOT EXISTS numbers (number INTEGER)")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Програма зі списком")

        # Основний контейнер
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Список
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        # Кнопка
        button = QPushButton("Додати число")
        button.clicked.connect(self.add_number)
        layout.addWidget(button)

        # Завантаження чисел з бази даних
        self.load_numbers()

    def load_numbers(self):
        # Очистити список перед завантаженням
        self.list_widget.clear()

        # Отримати числа з бази даних
        cursor.execute("SELECT * FROM numbers")
        rows = cursor.fetchall()

        # Додати числа до списку
        for row in rows:
            number = row[0]
            self.list_widget.addItem(str(number))

    def add_number(self):
        # Додати число до бази даних
        number = 42  # Замість 42 можна використовувати будь-яке інше число
        cursor.execute("INSERT INTO numbers (number) VALUES (?)", (number,))
        conn.commit()

        # Оновити список
        self.load_numbers()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
