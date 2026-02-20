from PyQt6.QtWidgets import QVBoxLayout, QLabel, QFrame
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
class Workspace(QFrame):
    def __init__(self):
        super().__init__()
        
        workspace_layout = QVBoxLayout(self)
        workspace_layout.addWidget(QLabel("Workspace"))