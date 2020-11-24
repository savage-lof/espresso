import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

    def select_data(self):
        # Получим результат запроса,
        # который ввели в текстовое поле
        query = self.textEdit.toPlainText()
        res = self.connection.cursor().execute(query).fetchall()
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
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
