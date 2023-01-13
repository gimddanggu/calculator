import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Calcuator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calcualtor')
        self.resize(256,256)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Calcuator()
    sys.exit(app.exec_())