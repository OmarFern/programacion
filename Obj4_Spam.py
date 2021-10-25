from tkinter import *
from tkinter import messagebox as MessageBox

def obtener_usuario_claves(var_usuario,var_clave):
    
    usuarios_validos = {"Karen Lima":"1111" ,"Nicolas Galvan":"2222", 
                        "Tomas Pibernus":"3333","Javier Tineo":"4444",
                        "Omar jaldin":"5555","Walter Pascual":"7777"}
    
    if var_usuario.get() not in usuarios_validos.keys():
        mensaje = MessageBox.showerror("Atencion", "Alguno de los datos ingresados es Incorrecto") 
    elif usuarios_validos[var_usuario.get()] == var_clave.get():
        mensaje = MessageBox.showinfo("Atencion","Usuario y Clave Correctos")
    else:
        mensaje = MessageBox.showerror("Atencion", "Alguno de los datos ingresados es Incorrecto")
    return mensaje

def main():
    raiz = Tk()
    raiz.title("Login Spam")
    raiz.resizable(False,False)
    raiz.geometry("300x130")
    raiz.iconbitmap("AveFenix.ico")
    raiz.config(bg="Black")

    lienzo_0 = Frame(raiz,bg="Blue")
    lienzo_0.pack(fill = "both", expand = True)

    lienzo = Frame(lienzo_0,bg="Blue")
    lienzo.pack(fill = "both", expand = True, pady = 15)

    var_usuario = StringVar()
    var_clave = StringVar()

    usuario = Label(lienzo,text ="Usuario Alumno: ")
    usuario.grid(row = 0, column = 0, sticky = "w", padx = 10, pady = 5)

    clave = Label(lienzo,text ="Clave: ")
    clave.grid(row = 1, column = 0, sticky = "w", padx = 10, pady = 5)

    entrada_usuario = Entry(lienzo, textvariable = var_usuario)
    entrada_usuario.grid(row = 0, column = 1, padx = 10)

    entrada_clave = Entry(lienzo,show = "*", textvariable = var_clave)
    entrada_clave.grid(row = 1, column = 1, padx = 10)

    boton = Button(raiz, text="Ingresar", command = lambda : obtener_usuario_claves(var_usuario,var_clave))
    boton.pack()

    raiz.mainloop()
    
main()
