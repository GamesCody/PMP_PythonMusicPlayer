from PyQt6.QtWidgets import QVBoxLayout, QLabel, QFrame, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize


class Sidebar(QFrame):
    def __init__(self):
        super().__init__()
        
        self.setFixedWidth(250)

        self.layout = QVBoxLayout(self)
        
        self.btn_lib = QPushButton(" Library")
        self.btn_playlist = QPushButton(" Playlists")
        self.btn_rec = QPushButton(" Recent")
        self.btn_fav = QPushButton(" Favourite")
        self.btn_artist = QPushButton(" Artist")
        self.btn_album = QPushButton(" Album")

        buttonQueue = [self.btn_lib, self.btn_playlist, self.btn_rec, self.btn_fav, self.btn_artist, self.btn_album]
        #loading buttons by array - going to be used
        for item in buttonQueue:
            self.layout.addWidget(item)

        self.layout.addStretch()