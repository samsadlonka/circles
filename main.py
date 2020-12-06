import sys
from random import randrange

from PyQt5.Qt import QMainWindow, QApplication

from PyQt5.QtGui import QPainter, QColor

from Ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.flag = False
        self.d = randrange(1, 100)
        self.x = randrange(0, 300)
        self.y = randrange(0, 300)
        self.color = (randrange(0, 256), randrange(0, 256), randrange(0, 256))
        self.pushButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        self.d = randrange(1, 100)
        self.x = randrange(0, 300)
        self.y = randrange(0, 300)
        self.color = (randrange(0, 256), randrange(0, 256), randrange(0, 256))

        self.flag = True
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()

            qp.begin(self)

            qp.setBrush(QColor(*self.color))

            qp.drawEllipse(self.x, self.y, self.d, self.d)

            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
