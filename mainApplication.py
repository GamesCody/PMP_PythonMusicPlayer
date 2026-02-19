import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QFontDatabase

def load_fonts():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    font_path = os.path.join(current_dir, "assets", "fonts", "Lato", "Lato-Regular.ttf")
    if os.path.exists(font_path):
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("Błąd: Nie udało się załadować czcionki!")
        else:
            family_names = QFontDatabase.applicationFontFamilies(font_id)
            print(f"Loaded font: {family_names[0]}")
            return family_names[0]
    else:
        print("Font does not exist")
    return None


app = QApplication(sys.argv)

font_family = load_fonts()

from GUI import TopBar, Workspace, Sidebar

def load_stylesheet(app):

    current_dir = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(current_dir, "GUI", "style.qss")

    if os.path.exists(path):
        with open(path, "r") as f:
            app.setStyleSheet(f.read())
    else:
        print("No .qss file found!")
load_stylesheet(app)

window = QWidget()
window.setWindowTitle("PMP - Python Music Player")

window.resize(1280, 800) #default size
window.setMinimumSize(800, 500) #minimum size

#main container
main_layout = QVBoxLayout()
window.setLayout(main_layout)

main_layout.addWidget(TopBar())

content_layout = QHBoxLayout()
main_layout.addLayout(content_layout)

content_layout.addWidget(Sidebar())
content_layout.addWidget(Workspace())

window.show()

sys.exit(app.exec())

'''TO DO
Opcje - window.showMaximized() do odkomentowania w momencie kiedy user chce zmienić domyślne otwierania okna
Settings - option to customize position of buttons
'''