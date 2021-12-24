from PyQt5 import uic
from PyQt5.QtWidgets import QApplication





def obtener():
    entrada = form_calculadora.valor.text()
    entrada += '0'
    form_calculadora.valor.setText(entrada)

def sumar():
    val1 = int(form_calculadora.sbOperator1.text())
    val2 = int(form_calculadora.sbOperator2.text())
    form_calculadora.lbResult.setText((str)(val1 + val2))

Form, Window = uic.loadUiType('calculadora-basic.ui') 

app_calculadora = QApplication([])
window_calculadora = Window()
form_calculadora = Form()
form_calculadora.setupUi(window_calculadora)
window_calculadora.show()
#form_calculadora.pbSum.clicked.connect(sumar)
form_calculadora.uno.clicked.connect(obtener)
app_calculadora.exec()