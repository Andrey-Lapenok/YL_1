import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QInputDialog
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL import Image, ImageDraw
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.w, self.h = 500, 500
        self.image = Image.new("RGBA", (self.w, self.h), (255, 255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)

        self.image.save('flag.png')
        self.label.setPixmap(QPixmap('flag.png'))

        self.bt.clicked.connect(self.create_circle)

    def create_circle(self):
        r = random.randint(0, min(self.w, self.h) // 2 + 1)
        color = "yellow"
        self.image = Image.new("RGBA", (self.w, self.h), (255, 255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.ellipse([(self.w // 2 - r, self.h // 2 - r), (self.w // 2 + r, self.h // 2 + r)],
                                fill=color)
        self.image.save('flag.png')
        self.label.setPixmap(QPixmap('flag.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())