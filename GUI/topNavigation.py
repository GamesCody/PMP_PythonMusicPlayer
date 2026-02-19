from PyQt6.QtWidgets import QHBoxLayout, QLabel, QFrame

class TopBar(QFrame):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(50)
        self.setStyleSheet("background-color: #E3D1E6;")

        menu_label = QLabel("Logo placeholder")
        menu_layout = QHBoxLayout(self)
        menu_layout.addWidget(menu_label)