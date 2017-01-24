# -*- coding: utf-8 -*-

import sys
from urllib.request import urlopen

from lxml import etree
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QDoubleSpinBox, QPushButton,
    QVBoxLayout
)

class Course(QObject):
    CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

    def get(self):
        with urlopen(self.CBR_URL) as r:
            tree = etree.parse(r)
            value = tree.xpath('*[@ID="R01235"]/Value')[0].text
            return float(value.replace(',', '.'))


class CurrencyConverter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.initSignals()
        self.initLayouts()

    def initLayouts(self):
        self.w = QWidget(self)

        self.mainLayout = QVBoxLayout(self.w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.nullBtn)

        self.setCentralWidget(self.w)

    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)

        self.convertBtn = QPushButton('Перевести', self)
        self.convertBtn.setShortcut('Enter')  # конвертация при нажатии на Enter

        self.nullBtn = QPushButton('Сброс')

    def initSignals(self):

        self.btnSetState(False)

        self.convertBtn.clicked.connect(self.onClick)
        self.convertBtn.clicked.connect(self.onClick2)

        self.srcAmount.valueChanged.connect(self.lineChange)
        self.resultAmount.valueChanged.connect(self.lineChange)
        self.nullBtn.clicked.connect(self.nullAll)

    def lineChange(self):  # Блокировка кнопки "Перевести"
        self.btnSetState(False)
        value1 = self.srcAmount.value()
        value2 = self.resultAmount.value()
        if value1 == 0 and value2 == 0:
            return self.btnSetState(False)
        elif value1 != 0 and value2 != 0:
            return self.btnSetState(False)
        else:
            return self.btnSetState(True)

    def btnSetState(self, state):
        return self.convertBtn.setEnabled(state)

    def nullAll(self):  # Обнулить значения
        self.srcAmount.setValue(0)
        self.resultAmount.setValue(0)

    def onClick(self):
        value = self.srcAmount.value()
        value2 = self.resultAmount.value()
        if value and value2 == 0:
            self.resultAmount.setValue(value / Course().get())

    def onClick2(self):  # Обратная конвертация
        value = self.resultAmount.value()
        value2 = self.srcAmount.value()
        if value and value2 == 0:
            self.srcAmount.setValue(value * Course().get())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    cc = CurrencyConverter()
    cc.show()

    sys.exit(app.exec_())