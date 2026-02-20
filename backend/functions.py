import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

def safePath(current_dir, path):
    filePath = os.path.join(current_dir, *path)
    return filePath

def scaleTrans(path):
    pixmap = QPixmap(path)
    scaled_pixmap = pixmap.scaledToWidth(250, Qt.TransformationMode.SmoothTransformation)
    return scaled_pixmap