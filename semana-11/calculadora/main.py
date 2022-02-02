from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

#numbers
def obtener():
    entrada = form_calculadora.valor.text()
    entrada += '0'
    form_calculadora.valor.setText(entrada)
    
def obtener2():
    entrada2 = form_calculadora.valor.text()
    entrada2 += '1'
    form_calculadora.valor.setText(entrada2)

def obtener3():
    entrada3 = form_calculadora.valor.text()
    entrada3 += '2'
    form_calculadora.valor.setText(entrada3)

def obtener4():
    entrada4 = form_calculadora.valor.text()
    entrada4 += '3'
    form_calculadora.valor.setText(entrada4)

def obtener5():
    entrada5 = form_calculadora.valor.text()
    entrada5 += '4'
    form_calculadora.valor.setText(entrada5)  

def obtener6():
    entrada6 = form_calculadora.valor.text()
    entrada6 += '5'
    form_calculadora.valor.setText(entrada6)

def obtener7():
    entrada7 = form_calculadora.valor.text()
    entrada7 += '6'
    form_calculadora.valor.setText(entrada7)   

def obtener8():
    entrada8 = form_calculadora.valor.text()
    entrada8 += '7'
    form_calculadora.valor.setText(entrada8)

def obtener9():
    entrada9 = form_calculadora.valor.text()
    entrada9 += '8'
    form_calculadora.valor.setText(entrada9)

def obtener10():
    entrada10 = form_calculadora.valor.text()
    entrada10 += '9'
    form_calculadora.valor.setText(entrada10)    

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
form_calculadora.nueve.clicked.connect(obtener10)
form_calculadora.ocho.clicked.connect(obtener9)
form_calculadora.siete.clicked.connect(obtener8)
form_calculadora.seis.clicked.connect(obtener7)
form_calculadora.cinco.clicked.connect(obtener6)
form_calculadora.cuatro.clicked.connect(obtener5)
form_calculadora.tres.clicked.connect(obtener4)
form_calculadora.dos.clicked.connect(obtener3)
form_calculadora.uno.clicked.connect(obtener2)
form_calculadora.cero.clicked.connect(obtener)
app_calculadora.exec()