from tkinter import *
import random
import string

root = Tk()
root.title("Generador de contraseñas")
root.geometry("400x300")
root.configure(bg="wheat")

# def generar_passw():
#     ll = int(longitud_spinbox.get())
#     caracteres = string.ascii_letters + string.digits + string.punctuation
#     for i in range(ll):
#         passw = ''.join(random.choice(caracteres))
#     contraseña_respuesta.config(text=passw)


def generador():
    ll = (int(longitud_spinbox.get()))
    carac = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    for _ in range(ll):
        passw = "".join(random.choice(carac))
        contrasena_respuesta.config(text=passw)



cuadro_opciones = LabelFrame(root,
                             text="¿Qué debe contener?",
                             font=("helvetica", 14),
                             bg="wheat", fg="grey")
cuadro_opciones.pack()

cero = 0
ll = IntVar()
opcion_minuscula = BooleanVar()
opcion_mayuscula = BooleanVar()
opcion_numero = BooleanVar()
opcion_special_carac = BooleanVar()


check_minusculas = Checkbutton(cuadro_opciones,
                               text="Minúsculas",
                               bg="wheat",
                               font=("helvetica", 12),
                               width=20, anchor=W,
                               variable=opcion_minuscula)
check_minusculas.pack()
check_minusculas.select()

check_mayusculas = Checkbutton(cuadro_opciones,
                               text="Mayúsculas",
                               bg="wheat",
                               font=("helvetica", 12),
                               width=20, anchor=W,
                               variable=opcion_mayuscula)
check_mayusculas.pack()
check_mayusculas.deselect()

check_numeros = Checkbutton(cuadro_opciones,
                               text="Númeross",
                               bg="wheat",
                               font=("helvetica", 12),
                               width=20, anchor=W,
                               variable=opcion_numero)
check_numeros.pack()
check_numeros.deselect()

check_special_carac = Checkbutton(cuadro_opciones,
                               text="Caracteres especiales",
                               bg="wheat",
                               font=("helvetica", 12),
                               width=20, anchor=W,
                               variable=opcion_special_carac)
check_special_carac.pack()
check_special_carac.deselect()

cuadro_longitud = LabelFrame(root,
                             text="Longitud",
                             font=("helvetica", 14),
                             bg="wheat", fg="grey")
cuadro_longitud.pack()

longitud_label = Label(cuadro_longitud,
                       text="Longitud: ",
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
                       width=20, anchor="center")
contrasena_respuesta.pack()

boton_generar = Button(root, text="GENERAR", command=generador)
boton_generar.pack()

root.mainloop()

