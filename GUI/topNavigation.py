from PyQt6.QtWidgets import QHBoxLayout, QLabel, QFrame, QPushButton
import os
import backend.functions as backend
from PyQt6.QtCore import Qt

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
class TopBar(QFrame):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(50)
        self.logo = QLabel()

        self.layout = QHBoxLayout(self)
        
        logo_path = ["..", "assets", "icons","logo_b.png"]

        self.logo_label = QLabel()
        self.logo_label.setPixmap(backend.scaleTrans(backend.safePath(CURRENT_DIR, logo_path)))
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn_export = QPushButton(" Export")
        self.btn_set = QPushButton(" Settings")
        self.btn_pref = QPushButton(" Preferences")
        
        
        buttonQueue = [self.logo_label, self.btn_export, self.btn_set, self.btn_pref]
        #loading buttons by array - going to be used also for switching their position in customization
        for item in buttonQueue:
            self.layout.addWidget(item)

        self.layout.addStretch()