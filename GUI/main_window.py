from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


app = QApplication([])
app.setWindowIcon(QIcon("assets/icon.png"))

window = QWidget()
window.setWindowTitle("PMP - Python Music Player")
window.resize(400, 300)
#creating layout
layout = QVBoxLayout()

#logo label
logo = QLabel()
picture = QPixmap("assets/logo.png")
logo.setPixmap(picture)
logo.setAlignment(Qt.AlignCenter)
layout.addWidget(logo)

#buttons
openPlaylist = QPushButton("Open playlist")
lib = QPushButton("Library")
getMusic = QPushButton("Get music")

layout.addWidget(openPlaylist)
layout.addWidget(lib)
layout.addWidget(getMusic)

#window layout setup
window.setLayout(layout)
#connecting to stylesheet
with open("GUI/styles.qss", "r") as f:
    app.setStyleSheet(f.read())

window.show()
app.exec()

