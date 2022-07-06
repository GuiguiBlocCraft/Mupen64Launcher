#!/usr/bin/env python3
import sys
from os import listdir, system, path, environ
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

rom_path = "/data/Jeux/N64/"
mupen_program = "mupen64plus"

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setGeometry(100, 100, 600, 600)
		self.setWindowTitle("Launcher for Mupen64Plus")
		self.initUI()
		self.loadFiles()

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
		self.list.itemSelectionChanged.connect(self.listClicked)

		self.btnReload = QToolButton(self)
		self.btnReload.setText("Reload files")
		self.btnReload.move(20, 475)
		self.btnReload.clicked.connect(self.buttonReloadClicked)

	def loadFiles(self):
		self.nbRoms = 0

		files = listdir(rom_path)
		files.sort()

		self.list.clear()

		for file in files:
			if file.endswith(".z64") or file.endswith(".n64") or file.endswith(".v64"):
				self.list.addItem(file)
				self.nbRoms += 1

		self.text.setText(str(self.nbRoms) + " file(s) loaded")

	def buttonReloadClicked(self):
		self.loadFiles()
		self.info.setText("Files reloaded!")

	def executeMupen(self):
		name = self.list.selectedItems()[0].text()
		script = mupen_program + " \"" + rom_path + name + "\""

		self.close()

		print("Starting:", script)
		system(script)

		self.show()

	def listClicked(self):
		if len(self.list.selectedItems()) > 0:
			name = self.list.selectedItems()[0].text()

			self.info.setText("ROM selected: " + name)

def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	fileExist = False

	envPath = environ.get("PATH")

	# Check if Mupen exists
	if envPath != None:
		for p in envPath.split(":"):
			if path.exists(path.join(p, mupen_program)):
				fileExist = True
				break
	
	win.show()
	
	if fileExist == False:
		win.info.setText("WARNING: Mupen64Plus is not installed!")
	
	sys.exit(app.exec_())

window()