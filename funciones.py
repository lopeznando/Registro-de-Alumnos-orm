from tkinter import *
from tkinter.messagebox import *
import orm as db
def f_limpiar(ventana):
    ventana.nombre_texto.delete(0,END)
    ventana.apellidos_texto.delete(0,END)
    ventana.dni_texto.delete(0,END)

    ventana.nombre_texto.focus()

def f_nuevo(ventana):
    nombre=ventana.nombre_texto.get()
    apellidos=ventana.apellidos_texto.get()
    dni=ventana.dni_texto.get()
    showinfo(title="Nuevo",message="nuevo contacto agregado")
    ventana.tabla_datos.insert("",END,text=nombre,values=(apellidos,dni))
    f_limpiar(ventana)
    
def f_eliminar(ventana):
    elem_eliminar=ventana.tabla_datos.selection()
    showwarning(title="ELIMINAR",message="registro eliminado")
    ventana.tabla_datos.delete(elem_eliminar)

def f_actualizar(ventana):
    if ventana.nombre_texto.get()=="":
        print("no hay para actualizar")
        showerror(title="SIN DATOS",message=" no hay nada para actualizar")
    else:
        nombre=ventana.nombre_texto.get()
        apellidos=ventana.apellidos_texto.get()
        dni=ventana.celular_texto.get()
        elem_actualizar=ventana.tabla_datos.selection()
        mensaje=askyesno(title="ACTUALIZAR",message="estas seguro que deseas actualizar")
    if mensaje ==True:
        f_limpiar(ventana)
        ventana.tabla_datos.selection_remove(elem_actualizar)
        return ventana.tabla_datos.item(elem_actualizar,text=nombre,values=(apellidos,dni))
    else:
        showinfo(title="NO ACTUALIZO",message="No se actualizo ningun registro")
        f_limpiar(ventana)
        ventana.tabla_datos.selection_remove(elem_actualizar)
def f_dobleClick(ventana,event):
    elem_actualizar=ventana.tabla_datos.selection()
    captura_datos=ventana.tabla_datos.item(elem_actualizar)
    mensaje=askyesnocancel(title="ACTULAIZAR",message="desea actualizar los datos")
    if mensaje== True:
        nombre=captura_datos["text"]
        apellido=captura_datos["values"][0]
        dni=captura_datos["values"][1]
        ventana.nombre_texto.insert(0,nombre)
        ventana.apelldios_texto.insert(0,apellido)
        ventana.dni_texto.insert(0,dni)
        ventana.tabla_datos.selection_remove(elem_actualizar)
    else:
        showinfo(title="ACTUALIZAR",message="ningun registro seleccionado para actualizacion")
        ventana.tabla_datos.selection_remove(elem_actualizar)
    # print(ventana.tabla_datos.item(elem_eliminar))

