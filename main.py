import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.db")
        self.cur = self.con.cursor()
        self.result = self.cur.execute("""SELECT name, ground, description, price, volume FROM Espresso""").fetchall()
        self.select_data()

    def select_data(self):
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(self.result):
            self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
