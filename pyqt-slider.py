import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette


class ColorMixer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Vytvoření posuvníků RGB
        self.sliders = [QSlider(Qt.Horizontal) for _ in range(3)]
        for slider in self.sliders:
            slider.setMaximum(255)
            slider.valueChanged.connect(self.updateColor)
            self.layout.addWidget(slider)

        # Vytvoření oblasti pro zobrazení barvy
        self.colorLabel = QLabel()
        self.colorLabel.setAutoFillBackground(True)
        self.layout.addWidget(self.colorLabel)

        self.setLayout(self.layout)
        self.setWindowTitle('RGB Color Mixer')
        self.updateColor()

    def updateColor(self):
        color = QColor(self.sliders[0].value(), self.sliders[1].value(), self.sliders[2].value())
        palette = self.colorLabel.palette()
        palette.setColor(QPalette.Window, color)
        self.colorLabel.setPalette(palette)


def main():
    app = QApplication(sys.argv)
    ex = ColorMixer()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

