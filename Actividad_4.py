from tkinter import *
from tkinter import messagebox as MessageBox
"""  hola"""
def main():
        raiz = Tk()
        raiz.title("Login Spam")
        raiz.resizable(False,False)
        raiz.geometry("300x130")
        raiz.iconbitmap("AveFenix.ico")
        raiz.config(bg="pink")
        lienzo = Frame(bg="grey")
        lienzo.pack(fill = "both", expand = True)

        var_usuario = StringVar()
        var_clave = StringVar()

        usuario = Label(lienzo,text ="Usuario Alumno")
        usuario.grid(row= 0, column = 0, sticky = "w", padx = 10, pady = 5)

        clave = Label(lienzo,text ="Clave")
        clave.grid(row= 1, column = 0, sticky = "w", padx = 10, pady = 5)

        entrada_usuario = Entry(lienzo, textvariable = var_usuario )
        entrada_usuario.grid(row= 0, column = 1,padx = 10)

        entrada_clave = Entry(lienzo,show = "*", textvariable = var_clave)
        entrada_clave.grid(row= 1, column = 1,padx = 10)

        def obtener_usuario_claves():
            var_1 = var_usuario.get()
            var_2 = var_clave.get()
            
            usuarios_validos = {"Karen Lima":"252001" ,"Nicolas Galvan":"123456",\
                                "Tomas Pibernus":"123456","Javier Vasquez":"123456",\
                                "Omar jaldin":"123456","Walter Pascual":"123456"}
            
            if var_1 not in usuarios_validos.keys():
                MessageBox.showerror("Atencion", "Alguno de los datos ingresados es Incorrecto") 
            elif usuarios_validos[var_usuario.get()] == var_clave.get():
                MessageBox.showinfo('Atencion',"Usuario y Clave Correctos")
            else:
                MessageBox.showerror("Atencion", "Alguno de los datos ingresados es Incorrecto") 

        boton = Button(raiz, text="Ingresar", command = obtener_usuario_claves)
        boton.pack()

        raiz.mainloop()
main()        
