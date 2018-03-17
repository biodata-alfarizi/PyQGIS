from PyQt4 import QtGui, QtCore 

import resources

class Ui_ExplorerWindow(object):
	def setupUi(self, window):
		window.setWindowTitle("Sistem Informasi Hutan Tanaman Industri - Dinas Kehutanan Provinsi Riau")

		self.centralWidget = QtGui.QWidget(window) 
		self.centralWidget.setMinimumSize(800, 400) 
		window.setCentralWidget(self.centralWidget)

		self.menubar = window.menuBar()
		self.fileMenu = self.menubar.addMenu("File") 
		self.modeMenu = self.menubar.addMenu("View")
		self.viewMenu = self.menubar.addMenu("Mode")  

		self.toolBar = QtGui.QToolBar(window)
		window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

		self.actionQuit = QtGui.QAction("Quit", window)
		self.actionQuit.setShortcut(QtGui.QKeySequence.Quit)

		self.actionShowBasemapLayer = QtGui.QAction("Basemap", window)
		self.actionShowBasemapLayer.setShortcut("Ctrl+B")
		self.actionShowBasemapLayer.setCheckable(True)

		self.actionShowLandmarkLayer = QtGui.QAction("Landmarks", window)
		self.actionShowLandmarkLayer.setShortcut("Ctrl+L")
		self.actionShowLandmarkLayer.setCheckable(True)

		icon = QtGui.QIcon(":/icons/mActionReupdate.png") 
		self.actionHD = QtGui.QAction(icon, "Hutan Desa", window) 
		
		icon = QtGui.QIcon(":/icons/mActionHutanAlam.png") 
		self.actionHA = QtGui.QAction(icon, "Hutan Alam", window) 
		
		icon = QtGui.QIcon(":/icons/mActionHTI.png") 
		self.actionHTI = QtGui.QAction(icon, "Hutan HTI", window) 
		
		icon = QtGui.QIcon(":/icons/mActionKSATBS.png") 
		self.actionKSATBS = QtGui.QAction(icon, "Hutan Kawasan Suaka Alam - Tandan Buah Sawit", window) 
		
		icon = QtGui.QIcon(":/icons/mActionTertentu.png") 
		self.actionKSARIAU = QtGui.QAction(icon, "Kawasan Hutan Tertentu RI-Korea", window) 
		
		icon = QtGui.QIcon(":/icons/mActionKPH.png") 
		self.actionKPH = QtGui.QAction(icon, "Areal - Kawasan Pengelolaan Hutan", window) 
		
		icon = QtGui.QIcon(":/icons/mActionZoomIn.png") 
		self.actionZoomIn = QtGui.QAction(icon, "Zoom In", window) 
		self.actionZoomIn.setShortcut(QtGui.QKeySequence.ZoomIn)
		
		icon = QtGui.QIcon(":/icons/mActionZoomOut.png")
		self.actionZoomOut = QtGui.QAction(icon, "Zoom Out", window)
		self.actionZoomOut.setShortcut(QtGui.QKeySequence.ZoomOut)

		icon = QtGui.QIcon(":/icons/mActionPan.png")

		self.actionPan = QtGui.QAction(icon, "Pan", window) 
		self.actionPan.setShortcut("Ctrl+1") 
		self.actionPan.setCheckable(True)

		icon = QtGui.QIcon(":/icons/mActionExplore.png")
		self.actionExplore = QtGui.QAction(icon, "Explore", window)
		self.actionExplore.setShortcut("Ctrl+2")
		self.actionExplore.setCheckable(True)

		self.fileMenu.addAction(self.actionQuit)

		self.viewMenu.addAction(self.actionShowBasemapLayer) 
		self.viewMenu.addAction(self.actionShowLandmarkLayer) 
		self.viewMenu.addSeparator() 
		self.viewMenu.addAction(self.actionZoomIn) 
		self.viewMenu.addAction(self.actionZoomOut)

		self.modeMenu.addAction(self.actionPan)
		self.modeMenu.addAction(self.actionExplore)

		self.toolBar.addAction(self.actionZoomIn) 
		self.toolBar.addAction(self.actionZoomOut) 
		self.toolBar.addAction(self.actionPan) 
		self.toolBar.addAction(self.actionExplore)
		self.toolBar.addAction(self.actionHD) 
		self.toolBar.addAction(self.actionHA) 
		self.toolBar.addAction(self.actionHTI) 
		self.toolBar.addAction(self.actionKSATBS) 
		self.toolBar.addAction(self.actionKSARIAU) 
		self.toolBar.addAction(self.actionKPH) 

		window.resize(window.sizeHint())
