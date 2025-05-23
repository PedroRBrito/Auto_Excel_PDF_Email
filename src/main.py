from PySide2.QtWidgets import QApplication, QMainWindow
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()