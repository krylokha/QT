import sys
import math
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Математика")
        self.setFixedSize(QSize(400, 100))
        self.__init_ui()

    def __init_ui(self):
        self.__first_edit = QLineEdit()
        self.__second_edit = QLineEdit()
        self.__button = QPushButton("Вычислить")
        self.__equal = QLabel("=")
        self.__label = QLabel("")
        self.__list = QComboBox()
        self.__list.activated.connect(self.__get_operand)
        self.__list.addItems(['+', '-', '/', 'x', 'MOD'])
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.__first_edit)
        input_layout.addWidget(self.__list)
        input_layout.addWidget(self.__second_edit)
        input_layout.addWidget(self.__equal)
        input_layout.addWidget(self.__label)
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.__button, 0, Qt.AlignLeft)
        self.setLayout(main_layout)

        self.__button.clicked.connect(self.__handle_button_click)

    def __handle_button_click(self):
        first_var = int(self.__first_edit.text())
        second_var = int(self.__second_edit.text())
        
        try:
            res = self.__count(first_var, second_var)
            self.__label.setText(str(res))
        except ValueError as e:
            QMessageBox.warning(self, "Ошибка значения", str(e))
    
    def __get_operand(self):
        ke = self.__list.currentText()
        return ke
            
    def __count(self, var_1: int, var_2: int) -> int:
        if self.__get_operand() == "+":
            if var_1 < 0 or var_2 < 0:
                raise ValueError("Для данного операнда вводимое число должно быть положительным")
            return var_1 + var_2
        elif self.__get_operand() == "-":
            return var_1 - var_2
        elif self.__get_operand() == "/":
            if var_2 == 0:
                raise ValueError("Проверьте корректность вводимых данных")
            return round(var_1 / var_2)
        elif self.__get_operand() == "x":
            return var_1 * var_2
        elif self.__get_operand() == "MOD":
            if var_2 == 0:
                raise ValueError("Проверьте корректность вводимых данных")
            return var_1 % var_2
        
            

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()