from conexion import *

class CClientes:

    def ingresarClientes(nombres,apellidos,sexo):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into usuarios values(null,%s,%s,%s);"

            # las variable valores tiene que ser una tupla, eso quiere decir que no se puede modificar
            # como minima expresion es: (valor,) la coma hace que sea una tupla
            valores = (nombres,apellidos,sexo) 
            cursor.execute(sql,valores) # cursor ejecuta el agrupamiento de la consulta (sql) con (valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()
        
        except mysql.connector.Error as error: 
            print(" Error al ingresar ala base de datos {}".format(error))
