import sys, os
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QListWidget,
    QListWidgetItem,
    QPushButton,
)
from PyQt5.QtCore import Qt, QUrl
from PIL import Image


class ListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(400, 400)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    im = Image.open(url.toLocalFile())
                    filename = os.path.basename(url.toLocalFile())
                    filename_without_ext = os.path.splitext(filename)
                    im.save(
                        filename_without_ext[0] + ".jpg",
                        optimize=True,
                        quality=30,
                    )
                else: 
                    im = Image.open(url.toString())
                    filename = os.path.basename(url.toString())
                    filename_without_ext = os.path.splitext(filename)
                    im.save(
                        filename_without_ext[0] + "_compressed" + ".jpg",
                        optimize=True,
                        quality=30,
                    )


class AppResizer(QMainWindow):

    
    def __init__(self):
        super().__init__()
        self.resize(600, 400)

        self.lstView = ListWidget(self)

        self.btn = QPushButton("get value", self)
        self.btn.setGeometry(850, 400, 200, 50)


app = QApplication(sys.argv)

demo = AppResizer()
demo.show()

sys.exit(app.exec_())
