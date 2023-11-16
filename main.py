import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_1 = QtWidgets.QPushButton(self)
        self.button_2 = QtWidgets.QPushButton(self)
        self.button_3 = QtWidgets.QPushButton(self)
        self.button_4 = QtWidgets.QPushButton(self)
        self.comboBox_1 = QtWidgets.QComboBox(self)
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.text1 = QtWidgets.QLabel(self)
        self.text2 = QtWidgets.QLabel(self)

        self.draw = False

        self.title = "PyQt5 Figure"
        self.x = 450
        self.y = 100
        self.width = 475
        self.height = 550

        self.window()

        self.combobox_1_in_window()
        self.button1()
        self.text_1()
        self.combobox_2_in_window()
        self.text_2()
        self.button2()
        self.button3()
        self.button4()
        self.cancel()

    def window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

    def text_1(self):
        self.text1.setText('Выберите тип фигуры: ')
        self.text1.move(75, 20)
        self.text1.adjustSize()

    def combobox_1_in_window(self):
        self.comboBox_1.setGeometry(50, 50, 165, 25)
        self.comboBox_1.setObjectName('ComboBox_1')
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setItemText(0, "Квадрат")
        self.comboBox_1.setItemText(1, "Круг")
        self.comboBox_1.setItemText(2, "Треугольник")
        self.comboBox_1.setItemText(3, "Прямоугольник")

    def button1(self):
        self.button_1.setText("Подтверждаю выбор")
        self.button_1.move(70, 90)
        self.button_1.adjustSize()
        self.button_1.clicked.connect(self.button_and_combobox_1_enabled)

    def button_and_combobox_1_enabled(self):
        self.button_1.setEnabled(False)
        self.comboBox_1.setEnabled(False)

    def combobox_2_in_window(self):
        self.comboBox_2.setGeometry(250, 50, 165, 25)
        self.comboBox_2.setObjectName('ComboBox_2')
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "Чёрный")
        self.comboBox_2.setItemText(1, "Пурпурный")
        self.comboBox_2.setItemText(2, "Красный")
        self.comboBox_2.setItemText(3, "Синий")

    def text_2(self):
        self.text2.setText('Выберите цвет фигуры: ')
        self.text2.move(270, 20)
        self.text2.adjustSize()

    def button2(self):
        self.button_2.setText("Подтверждаю выбор")
        self.button_2.move(270, 90)
        self.button_2.adjustSize()
        self.button_2.clicked.connect(self.button_and_combobox_2_enabled)

    def button_and_combobox_2_enabled(self):
        self.button_2.setEnabled(False)
        self.comboBox_2.setEnabled(False)

    def button3(self):
        self.button_3.setText('Нарисовать')
        self.button_3.move(180, 160)
        self.button_3.adjustSize()
        self.button_3.clicked.connect(self.button_and_combobox_1_enabled)
        self.button_3.clicked.connect(self.button_and_combobox_2_enabled)
        self.button_3.clicked.connect(self.button_3_clicked)
        self.button_3.clicked.connect(self.figure_draw)
        self.button_3.clicked.connect(self.button4)
        self.button_3.clicked.connect(self.button_4_clicked)

    def button_3_clicked(self):
        self.button_3.setEnabled(False)

    def figure_draw(self):
        self.draw = True
        self.update()

    def figure_erase(self):
        self.draw = False
        self.update()

    def paintEvent(self, event):
        figure_name = self.comboBox_1.currentText()
        color_name = self.comboBox_2.currentText()
        painter = QPainter(self)
        if self.draw:
            if color_name == "Чёрный":
                color = Qt.black
            elif color_name == "Пурпурный":
                color = Qt.magenta
            elif color_name == "Красный":
                color = Qt.red
            elif color_name == "Синий":
                color = Qt.blue
            if figure_name == "Квадрат":
                pen = QPen(color)
                pen.setWidth(3)
                pen.setStyle(Qt.SolidLine)
                painter.setPen(pen)

                painter.drawRect(120, 200, 200, 200)
            elif figure_name == "Круг":
                pen = QPen(color)
                pen.setWidth(3)
                pen.setStyle(Qt.SolidLine)
                painter.setPen(pen)

                painter.drawEllipse(120, 200, 200, 200)
            elif figure_name == "Треугольник":
                pen = QPen(color)
                pen.setWidth(3)
                pen.setStyle(Qt.SolidLine)
                painter.setPen(pen)

                painter.drawLine(300, 300, 220, 200)
                painter.drawLine(220, 200, 150, 300)
                painter.drawLine(150, 300, 300, 300)
            elif figure_name == "Прямоугольник":
                pen = QPen(color)
                pen.setWidth(3)
                pen.setStyle(Qt.SolidLine)
                painter.setPen(pen)

                painter.drawRect(70, 200, 300, 200)

    def button4(self):
        self.button_4.setText('Отмена')
        self.button_4.move(350, 500)
        self.button_4.clicked.connect(self.cancel)

    def cancel(self):
        self.button_1.setEnabled(True)
        self.button_2.setEnabled(True)
        self.button_3.setEnabled(True)
        self.button_4.setEnabled(False)
        self.comboBox_1.setEnabled(True)
        self.comboBox_2.setEnabled(True)

    def button_4_clicked(self):
        self.button_4.setEnabled(True)
        self.button_4.clicked.connect(self.figure_erase)


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
