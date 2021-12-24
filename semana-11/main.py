from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("mi-primer-gui.ui")

app_gui = QApplication([])
window_gui = Window()
form_gui = Form()
form_gui.setupUi(window_gui)
window_gui.show()
app_gui.exec()