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

