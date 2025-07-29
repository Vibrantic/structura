import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget,
    QVBoxLayout, QGroupBox, QHBoxLayout, QPushButton
)

class RibbonDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ribbon Menu Example")
        self.setGeometry(100, 100, 800, 400)

        # Create a tab widget for the ribbon
        self.ribbon = QTabWidget()
        self.ribbon.setTabPosition(QTabWidget.North)

        # Add tabs
        self.ribbon.addTab(self.create_home_tab(), "Home")
        self.ribbon.addTab(self.create_insert_tab(), "Insert")
        self.ribbon.addTab(self.create_view_tab(), "View")

        # Set ribbon as top widget
        central = QWidget()
        layout = QVBoxLayout(central)
        layout.addWidget(self.ribbon)
        self.setCentralWidget(central)

    def create_home_tab(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)

        # Clipboard group
        clipboard_group = self.create_group("Clipboard", ["Copy", "Paste", "Cut"])

        # Font group
        font_group = self.create_group("Font", ["Bold", "Italic", "Underline"])

        layout.addWidget(clipboard_group)
        layout.addWidget(font_group)
        layout.addStretch()
        return widget

    def create_insert_tab(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(self.create_group("Illustrations", ["Picture", "Shapes"]))
        layout.addStretch()
        return widget

    def create_view_tab(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(self.create_group("Show", ["Ruler", "Gridlines"]))
        layout.addStretch()
        return widget

    def create_group(self, title, buttons):
        group = QGroupBox(title)
        layout = QVBoxLayout(group)
        for btn_text in buttons:
            layout.addWidget(QPushButton(btn_text))
        return group

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RibbonDemo()
    window.show()
    sys.exit(app.exec_())
