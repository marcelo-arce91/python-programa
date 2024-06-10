import tkinter as tk

#importar los modulos restante


from tkinter import *

from tkinter import ttk

from tkinter import messagebox

from clientes import *

from conexion import *


class FormularioClientes:
 
 global base
 base =None
 
 global texBoxId
 texBoxId =None

 global texBoxNombres
 texBoxNombres =None

 global texBoxApellidos
 texBoxApellidos =None

 global combo
 combo =None

 global groupBox
 groupBox =None

 global tree
 tree =None

 



def Formulario():
  

  global texBoxId
  global texBoxNombres
  global texBoxApellidos
  global combo
  global groupBox
  global tree


  try:
   base = Tk()
   base.geometry("1200x300")
   base.title("Formulario Python")

   groupBox = LabelFrame(base,text= "Datos del personal",padx=5,pady=5)
   groupBox.grid(row=0,column=0,padx=10,pady=10)

   labelId=Label(groupBox,text= "id:",width=13,font=("arial",12)).grid(row=0,column=0)
   texBoxId = Entry(groupBox)
   texBoxId.grid(row=0,column=1)

   labelNombres=Label(groupBox,text= "Nombres:",width=13,font=("arial",12)).grid(row=1,column=0)
   texBoxNombres = Entry(groupBox)
   texBoxNombres.grid(row=1,column=1)

   labelApellidos=Label(groupBox,text= "Apellidos:",width=13,font=("arial",12)).grid(row=2,column=0)
   texBoxApellidos = Entry(groupBox)
   texBoxApellidos.grid(row=2,column=1)

   labelSexo=Label(groupBox,text= "Sexo:",width=13,font=("arial",12)).grid(row=3,column=0)
   seleccionSexo = tk.StringVar()
   combo= ttk.Combobox(groupBox,values=["Masculino","Femenino","sangu(gay)","yiyo(virgen)"],textvariable=seleccionSexo)
   combo.grid(row=3,column=1)
   seleccionSexo.set("Masculino") # selecciona por defecto el sexo asignado

   Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=4,column=0)
   Button(groupBox,text="Modificar",width=10).grid(row=4,column=1)
   Button(groupBox,text="Eliminar",width=10).grid(row=4,column=2)

   groupBox = LabelFrame(base,text= "Lista del personal",padx=5,pady=5)
   groupBox.grid(row=0,column=1,padx=5,pady=5)

   #crear un treeview, este es el control que nos a permitir crear esta grilla,donde podemos mostrar nuestros registros

   # configurar las columnas

   tree = ttk.Treeview(groupBox,columns=("Id","Nombres","Apellidos","Sexo"),show='headings',height=5) # headings es la cabecera
   tree.column("# 1",anchor=CENTER)
   tree.heading("# 1",text="Id")
   tree.column("# 2",anchor=CENTER)
   tree.heading("# 2",text="Nombres")
   tree.column("# 3",anchor=CENTER)
   tree.heading("# 3",text="Apellidos")
   tree.column("# 4",anchor=CENTER)
   tree.heading("# 4",text="Sexo")

   tree.pack()

   base.mainloop()


  except ValueError as error:
      print(" Error al mostrar la interfaz, error: {}".format(error))

def guardarRegistros():
   global texBoxNombres,texBoxApellidos,combo,groupBox

   try:
     #verificar si los widgets (botoncitos) estan inicializados

     if texBoxNombres is None or texBoxApellidos is None or combo is None:
       print(" Los widgets no estan inicializados")
       return
     
     nombres = texBoxNombres.get()
     apellidos = texBoxApellidos.get()
     sexo = combo.get()

     CClientes.ingresarClientes(nombres,apellidos,sexo)
     messagebox.showinfo("Informacion","Los datos fueron guardados")

     # limpiamos los campos

     texBoxNombres.delete(0,END)
     texBoxApellidos.delete(0,END)
   except ValueError as error:
    print("Error al ingresar los datos{}".format(error))

Formulario()
