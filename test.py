import sys
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
        self.__plus = QLabel("+")
        self.__equal = QLabel("=")
        self.__label = QLabel("")
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.__first_edit)
        input_layout.addWidget(self.__plus)
        input_layout.addWidget(self.__second_edit)
        input_layout.addWidget(self.__equal)
        input_layout.addWidget(self.__label)
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.__button, 0, Qt.AlignLeft)
        self.setLayout(main_layout)

        # try - exceprt - else?
        self.__button.clicked.connect(self.__handle_button_click)

    def __handle_button_click(self):
        try:
            first_var = int(self.__first_edit.text())
            second_var = int(self.__second_edit.text())
            res = self.__count(first_var, second_var)
            self.__label.setText(str(res))
        except:
            QMessageBox.warning(self, "Ошибка значения", "Проверьте корректность вводимых данных")
            
    def __count(self, var_1: int, var_2: int) -> int:
        return var_1 + var_2

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()