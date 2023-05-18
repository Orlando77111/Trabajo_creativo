# boton aceptar
boton_aceptar_datos_estudiante = Button(frame_datos_estudiante, text="Aceptar", command=frame_datos_estudiante)
boton_aceptar_datos_estudiante.config(font=("Arial", 10), fg="white", bg="red4")
boton_aceptar_datos_estudiante.place(x=380, y=60, width=70)

def aceptar_datos_estudiante():
    global nombre_estudiante
    global grado_estudiante
    grado_estudiante = grado_estudiante.get()
    nombre_estudiante = nombre_estudiante.get()