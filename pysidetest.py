




import sys
from PySide2.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("DXML")
    label.show()
    sys.exit(app.exec_())