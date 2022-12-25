import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QInputDialog
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL import Image, ImageDraw
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt = QtWidgets.QPushButton(self.centralwidget)
        self.bt.setGeometry(QtCore.QRect(160, 10, 200, 30))
        self.bt.setObjectName("bt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 500, 500))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt.setText(_translate("MainWindow", "Создать круг"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.w, self.h = 500, 500
        self.image = Image.new("RGBA", (self.w, self.h), (255, 255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)

        self.image.save('flag.png')
        self.label.setPixmap(QPixmap('flag.png'))

        self.bt.clicked.connect(self.create_circle)

    def create_circle(self):
        r = random.randint(0, min(self.w, self.h) // 2 + 1)
        color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
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