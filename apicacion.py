from tkinter import *
from tkinter import messagebox
from tkinter import ttk
global logo



def abrir_notas():
    global abrir_notas
    abrir_notas=Toplevel()

    #Frame blanco
    frame_entrada = Frame(abrir_notas)
    frame_entrada.config(bg = "white", width=380, height=480)
    frame_entrada.place(x=10, y=10)

    entry_n1 = Entry(abrir_notas, textvariable=d)
    entry_n1.config(bg="white", fg="green3", font=("Times New Roman", 18), width=10)
    entry_n1.focus_set()
    entry_n1.place(x=250,y=100)

    text_1 = Label(abrir_notas, text= "Procedimental = ")
    text_1.config(bg="white", fg="red", font=("Helvetica", 18))
    text_1.place(x=50, y=100)

    entry_n2 = Entry(abrir_notas, textvariable=d)
    entry_n2.config(bg="white", fg="green3", font=("Times New Roman", 18), width=10)
    entry_n2.focus_set()
    entry_n2.place(x=250,y=150)

    text_2 = Label(abrir_notas, text= "Cognitivo = ")
    text_2.config(bg="white", fg="yellow", font=("Helvetica", 18))
    text_2.place(x=50, y=150)

    entry_n3 = Entry(abrir_notas, textvariable=d)
    entry_n3.config(bg="white", fg="green3", font=("Times New Roman", 18), width=10)
    entry_n3.focus_set()
    entry_n3.place(x=250,y=200)

    text_3 = Label(abrir_notas, text= "Actitudinal = ")
    text_3.config(bg="white", fg="green2", font=("Helvetica", 18))
    text_3.place(x=50, y=200)

    entry_n4 = Entry(abrir_notas, textvariable=d)
    entry_n4.config(bg="white", fg="green3", font=("Times New Roman", 18), width=10)
    entry_n4.focus_set()
    entry_n4.place(x=250,y=250)

    text_4 = Label(abrir_notas, text= "Autoevaluacion = ")
    text_4.config(bg="white", fg="blue", font=("Helvetica", 18))
    text_4.place(x=50, y=250)

    entry_n5 = Entry(abrir_notas, textvariable=d)
    entry_n5.config(bg="white", fg="green3", font=("Times New Roman", 18), width=10)
    entry_n5.focus_set()
    entry_n5.place(x=250,y=300)

    text_5 = Label(abrir_notas, text= "Bimestral = ")
    text_5.config(bg="white", fg="maroon", font=("Helvetica", 18))
    text_5.place(x=50, y=300)

    text_6 = Label(abrir_notas, text= "Materia = ")
    text_6.config(bg="white", fg="black", font=("Helvetica", 18))
    text_6.place(x=50, y=50)

    combo_1 = ttk.Combobox(abrir_notas)
    combo_1.place(x=250,y=50, width=130, height=30)
    combo_1 ['values'] = ('Matematicas', 'Ciencias Naturales', 'Edu.Fisica', 'Valores', 'Geometria', 'Español', 'Ingles', 'Sociales')

    
    def calcular():
        pass
    
    bt_notas = Button(abrir_notas, text = "Calcular")
    bt_notas.place(x=180,y=380)

    abrir_notas.geometry("400x500")
    abrir_notas.title("Notas")
    abrir_notas.resizable(False,False)
    abrir_notas.config(bg="blue")
    
    

def abrir_imc():
    global abrir_imc
    abrir_imc=Toplevel()
    abrir_imc.geometry("400x500")
    abrir_imc.title("IMC")
    abrir_imc.resizable(False,False)
    abrir_imc.config(bg="red")


    frame_entrada = Frame(abrir_imc)
    frame_entrada.config(bg = "white", width=380, height=480)
    frame_entrada.place(x=10, y=10)





#Frame blanco


#----------------------
#creamos la ventana tk
#----------------------

d = StringVar

ventana_principal = Tk()
ventana_principal.geometry("700x600")
ventana_principal.title("1.0")
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

image_imc = PhotoImage(file="img/salud.png")
botton_imc = Button(ventana_principal, image=image_imc, command=abrir_imc)
botton_imc.place(x=400,y=200, width=250, height=250)




ventana_principal.mainloop()