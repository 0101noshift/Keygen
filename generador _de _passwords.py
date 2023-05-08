from tkinter import *
import random
import string

root = Tk()

# def generar_passw():
#     global longitud
#     caracteres = string.ascii_letters + string.digits + string.punctuation
#     passw = ''.join(random.choice(caracteres) for i in range(longitud))
#     return passw

# def actualizar_passw():
#     passw = generar_passw()
#     etiqueta_passw.config(text=passw)

longitud = Spinbox(from_=4, to=25, increment=1, state="readonly").pack()


root.title("Generador de passws")
root.geometry("200x200")
etiq_titulo = Label(root, text="Contraseña generada:")
etiq_titulo.pack()

etiqueta_passw = Label(root, text="")
etiqueta_passw.pack()

boton_generar = Button(root, text="Generar Contraseña", command=actualizar_passw)
boton_generar.pack()

root.mainloop()
