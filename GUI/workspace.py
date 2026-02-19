from PyQt6.QtWidgets import QVBoxLayout, QLabel, QFrame

class Workspace(QFrame):
    def __init__(self):
        super().__init__()
        
        workspace_layout = QVBoxLayout(self)
        workspace_layout.addWidget(QLabel("Workspace"))