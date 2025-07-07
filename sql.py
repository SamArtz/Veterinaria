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

    


mysql_connect()