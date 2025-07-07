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
    def __init__(self, comb_Log):
        super().__init__()
        self.resize(500, 700)

        self.label = QLabel(str(comb_Log))
        if str(comb_Log) == "Administrador":
            self.administrador()
        if str(comb_Log) == "Doctor":
            self.doctor()
        if str(comb_Log) == "Recepcion":
            self.recepcion()

    # def administrador(self): ...
    # def recepcion(self): ...



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
         self.setWindowTitle("Panel del Doctor")
         self.resize(1000, 700)  # ventana 

         ancho_campos = 300  # más largo para nombre y apellido
         alto_campos_grandes = 80  
         separacion = 20
         y = 20

         # Etiqueta de bienvenida
         self.label = QLabel("Bienvenido Doctor", self)
         self.label.setFont(QFont("Arial", 20))
         self.label.adjustSize()
         self.label.move(50, y)
         y += 50

         # Nombre y apellido de la mascota
         self.nombre_mascota = QLineEdit(self)
         self.nombre_mascota.setPlaceholderText("Nombre de la mascota")
         self.nombre_mascota.setFixedWidth(ancho_campos)
         self.nombre_mascota.move(50, y)

         self.apellido_mascota = QLineEdit(self)
         self.apellido_mascota.setPlaceholderText("Apellido de la mascota")
         self.apellido_mascota.setFixedWidth(ancho_campos)
         self.apellido_mascota.move(50 + ancho_campos + separacion, y)

         y += 50

         # especie (Perro/Gato)
         self.especie = QComboBox(self)
         self.especie.addItems(["Perro", "Gato"])
         self.especie.setFixedWidth(150)
         self.especie.move(50, y)
         self.especie.currentTextChanged.connect(self.actualizar_razas)

         # autocompletado
         self.raza_mascota = QComboBox(self)
         self.raza_mascota.setEditable(True) 
         self.raza_mascota.setFixedWidth(400)
         self.raza_mascota.move(220, y)

         y += 50

         # Nombre y apellido del dueño 
         self.nombre_dueno = QLineEdit(self)
         self.nombre_dueno.setPlaceholderText("Nombre del dueño")
         self.nombre_dueno.setFixedWidth(ancho_campos)
         self.nombre_dueno.move(50, y)

         self.apellido_dueno = QLineEdit(self)
         self.apellido_dueno.setPlaceholderText("Apellido del dueño")
         self.apellido_dueno.setFixedWidth(ancho_campos)
         self.apellido_dueno.move(50 + ancho_campos + separacion, y)

         y += 50

         # Fecha de la consulta 
         from datetime import datetime
         self.fecha_consulta = QLineEdit(self)
         self.fecha_consulta.setReadOnly(True)
         self.fecha_consulta.setPlaceholderText("Fecha de la consulta")
         self.fecha_consulta.setFixedWidth(300)
         self.fecha_consulta.move(50, y)
         self.fecha_consulta.setText(datetime.now().strftime("%d/%m/%Y %H:%M"))

         y += 50

         # Edad de la mascota
         self.edad_paciente = QSpinBox(self)
         self.edad_paciente.setRange(0, 120)
         self.edad_paciente.setPrefix("Edad: ")
         self.edad_paciente.setFixedWidth(150)
         self.edad_paciente.move(50, y)

         y += 60

         # Campo de razón de consulta 
         self.sintomas_paciente = QLineEdit(self)
         self.sintomas_paciente.setPlaceholderText("Razón de consulta / Síntomas")
         self.sintomas_paciente.setFixedWidth(700)
         self.sintomas_paciente.setFixedHeight(alto_campos_grandes)
         self.sintomas_paciente.move(50, y)
         y += alto_campos_grandes + 20

         # Campo de diagnóstico 
         self.diagnostico = QLineEdit(self)
         self.diagnostico.setPlaceholderText("Diagnóstico y receta médica")
         self.diagnostico.setFixedWidth(700)
         self.diagnostico.setFixedHeight(alto_campos_grandes)
         self.diagnostico.move(50, y)
         y += alto_campos_grandes + 30

         # Botón para simular guardar
         self.boton_guardar = QPushButton("Guardar información", self)
         self.boton_guardar.setFixedWidth(200)
         self.boton_guardar.move(50, y)
         self.boton_guardar.clicked.connect(self.simular_guardado)

         # Botón Ver pacientes (abajo a la derecha)
         self.ver_Paciente = QPushButton("Ver pacientes", self)
         self.ver_Paciente.setFixedWidth(200)
         self.ver_Paciente.move(750, 600)
         self.ver_Paciente.clicked.connect(self.mostrar_pacientes)

         # ComboBox de pacientes
         self.pacientes = QComboBox(self)
         self.pacientes.addItems(["Paciente 1", "Paciente 2", "Paciente 3"])
         self.pacientes.move(750, 560)
         self.pacientes.hide()

         # Listas de razas para especie
         self.razas_perro = [
            "Labrador Retriever", "Bulldog", "Beagle", "Poodle", "Pastor Alemán",
            "Golden Retriever", "Chihuahua", "Rottweiler", "Dálmata", "Boxer"
        ]
         self.razas_gato = [
            "Persa", "Siamés", "Maine Coon", "Bengala", "Ragdoll",
            "Esfinge", "Británico", "Abisinio", "Siberiano", "Exótico"
        ]
         self.actualizar_razas("Perro")  # carga inicial


    def actualizar_razas(self, especie):
        self.raza_mascota.clear()
        if especie == "Perro":
            self.raza_mascota.addItems(self.razas_perro)
        elif especie == "Gato":
            self.raza_mascota.addItems(self.razas_gato)
  

    def mostrar_pacientes(self):
        self.pacientes.show()
        self.ver_Paciente.hide()

    def simular_guardado(self):
        nombre = self.nombre_paciente.text()
        edad = self.edad_paciente.value()
        sintomas = self.sintomas_paciente.text()
        
        mensaje = f"Información capturada:\nNombre: {nombre}\nEdad: {edad}\nSíntomas: {sintomas}"
        QMessageBox.information(self, "Datos del paciente", mensaje)

    def administrador(self):
        self.label = QLabel("Bienvenido Administrador", self)
        self.label.move(50, 50)
        self.label.setFont(QFont("Arial", 20))
        self.label.adjustSize()
        self.add = QPushButton("Agregar usuario", self)
        self.add.move(200, 100)

        self.add.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.add.setFixedWidth(100)

    def recepcion(self):
        self.label = QLabel("Recepción", self)
        self.label.move(50, 50)
        self.label.setFont(QFont("Arial", 20))
        self.label.adjustSize()
        
       

        
        

def Veterinaria():
    app=QApplication([])
    window=pantalla_inicial()
    #window.setWindowTitle()
    window.show()
    app.exec() 

if __name__=="__main__":
    Veterinaria()