import unittest
import os
import cfg
import sys
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui


'''DesktopPet'''
class DesktopPet(QWidget):
	def __init__(self, parent=None, **kwargs):
		super(DesktopPet, self).__init__(parent)
		# initialization
		self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
		self.setAutoFillBackground(False)
		self.setAttribute(Qt.WA_TranslucentBackground, True)
		self.repaint()
		# Import a pet
		self.pet_images, iconpath = self.LoadPetImages()
		# Set exit options
		quit_action = QAction('exit', self, triggered=self.quit)
		quit_action.setIcon(QIcon(iconpath))
		self.tray_icon_menu = QMenu(self)
		self.tray_icon_menu.addAction(quit_action)
		self.tray_icon = QSystemTrayIcon(self)
		self.tray_icon.setIcon(QIcon(iconpath))
		self.tray_icon.setContextMenu(self.tray_icon_menu)
		self.tray_icon.show()
		# Picture currently displayed
		self.image = QLabel(self)
		self.setImage(self.pet_images[0][0])
		# Whether to follow the mouse
		self.is_follow_mouse = False
		# Avoid the mouse jumping directly to the upper left corner when the pet is dragging
		self.mouse_drag_pos = self.pos()
		# display
		self.resize(128, 128)
		self.randomPosition()
		self.show()
		# Some variables needed for pet animation action execution
		self.is_running_action = False
		self.action_images = []
		self.action_pointer = 0
		self.action_max_len = 0
		# Do an action every once in a while
		self.timer = QTimer()
		self.timer.timeout.connect(self.randomAct)
		self.timer.start(500)
	'''Make a random move'''
	def randomAct(self):
		if not self.is_running_action:
			self.is_running_action = True
			self.action_images = random.choice(self.pet_images)
			self.action_max_len = len(self.action_images)
			self.action_pointer = 0
		self.runFrame()
	'''Complete every frame of the action'''
	def runFrame(self):
		if self.action_pointer == self.action_max_len:
			self.is_running_action = False
			self.action_pointer = 0
			self.action_max_len = 0
		self.setImage(self.action_images[self.action_pointer])
		self.action_pointer += 1
	'''Set the currently displayed picture'''
	def setImage(self, image):
		self.image.setPixmap(QPixmap.fromImage(image))
	'''Import all pictures of a desktop pet'''
	def LoadPetImages(self):
		a = input("Please enter the pet serial number(1 <= num <= 64):")
		pet_name = 'pet_'+a
		actions = cfg.PET_ACTIONS_MAP[pet_name]
		pet_images = []
		for action in actions:
			pet_images.append([self.loadImage(os.path.join(cfg.ROOT_DIR, pet_name, 'shime'+item+'.png')) for item in action])
		iconpath = os.path.join(cfg.ROOT_DIR, pet_name, 'shime1.png')
		file = open(r'D:/python_test/a.txt','w')        
		file.write(iconpath)
		return pet_images, iconpath
	'''When the left mouse button is pressed, the pet will be bound to the mouse position'''
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.is_follow_mouse = True
			self.mouse_drag_pos = event.globalPos() - self.pos()
			event.accept()
			self.setCursor(QCursor(Qt.OpenHandCursor))
	'''When the mouse moves, the pet also moves'''
	def mouseMoveEvent(self, event):
		if Qt.LeftButton and self.is_follow_mouse:
			self.move(event.globalPos() - self.mouse_drag_pos)
			event.accept()
	'''When the mouse is released, unbind'''
	def mouseReleaseEvent(self, event):
		self.is_follow_mouse = False
		self.setCursor(QCursor(Qt.ArrowCursor))
	'''Import image'''
	def loadImage(self, imagepath):
		image = QImage()
		image.load(imagepath)
		return image
	'''Randomly to a certain position on the screen'''
	def randomPosition(self):
		screen_geo = QDesktopWidget().screenGeometry()
		pet_geo = self.geometry()
		width = (screen_geo.width() - pet_geo.width()) * random.random()
		height = (screen_geo.height() - pet_geo.height()) * random.random()
		self.move(width, height)
	'''exit the program'''
	def quit(self):
		self.close()
		sys.exit()



'''run'''
if __name__ == '__main__':
	app = QApplication(sys.argv)
	pet = DesktopPet()
	sys.exit(app.exec_())
    
