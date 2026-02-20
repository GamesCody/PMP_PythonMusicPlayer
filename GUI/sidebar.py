from PyQt6.QtWidgets import QVBoxLayout, QFrame, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
class Sidebar(QFrame):
    def __init__(self):
        super().__init__()
        
        self.setFixedWidth(250)

        self.layout = QVBoxLayout(self)
        
        self.btn_lib = QPushButton(" Library")
        self.btn_lib.setIcon(QIcon("assets/icons/library_black.png"))
        self.btn_lib.setIconSize(QSize(30, 30))

        self.btn_playlist = QPushButton(" Playlists")
        self.btn_playlist.setIcon(QIcon("assets/icons/playlist_black.png"))
        self.btn_playlist.setIconSize(QSize(30, 30))

        self.btn_rec = QPushButton(" Recent")
        self.btn_rec.setIcon(QIcon("assets/icons/recent_black.png"))
        self.btn_rec.setIconSize(QSize(30, 30))


        self.btn_fav = QPushButton(" Favourite")
        self.btn_fav.setIcon(QIcon("assets/icons/favourite_b.png"))
        self.btn_fav.setIconSize(QSize(30, 30))

        self.btn_artist = QPushButton(" Artist")
        self.btn_artist.setIcon(QIcon("assets/icons/author_b.png"))
        self.btn_artist.setIconSize(QSize(30, 30))

        self.btn_album = QPushButton(" Album")
        self.btn_album.setIcon(QIcon("assets/icons/album_b.png"))
        self.btn_album.setIconSize(QSize(30, 30))

        self.btn_addMusic = QPushButton(" Add music")
        self.btn_addMusic.setIcon(QIcon("assets/icons/addMusic_b.png"))
        self.btn_addMusic.setIconSize(QSize(30, 30))

        buttonQueue = [self.btn_lib, self.btn_playlist, self.btn_rec, self.btn_fav, self.btn_artist, self.btn_album, self.btn_addMusic]
        #loading buttons by array - going to be used also for switching their position in customization
        for item in buttonQueue:
            self.layout.addWidget(item)

        self.layout.addStretch()