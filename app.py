from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel, QHBoxLayout, QSlider, QLineEdit, QVBoxLayout, QMessageBox, QSpinBox, QComboBox, QSizePolicy, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class pantalla_inicial(QMainWindow):
    def __init__(self):
        super().__init__()
        # Usuarios predefinidos
        self.usuarios = {
            "juan123": "pass123",
            "maria456": "maria_pass",
            "pedro89": "clave89",
            "usuario_test": "test123"
        }

        self.admin = {
            "admin": "admin1234",
        }

        self.doctor={
            "pedro89": "clave89",
            "usuario_test": "test123"
            }

        self.setWindowTitle("Login")

        # Widgets de login
        self.nombre = QLabel("Nombre de usuario")
        self.nombre_line = QLineEdit()
        self.contra = QLabel("Contraseña")
        self.contra_line = QLineEdit()
        self.contra_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.login = QPushButton("Login")
        self.comb_Log = QComboBox()
        self.comb_Log.addItems(["Administrador","Doctor","Recepcion"])

        layout_princ = QVBoxLayout()

        layout_nombre = QHBoxLayout()
        layout_nombre.addWidget(self.nombre)
        layout_nombre.addWidget(self.nombre_line)

        layout_contra = QHBoxLayout()
        layout_contra.addWidget(self.contra)
        layout_contra.addWidget(self.contra_line)

        layout_boton = QHBoxLayout()
        layout_boton.addWidget(self.login)
        self.login.clicked.connect(self.comprobar_cred)

        layout_princ.addLayout(layout_nombre)
        layout_princ.addLayout(layout_contra)
        layout_princ.addWidget(self.comb_Log)
        layout_princ.addLayout(layout_boton)
        self.actualizar_combo("Administrador")
        self.comb_Log.currentTextChanged.connect(self.actualizar_combo)

        container = QWidget()
        container.setLayout(layout_princ)
        self.setCentralWidget(container)

    # Comprueba si las credenciales ingresadas son correctas
    def comprobar_cred(self):
        if self.nombre_line.text() in self.usuarios and self.usuarios[self.nombre_line.text()] == self.contra_line.text()and self.profile==2:
            self.programa()
        elif self.nombre_line.text() in self.doctor and self.doctor[self.nombre_line.text()] == self.contra_line.text()and self.profile==3:
            self.programa()
        elif self.nombre_line.text() in self.admin and self.admin[self.nombre_line.text()] == self.contra_line.text()and self.profile==1:
            self.programa()
        else:
            QMessageBox.information(self, "Credenciales incorrectas", "La contraseña o el nombre de usuario son incorrectos. Vuelva a intentarlo")

            

    # Lanza la ventana principal si el login fue exitoso
    def programa(self):
        self.hide()  # Oculta la ventana de login
        self.ventana_principal = ventana_principal(self.comb_Log.currentText())
        self.ventana_principal.show()

    def actualizar_combo(self,text):
        
        if text=="Administrador":
            self.profile=1
        if text=="Recepcion":
            self.profile=2
        if text=="Doctor":
            self.profile=3

    
        



class ventana_principal(QMainWindow):
    def __init__(self,comb_Log):
        super().__init__()

        self.resize(1366,768)

        self.label=QLabel(str(comb_Log))
        if str(comb_Log)=="Administrador":
            self.administrador()
        if str(comb_Log)=="Doctor":
            self.doctor()
        if str(comb_Log)=="Recepcion":
            self.recepcion()


    def administrador(self):

        self.label=QLabel("Bienvenido Administrador",self)
        self.label.move(50,50)
        self.label.setFont(QFont("Arial", 20))
        self.label.adjustSize()
        self.add=QPushButton("Agregar usuario",self)
        self.add.move(200,100)

        self.add.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.add.setFixedWidth(100)
        
        #layout_admin=QGridLayout()

        ##layout_admin.addWidget(self.add,0,2)
        
        

    
        #container=QWidget()
        #container.setLayout(layout_admin)
        #self.setCentralWidget(container)

    def doctor(self):

        self.label=QLabel("doctor")
        
        layout_admin=QHBoxLayout()

        layout_admin.addWidget(self.label)

        container=QWidget()
        container.setLayout(layout_admin)
        self.setCentralWidget(container)
    
    def recepcion(self):

        self.label=QLabel("recepcion")
        
        layout_admin=QHBoxLayout()

        layout_admin.addWidget(self.label)

        container=QWidget()
        container.setLayout(layout_admin)
        self.setCentralWidget(container)
        
       

        
        

def Veterinaria():
    app=QApplication([])
    window=pantalla_inicial()
    #window.setWindowTitle()
    window.show()
    app.exec() 

if __name__=="__main__":
    Veterinaria()