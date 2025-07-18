from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel, QHBoxLayout, QSlider, QLineEdit, QVBoxLayout, QMessageBox, QSpinBox, QComboBox, QSizePolicy, QGridLayout, QFormLayout, QDateEdit, QCheckBox, QDoubleSpinBox, QCompleter,QDialog, QAbstractItemView
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel, QHBoxLayout, QSlider, QLineEdit, QVBoxLayout, QMessageBox, QSpinBox, QComboBox, QSizePolicy, QGridLayout,QTableWidget, QTableWidgetItem,QDialog,QTextEdit
from PyQt6.QtCore import Qt, QSize, QDate
from PyQt6.QtGui import QFont
from sql import mysql_connect
from decimal import Decimal
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
        self.user_id=1

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
        container = QWidget()
        layout = QHBoxLayout(container)

        # Left side: Appointments for the day
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("Citas de Hoy"))
        self.tabla_citas_doctor = QTableWidget()
        self.tabla_citas_doctor.setColumnCount(5)
        self.tabla_citas_doctor.setHorizontalHeaderLabels(["ID Cita", "Dueño", "Mascota", "Motivo", "Id_mascota"])
        self.tabla_citas_doctor.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabla_citas_doctor.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla_citas_doctor.itemSelectionChanged.connect(self.mostrar_historial_medico)
        self.tabla_citas_doctor.resizeColumnsToContents()
        left_layout.addWidget(self.tabla_citas_doctor)

        # Right side: Medical History and Consultation
        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Historial Médico de la Mascota"))
        self.tabla_historial_medico = QTableWidget()
        self.tabla_historial_medico.setColumnCount(4)
        self.tabla_historial_medico.setHorizontalHeaderLabels(["Fecha", "Motivo", "Diagnóstico", "Tratamiento"])
        self.tabla_historial_medico.resizeColumnsToContents()
        right_layout.addWidget(self.tabla_historial_medico)

        self.btn_iniciar_consulta = QPushButton("Iniciar Consulta")
        self.btn_iniciar_consulta.clicked.connect(self.iniciar_consulta_dialog)
        right_layout.addWidget(self.btn_iniciar_consulta)

        layout.addLayout(left_layout, 1)
        layout.addLayout(right_layout, 1)
        self.setCentralWidget(container)

        self.cargar_citas_doctor()

    def cargar_citas_doctor(self):
        self.db=mysql_connect()
        doctor_id = self.user_id       
        hoy = QDate.currentDate().toString("yyyy-MM-dd")      
        citas = self.db.get_citas_by_doctor_and_date(doctor_id, hoy)
        self.tabla_citas_doctor.setRowCount(len(citas))
        for row, cita_data in enumerate(citas):
            id_cita, dueno, mascota, motivo, id_mascota = cita_data
            self.tabla_citas_doctor.setItem(row, 0, QTableWidgetItem(str(id_cita)))
            self.tabla_citas_doctor.setItem(row, 1, QTableWidgetItem(dueno))
            self.tabla_citas_doctor.setItem(row, 2, QTableWidgetItem(mascota))
            #self.tabla_citas_doctor.setItem(row, 3, QTableWidgetItem(str(hora)))
            self.tabla_citas_doctor.setItem(row, 3, QTableWidgetItem(motivo))
            #self.tabla_citas_doctor.setItem(row, 4, QTableWidgetItem(estado))
            self.tabla_citas_doctor.item(row, 0).setData(Qt.ItemDataRole.UserRole, id_mascota)

    def mostrar_historial_medico(self):
        selected_items = self.tabla_citas_doctor.selectedItems()
        if not selected_items:
            self.tabla_historial_medico.setRowCount(0)
            return

        id_mascota = selected_items[0].data(Qt.ItemDataRole.UserRole)
        historial = self.db.get_historial_medico(id_mascota)
        self.tabla_historial_medico.setRowCount(len(historial))
        for row, record in enumerate(historial):
            for col, data in enumerate(record):
                self.tabla_historial_medico.setItem(row, col, QTableWidgetItem(str(data)))

    def iniciar_consulta_dialog(self):
        selected_items = self.tabla_citas_doctor.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Error", "Por favor, seleccione una cita para iniciar la consulta.")
            return

        row = selected_items[0].row()
        cita_id = self.tabla_citas_doctor.item(row, 0).text()
        id_mascota = self.tabla_citas_doctor.item(row, 0).data(Qt.ItemDataRole.UserRole)
        motivo = self.tabla_citas_doctor.item(row, 3).text()
        id_doctor = self.user_id

        dialog = mini_ventana_consulta(cita_id, id_mascota, id_doctor, motivo, self)
        if dialog.exec():
            self.cargar_citas_doctor()
            self.mostrar_historial_medico()


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
        self.setFixedSize(1100, 600)
        
        self.layout_section_0 = QHBoxLayout()
        self.layout_section_0.setSpacing(2)
        
        fuente=QFont()
        fuente.setPointSize(14)
        
        self.checkBox_0 = QPushButton("Registrar cliente")
        self.checkBox_0.setCheckable(True)
        self.checkBox_0.setFont(fuente)
        self.checkBox_0.setFixedSize(150,35)
        #self.checkBox_0.setStyleSheet(" QPushButton { width: 180px; height: 25px; font-size: 18px; } ")
        self.layout_section_0.addWidget(self.checkBox_0)
        self.checkBox_0.clicked.connect(self.gestor_formularios)
        
        self.checkBox_1 = QPushButton("Registrar cita")
        self.checkBox_1.setCheckable(True)
        self.checkBox_1.setFont(fuente)
        self.checkBox_1.setFixedSize(150,35)
        #self.checkBox_1.setStyleSheet(" QPushButton { width: 150px; height: 25px; font-size: 18px; } ")
        self.layout_section_0.addWidget(self.checkBox_1)
        self.checkBox_1.clicked.connect(self.gestor_formularios)

        self.button_factura = QPushButton("Factura")
        self.button_factura.setCheckable(True)
        self.button_factura.setFixedSize(150,35)
        self.button_factura.setFont(fuente)

        #self.button_factura.setStyleSheet(" QPushButton{ width: 80px; height: 25px; font-size: 18px; } ")
        self.layout_section_0.addWidget(self.button_factura)
        self.button_factura.clicked.connect(self.abrir_ventana_factura)
        
        layout_admin.addLayout(self.layout_section_0)

        self.layout_section_1 = QHBoxLayout()
        
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
        self.formulario_admin_0.addRow("Apellido de la mascota:", self.input_mascota_1)
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
        self.formulario_admin_0.addRow("Raza de la mascota:", self.input_mascota_3)
        self.item_mascota_3 = self.formulario_admin_0.itemAt(4, QFormLayout.ItemRole.LabelRole )
        self.item_mascota_3 = self.item_mascota_3.widget()
        self.item_mascota_3.setStyleSheet("  font-size: 20px; ")
        
        self.spin_mascota_0 = QSpinBox()
        self.spin_mascota_0.setRange(0, 30)
        self.spin_mascota_0.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px;")
        self.formulario_admin_0.addRow("Edad de la mascota :", self.spin_mascota_0)
        self.item_mascota_4 = self.formulario_admin_0.itemAt(5, QFormLayout.ItemRole.LabelRole )
        self.item_mascota_4 = self.item_mascota_4.widget()
        self.item_mascota_4.setStyleSheet("  font-size: 20px; ")
        
        self.layout_section_1.addLayout(self.formulario_admin_0)
        self.formulario_admin_1 = QFormLayout()
        
        self.label_dueno_0 = QLabel("Agregar un nuevo dueño")
        self.label_dueno_0.setStyleSheet(" font: 20px; ")
        self.formulario_admin_1.addWidget(self.label_dueno_0)
        
        self.layout_section_1.addLayout(self.formulario_admin_1)
        layout_admin.addLayout(self.layout_section_1)
        
        self.input_dueno_0 = QLineEdit()
        self.input_dueno_0.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px; ")
        self.formulario_admin_1.addRow("Nombre del dueño:", self.input_dueno_0)
        self.item_dueno_0 = self.formulario_admin_1.itemAt(1, QFormLayout.ItemRole.LabelRole )
        self.item_dueno_0 = self.item_dueno_0.widget()
        self.item_dueno_0.setStyleSheet(" font-size: 20px; ")
        
        self.input_dueno_1 = QLineEdit()
        self.input_dueno_1.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px; ")
        self.formulario_admin_1.addRow("Apellido del dueño:", self.input_dueno_1)
        self.item_dueno_1 = self.formulario_admin_1.itemAt(2, QFormLayout.ItemRole.LabelRole )
        self.item_dueno_1 = self.item_dueno_1.widget()
        self.item_dueno_1.setStyleSheet(" font-size: 20px; ")
        
        self.input_dueno_2 = QLineEdit()
        self.input_dueno_2.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px; ")
        self.formulario_admin_1.addRow("Direccion del dueño:", self.input_dueno_2)
        self.item_dueno_2 = self.formulario_admin_1.itemAt(3, QFormLayout.ItemRole.LabelRole )
        self.item_dueno_2 = self.item_dueno_2.widget()
        self.item_dueno_2.setStyleSheet(" font-size: 20px; ")

        self.input_dueno_telefono = QLineEdit()
        self.input_dueno_telefono.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px; ")
        self.formulario_admin_1.addRow("Teléfono del dueño:", self.input_dueno_telefono)
        self.item_dueno_telefono = self.formulario_admin_1.itemAt(4, QFormLayout.ItemRole.LabelRole)
        self.item_dueno_telefono = self.item_dueno_telefono.widget()
        self.item_dueno_telefono.setStyleSheet(" font-size: 20px; ")
        
        self.input_dueno_3 = QLineEdit()
        self.input_dueno_3.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px; ")
        self.formulario_admin_1.addRow("Correo electronico:", self.input_dueno_3)
        self.item_dueno_3 = self.formulario_admin_1.itemAt(5, QFormLayout.ItemRole.LabelRole )
        self.item_dueno_3 = self.item_dueno_3.widget()
        self.item_dueno_3.setStyleSheet(" font-size: 20px; ")
        
        self.fecha_dueno_0 = QDateEdit()
        self.fecha_dueno_0.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px;")
        self.fecha_dueno_0.setCalendarPopup(True)
        self.fecha_dueno_0.setDateTime(QDateTime.currentDateTime())
        self.formulario_admin_1.addRow("Fecha de nacimiento: ", self.fecha_dueno_0)
        self.item_dueno_1 = self.formulario_admin_1.itemAt(6, QFormLayout.ItemRole.LabelRole )
        self.item_dueno_1 = self.item_dueno_1.widget()
        self.item_dueno_1.setStyleSheet(" font-size: 20px;")
        
        self.formulario_cita_1 = QFormLayout ()
        
        
        self.label_cita_0 = QLabel("Hacer una cita")
        self.label_cita_0.setStyleSheet(" font-size: 20px; ")
        self.formulario_cita_1.addWidget(self.label_cita_0)
        
        self.combo_cita_0 = QComboBox()
        self.combo_cita_0.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px;")
        db=mysql_connect()
        self.obtener_mascotas()
        #self.formulario_cita_1.addRow("Nombre de la mascota: ", self.combo_cita_0)
        #mascotas=self.obtener_mascotas()

        #for mascota in mascotas:
            #nombre_combo = f'{mascota["nombre"]} {mascota["apellido_cliente"]}'
            #self.combo_cita_0.addItem(nombre_combo, mascota["id"])
        self.formulario_cita_1.addRow("Nombre de la mascota: ", self.combo_cita_0)
        self.item_cita_0 = self.formulario_cita_1.itemAt(1, QFormLayout.ItemRole.LabelRole )
        self.item_cita_0 = self.item_cita_0.widget()
        self.item_cita_0.setStyleSheet(" font-size: 20px;")
        
        self.combo_cita_1 = QComboBox()
        self.combo_cita_1.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px;")
        veterinarios = db.obtener_veterinarios()
        for vet in veterinarios:
            nombre_completo = f'{vet["nombre"]} {vet["apellido"]}'
            self.combo_cita_1.addItem(nombre_completo, vet["id"])
        self.formulario_cita_1.addRow("Veterianario asignado: ", self.combo_cita_1)
        self.item_cita_1 = self.formulario_cita_1.itemAt(2, QFormLayout.ItemRole.LabelRole )
        self.item_cita_1 = self.item_cita_1.widget()
        self.item_cita_1.setStyleSheet(" font-size: 20px;")
        
        self.fecha_cita_0 = QDateEdit()
        self.fecha_cita_0.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px;")
        self.fecha_cita_0.setCalendarPopup(True)
        self.fecha_cita_0.setDateTime(QDateTime.currentDateTime())
        self.formulario_cita_1.addRow("Fecha de la cita: ", self.fecha_cita_0)
        self.item_cita_2 = self.formulario_cita_1.itemAt(3, QFormLayout.ItemRole.LabelRole )
        self.item_cita_2 = self.item_cita_2.widget()
        self.item_cita_2.setStyleSheet(" font-size: 20px; ")
        
        self.input_cita_0 = QLineEdit()
        self.input_cita_0.setStyleSheet(" height: 25px; font-size: 20px; max-width: 500px; ")
        self.formulario_cita_1.addRow("Motivo de la cita: ", self.input_cita_0)
        self.item_cita_3 = self.formulario_cita_1.itemAt(4, QFormLayout.ItemRole.LabelRole )
        self.item_cita_3 = self.item_cita_3.widget()
        self.item_cita_3.setStyleSheet(" font-size: 20px; ")
        
        self.spin_cita_0 = QDoubleSpinBox()
        self.spin_cita_0.setPrefix("$")
        self.spin_cita_0.setDecimals(2)
        self.spin_cita_0.setRange(0, 1000)
        self.spin_cita_0.setSingleStep(0.25)
        self.spin_cita_0.setStyleSheet("  height: 25px; font-size: 20px; max-width: 500px; ")
        self.formulario_cita_1.addRow("Precio de la cita: ", self.spin_cita_0)
        self.item_cita_4 = self.formulario_cita_1.itemAt(5, QFormLayout.ItemRole.LabelRole )
        self.item_cita_4 = self.item_cita_4.widget()
        self.item_cita_4.setStyleSheet(" font-size: 20px; ")

        
        self.layout_section_1.addLayout(self.formulario_cita_1)

        self.layout_section_2 = QHBoxLayout()

        self.button_registrar_cliente = QPushButton("Registrar cliente")
        self.button_registrar_cliente.setStyleSheet(" max-width: 200px; height: 25px; font-size: 20px; ")
        self.layout_section_2.addWidget(self.button_registrar_cliente)
        self.button_registrar_cliente.clicked.connect(self.registrar_datos)
        
        self.button_registrar_cita = QPushButton("Registrar cita")
        self.button_registrar_cita.setStyleSheet(" max-width: 200px; height: 25px; font-size: 20px; ")
        self.layout_section_2.addWidget(self.button_registrar_cita)

        self.button_registrar_cita.clicked.connect(self.registrar_cita)
        
        layout_admin.addLayout(self.layout_section_2)
        
        for a in range(self.formulario_cita_1.rowCount()):
            self.formulario_cita_1.setRowVisible(a, False)
        self.button_registrar_cita.setVisible(False)

        
        self.layout_section_3 = QHBoxLayout()
        
        self.button_mostrar_0 = QPushButton("Mascotas resgistradar")
        self.button_mostrar_0.setStyleSheet(" max-width: 200px; font: 19px;")
        self.layout_section_3.addWidget(self.button_mostrar_0)
        self.button_mostrar_0.clicked.connect(self.botones_mostrar)

        self.button_mostrar_1 = QPushButton("Citas pendientes")
        self.button_mostrar_1.setStyleSheet(" max-width: 200px; font: 19px;")
        self.layout_section_3.addWidget(self.button_mostrar_1)

        self.button_mostrar_2 = QPushButton("Veterinarios")
        self.button_mostrar_2.setStyleSheet(" max-width: 200px; font: 19px;")
        self.layout_section_3.addWidget(self.button_mostrar_2)

        self.button_mostrar_3 = QPushButton("Mascotas resgistradar")
        self.button_mostrar_3.setStyleSheet(" max-width: 200px; font: 19px;")
        self.layout_section_3.addWidget(self.button_mostrar_3)
        
        layout_admin.addLayout(self.layout_section_3)
        
        self.layout_section_4 = QVBoxLayout()
        
        self.label_mostrar_0 = QLabel("")
        self.label_mostrar_0.setStyleSheet(" font-size: 20px; ")
        
        self.layout_section_4.addWidget(self.label_mostrar_0)
        layout_admin.addLayout(self.layout_section_4)
        self.productos_agregados = []

    def obtener_mascotas(self):
        db = mysql_connect()
        mascotas = db.obtener_mascotas_con_apellido_cliente()

        self.combo_cita_0.clear()

        for mascota in mascotas:
            nombre_combo = f'{mascota["nombre"]} {mascota["apellido_cliente"]}'
            self.combo_cita_0.addItem(nombre_combo, mascota["id"])
        return mascotas

    def registrar_cita(self):
        if (
            self.combo_cita_0.currentIndex() == -1 or
            self.combo_cita_1.currentIndex() == -1 or
            self.input_cita_0.text().strip() == ""
        ):
            QMessageBox.warning(self, "Campos incompletos", "Por favor, completa todos los campos.")
            return

        # Obtener ID reales (asumo que .currentData() guarda el ID)
        id_mascota = self.combo_cita_0.currentData()
        id_veterinario = self.combo_cita_1.currentData()
        fecha = self.fecha_cita_0.date().toString("yyyy-MM-dd")
        motivo = self.input_cita_0.text().strip()
        precio = self.spin_cita_0.value()

        db = mysql_connect()
        if db.registrar_cita(id_mascota, id_veterinario, fecha, motivo, precio):
            QMessageBox.information(self, "Éxito", "La cita fue registrada correctamente.")
        else:
            QMessageBox.critical(self, "Error", "No se pudo registrar la cita.")

    def registrar_datos(self):
        # Validar que todos los campos estén llenos
        if not all([
            self.input_mascota_0.text(),
            self.input_mascota_1.text(),
            self.input_mascota_2.text(),
            self.input_mascota_3.text(),
            self.input_dueno_0.text(),
            self.input_dueno_1.text(),
            self.input_dueno_2.text(),
            self.input_dueno_3.text()
        ]):
            QMessageBox.warning(self, "Campos vacíos", "Por favor, completa todos los campos.")
            return

        # Obtener datos
        cliente_data = (
            self.input_dueno_0.text(),
            self.input_dueno_1.text(),
            self.input_dueno_2.text(),
            self.input_dueno_telefono.text(),
            self.input_dueno_3.text(),
            self.fecha_dueno_0.date().toString("yyyy-MM-dd")
        )

        mascota_data = (
            self.input_mascota_2.text(),
            self.input_mascota_3.text(),
            self.spin_mascota_0.value(),
            self.input_mascota_0.text()
        )

        # Llamar al método del archivo sql.py
        db = mysql_connect()
        exito = db.registrar_cliente_y_mascota(cliente_data, mascota_data)
        self.obtener_mascotas()

        if exito:
            QMessageBox.information(self, "Éxito", "Cliente y mascota registrados correctamente.")
        else:
            QMessageBox.critical(self, "Error", "Ocurrió un error al registrar los datos.")


    def abrir_ventana_factura(self):
        ventana = VentanaFactura(self)
        print(type(ventana))
        ventana.exec() 
        
        

    

    def gestor_formularios(self):
        # Si los dos quedan marcados, deja solo el que se acaba de marcar
        sender_0 = self.sender()
        if sender_0 == self.checkBox_0:
            self.checkBox_1.blockSignals(True)
            self.checkBox_1.setChecked(False)
            self.checkBox_1.blockSignals(False)
            
            self.button_registrar_cita.setVisible(False)
            self.button_registrar_cliente.setVisible(True)
            
            for a in range(self.formulario_cita_1.rowCount()):
                self.formulario_cita_1.setRowVisible(a, False)
            
            for a in range(self.formulario_admin_1.rowCount()):
                self.formulario_admin_1.setRowVisible(a, True)
            
            for a in range(self.formulario_admin_0.rowCount()):
                self.formulario_admin_0.setRowVisible(a, True)

            
        elif sender_0 == self.checkBox_1:
            self.checkBox_0.blockSignals(True)
            self.checkBox_0.setChecked(False)
            self.checkBox_0.blockSignals(False)

            self.button_registrar_cita.setVisible(True)
            self.button_registrar_cliente.setVisible(False)
            
            for a in range(self.formulario_cita_1.rowCount()):
                self.formulario_cita_1.setRowVisible(a, True)
            
            for a in range(self.formulario_admin_1.rowCount()):
                self.formulario_admin_1.setRowVisible(a, False)
            
            
            for a in range(self.formulario_admin_0.rowCount()):
                self.formulario_admin_0.setRowVisible(a, False)
    
        

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

class VentanaFactura(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nueva Factura")
        self.setFixedSize(600, 500)

        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)

        # Aquí colocas lo que tenías en mostrar_factura()
        #self.mostrar_factura()

    #def mostrar_factura(self):
    # Limpiar contenido anterior del layout
        

        # Instancia de conexión
        db = mysql_connect()

        # Layout del formulario de factura
        form_factura = QFormLayout()
        form_factura.setSpacing(12)

        self.productos_layout = QVBoxLayout()

       

        # ======= Cliente =======
        self.combo_cliente_factura = QComboBox()
        self.combo_cliente_factura.setEditable(True)
        self.combo_cliente_factura.addItem("-- Seleccione cliente --")
        clientes = db.consultar_clientes()
        self.combo_cliente_factura.addItems(clientes)
        self.combo_cliente_factura.setCompleter(QCompleter(clientes))
        self.combo_cliente_factura.setStyleSheet("font-size: 18px; height: 30px; max-width: 400px;")
        form_factura.addRow("Cliente:", self.combo_cliente_factura)

        # ======= Producto =======
        self.combo_producto_factura = QComboBox()
        self.combo_producto_factura.setEditable(True)
        self.combo_producto_factura.addItem("Ninguno")
        productos = db.consultar_productos()
        self.combo_producto_factura.addItems(productos)
        self.combo_producto_factura.setCompleter(QCompleter(["Ninguno"] + productos))
        self.combo_producto_factura.setStyleSheet("font-size: 18px; height: 30px; max-width: 400px;")
        form_factura.addRow("Producto:", self.combo_producto_factura)

        # ======= Cantidad =======
        self.spin_cantidad_factura = QSpinBox()
        self.spin_cantidad_factura.setRange(0, 100)
        self.spin_cantidad_factura.setStyleSheet("font-size: 18px; height: 30px; max-width: 120px;")
        form_factura.addRow("Cantidad:", self.spin_cantidad_factura)

        # ======= Precio de la consulta =======
        self.combo_consultas = QComboBox()
        self.combo_consultas.setEnabled(False)
        self.combo_consultas.setStyleSheet("font-size: 18px; height: 30px; max-width: 200px;")
        form_factura.addRow("Consulta:", self.combo_consultas)

        # ======= Precio de la consulta =======
        self.label_precio_consulta = QLabel("Seleccione cliente y consulta")
        self.label_precio_consulta.setStyleSheet("font-size: 18px; color: gray;")
        form_factura.addRow("Precio consulta:", self.label_precio_consulta)

        self.label_precio_total = QLabel("$0.00")
        self.label_precio_total.setStyleSheet("font-size: 18px; color: blue;")
        form_factura.addRow("Precio total:", self.label_precio_total)

        self.combo_cliente_factura.currentIndexChanged.connect(self.actualizar_consultas_del_cliente)
        self.combo_consultas.currentIndexChanged.connect(self.actualizar_precio_consulta)

        self.combo_producto_factura.currentIndexChanged.connect(self.actualizar_precio_total)
        self.spin_cantidad_factura.valueChanged.connect(self.actualizar_precio_total)
        self.combo_consultas.currentIndexChanged.connect(self.actualizar_precio_total) 


        # Añadir el layout al contenedor
        widget_factura = QWidget()
        widget_factura.setLayout(form_factura)
        self.layout_principal.addWidget(widget_factura)
    


    def actualizar_consultas_del_cliente(self):
        nombre = self.combo_cliente_factura.currentText().strip()

        if nombre == "" or nombre == "-- Seleccione cliente --":
            self.combo_consultas.clear()
            self.combo_consultas.setEnabled(False)
            self.label_precio_consulta.setText("Seleccione un cliente válido")
            self.label_precio_consulta.setStyleSheet("font-size: 18px; color: red;")
            return

        db = mysql_connect()

        nombre = self.combo_cliente_factura.currentText()
        consultas = db.obtener_consultas_por_cliente(nombre)

        self.combo_consultas.clear()
        if consultas:
            self.combo_consultas.addItems([str(c) for c in consultas])
            self.combo_consultas.setEnabled(True)
        else:
            self.combo_consultas.setEnabled(False)
            self.label_precio_consulta.setText("No hay consultas registradas")
            self.label_precio_consulta.setStyleSheet("font-size: 18px; color: red;")

    def actualizar_precio_consulta(self):
        
        db = mysql_connect()

        id_consulta = self.combo_consultas.currentText()
        if not id_consulta:
            return

        db.cursor.execute("SELECT Id_precio FROM consultas WHERE Id_consultas = %s", (id_consulta,))
        resultado = db.cursor.fetchone()

        if resultado:
            precio = resultado[0]
            self.label_precio_consulta.setText(f"${precio:.2f}")
            self.label_precio_consulta.setStyleSheet("font-size: 18px; color: green;")
        else:
            self.label_precio_consulta.setText("Consulta no encontrada")
            self.label_precio_consulta.setStyleSheet("font-size: 18px; color: red;")

    def actualizar_precio_total(self):
        
        db = mysql_connect()

        # Obtener precio de la consulta actual
        id_consulta = self.combo_consultas.currentText()
        try:
            db.cursor.execute("SELECT Id_precio FROM consultas WHERE Id_consultas = %s", (id_consulta,))
            resultado = db.cursor.fetchone()
            precio_consulta = resultado[0] if resultado else 0.0
        except:
            precio_consulta = 0.0

        # Obtener precio del producto
        nombre_producto = self.combo_producto_factura.currentText()
        cantidad = self.spin_cantidad_factura.value()

        if nombre_producto and nombre_producto != "Ninguno" and cantidad > 0:
            precio_producto_unitario = db.obtener_precio_producto(nombre_producto)
            precio_productos = precio_producto_unitario * cantidad
        else:
            precio_productos = 0.0

        total = Decimal(precio_consulta) + Decimal(precio_productos)
        self.label_precio_total.setText(f"${total:.2f}")


class mini_ventana_consulta(QDialog):
    def __init__(self, cita_id, mascota_id, doctor_id, motivo, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Registrar Consulta")
        self.setFixedSize(500, 400)

        self.cita_id = cita_id
        self.mascota_id = mascota_id
        self.doctor_id = doctor_id
        self.motivo = motivo

        layout = QFormLayout(self)

        self.motivo_label = QLabel(f"<b>Motivo de la Consulta:</b> {self.motivo}")
        self.diagnostico_edit = QTextEdit()
        self.tratamiento_edit = QTextEdit()

        layout.addRow(self.motivo_label)
        layout.addRow("Diagnóstico:", self.diagnostico_edit)
        layout.addRow("Tratamiento:", self.tratamiento_edit)

        self.btn_guardar = QPushButton("Guardar Consulta")
        self.btn_guardar.clicked.connect(self.guardar_consulta)
        layout.addRow(self.btn_guardar)

    def guardar_consulta(self):
        diagnostico = self.diagnostico_edit.toPlainText()
        tratamiento = self.tratamiento_edit.toPlainText()

        if not diagnostico or not tratamiento:
            QMessageBox.warning(self, "Campos incompletos", "Por favor, complete el diagnóstico y el tratamiento.")
            return

        fecha = QDate.currentDate().toString("yyyy-MM-dd")

        conexion = mysql_connect()
        try:
            conexion.agregar_consulta(self.cita_id, self.mascota_id, self.doctor_id, fecha, self.motivo, diagnostico)
            #conexion.actualizar_estado_cita(self.cita_id, "Completada")
            QMessageBox.information(self, "Éxito", "Consulta guardada y cita completada.")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar la consulta: {e}")
        finally:
            conexion.close()
    
class CrearUsuarioDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.setWindowTitle("Crear Nuevo Usuario")

        self.user_line = QLineEdit()
        self.pass_line = QLineEdit()
        self.pass_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.rol_combo = QComboBox()
        self.rol_combo.addItems(["Administrador", "Doctor", "Recepcion"])

        self.btn_crear = QPushButton("Crear")
        self.btn_crear.clicked.connect(self.agregar_def)

        form_layout = QFormLayout()
        form_layout.addRow("Usuario:", self.user_line)
        form_layout.addRow("Contraseña:", self.pass_line)
        form_layout.addRow("Rol:", self.rol_combo)
        form_layout.addRow(self.btn_crear)

        self.setLayout(form_layout)

    def agregar_def(self):
        usuario = self.user_line.text()
        clave = self.pass_line.text()
        rol = self.rol_combo.currentText()

        if not usuario or not clave:
            QMessageBox.warning(self, "Error", "Usuario y contraseña no pueden estar vacíos.")
            return

        # Call the method from the parent window (pantalla_inicial)
        self.parent_window.agregar_usuario(rol, usuario, clave)
        QMessageBox.information(self, "Éxito", f"Usuario '{usuario}' agregado como {rol}.")
        self.accept() # Use accept() to close the dialog and return a success signal
    
       

        
        

def Veterinaria():
    app=QApplication([])
    window=pantalla_inicial()
    #window.setWindowTitle()
    window.show()
    app.exec() 

if __name__=="__main__":
    Veterinaria()