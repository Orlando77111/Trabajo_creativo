from tkinter import *
from tkinter import messagebox
from tkinter import ttk
global logo



def abrir_notas():
    global abrir_notas
    abrir_notas=Toplevel()

def abrir_imc():
    global abrir_imc
    abrir_imc=Toplevel()


#----------------------
#creamos la ventana tk
#----------------------

d = StringVar

ventana_principal = Tk()
ventana_principal.geometry("700x600")
ventana_principal.title("Formulario de Datos 1.0")
ventana_principal.resizable(False,False)
ventana_principal.config(bg="white")


#logo del coleguio
lg_col = PhotoImage(file="img/escudo.png")
lb_col = Label(ventana_principal, image=lg_col, bg="snow")
lb_col.place(x=50,y=20)

# :)
lb_n = Label(ventana_principal, text = "Nombre = ")
lb_n.config(bg="white", fg="red", font=("Helvetica", 18))
lb_n.place(x=180, y=60)


lb_combo_grado = ttk.Combobox(ventana_principal)
lb_combo_grado.place(x=300, y=120, width=250, height=30)
lb_combo_grado['values'] = ('6-1', '6-2', '6-3', '6-4', '6-5', '6-6', '6-7','7-1', '7-2', '7-3', '7-4', '7-5', '7-6', '7-7','8-1', '8-2', '8-3', '8-4', '8-5', '8-6', '8-7', '9-1', '9-2', '9-3', '9-4', '9-5', '9-6', '9-7','10-1', '10-2', '10-3', '10-4', '10-5', '10-6', '10-7', '11-1', '11-2', '11-3', '11-4', '11-5', '11-6', '11-7',)


lb_g = Label(ventana_principal, text= "Grado = ")
lb_g.config(bg = "white", fg = "blue", font=("Helvetica", 18))
lb_g.place(x=200, y=120)

#cajas de textos para los datos iniciales
entry_n = Entry(ventana_principal, textvariable=d)
entry_n.config(bg="white", fg="green3", font=("Times New Roman", 18), width=20)
entry_n.focus_set()
entry_n.place(x=300,y=60)

#Botones 
image_datos = PhotoImage(file="img/Datos.png")
botton_datos = Button(ventana_principal, image=image_datos, command=abrir_notas)
botton_datos.place(x=100,y=200, width=250, height=250)

image_imc = PhotoImage(file="img/Datos.png")
botton_imc = Button(ventana_principal, image=image_datos, command=abrir_imc)
botton_imc.place(x=400,y=200, width=250, height=250)




ventana_principal.mainloop()