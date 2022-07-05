#!/usr/bin/env python3
import sys
from os import listdir, system
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

path = "/data/Jeux/N64/"

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setGeometry(100, 100, 600, 600)
		self.setWindowTitle("Launcher for Mupen64Plus")
		self.initUI()

	def initUI(self):
		self.text = QLabel(self)
		self.text.move(20, 20)
		self.text.setFixedWidth(400)

		self.info = QLabel(self)
		self.info.move(20, 445)
		self.info.setFixedWidth(600)
		self.info.setText("Ready!")

		self.list = QListWidget(self)
		self.list.move(20, 50)
		self.list.setFixedWidth(400)
		self.list.setFixedHeight(400)
		self.list.activated.connect(self.executeMupen)
		self.list.itemSelectionChanged.connect(self.selected)

		files = listdir(path)
		files.sort()

		for file in files:
			if file.endswith(".z64") or file.endswith(".n64") or file.endswith(".v64"):
				self.list.addItem(file)

		print(str(len(files)) + " file(s) loaded")

		self.text.setText(str(len(files)) + " fichier(s) chargé(s)")

	def executeMupen(self):
		name = self.list.selectedItems()[0].text()

		self.close()

		print("Starting: ", name)
		system("mupen64plus \"" + path + name + "\"")

		self.show()

	def selected(self):
		name = self.list.selectedItems()[0].text()

		self.info.setText("ROM selected: " + name)

def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())

window()