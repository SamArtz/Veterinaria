from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel, QHBoxLayout, QSlider, QLineEdit, QVBoxLayout, QMessageBox, QSpinBox, QComboBox, QSizePolicy, QGridLayout,QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont
from sql import mysql_connect



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

        self.direccion=QLabel("Telefono: ",self)
        self.direccion.move(650,240)
        self.direccion.setFont(QFont("Arial", 13))
        self.direccion.adjustSize()
        
        self.direccion_line=QLineEdit(self)
        self.direccion_line.setFixedSize(400,28)
        self.direccion_line.move(750,235)

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

        #self.add.clicked.connect()
        
        


        #self.add.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        #self.add.setFixedWidth(100)
        
        #layout_admin=QGridLayout()

        ##layout_admin.addWidget(self.add,0,2)
        
        

    
        #container=QWidget()
        #container.setLayout(layout_admin)
        #self.setCentralWidget(container)

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


            

    def doctor(self):
    # Crear widgets
        self.label = QLabel("Bienvenido Doctor", self)
        self.label.setFont(QFont("Arial", 20))
        self.label.adjustSize()

        self.ver_Paciente = QPushButton("Ver pacientes", self)
        self.ver_Paciente.clicked.connect(self.mostrar_pacientes)

        self.pacientes = QComboBox()
        self.pacientes.addItems(["Paciente 1", "Paciente 2", "Paciente 3"])
        self.pacientes.hide()

        # Layout para botones y combo
        controles_layout = QVBoxLayout()
        controles_layout.addWidget(self.ver_Paciente)
        controles_layout.addWidget(self.pacientes)

        # Layout principal
        layout_doc = QHBoxLayout()
        layout_doc.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout_doc.addLayout(controles_layout)  

        # Establecer layout en el contenedor central
        container = QWidget()
        container.setLayout(layout_doc)
        self.setCentralWidget(container)

    def mostrar_pacientes(self):
        self.pacientes.show()


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