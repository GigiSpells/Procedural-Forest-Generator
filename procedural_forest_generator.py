import maya.cmds as cmds
from PySide6 import QtWidgets, QtCore


# Creates an instance of the GUI for the procedural forest generator
# TODO:
# Define layout & connections
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
    def create(self):
        pass


# Creates an instance of a tree 
# TODO: 
# Add at least 2 tree types
# Define create functions
class Tree():

    def __init__(self):
        self.trunk_radius = 0
        self.trunk_height = 0
        self.canopy_height = 0
        self.canopy_radius = 0

    def create_trunk(self):
        pass

    def create_canopy(self):
        pass