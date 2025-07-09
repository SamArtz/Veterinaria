from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel, QHBoxLayout, QSlider, QLineEdit, QVBoxLayout, QMessageBox, QSpinBox, QComboBox, QSizePolicy, QGridLayout, QFormLayout, QDateEdit, QCheckBox
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel, QHBoxLayout, QSlider, QLineEdit, QVBoxLayout, QMessageBox, QSpinBox, QComboBox, QSizePolicy, QGridLayout,QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont
from sql import mysql_connect
import json
import os


class mini_ventana_elim_productos(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eliminar prod")
        self.setFixedSize(500, 300)

        self.buscador = QLineEdit(self)
        self.buscador.setPlaceholderText("Buscar producto...")
        self.buscador.move(20, 20)
        self.buscador.resize(200, 30)

        self.select = QLineEdit(self)
        self.select.setPlaceholderText("Escriba el ID del producto")
        self.select.move(225, 20)
        self.select.resize(150, 30)

        self.select_btn=QPushButton("Eliminar",self)
        self.select_btn.setFixedSize(100,30)
        self.select_btn.move(375,20)


        self.buscador.textChanged.connect(self.filtrar_tabla)
        self.tabla = QTableWidget(self)
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Descripcion","Precio","Stock"])
        self.tabla.setGeometry(20, 60, 500, 300)
        self.select_btn.clicked.connect(self.elim_prod)

    def elim_prod(self):
        conexion=mysql_connect()
        conexion.elim_prod(self.select.text())

    def filtrar_tabla(self):
        filtro = self.buscador.text().lower()
        conexion = mysql_connect()
        resultados = conexion.buscar_productos(filtro)

        self.tabla.setRowCount(len(resultados))
        for fila, datos in enumerate(resultados):
            for col, valor in enumerate(datos):
                self.tabla.setItem(fila, col, QTableWidgetItem(str(valor)))


class edit_prod(mini_ventana_elim_productos):
    def __init__(self):
        super().__init__()

        self.select_btn.hide()
        self.setFixedSize(700, 300)
        #self.select_btn.setText("Editar")
        self.mod_prod=QPushButton("Editar",self)
        self.mod_prod.setFixedSize(100,30)
        self.mod_prod.move(550,20)
        self.mod_prod.clicked.connect(self.editar_producto_clicked)
        self.select.hide()
        self.mod_select=QLineEdit(self)
        self.mod_select.setPlaceholderText("Escriba el ID del producto")
        self.mod_select.move(225, 20)
        self.mod_select.resize(150, 30)
        self.mod_select_cantidad=QLineEdit(self)
        self.mod_select_cantidad.setPlaceholderText("Escriba la cantidad del producto")
        self.mod_select_cantidad.move(380, 20)
        self.mod_select_cantidad.resize(150, 30)

    def editar_producto_clicked(self):
        conexion=mysql_connect()
        id=self.mod_select.text()
        cantidad=self.mod_select_cantidad.text()
        conexion.update_prod(cantidad,id)

class mini_ventana_productos(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Agregar producto")
        self.setFixedSize(500, 500)

        self.nombre_prod = QLabel("Nombre Producto: ", self)
        self.nombre_prod.move(50, 84)
        self.nombre_prod.setFont(QFont("Arial", 13))
        self.nombre_prod_line=QLineEdit(self)
        self.nombre_prod_line.setFixedSize(200,28)
        self.nombre_prod_line.move(200,80)

        self.descripcion_prod = QLabel("Descipcion: ", self)
        self.descripcion_prod.move(50, 154)
        self.descripcion_prod.setFont(QFont("Arial", 13))
        self.descripcion_prod_line=QLineEdit(self)
        self.descripcion_prod_line.setFixedSize(200,28)
        self.descripcion_prod_line.move(200,150)

        self.precio_prod = QLabel("Precio: ", self)
        self.precio_prod.move(50, 224)
        self.precio_prod.setFont(QFont("Arial", 13))
        self.precio_prod_line=QLineEdit(self)
        self.precio_prod_line.setFixedSize(200,28)
        self.precio_prod_line.move(200,220)

        self.stock = QLabel("Stock: ", self)
        self.stock.move(50, 294)
        self.stock.setFont(QFont("Arial", 13))
        self.stock_line=QLineEdit(self)
        self.stock_line.setFixedSize(200,28)
        self.stock_line.move(200,290)

        self.add_product=QPushButton("Agregar producto",self)
        self.add_product.setFont(QFont("Arial",13))
        self.add_product.move(100,350)
        self.add_product.setFixedSize(300,40)
        self.add_product.clicked.connect(self.agregar_prod_boton)
        

    def agregar_prod_boton(self):
        nombre=self.nombre_prod_line.text()
        descripcion=self.descripcion_prod_line.text()
        precio=self.precio_prod_line.text()
        stock=self.stock_line.text()
        line=f"{nombre},{descripcion},{precio},{stock}"
        conexion=mysql_connect()
        conexion.agregar_prod(nombre,descripcion,precio,stock)


        

class mini_ventana_usuarios(mini_ventana_productos):
    def __init__(self,rol):
        super().__init__()

        self.nombre_prod.setText("Nombre de usuario:")
        self.descripcion_prod.setText("Contraseña:")
        self.nombre_prod_line.hide()
        self.descripcion_prod_line.hide()
        self.user_line=QLineEdit(self)
        
        self.user_line.setFixedSize(200,28)
        self.user_line.move(200,80)
        self.pass_line=QLineEdit(self)
        self.pass_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_line.setFixedSize(200,28)
        self.pass_line.move(200,150)
        #self.descripcion_prod_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.add_product.hide()
        self.add_user=QPushButton(self)
        self.add_user.setText("Agregar usuario")
        self.add_user.setFont(QFont("Arial",13))
        self.add_user.move(100,350)
        self.add_user.setFixedSize(300,40)
        self.precio_prod.hide()
        self.precio_prod_line.hide()
        self.stock.hide()
        self.stock_line.hide()
        self.rol=QLabel(str(rol),self)
        self.rol.move(100,400)
        self.rolstr=str(self.rol.text())


        self.principal=pantalla_inicial()
        
        self.add_user.clicked.connect(self.agregar_def)

    def agregar_def(self):
        rol=self.rolstr
        usuario=self.user_line.text()
        clave=self.pass_line.text()
        self.principal.agregar_usuario(rol,usuario,clave)
        QMessageBox.information(self, "Usuario agregado correctamente.","El usuario ha sido agregado con exito!")
        



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

        self.RUTA_ARCHIVO = "credenciales.json"

        if not os.path.exists(self.RUTA_ARCHIVO):
            datos_iniciales = {
                "Administrador": {
                    "admin": "admin1234"
                },
                "Doctor": {
                    "pedro89": "clave89",
                    "usuario_test": "test123"
                },
                "Recepcion": {
                    "juan123": "pass123",
                    "maria456": "maria_pass",
                    "pedro89": "clave89",
                    "usuario_test": "test123"
                }
            }

            with open(self.RUTA_ARCHIVO, "w") as f:
                json.dump(datos_iniciales, f, indent=4)

        self.credenciales = self.cargar_credenciales()



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


    def cargar_credenciales(self):
            with open(self.RUTA_ARCHIVO, "r") as f:
                return json.load(f)
            
    def guardar_credenciales(self):
        with open(self.RUTA_ARCHIVO, "w") as f:
            json.dump(self.credenciales, f, indent=4)

        

    def agregar_usuario(self, rol, usuario, clave):
        self.credenciales[rol][usuario] = clave
        self.guardar_credenciales()

    # Comprueba si las credenciales ingresadas son correctas

    def cargar_credenciales(self):
        with open("credenciales.json", "r") as f:
            return json.load(f)
        
    def guardar_credenciales(self):
        with open("credenciales.json", "w") as f:
            json.dump(self.credenciales, f, indent=4)
    
    def comprobar_cred(self):
        usuario=self.nombre_line.text()
        clave=self.contra_line.text()
        rol=self.comb_Log.currentText()
        if rol == "Administrador" and usuario in self.credenciales["Administrador"] and self.credenciales["Administrador"][usuario] == clave:
            self.programa()
        elif rol == "Doctor" and usuario in self.credenciales["Doctor"] and self.credenciales["Doctor"][usuario] == clave:
            self.programa()
        elif rol == "Recepcion" and usuario in self.credenciales["Recepcion"] and self.credenciales["Recepcion"][usuario] == clave:
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
        self.setFixedSize(1300,800)

        #Usuarios
        self.usuarios_label=QLabel("Tipo de usuario: ",self) 
        self.usuarios_label.move(75,105)
        self.usuarios_label.setFont(QFont("Arial", 13))
        self.usuarios_label.adjustSize()
        self.usuario_combo=QComboBox(self)
        self.usuario_combo.addItems(['Administrador','Doctor','Recepcion'])
        self.usuario_combo.move(200,100)
        self.usuario_combo.setFixedSize(200,28)

        self.nombre=QLabel("Nombre: ",self)
        self.nombre.move(100,180)
        self.nombre.setFont(QFont("Arial", 13))
        self.nombre.adjustSize()
        
        self.usuario_line=QLineEdit(self)
        self.usuario_line.setFixedSize(400,28)
        self.usuario_line.move(200,175)
        #self.rm=QPushButton("Eliminar usuario",self)
        #self.rm.move(200,250)
        self.add=QPushButton("Agregar usuario",self)
        self.add.move(190,300)
        self.add.setFixedSize(975,30)

        self.apellido=QLabel("Apellido: ",self)
        self.apellido.move(100,240)
        self.apellido.setFont(QFont("Arial", 13))
        self.apellido.adjustSize()
        
        self.apellido_line=QLineEdit(self)
        self.apellido_line.setFixedSize(400,28)
        self.apellido_line.move(200,235)

        self.telefono=QLabel("Telefono: ",self)
        self.telefono.move(650,240)
        self.telefono.setFont(QFont("Arial", 13))
        self.telefono.adjustSize()
        
        self.telefono_line=QLineEdit(self)
        self.telefono_line.setFixedSize(400,28)
        self.telefono_line.move(750,235)

        self.direccion=QLabel("Direccion: ",self)
        self.direccion.move(650,180)
        self.direccion.setFont(QFont("Arial", 13))
        self.direccion.adjustSize()
        
        self.direccion_line=QLineEdit(self)
        self.direccion_line.setFixedSize(400,28)
        self.direccion_line.move(750,180)

        self.especialidad=QLabel("Especialidad: ",self)
        self.especialidad.move(650,288)
        self.especialidad.setFont(QFont("Arial", 12))
        self.especialidad.adjustSize()
        self.especialidad.hide()

        self.especialidad_line=QLineEdit(self)
        self.especialidad_line.setFixedSize(400,28)
        self.especialidad_line.move(750,285)
        self.especialidad_line.hide()
        

        #Productos
        self.view=QPushButton("Ver Productos",self)
        self.view.move(200,400)
        fuente=QFont()
        fuente.setPointSize(12)
        
        self.tabla = QTableWidget(self)
        self.tabla.setFont(fuente)
        self.tabla.setGeometry(400, 400, 600, 200)
        #self.tabla.resizeColumnsToContents()
        #self.tabla.setColumnWidth(2, 280)
        
        self.view.clicked.connect(self.ver_productos)
        self.view.click()
        #self.tabla.move(200,400)


        self.addp=QPushButton("Agregar producto",self)
        self.addp.move(200,475)
        self.rmp=QPushButton("Eliminar producto",self)
        self.rmp.move(200,550)

        self.edit_prod=QPushButton("Editar producto",self)
        self.edit_prod.move(1075,400)

        self.ventana_extra=None

        self.usuario_combo.currentTextChanged.connect(self.tipo_usuario_combo)
        self.addp.clicked.connect(self.agregar_productos)
        self.rmp.clicked.connect(self.eliminar_productos)
        self.edit_prod.clicked.connect(self.edit_productos)
        self.add.clicked.connect(self.agregar_usuariobtn)
        

        #self.add.clicked.connect()
        
        


        #self.add.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        #self.add.setFixedWidth(100)
        
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
    def tipo_usuario_combo(self,texto):
        if texto =="Doctor":
            self.add.move(190,340)
            self.especialidad.show()
            self.especialidad_line.show()
        elif texto =="Administrador":
            self.add.move(190,275)
            self.especialidad.hide()
            self.especialidad_line.hide()
        elif texto=="Recepcion":
            self.add.move(190,275)
            self.especialidad.hide()
            self.especialidad_line.hide()

    def ver_productos(self):
        
        conexion = mysql_connect()
        datos = conexion.obtener_productos()

        self.tabla.setRowCount(len(datos))
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Descripcion","Precio","Stock"])

        for fila, registro in enumerate(datos):
            for columna, valor in enumerate(registro):
                self.tabla.setItem(fila, columna, QTableWidgetItem(str(valor)))

    def agregar_productos(self):
        conexion=mysql_connect()
        self.ventana_extra = mini_ventana_productos()
        self.ventana_extra.show()

    def eliminar_productos(self):
        self.ventana_extra = mini_ventana_elim_productos()
        self.ventana_extra.show()

    def edit_productos(self):
        self.ventana_extra = edit_prod()
        self.ventana_extra.show()

    def agregar_usuariobtn(self):
        nombre=self.usuario_line.text()
        apellido=self.apellido_line.text()
        correo=self.direccion_line.text()
        telefono=self.telefono_line.text()
        especialidad=self.especialidad_line.text()

        conexion=mysql_connect()
        if self.usuario_combo.currentText()=="Doctor":
            conexion.agregar_user(nombre,apellido,correo,telefono,especialidad)
        elif self.usuario_combo.currentText()=="Recepcion":
            especialidad=""
            conexion.agregar_user(nombre,apellido,correo,telefono,especialidad)
        
        self.ventana_extra = mini_ventana_usuarios(self.usuario_combo.currentText())
        self.ventana_extra.show()

    def mostrar_pacientes(self):
        self.pacientes.show()


    def simular_guardado(self):
        nombre = self.nombre_paciente.text()
        edad = self.edad_paciente.value()
        sintomas = self.sintomas_paciente.text()
        
        mensaje = f"Información capturada:\nNombre: {nombre}\nEdad: {edad}\nSíntomas: {sintomas}"
        QMessageBox.information(self, "Datos del paciente", mensaje)


    def recepcion(self):

        self.label=QLabel("recepcion")
        
        self.Juno = {
            "nombre": "Juno",
            "edad": 4,
            "especie": "Perro",
            "dueno": "Yo"
        }
        
        self.mascotas_registradas = [self.Juno]
        
        layout_admin=QVBoxLayout()

        # layout_admin.addWidget(self.label)

        container=QWidget()
        container.setLayout(layout_admin)
        self.setCentralWidget(container)
        self.setFixedSize(900, 1000)
        
        layout_section_0 = QHBoxLayout()
        self.label = QLabel("Recepción", self)
        self.label.move(50, 50)
        self.label.setFont(QFont("Arial", 20))
        self.label.adjustSize()
        
       

        
        self.checkBox_0 = QPushButton("Registrar mascota")
        self.checkBox_0.setCheckable(True)
        self.checkBox_0.setStyleSheet(" QPushButton { width: 180px; height: 25px; font-size: 18px; } ")
        layout_section_0.addWidget(self.checkBox_0, alignment=Qt.AlignmentFlag.AlignRight)
        self.checkBox_0.clicked.connect(self.gestor_formularios)
        
        self.checkBox_1 = QPushButton("Registrar veterinario")
        self.checkBox_1.setCheckable(True)
        self.checkBox_1.setStyleSheet(" QPushButton { width: 150px; height: 25px; font-size: 18px; } ")
        layout_section_0.addWidget(self.checkBox_1, alignment=Qt.AlignmentFlag.AlignLeft)
        self.checkBox_1.clicked.connect(self.gestor_formularios)
        
        layout_admin.addLayout(layout_section_0)

        layout_section_1 = QHBoxLayout()
        
        self.formulario_admin_0 = QFormLayout ()
        
        
        self.label_mascota_0 = QLabel("Registar a una mascota")
        self.label_mascota_0.setStyleSheet(" font-size: 20px; ")
        self.formulario_admin_0.addWidget(self.label_mascota_0)
        
        self.input_mascota_0 = QLineEdit()
        self.input_mascota_0.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px; ")
        self.formulario_admin_0.addRow("Nombre de la mascota:", self.input_mascota_0)
        self.item_mascota_0 = self.formulario_admin_0.itemAt(1, QFormLayout.ItemRole.LabelRole)
        self.item_mascota_0 = self.item_mascota_0.widget()
        self.item_mascota_0.setStyleSheet(" font-size: 20px; ")
        
        self.input_mascota_1 = QLineEdit()
        self.input_mascota_1.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px;")
        self.formulario_admin_0.addRow("Edad de la mascota:", self.input_mascota_1)
        self.item_mascota_1 = self.formulario_admin_0.itemAt(2, QFormLayout.ItemRole.LabelRole)
        self.item_mascota_1 = self.item_mascota_1.widget()
        self.item_mascota_1.setStyleSheet("  font-size: 20px; ")
        
        self.input_mascota_2 = QLineEdit()
        self.input_mascota_2.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px;")
        self.formulario_admin_0.addRow("Especie de la mascota:", self.input_mascota_2)
        self.item_mascota_2 = self.formulario_admin_0.itemAt(3, QFormLayout.ItemRole.LabelRole)
        self.item_mascota_2 = self.item_mascota_2.widget()
        self.item_mascota_2.setStyleSheet("  font-size: 20px; ")
        
        self.input_mascota_3 = QLineEdit()
        self.input_mascota_3.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px;")
        self.formulario_admin_0.addRow("Dueño de la mascota:", self.input_mascota_3)
        self.item_mascota_3 = self.formulario_admin_0.itemAt(4, QFormLayout.ItemRole.LabelRole )
        self.item_mascota_3 = self.item_mascota_3.widget()
        self.item_mascota_3.setStyleSheet("  font-size: 20px; ")
        
        self.button_mascota_0 = QPushButton("Registrar")
        self.button_mascota_0.setStyleSheet(" QPushButton { height: 25px; font-size: 18px; max-width: 500px;} ")
        self.formulario_admin_0.addWidget(self.button_mascota_0)
        self.button_mascota_0.clicked.connect(self.agregar_mascota)
        
        layout_section_1.addLayout(self.formulario_admin_0)
        self.formulario_admin_1 = QFormLayout()
        
        self.label_veterinario_0 = QLabel("Agregar un nuevo veterinario")
        self.label_veterinario_0.setStyleSheet(" font: 20px; ")
        self.formulario_admin_1.addWidget(self.label_veterinario_0)
        
        self.input_veterinario_0 = QLineEdit()
        
        layout_section_1.addLayout(self.formulario_admin_1)
        layout_admin.addLayout(layout_section_1)
        
        self.input_veterinario_0 = QLineEdit()
        self.input_veterinario_0.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px; ")
        self.formulario_admin_1.addRow("Nombre :", self.input_veterinario_0)
        self.item_veterinario_0 = self.formulario_admin_1.itemAt(1, QFormLayout.ItemRole.LabelRole )
        self.item_veterinario_0 = self.item_veterinario_0.widget()
        self.item_veterinario_0.setStyleSheet(" font-size: 20px; ")
        
        self.input_veterinario_1 = QLineEdit()
        self.input_veterinario_1.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px; ")
        self.formulario_admin_1.addRow("Especialidad :", self.input_veterinario_1)
        self.item_veterinario_1 = self.formulario_admin_1.itemAt(2, QFormLayout.ItemRole.LabelRole )
        self.item_veterinario_1 = self.item_veterinario_1.widget()
        self.item_veterinario_1.setStyleSheet(" font-size: 20px; ")
        
        self.fecha_veterinario_0 = QDateEdit()
        self.fecha_veterinario_0.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px;")
        self.fecha_veterinario_0.setCalendarPopup(True)
        self.fecha_veterinario_0.setDateTime(QDateTime.currentDateTime())
        self.formulario_admin_1.addRow("Fecha de ingreso: ", self.fecha_veterinario_0)
        self.item_veterinario_1 = self.formulario_admin_1.itemAt(3, QFormLayout.ItemRole.LabelRole )
        self.item_veterinario_1 = self.item_veterinario_1.widget()
        self.item_veterinario_1.setStyleSheet(" font-size: 20px;")
        
        layout_section_2 = QHBoxLayout()
        self.formulario_cita_1 = QFormLayout ()
        
        
        self.label_cita_0 = QLabel("Hacer una cita")
        self.label_cita_0.setStyleSheet(" font-size: 20px; ")
        self.formulario_cita_1.addWidget(self.label_cita_0)
        
        self.combo_cita_0 = QComboBox()
        self.combo_cita_0.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px;")
        for i in self.mascotas_registradas: self.combo_cita_0.addItem(str(list(i.values())[0]))
        self.formulario_cita_1.addRow("Nombre de la mascota: ", self.combo_cita_0)
        self.item_cita_0 = self.formulario_cita_1.itemAt(1, QFormLayout.ItemRole.LabelRole )
        self.item_cita_0 = self.item_cita_0.widget()
        self.item_cita_0.setStyleSheet(" font-size: 20px;")
        
        self.fecha_cita_0 = QDateEdit()
        self.fecha_cita_0.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px;")
        self.fecha_cita_0.setCalendarPopup(True)
        self.fecha_cita_0.setDateTime(QDateTime.currentDateTime())
        self.formulario_cita_1.addRow("Fecha de la cita: ", self.fecha_cita_0)
        self.item_cita_1 = self.formulario_cita_1.itemAt(2, QFormLayout.ItemRole.LabelRole )
        self.item_cita_1 = self.item_cita_1.widget()
        self.item_cita_1.setStyleSheet(" font-size: 20px;")
        
        self.input_cita_0 = QLineEdit()
        self.input_cita_0.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px;")
        self.formulario_cita_1.addRow("Detalles de la cita: ", self.input_cita_0)
        self.item_cita_2 = self.formulario_cita_1.itemAt(3, QFormLayout.ItemRole.LabelRole )
        self.item_cita_2 = self.item_cita_2.widget()
        self.item_cita_2.setStyleSheet(" font-size: 20px;")
        
        self.button_cita_0 = QPushButton("Registrar")
        self.button_cita_0.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px")
        self.formulario_cita_1.addWidget(self.button_cita_0)
        
        layout_section_2.addLayout(self.formulario_cita_1)
        layout_admin.addLayout(layout_section_1)
        
        self.formulario_admin_1.setRowVisible(0, False)
        self.formulario_admin_1.setRowVisible(1, False)
        self.formulario_admin_1.setRowVisible(2, False)
        self.formulario_admin_1.setRowVisible(3, False)
        #self.formulario_admin_1.setRowVisible(4, False)

        layout_admin.addLayout(layout_section_2)
        
        layout_section_3 = QHBoxLayout()
        
        self.button_mostrar_0 = QPushButton("Mascotas resgistradar")
        self.button_mostrar_0.setStyleSheet(" max-width: 200px; font: 19px;")
        layout_section_3.addWidget(self.button_mostrar_0)
        self.button_mostrar_0.clicked.connect(self.botones_mostrar)

        self.button_mostrar_1 = QPushButton("Citas pendientes")
        self.button_mostrar_1.setStyleSheet(" max-width: 200px; font: 19px;")
        layout_section_3.addWidget(self.button_mostrar_1)

        self.button_mostrar_2 = QPushButton("Veterinarios")
        self.button_mostrar_2.setStyleSheet(" max-width: 200px; font: 19px;")
        layout_section_3.addWidget(self.button_mostrar_2)

        self.button_mostrar_3 = QPushButton("Mascotas resgistradar")
        self.button_mostrar_3.setStyleSheet(" max-width: 200px; font: 19px;")
        layout_section_3.addWidget(self.button_mostrar_3)
        
        layout_admin.addLayout(layout_section_3)
        
        layout_section_4 = QVBoxLayout()
        
        self.label_mostrar_0 = QLabel("Algo")
        self.label_mostrar_0.setStyleSheet(" font-size: 20px; ")
        
        layout_section_4.addWidget(self.label_mostrar_0)
        layout_admin.addLayout(layout_section_4)
        
    def gestor_formularios(self):
        # Si los dos quedan marcados, deja solo el que se acaba de marcar
        sender_0 = self.sender()
        if sender_0 == self.checkBox_0:
            self.checkBox_1.blockSignals(True)
            self.checkBox_1.setChecked(False)
            self.checkBox_1.blockSignals(False)
            
            self.formulario_admin_1.setRowVisible(0, False)
            self.formulario_admin_1.setRowVisible(1, False)
            self.formulario_admin_1.setRowVisible(2, False)
            self.formulario_admin_1.setRowVisible(3, False)
            
            self.formulario_admin_0.setRowVisible(0, True)
            self.formulario_admin_0.setRowVisible(1, True)
            self.formulario_admin_0.setRowVisible(2, True)
            self.formulario_admin_0.setRowVisible(3, True)
            self.formulario_admin_0.setRowVisible(4, True)
            self.formulario_admin_0.setRowVisible(5, True)
            
        elif sender_0 == self.checkBox_1:
            self.checkBox_0.blockSignals(True)
            self.checkBox_0.setChecked(False)
            self.checkBox_0.blockSignals(False)
            
            self.formulario_admin_1.setRowVisible(0, True)
            self.formulario_admin_1.setRowVisible(1, True)
            self.formulario_admin_1.setRowVisible(2, True)
            self.formulario_admin_1.setRowVisible(3, True)
            
            self.formulario_admin_0.setRowVisible(0, False)
            self.formulario_admin_0.setRowVisible(1, False)
            self.formulario_admin_0.setRowVisible(2, False)
            self.formulario_admin_0.setRowVisible(3, False)
            self.formulario_admin_0.setRowVisible(4, False)
            self.formulario_admin_0.setRowVisible(5, False)
                
    def agregar_mascota(self):
        nombre = self.input_mascota_0.text()
        edad = self.input_mascota_0.text()
        especie = self.input_mascota_0.text()
        dueno = self.input_mascota_0.text()
        
        nuevo_registro = {
            "nombre": nombre,
            "edad": edad,
            "especie": especie,
            "dueno": dueno
        }
        
        self.mascotas_registradas.append(nuevo_registro)
        self.combo_cita_0.addItem(nuevo_registro["nombre"])
        
        print(self.mascotas_registradas)
        
    def botones_mostrar(self):
        sender_1 = self.sender()
        if sender_1 == self.button_mostrar_0:
            self.label_mostrar_0.setText("Veterinarios")
        
       

        
        

def Veterinaria():
    app=QApplication([])
    window=pantalla_inicial()
    #window.setWindowTitle()
    window.show()
    app.exec() 

if __name__=="__main__":
    Veterinaria()