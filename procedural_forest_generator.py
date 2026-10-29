import maya.cmds as cmds
from PySide6 import QtWidgets, QtCore

#Creates an instance of the GUI for the procedural forest generator
class ForestGUI(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.tree_generator = Forest()
        self.setWindowTitle("Procedural Forest")
        self.create_layout()
        self.create_connections

    def create_layout(self):
        pass

    def create_connections(self):
        pass

    @QtCore.Slot()