# coding: utf-8

from PyQt5.QtWidgets import QMainWindow

from .ui.Ui_MainWindow import Ui_MainWindow

from .NotesWidget import NotesWidget
from .LoginWidget import LoginWidget

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # для python3: super().__init__(*args, **kwargs)
        self.init_ui()
        self.init_signals()

    def init_ui(self):
        self.setupUi(self)
        self.notesWidget = NotesWidget(self)
        self.stackedWidget.addWidget(self.notesWidget)

        self.loginWidget = LoginWidget(self)
        self.stackedWidget.addWidget(self.loginWidget)
        self.stackedWidget.setCurrentWidget(self.loginWidget)
        self.menubar.hide()
        self.toolBar.hide()

    def init_signals(self):
        self.loginWidget.loginBtn.clicked.connect(self.__load_main_window)
        self.loginWidget.exitBtn.clicked.connect(self.window_close)

    def __load_main_window(self):
        login = self.loginWidget.editLogin.text()
        password = self.loginWidget.editPassword.text()
        if login == "admin" and password == "admin":
            self.stackedWidget.setCurrentWidget(self.notesWidget)
            self.menubar.show()
            self.toolBar.show()
        else:
            self.loginWidget.warning.show()

    def window_close(self):
        self.close()

    

    
