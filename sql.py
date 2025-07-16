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

    


mysql_connect()