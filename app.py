from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel, QHBoxLayout, QSlider, QLineEdit, QVBoxLayout, QMessageBox, QSpinBox, QComboBox, QSizePolicy

from PyQt6.QtCore import Qt

class pantalla_inicial(QMainWindow):
    def __init__(self):
        super().__init__()
        # Usuarios predefinidos
        self.usuarios = {
            "juan123": "pass123",
            "maria456": "maria_pass",
            "admin": "admin1234",
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
        layout_princ.addLayout(layout_boton)

        container = QWidget()
        container.setLayout(layout_princ)
        self.setCentralWidget(container)

    # Comprueba si las credenciales ingresadas son correctas
    def comprobar_cred(self):
        if self.nombre_line.text() in self.usuarios and self.usuarios[self.nombre_line.text()] == self.contra_line.text():
            self.programa()
        else:
            QMessageBox.information(self, "Credenciales incorrectas", "La contraseña o el nombre de usuario son incorrectos. Vuelva a intentarlo")

    # Lanza la ventana principal si el login fue exitoso
    def programa(self):
        self.hide()  # Oculta la ventana de login
        self.ventana_principal = MainWindow()
        self.ventana_principal.show()


def Veterinaria():
    app=QApplication([])
    window=pantalla_inicial()
    #window.setWindowTitle()
    window.show()
    app.exec() 

if __name__=="__main__":
    Veterinaria()