import db
import hair
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QTableWidgetItem, 
    QStackedWidget
)
import datetime

import sys

class Hair(QtWidgets.QMainWindow, hair.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.olga_alina.clicked.connect(self.load_accidents)
        self.olga_alina_2.clicked.connect(self.load_accidents_2)
        self.olga_alina_3.clicked.connect(self.load_accidents_3)
        self.olga_alina_4.clicked.connect(self.load_accidents_4)

    def establish_connection(self):
        connection = sqlite3.connect(r"C:\Users\lovea\OneDrive\Документы\nastya\spa.db")
        cursor = connection.cursor()
        return connection, cursor

    
    def load_accidents(self):

        selected_item = self.olga_combo.currentText()
        print(f"Loading Accidents...{selected_item}")
        connection, cursor = self.establish_connection()
        now = datetime.date.today()
        cursor.execute("INSERT INTO zapisi (zapiz, name) VALUES (?, ?)",
                       (f'{now}:{selected_item}', 'Олег'))
        connection.commit()
        connection.close()

    def load_accidents_2(self):
        selected_item = self.olga_combo_2.currentText()
        print(f"Loading Accidents...{selected_item}")
        connection, cursor = self.establish_connection()
        now = datetime.date.today()
        cursor.execute("INSERT INTO zapisi (zapiz, name) VALUES (?, ?)",
                       (f'{now}:{selected_item}', 'Ольга'))
        connection.commit()
        connection.close()

    def load_accidents_3(self):
        selected_item = self.olga_combo_3.currentText()
        print(f"Loading Accidents...{selected_item}")
        connection, cursor = self.establish_connection()
        now = datetime.date.today()
        cursor.execute("INSERT INTO zapisi (zapiz, name) VALUES (?, ?)",
                       (f'{now}:{selected_item}', 'Дарья'))
        connection.commit()
        connection.close()

    def load_accidents_4(self):
        selected_item = self.olga_combo_4.currentText()
        print(f"Loading Accidents...{selected_item}")
        connection, cursor = self.establish_connection()
        now = datetime.date.today()
        cursor.execute("INSERT INTO zapisi (zapiz, name) VALUES (?, ?)",
                       (f'{now}:{selected_item}', 'Виктория'))
        connection.commit()
        connection.close()


class Db_load(QtWidgets.QMainWindow,db.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.load_accidents)

    def establish_connection(self):
        connection = sqlite3.connect(r"C:\Users\lovea\OneDrive\Документы\nastya\spa.db")
        cursor = connection.cursor()
        return connection, cursor

    def load_accidents(self):
        connection, cursor = self.establish_connection()
        cursor.execute('SELECT * FROM "zapisi"')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def display_table_data(self, column_names, rows):
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i + 1, j, item)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)



        self.example = Hair()
        self.load_db = Db_load()


        self.stacked_widget.addWidget(self.example)
        self.stacked_widget.addWidget(self.load_db)
   
        self.example.pushButton_4.clicked.connect(self.show_db_example)

        self.load_db.hair.clicked.connect(self.show_hair_from)


    def show_db_example(self):
        self.stacked_widget.setCurrentWidget(self.load_db)

    def show_hair_from(self):
        self.stacked_widget.setCurrentWidget(self.example)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())