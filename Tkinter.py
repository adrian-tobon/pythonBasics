import backendTkinter as back
import tkinter as tk
from tkinter import ttk

def suma():
    resultado = back.suma(int(entryA.get()),int(entryB.get()))
    entryResult.insert(0,resultado)
    label.config(text="operacion exitosa")

'''def obtenerComentario():
    comentario = text.get("1.0",tk.END).strip()
    label2.config(text=f"comentario: {comentario}")


def configuracionNotificaciones():
    if optionVar == 1:
        configuracion.config(text="Activadas")
    else:
        configuracion.config(text="Desactivadas")    
 

def mostrarSeleccion():
    seleccion = lista.get(lista.curselection)
    resultado.config(text=str(seleccion))           
'''    
ventana = tk.Tk()
ventana.title("Principal")
ventana.geometry("800x600")
#ventana.resizable(False,False)
menuBar = tk.Menu()
ventana.config(menu=menuBar)

archivoMenu = tk.Menu(menuBar,tearoff=0)
editarMenu = tk.Menu(menuBar,tearoff=0)

menuBar.add_cascade(label="Archivo",menu=archivoMenu)
menuBar.add_cascade(label="Editar",menu=editarMenu)

archivoMenu.add_command(label="Nuevo",command=lambda: resultado.config(text="Nuevo Archivo"))
archivoMenu.add_command(label="Abrir",command=lambda: resultado.config(text="Abrir Archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=lambda: resultado.config(text="Salir"))

editarMenu.add_command(label="Deshacer",command=lambda: resultado.config(text="Deshacer accion"))


marco = tk.Frame(ventana,width=300,height=200,bg="lightgray", borderwidth=2,relief="solid")
label = tk.Label(marco, text="Matematicas",anchor="center",font=("Helvetica",24,"normal"))
entryA = tk.Entry(marco)
entryB = tk.Entry(marco)
entryResult = tk.Entry(marco,state="disabled")

boton = tk.Button(marco,text="Suma",command=suma,activebackground="red",activeforeground="yellow")
resultado = tk.Label(marco,bg="lightgray")

n = 0
def progreso():
    global n
    barraProgreso['value'] = n
    marco.update()
    n += 10
    '''
    for i in range(101):
        barraProgreso['value'] = i
        marco.update()
        marco.after(50)
    '''
    

barraProgreso = ttk.Progressbar(marco,mode="determinate",length=200)
botonProgreso = tk.Button(marco,text="Progreso",command=progreso,activebackground="red",activeforeground="yellow")

'''
text = tk.Text(marco, wrap="word",width=50,height=20)
boton2 = tk.Button(marco,text="Comentario",command=obtenerComentario,activebackground="red",activeforeground="yellow")
label2 = tk.Label(marco,bg="lightgray")
'''
'''
optionVar = tk.IntVar()
checkButton = tk.Checkbutton(marco, text="Desea recibir notificaciones?",variable=optionVar, onvalue=1,offvalue=0)

radioOption = tk.StringVar()
radioButton1= tk.Radiobutton(marco,text="opcion 1",variable=radioOption,value="opcion1")
radioButton2= tk.Radiobutton(marco,text="opcion 2",variable=radioOption,value="opcion2")
radioButton3= tk.Radiobutton(marco,text="opcion 3",variable=radioOption,value="opcion3")
radioButton4= tk.Radiobutton(marco,text="opcion 4",variable=radioOption,value="opcion4")
radioButton5= tk.Radiobutton(marco,text="opcion 5",variable=radioOption,value="opcion5")


valorVar = tk.IntVar()
escala = tk.Scale(marco,from_=0,to=100,orient=tk.HORIZONTAL,variable=valorVar)

lista = tk.Listbox(marco, selectmode=tk.SINGLE)
opciones = ["Azul", "Rojo", "Negro", "Amarillo"]
for opcion in opciones:
    lista.insert(tk.END,opcion)

resultado = tk.Label(marco,bg="lightgray")
'''

marco.pack(pady=10,padx=10,fill=tk.BOTH, expand=True)
label.pack(side="top")
entryA.pack()
entryB.pack()
entryResult.pack()
boton.pack(side="bottom")
#escala.pack()
#lista.pack()
resultado.pack()
barraProgreso.pack()
botonProgreso.pack()
'''
checkButton.pack()
radioButton1.pack()
radioButton2.pack()
radioButton3.pack()
radioButton4.pack()
radioButton5.pack()


text.pack(pady=2,padx=2)
boton2.pack()
label2.pack()
'''
ventana.mainloop()








