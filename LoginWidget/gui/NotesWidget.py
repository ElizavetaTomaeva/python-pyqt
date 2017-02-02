# coding: utf-8

from PyQt5.QtWidgets import QWidget
# как-будто файлы не скомпиллены - loadUi
from PyQt5.uic import loadUi

class NotesWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()
        
    def init_ui(self):
        loadUi('gui/ui/notes_widget.ui', self)

