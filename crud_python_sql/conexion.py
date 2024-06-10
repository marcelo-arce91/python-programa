# pip install mysqsl-connector-python(libreria) este es el comando que usamos para descargar el connector

import mysql.connector

class CConexion:

    def ConexionBaseDeDatos():

        try:
            conexion = mysql.connector.connect(user='root',
                                               password='lena0110',
                                               host='127.0.0.1',
                                               database='clientesdb',
                                               port='3306')
            print("conexion correcta")
            
            return conexion
            

        except mysql.connector.Error as error:
            print("Error al conectarte a la base de datos {}".format(error))

    ConexionBaseDeDatos()


