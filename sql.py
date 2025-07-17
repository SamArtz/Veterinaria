import mysql.connector

class mysql_connect():

    def __init__(self):
        self.conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="vet"
        )

        self.cursor = self.conexion.cursor()
    
    def obtener_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()
        #self.cursor.close()
        #self.conexion.close()

    def agregar_prod(self,nombre,descripcion,precio,stock):
        query=f"INSERT INTO productos (Nombre_Producto, Descripcion_Producto, Precio_Producto, Stock_Producto) VALUES ('{nombre}', '{descripcion}', {precio}, {stock})"

        print(f"{query} agregado exitosamente")
        self.cursor.execute(query)
        self.conexion.commit()
    
    def elim_prod(self,id):
        query1=f"DELETE FROM productos WHERE ID_Producto = {id}"

        self.cursor.execute(query1)
        print(f"{query1} Eliminado exitosamente")
        self.conexion.commit()
        


    def buscar_productos(self,filtro=""):
        
        query = "SELECT ID_Producto, Nombre_Producto, Descripcion_Producto, Precio_Producto, Stock_Producto FROM productos"
        if filtro:
            query += " WHERE Nombre_Producto LIKE %s"
            self.cursor.execute(query, (f"%{filtro}%",))
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def update_prod(self,cantidad,id):

        query=f"UPDATE productos SET Stock_Producto = {cantidad} WHERE ID_Producto = {id};"

        self.cursor.execute(query)
        print(f"{query} Editado exitosamente")
        self.conexion.commit()
    
    def agregar_user(self,nombre,apellido,correo,telefono,especialidad):
        if especialidad=="":
            query=f"INSERT INTO Vendedores (Nombre_Vendedor, Apellido_Vendedor, Telefono_Vendedor, Correo_Vendedor) VALUES ('{nombre}', '{apellido}', '{telefono}', '{correo}')"
            self.cursor.execute(query)
            self.conexion.commit()
        else:
            query=f"INSERT INTO doctor (Nombre, Apellido, Especialidad, Telefono, Correo_elec) VALUES ('{nombre}', '{apellido}', '{especialidad}', '{telefono}','{correo}')"
            self.cursor.execute(query)
            self.conexion.commit()

    def consultar_clientes(self):
        self.cursor.execute("SELECT Nombre FROM cliente")
        return [fila[0] for fila in self.cursor.fetchall()]

    def consultar_productos(self):
        self.cursor.execute("SELECT nombre_producto FROM productos")
        return [fila[0] for fila in self.cursor.fetchall()]

    def consultar_mascotas(self):
        self.cursor.execute("SELECT nombre FROM mascota")
        return [fila[0] for fila in self.cursor.fetchall()]

    def consultar_veterinarios(self):
        self.cursor.execute("SELECT nombre FROM veterinario")
        return [fila[0] for fila in self.cursor.fetchall()]
    
    def obtener_consultas_por_cliente(self, nombre_cliente):
    # 1. Buscar ID del cliente
        self.cursor.execute("SELECT id_cliente FROM cliente WHERE nombre = %s", (nombre_cliente,))
        resultado = self.cursor.fetchone()
        if not resultado:
            return []

        id_cliente = resultado[0]

        # 2. Buscar ID de consultas del cliente (vía mascota)
        query = """
            SELECT c.id_consultas
            FROM consultas c
            JOIN mascota m ON c.Id_Mascota = m.Id_Mascota
            WHERE m.Id_cliente = %s
            ORDER BY c.fecha_consult DESC
        """
        self.cursor.execute(query, (id_cliente,))
        return [fila[0] for fila in self.cursor.fetchall()]
    
    def obtener_precio_producto(self, nombre_producto):
        self.cursor.execute("SELECT precio_producto FROM productos WHERE nombre_producto = %s", (nombre_producto,))
        resultado = self.cursor.fetchone()
        return resultado[0] if resultado else 0.0
    
    def get_citas_by_doctor_and_date(self, doctor_id, fecha):
        query = """SELECT c.Id_Cita, cl.Nombre, m.Nombre, c.Hora, c.Motivo, c.Estado, c.Id_Mascota
                 FROM cita c
                 JOIN mascota m ON c.Id_Mascota = m.Id_Mascota
                 JOIN cliente cl ON m.Id_Cliente = cl.Id_Cliente
                 WHERE c.Id_Doctor = %s AND c.Fecha = %s
                 ORDER BY c.Hora"""
        self.cursor.execute(query, (doctor_id, fecha))
        return self.cursor.fetchall()
    
    def get_historial_medico(self, mascota_id):
        query = """SELECT Fecha, Motivo, Diagnostico, Tratamiento
                 FROM consulta
                 WHERE Id_Mascota = %s
                 ORDER BY Fecha DESC"""
        self.cursor.execute(query, (mascota_id,))
        return self.cursor.fetchall()
    
    def agregar_consulta(self, id_cita, id_mascota, id_doctor, fecha, motivo, diagnostico, tratamiento):
        query = """INSERT INTO consulta (Id_Cita, Id_Mascota, Id_Doctor, Fecha, Motivo, Diagnostico, Tratamiento)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (id_cita, id_mascota, id_doctor, fecha, motivo, diagnostico, tratamiento)
        try:
            self.cursor.execute(query, values)
            self.conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error al agregar consulta: {err}")
            self.conexion.rollback()

    def actualizar_estado_cita(self, id_cita, nuevo_estado):
        query = "UPDATE consulta SET Estado = %s WHERE Id_Cita = %s"
        try:
            self.cursor.execute(query, (nuevo_estado, id_cita))
            self.conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error al actualizar estado de la cita: {err}")
            self.conexion.rollback()

    def close(self):
        if self.conexion.is_connected():
            self.cursor.close()
            self.conexion.close()
            print("Conexión a MySQL cerrada")


    def registrar_cliente_y_mascota(self, cliente_data, mascota_data):
        try:
            # Insertar cliente
            query_cliente = """
                INSERT INTO cliente (Nombre, Apellido, Direccion,Telefono, Correo_elec, Fecha_nacimiento)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query_cliente, cliente_data)
            cliente_id = self.cursor.lastrowid  # ID generado automáticamente

            # Insertar mascota
            query_mascota = """
                INSERT INTO mascota (Id_cliente, especie, Raza, Edad, Nombre)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query_mascota, (cliente_id, *mascota_data))
            self.conexion.commit()
            return True

        except mysql.connector.Error as err:
            print("Error:", err)
            self.conexion.rollback()
            return False
        
    def registrar_cita(self, id_mascota, id_veterinario, fecha, motivo, precio):
        try:
            query = """
                INSERT INTO consultas (Id_mascota, Id_doctor, Fecha_consult, Motiv_consult, Id_Precio)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (id_mascota, id_veterinario, fecha, motivo, precio))
            self.conexion.commit()
            return True
        except mysql.connector.Error as err:
            print("Error al registrar cita:", err)
            self.conexion.rollback()
            return False
        
    def obtener_mascotas_con_apellido_cliente(self):
        try:
            query = """
                SELECT m.Id_Mascota, m.Nombre, c.Apellido
                FROM mascota m
                JOIN cliente c ON m.Id_cliente = c.Id_cliente
            """
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()
            return [{"id": fila[0], "nombre": fila[1], "apellido_cliente": fila[2]} for fila in resultados]
        except mysql.connector.Error as err:
            print("Error al obtener mascotas:", err)
            return []
        
    def obtener_veterinarios(self):
        try:
            query = "SELECT Id_doctor, Nombre, Apellido FROM doctor"
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()
            return [{"id": fila[0], "nombre": fila[1], "apellido": fila[2]} for fila in resultados]
        except mysql.connector.Error as err:
            print("Error al obtener veterinarios:", err)
            return []


            


mysql_connect()