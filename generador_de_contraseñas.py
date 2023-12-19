from tkinter import *
from tkinter import messagebox
import random
import string

root = Tk()
root.title("Generador de contraseñas")
root.geometry("500x400")
root.configure(bg="wheat")

ll = IntVar()

def generador():
    if (opcion_minuscula.get() + opcion_mayuscula.get() + opcion_numero.get() + opcion_special_carac.get()) == 0:
        messagebox.showwarning(message="Debe escoger por lo menos una opción", title="Alerta")
    else:
        ll = (int(longitud_spinbox.get()))
        carac = (string.ascii_lowercase * opcion_minuscula.get()) + (string.ascii_uppercase * opcion_mayuscula.get()) + (string.digits * opcion_numero.get()) + (string.punctuation * opcion_special_carac.get())
        passw = ""
        for i in range(ll):
            passw = passw + "".join(random.choice(carac))
            contrasena_respuesta.config(text=passw)



cuadro_opciones = LabelFrame(root,
                             text="¿Qué debe contener?",
                             font=("helvetica", 14),
                             bg="wheat", fg="grey")
cuadro_opciones.pack()

opcion_minuscula = BooleanVar()
check_minusculas = Checkbutton(cuadro_opciones,
                               text="Minúsculas",
                               bg="wheat",
                               font=("helvetica", 12),
                               width=20, anchor=W,
                               onvalue=True,
                               offvalue=False,
                               variable=opcion_minuscula)
check_minusculas.pack()
check_minusculas.select()

opcion_mayuscula = BooleanVar()
check_mayusculas = Checkbutton(cuadro_opciones,
                               text="Mayúsculas",
                               bg="wheat",
                               font=("helvetica", 12),
                               width=20, anchor=W,
                               onvalue=True,
                               offvalue=False,
                               variable=opcion_mayuscula)
check_mayusculas.pack()
check_mayusculas.deselect()

opcion_numero = BooleanVar()
check_numeros = Checkbutton(cuadro_opciones,
                               text="Números",
                               bg="wheat",
                               font=("helvetica", 12),
                               width=20, anchor=W,
                               onvalue=True,
                               offvalue=False,
                               variable=opcion_numero)
check_numeros.pack()
check_numeros.deselect()

opcion_special_carac = BooleanVar()
check_special_carac = Checkbutton(cuadro_opciones,
                               text="Caracteres especiales",
                               bg="wheat",
                               font=("helvetica", 12),
                               width=20, anchor=W,
                               onvalue=True,
                               offvalue=False,
                               variable=opcion_special_carac)
check_special_carac.pack()
check_special_carac.deselect()

cuadro_longitud = LabelFrame(root,
                             text="Longitud",
                             font=("helvetica", 14),
                             bg="wheat", fg="grey")
cuadro_longitud.pack()

longitud_label = Label(cuadro_longitud,
                       text="Cantidad de caracteres: ",
                       bg="wheat",
                       font=("helvetica", 12),
                       width=20, anchor=W,)
longitud_label.pack(anchor=W)

longitud_spinbox = Spinbox(cuadro_longitud,
                           font=("Calibri", 12, "bold"),
                           from_=4, to=25,
                           increment=1,
                           textvariable=ll,
                           state="readonly",
                           width=5)
longitud_spinbox.pack(anchor=E)

contraseña_generada_label = Label(root,
                       text="Contraseña generada:",
                       bg="wheat", fg="grey",
                       font=("helvetica", 12),
                       anchor="center",).pack()

contrasena_respuesta = Label(root,
                       text=" ",
                       bg="wheat", fg="black",
                       font=("helvetica", 20),
                       width=35, anchor="center")
contrasena_respuesta.pack()

boton_generar = Button(root, text="GENERAR", command= lambda:(generador()))
boton_generar.pack()

root.mainloop()

