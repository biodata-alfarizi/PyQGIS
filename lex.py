import os, os.path, sys

from qgis.core import *
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import psycopg2

from ui_explorerWindow import Ui_ExplorerWindow

import resources

#############################################################################

class MapExplorer(QMainWindow, Ui_ExplorerWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setupUi(self)

        self.connect(self.actionQuit, SIGNAL("triggered()"),
                     qApp.quit)
        self.connect(self.actionShowBasemapLayer, SIGNAL("triggered()"),
                     self.showBasemapLayer)
        self.connect(self.actionShowLandmarkLayer, SIGNAL("triggered()"),
                     self.showLandmarkLayer)
        self.connect(self.actionHD, SIGNAL("triggered()"),
                     self.hd)
        self.connect(self.actionHA, SIGNAL("triggered()"),
                     self.ha)
        self.connect(self.actionHTI, SIGNAL("triggered()"),
                     self.hti)
        self.connect(self.actionKSATBS, SIGNAL("triggered()"),
                     self.ksatbs)
        self.connect(self.actionKSARIAU, SIGNAL("triggered()"),
                     self.ksariau)
        self.connect(self.actionKPH, SIGNAL("triggered()"),
                     self.kph)
        self.connect(self.actionZoomIn, SIGNAL("triggered()"),
                     self.zoomIn)
        self.connect(self.actionZoomOut, SIGNAL("triggered()"),
                     self.zoomOut)
        self.connect(self.actionPan, SIGNAL("triggered()"),
                     self.setPanMode)
        self.connect(self.actionExplore, SIGNAL("triggered()"),
                     self.setExploreMode)

        self.mapCanvas = QgsMapCanvas()
        self.mapCanvas.useImageToRender(False)
        self.mapCanvas.setCanvasColor(Qt.white)
        self.mapCanvas.show()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.mapCanvas)
        self.centralWidget.setLayout(layout)

        self.panTool = PanTool(self.mapCanvas)
        self.panTool.setAction(self.actionPan)

        self.exploreTool = ExploreTool(self)
        self.exploreTool.setAction(self.actionExplore)

        self.actionShowBasemapLayer.setChecked(True)
        self.actionShowLandmarkLayer.setChecked(True)


    def loadMap(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(cur_dir, "data",
                                "HTI",
                                "siak32648.tif")
        self.basemap_layer = QgsRasterLayer(filename, "basemap")
        QgsMapLayerRegistry.instance().addMapLayer(self.basemap_layer)

        uri = QgsDataSourceURI()
        uri.setConnection("localhost", "5432", "db_hti", "hti", "admin")
        uri.setDataSource("public", "hti", "geom", "")
        self.landmark_layer = QgsVectorLayer(uri.uri(), "Hutan Taman Industri", "postgres")
        QgsMapLayerRegistry.instance().addMapLayer(self.landmark_layer)
#        filename = os.path.join(cur_dir, "data",
#                                "HTI",
#                                "HTI_UPDATE.shp")
#        self.landmark_layer = QgsVectorLayer(filename, "landmarks", "ogr")
#        QgsMapLayerRegistry.instance().addMapLayer(self.landmark_layer)

        p = QgsPalLayerSettings()
        p.readFromLayer(self.landmark_layer)
        p.enabled = True
        p.fieldName = "nama_prh" 
        p.placement = QgsPalLayerSettings.OverPoint
        p.displayAll = True
        p.setDataDefinedProperty(QgsPalLayerSettings.Size, True, True, "8", "")
        p.quadOffset = QgsPalLayerSettings.QuadrantBelow
        p.yOffset = 1
        p.labelOffsetInMapUnits = False
        p.writeToLayer(self.landmark_layer)
       
        labelingEngine = QgsPalLabeling()
        self.mapCanvas.mapRenderer().setLabelingEngine(labelingEngine)

        self.showVisibleMapLayers()
        self.mapCanvas.setExtent(QgsRectangle(29214.9287048759870231,-96245.6389672261138912, 388500.7670372644206509,152768.1265135572175495))


    def showVisibleMapLayers(self):
        layers = []
        if self.actionShowLandmarkLayer.isChecked():
            layers.append(QgsMapCanvasLayer(self.landmark_layer))
        if self.actionShowBasemapLayer.isChecked():
            layers.append(QgsMapCanvasLayer(self.basemap_layer))
        self.mapCanvas.setLayerSet(layers)


    def showBasemapLayer(self):
        self.showVisibleMapLayers()

    def showLandmarkLayer(self):
        self.showVisibleMapLayers()
	
    def hd(self):
        uri = QgsDataSourceURI()
        uri.setConnection("localhost", "5432", "db_hti", "hti", "admin")
        uri.setDataSource("public", "hutan_desa_updatet", "geom", "")
        self.landmark_layer = QgsVectorLayer(uri.uri(), "Hutan Desa Update", "postgres")
        QgsMapLayerRegistry.instance().addMapLayer(self.landmark_layer)

        p = QgsPalLayerSettings()
        p.readFromLayer(self.landmark_layer)
        p.enabled = True
        p.fieldName = "perusahaan"
        p.placement = QgsPalLayerSettings.OverPoint
        p.displayAll = True
        p.setDataDefinedProperty(QgsPalLayerSettings.Size, True, True, "8", "")
        p.quadOffset = QgsPalLayerSettings.QuadrantBelow
        p.yOffset = 1
        p.labelOffsetInMapUnits = False
        p.writeToLayer(self.landmark_layer)
       
        labelingEngine = QgsPalLabeling()
        self.mapCanvas.mapRenderer().setLabelingEngine(labelingEngine)

        self.showVisibleMapLayers()
        self.mapCanvas.setExtent(QgsRectangle(135101.405365394, 19032.0771649993, 315420.983334606, 114389.945435))

    def ha(self):
        uri = QgsDataSourceURI()
        uri.setConnection("localhost", "5432", "db_hti", "hti", "admin")
        uri.setDataSource("public", "re_update_ok", "geom", "")
        self.landmark_layer = QgsVectorLayer(uri.uri(), "Hutan Alam", "postgres")
        QgsMapLayerRegistry.instance().addMapLayer(self.landmark_layer)
        p = QgsPalLayerSettings()
        p.readFromLayer(self.landmark_layer)
        p.enabled = True
        p.fieldName = "PERUSAHAAN"
        p.placement = QgsPalLayerSettings.OverPoint
        p.displayAll = True
        p.setDataDefinedProperty(QgsPalLayerSettings.Size, True, True, "8", "")
        p.quadOffset = QgsPalLayerSettings.QuadrantBelow
        p.yOffset = 1
        p.labelOffsetInMapUnits = False
        p.writeToLayer(self.landmark_layer)
       
        labelingEngine = QgsPalLabeling()
        self.mapCanvas.mapRenderer().setLabelingEngine(labelingEngine)

        self.showVisibleMapLayers()
        self.mapCanvas.setExtent(QgsRectangle(135101.405365394, 19032.0771649993, 315420.983334606, 114389.945435))

    def hti(self):
        uri = QgsDataSourceURI()
        uri.setConnection("localhost", "5432", "db_hti", "hti", "admin")
        uri.setDataSource("public", "hti", "geom", "")
        self.landmark_layer = QgsVectorLayer(uri.uri(), "Hutan Taman Industri", "postgres")
        QgsMapLayerRegistry.instance().addMapLayer(self.landmark_layer)
        p = QgsPalLayerSettings()
        p.readFromLayer(self.landmark_layer)
        p.enabled = True
        p.fieldName = "nama_prh"
        p.placement = QgsPalLayerSettings.OverPoint
        p.displayAll = True
        p.setDataDefinedProperty(QgsPalLayerSettings.Size, True, True, "8", "")
        p.quadOffset = QgsPalLayerSettings.QuadrantBelow
        p.yOffset = 1
        p.labelOffsetInMapUnits = False
        p.writeToLayer(self.landmark_layer)
       
        labelingEngine = QgsPalLabeling()
        self.mapCanvas.mapRenderer().setLabelingEngine(labelingEngine)

        self.showVisibleMapLayers()
        self.mapCanvas.setExtent(QgsRectangle(135101.405365394, 19032.0771649993, 315420.983334606, 114389.945435))

    def ksatbs(self):
        uri = QgsDataSourceURI()
        uri.setConnection("localhost", "5432", "db_hti", "hti", "admin")
        uri.setDataSource("public", "ksa_tbs", "geom", "")
        self.landmark_layer = QgsVectorLayer(uri.uri(), "Kesatuan Hutan Alam - Tandan Buah Sawit", "postgres")
        QgsMapLayerRegistry.instance().addMapLayer(self.landmark_layer)

        p = QgsPalLayerSettings()
        p.readFromLayer(self.landmark_layer)
        p.enabled = True
        p.fieldName = "id"
        p.placement = QgsPalLayerSettings.OverPoint
        p.displayAll = True
        p.setDataDefinedProperty(QgsPalLayerSettings.Size, True, True, "8", "")
        p.quadOffset = QgsPalLayerSettings.QuadrantBelow
        p.yOffset = 1
        p.labelOffsetInMapUnits = False
        p.writeToLayer(self.landmark_layer)
       
        labelingEngine = QgsPalLabeling()
        self.mapCanvas.mapRenderer().setLabelingEngine(labelingEngine)

        self.showVisibleMapLayers()
        self.mapCanvas.setExtent(QgsRectangle(135101.405365394, 19032.0771649993, 315420.983334606, 114389.945435))

    def ksariau(self):
#        cur_dir = os.path.dirname(os.path.realpath(__file__))
#        
#        filename = os.path.join(cur_dir, "data",
#                                "HTI",
#                                "wil_tertentu_kph.shp")
#        self.landmark_layer = QgsVectorLayer(filename, "landmarks", "ogr")
#        QgsMapLayerRegistry.instance().addMapLayer(self.landmark_layer)
        uri = QgsDataSourceURI()
        uri.setConnection("localhost", "5432", "db_hti", "hti", "admin")
        uri.setDataSource("public", "wil_tertentu_kph", "geom", "")
        self.landmark_layer = QgsVectorLayer(uri.uri(), "Hutan Taman Industri", "postgres")
        QgsMapLayerRegistry.instance().addMapLayer(self.landmark_layer)

        p = QgsPalLayerSettings()
        p.readFromLayer(self.landmark_layer)
        p.enabled = True
        p.fieldName = "BLOK"
        p.placement = QgsPalLayerSettings.OverPoint
        p.displayAll = True
        p.setDataDefinedProperty(QgsPalLayerSettings.Size, True, True, "8", "")
        p.quadOffset = QgsPalLayerSettings.QuadrantBelow
        p.yOffset = 1
        p.labelOffsetInMapUnits = False
        p.writeToLayer(self.landmark_layer)
       
        labelingEngine = QgsPalLabeling()
        self.mapCanvas.mapRenderer().setLabelingEngine(labelingEngine)

        self.showVisibleMapLayers()
        self.mapCanvas.setExtent(QgsRectangle(135101.405365394, 19032.0771649993, 315420.983334606, 114389.945435))

    def kph(self):
        uri = QgsDataSourceURI()
        uri.setConnection("localhost", "5432", "db_hti", "hti", "admin")
        uri.setDataSource("public", "gabungan", "geom", "")
        self.landmark_layer = QgsVectorLayer(uri.uri(), "Areal KPH", "postgres")
        QgsMapLayerRegistry.instance().addMapLayer(self.landmark_layer)

        p = QgsPalLayerSettings()
        p.readFromLayer(self.landmark_layer)
        p.enabled = True
        p.fieldName = "nama_prh"
        p.placement = QgsPalLayerSettings.OverPoint
        p.displayAll = True
        p.setDataDefinedProperty(QgsPalLayerSettings.Size, True, True, "8", "")
        p.quadOffset = QgsPalLayerSettings.QuadrantBelow
        p.yOffset = 1
        p.labelOffsetInMapUnits = False
        p.writeToLayer(self.landmark_layer)
       
        labelingEngine = QgsPalLabeling()
        self.mapCanvas.mapRenderer().setLabelingEngine(labelingEngine)

        self.showVisibleMapLayers()
        self.mapCanvas.setExtent(QgsRectangle(135101.405365394, 19032.0771649993, 315420.983334606, 114389.945435))

    def zoomIn(self):
        self.mapCanvas.zoomIn()


    def zoomOut(self):
        self.mapCanvas.zoomOut()


    def setPanMode(self):
        self.actionPan.setChecked(True)
        self.actionExplore.setChecked(False)
        self.mapCanvas.setMapTool(self.panTool)


    def setExploreMode(self):
        self.actionPan.setChecked(False)
        self.actionExplore.setChecked(True)
        self.mapCanvas.setMapTool(self.exploreTool)

#############################################################################

class ExploreTool(QgsMapToolIdentify):
    def __init__(self, window):
        QgsMapToolIdentify.__init__(self, window.mapCanvas)
        self.window = window
    def canvasReleaseEvent(self, event):
        found_features = self.identify(event.x(), event.y(),
                                       self.TopDownStopAtFirst,
                                       self.VectorLayer)
        if len(found_features) > 0:
            layer = found_features[0].mLayer
            feature = found_features[0].mFeature
            geometry = feature.geometry()

            info = []

            info.append("Nama Perusahaan :")
            name = feature.attribute("nama_prh")
            if name != None: info.append(name)

            info.append("Group Perusahaan :")
            group = feature.attribute("hti_group")
            if group != None: info.append(group)

            info.append("Nomor SK :")
            sk = feature.attribute("sk_iuphhk")
            if sk != None: info.append(sk)

            info.append("___________________________________________________________________________________ ")
            info.append("Nama Group ")
            info.append("RAPP  : Jenis Kayu Hutan Alam Seperti : Meranti, Balam, Suntai, Punak, Ramin, Kempas, Bintangur, Jangkang, Kelat dan jenis rimba campuran lainnya. Kayu Hutan Tanaman seperti : Akasia, Karet, Kayu Putih dan Ekaliptus.")

            info.append("___________________________________________________________________________________ ")
            info.append("Nama Group ")
            info.append("Lokasi A  : Didominasi oleh jenis Meranti, Pelawan, Kelat, dan Bintangur.")
            info.append("Lokasi B  : Didominasi oleh Pohon Meranti.")
            info.append("Lokasi C  : Didominasi oleh Pohon Kempas, Suntai, Punak, Ramin, Kelat, Bintangur, Balam, Tampui.")
            info.append("Lokasi D  : Didominasi oleh Jenis Kelat, Meranti, Punak, Suntai, Jangkang, dan Bintangur.")
            info.append("Lokasi E  : Didominasi oleh oleh Jenis Kelat, dan Meranti.")
            info.append("Lokasi F  : Didominasi oleh Pohon Meranti, Kelat, Jenis Simpur, dan Kayu Tempurung.")
            info.append("Lokasi G  : Didominasi oleh Pohon Meranti, Sunak, dan Puntai.")
            info.append("Lokasi H  : Belum diketahui.")
            info.append("Lokasi I  : Belum diketahui.")
            info.append("Lokasi J  : Didominasi oleh jenis Bakau.")
            info.append("Lokasi K  : Didominasi oleh Sawit dan Kelapa.")

            info.append("___________________________________________________________________________________ ")
            info.append("Nama Group ")
            info.append("Hutan Desa  : Didominasi oleh tanaman Jahe dan Pinang.")
            info.append("___________________________________________________________________________________ ")
            info.append("Nama Group ")
            info.append("Hutan Alam  : Jenis Kayu Hutan Alam Seperti : Meranti, Balam, Suntai, Punak, Ramin, Kempas, Bintangur, Jangkang, Kelat dan jenis rimba campuran lainnya.")
            info.append("___________________________________________________________________________________ ")
            info.append("Nama Group ")
            info.append("KSA-TBS  : Kawasan Suaka Alam Tandan Buah Sawit.")
            QMessageBox.information(self.window,
                                    "Informasi Wilayah",
                                    "\n".join(info))

#############################################################################

class PanTool(QgsMapTool):
    def __init__(self, mapCanvas):
        QgsMapTool.__init__(self, mapCanvas)
        self.setCursor(Qt.OpenHandCursor)
        self.dragging = False

    def canvasMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragging = True
            self.canvas().panAction(event)

    def canvasReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.dragging:
            self.canvas().panActionEnd(event.pos())
            self.dragging = False

#############################################################################

def main():
    QgsApplication.setPrefixPath(os.environ['QGIS_PREFIX'], True)
    QgsApplication.initQgis()

    app = QApplication(sys.argv)

    window = MapExplorer()
    window.show()
    window.raise_()
    window.loadMap()
    window.setPanMode()

    app.exec_()
    app.deleteLater()
    QgsApplication.exitQgis()

#############################################################################

if __name__ == "__main__":
    main()

