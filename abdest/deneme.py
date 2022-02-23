import sys
import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
class pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setGeometry(100, 100, 500, 500)

    def init_ui(self):
        self.player = QMediaPlayer()
        self.yazi = QtWidgets.QLabel("")
        self.buton = QtWidgets.QPushButton("Abdest almak için tıkla")
        self.pepe1 = QtWidgets.QLabel()
        self.pepe1.setPixmap(QtGui.QPixmap("pepe1.png"))

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi)
        v_box.addStretch()
        v_box.addWidget(self.pepe1)
        v_box.addStretch()
        v_box.addWidget(self.buton)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.buton.clicked.connect(self.click)

        self.show()
    def click(self):
        self.yazi.setText("                                   A B D S T L E N D İ N")
        self.pepe2 = QtWidgets.QLabel()
        self.pepe1.setPixmap(QtGui.QPixmap("pepe2.png"))
        ses = os.path.join(os.getcwd(), "choir.mp3")
        url = QUrl.fromLocalFile(ses)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()



app = QtWidgets.QApplication(sys.argv)
pencere = pencere()
sys.exit(app.exec_())

