import os
from qgis.PyQt.QtCore import QSettings
from qgis.PyQt.QtWidgets import QAction, QDialog
from qgis.PyQt.QtGui import QIcon
from qgis.gui import QgsMapToolEmitPoint
from .ui.ui_dialog import Ui_Dialog


class ElevationProfileAndSlopePlugin:

    def __init__(self, iface):
        self.iface = iface
        self.map_canvas = self.iface.mapCanvas()
        self.map_tool = QgsMapToolEmitPoint(self.map_canvas)

    def initGui(self):
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        self.action = QAction(QIcon(icon_path), "Elevation Profile and Slope", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("Elevation Profile and Slope", self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("Elevation Profile and Slope", self.action)

    def run(self):
        self.dialog = Dialog()
        self.dialog.select_points_button.clicked.connect(self.select_points)
        self.dialog.clear_points_button.clicked.connect(self.clear_points)
        self.dialog.save_profile_button.clicked.connect(self.save_profile)
        self.dialog.show()

    def select_points(self):
        # Implement the functionality to select points on the map canvas
        pass

    def clear_points(self):
        # Implement the functionality to clear the selected points
        pass

    def save_profile(self):
        # Implement the functionality to save the elevation profile
        pass


class Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.select_points_button = self.select_points_button
        self.clear_points_button = self.clear_points_button
        self.save_profile_button = self.save_profile_button
