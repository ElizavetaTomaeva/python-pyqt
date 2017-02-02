from PyQt5.QtWidgets import QWidget

# from .MainWindow import MainWindow
from PyQt5.uic import loadUi


class LoginWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        loadUi('gui/ui/login_widget.ui', self)
        self.warning.hide()