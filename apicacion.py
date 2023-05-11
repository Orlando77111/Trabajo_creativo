from tkinter import *
from tkinter import messagebox

#----------------------
#creamos la ventana tk
#----------------------

ventana_principal = Tk()
ventana_principal.geometry("700x500")
ventana_principal.title("Formulario de Datos 1.0")
ventana_principal.resizable(False,False)
ventana_principal.config(bg="gray7")

d = StringVar()
 
#Funciones del boton datos
def abrir_toplevel_datos():
    global toplevel_datos
    toplevel_datos = Toplevel()
    toplevel_datos.title("Centigrados")
    toplevel_datos.resizable(False, False)
    toplevel_datos.geometry("300x200")
    toplevel_datos.config(bg="white")

    # etiqueta para valor en centigrados
    lb_c = Label(ventana_principal, text = "°C = ")
    lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_c.place(x=150, y=60)

    # caja de texto para valor en centigrados
    entry_c = Entry(toplevel_datos, textvariable=d)
    entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=210,y=60)

   # boton para convertir
    bt_aceptar = Button(toplevel_datos,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=100, y=150, width=100, height=30)

# aceptar
def aceptar():
    global cent
    cent = int(d.get())
    toplevel_datos.destroy()


# Titulo de la aplicacion

texto_resultados = Text(ventana_principal)
texto_resultados.config(fg="green yellow",  width=45,height=4, font=(" Proggy Fonts",18), bg="gray7")
texto_resultados.place(x=10, y=350)

#Boton para ingresar los datos
img=PhotoImage(file="img/Datos.png")
bt_datos = Button(ventana_principal,)
bt_datos.config(image=img, width=200, height=200)
bt_datos.place(x=10,y=10)


ventana_principal.mainloop()