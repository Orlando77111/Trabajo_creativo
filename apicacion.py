from tkinter import *
from tkinter import messagebox
from tkinter import ttk
global logo

#----------------------
#creamos la ventana tk
#----------------------

d = StringVar

ventana_principal = Tk()
ventana_principal.geometry("700x600")
ventana_principal.title("Formulario de Datos 1.0")
ventana_principal.resizable(False,False)
ventana_principal.config(bg="snow")


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

lb_g = Label(ventana_principal, text= "Grado = ")
lb_g.config(bg = "white", fg = "blue", font=("Helvetica", 18))

#cajas de textos para los datos iniciales
entry_n = Entry(ventana_principal, textvariable=d)
entry_n.config(bg="white", fg="blue", font=("Times New Roman", 18), width=20)
entry_n.focus_set()
entry_n.place(x=300,y=60)



ventana_principal.mainloop()