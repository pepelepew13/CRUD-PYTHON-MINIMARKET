import datetime
import time
from tkinter import messagebox as messagebox
from tkinter import *
from tkinter import ttk as ttk
from tkinter.simpledialog import *


productos=[[120, "Huevo", 1000],[112, "Harina", 4000],[212, "Panela", 2000],[902, "Café", 3000],[403, "Sal", 1000],[402, "Arroz", 2000],[202, "Salsa", 4000]]
users=[["Maria Paz", 103546378],["Juana Lu", 104746372],["Mía", 102596378],["Manuel", 103873278],["Pablo", 107546342],["Samuel", 102546354],["Sonia", 101246438],["Maria", 101246438]]
ganancias = []
perdidas = []
pag_prin = Tk()
ventafac = []

def pagprin():
    
    mainframe= Frame(pag_prin)
    mainframe.pack()
    mainframe.config(width=460,height=460,bg="#B9B8FA")
    
    pag_prin.title("PÁGINA PRINCIPAL")
    pag_prin.geometry("1422x734")
    pag_prin.configure(bg='#B9B8FA')

    lblin = Label(pag_prin,text="¡BIENVENIDO!", fg="#5E0098", bg="#B9B8FA", font=("Book Antiqua",80,"bold"))
    lblin.place(x=330, y =120)
    btnventa=Button(pag_prin,text="VENTA DE\nPRODUCTOS", fg="#5E0098", bg="white", font=("Book Antiqua",30),activebackground="#5E0098",activeforeground="white", command = ventaprod).place(x=350, y=350)
    btnsur=Button(pag_prin,text="‎ ‏‏‏ ‏‏‎ ‏‏‎‎‏‏‎‎‎‎ ‏‏‎‎‏‏‎‎‏‏‎‏SURTIR‏‏‎  ‏‏‎ ‏‏ ‏‏‎‎‏‏‎‎‏\n‎‏‏‎‎‏‏‎‎ ‏‏‎‎ ‏‏‎‎ ‏‏‎‎ ‏‏‎‎‏‏‎‎ ‏‏‎‏‏TIENDA‎‏‏‎‎‏‏‎‎‏‏‎‎ ‏‏‎ ‏‏‎‎ ‏‏‎ ‏‏‎ ‏‎‎‏‏‎‎", fg="#5E0098", bg="white", font=("Book Antiqua",30),activebackground="#5E0098",activeforeground="white", command = surtir_tienda).place(x=800, y=350)
    btninve=Button(pag_prin,text="INVENTARIO\nGANANCIAS", fg="#5E0098", bg="white", font=("Book Antiqua",29),activebackground="#5E0098",activeforeground="white", command = inventario_tienda).place(x=350, y=520)
    btnregistr=Button(pag_prin,text="‎ ‏‏‏‏‏ REGISTRAR‏‏‎ ‏‏‎‎\n‎‏‏‎‎‏‏‎‎ ‏‏‎‎‏‏‎‎ USUARIO ‏‏‎‏‎‏‏‎ ‏‏‎‏‎‎‏‏‎", fg="#5E0098", bg="white", font=("Book Antiqua",30),activebackground="#5E0098",activeforeground="white", command=regusu).place(x=800, y=520)
    
    pag_prin.mainloop()

def ventaprod():
    
    pag_prin.withdraw()
    global venta
    venta = Toplevel()
    global mainframe2
    mainframe2= Frame(venta)
    mainframe2.pack(ipadx = 50,ipady=30, side=LEFT,padx = 50)
    mainframe2.config(width=460,height=460,bg="#9D9BAC")
    
    mainframev= Frame(venta)
    mainframev.pack(ipadx = 10 ,padx = 80,ipady =10, side=LEFT)
    mainframev.config(width=460,height=460,bg="#9D9BAC")
    
    venta.title("VENTA DE PRODUCTOS")
    venta.geometry("1422x734")
    venta.configure(bg='#B9B8FA')

    #fondo=PhotoImage(file="fondoventa.gif")
    #lblFondo=Label(venta,image=fondo)
    #lblFondo.place(x=0,y=0)
    titulo= Label(venta,text="VENDER PRODUCTOS",font=("Book Antiqua",30),bg="#B9B8FA", fg="#5E0098").place(x=500, y=10)

    volver=Button(venta,text="Volver", fg="#5E0098", bg="white", font=("Book Antiqua",12),activebackground="#5E0098",activeforeground="white", command=cerrarvent).place(x=1000, y=10)

    titulo= Label(mainframe2,text="Cédula del comprador:",font=("Book Antiqua",17),bg="#9D9BAC", fg="#000000")
    titulo.grid(column=0,row=1, pady=2, padx=10)
    
    global cedula
    
    cedula = StringVar()
    
    cedula= Entry(mainframe2, textvariable=cedula)
    cedula.grid(column=1,row=1)
    
    titulo2= Label(mainframe2,text="LISTA DE COMPRA",font=("Book Antiqua",20),bg="#9D9BAC", fg="#5E0098")
    titulo2.grid(column=1,row=0,pady=10)

    titulo2= Label(mainframev,text="PRODUCTOS DE LA TIENDA",font=("Book Antiqua",20),bg="#9D9BAC", fg="#5E0098")
    titulo2.grid(column=0,row=0,padx = 10,pady =10)
    
    titulo3= Label(mainframev,text="{:<11} {:<9} {:<15} {:<10}".format('Indice','Codigo','Nombre','Precio'),font=("Book Antiqua",13),bg="#9D9BAC", fg="#000000")
    titulo3.grid(column=0,row=1)

    btncom=Button(venta,text="‎Agregar‏‎‎‏‏‎‎", fg="#5E0098", bg="white", font=("Book Antiqua",20),activebackground="#5E0098",activeforeground="white", command=agcompra)
    btncom.place(x=500, y=600)
    
    for i in range (len(productos)):
        global producto
        producto= Button(mainframev, text="{:<14}\t{:<9}\t{:<15}\t{:<10}".format(i+1, productos[i][0], productos[i][1], productos[i][2]), fg="#000000", bg="white", font=("Book Antiqua",12),activebackground="#5E0098",activeforeground="white", command=producven)
        producto.grid(column=0,row=i+2,columnspan=2, pady=5, padx = 10)
    global facturar
    facturar=Button(venta,text="Facturar", fg="#5E0098", bg="white", font=("Book Antiqua",20),activebackground="#5E0098",activeforeground="white", command=factura_tienda, state= "disabled")
    facturar.place(x=700, y=600)

def agcompra():
    
    facturar.configure(state="normal")
    elemento1=askinteger('AGREGAR: ', 'Ingrese el índice del producto a agregar: ')
    for i in range (len(productos)):
        if elemento1 ==  i+1:
            messagebox.showinfo("Bien",f"Producto {productos[i]} agregado a la compra")
            ventafac.append(productos[i])
            printeo()
            
def printeo():
    global identificador
    identificador = cedula.get()
    global suma
    suma=0
    for i in range (len(ventafac)):
        suma=suma+int(ventafac[i][2])
        ventafacs= Label(mainframe2,text="{:<9} {:<15} {:<10} ".format(ventafac[i][0], ventafac[i][1], ventafac[i][2]), fg="black",bg='#B9B8FA', font=("Book Antiqua",15))
        ventafacs.grid(column=0,row=i+2,padx=100,pady=5,columnspan=2)
    ventasub= Label(mainframe2,text=f"Subtotal: {suma}", fg="#5E0098",bg='#B9B8FA', font=("Book Antiqua",12))
    ventasub.grid(column=0,row=i+3,padx=100,pady=5,columnspan=2)

def surtir_tienda():
    
    pag_prin.withdraw()
    global surtir
    surtir = Toplevel()
    global mainframe5
    mainframe5= Frame(surtir)
    mainframe5.pack(ipadx = 50 ,padx = 100, side=LEFT)
    mainframe5.config(width=460,height=460,bg="#9D9BAC")
    
    mainframer= Frame(surtir)
    mainframer.pack(padx = 30,side=LEFT)
    mainframer.config(width=460,height=460,bg="#9D9BAC")
    
    surtir.title("SURTIR TIENDA")
    surtir.geometry("1422x734")
    surtir.configure(bg='#B9B8FA')

    #fondo=PhotoImage(file="fondoventa.gif")
    #lblFondo=Label(venta,image=fondo)
    #lblFondo.place(x=0,y=0)
    

    volver=Button(surtir,text="Volver", fg="#5E0098", bg="white", font=("Book Antiqua",12),activebackground="#5E0098",activeforeground="white", command=cerrarsurtir).place(x=1000, y=10)

    titulo= Label(mainframe5,text="SURTIR LA TIENDA",font=("Book Antiqua",30),bg="#9D9BAC", fg="#5E0098", padx = 10, pady=10)
    titulo.grid(column=1,row=2)

    titulo= Label(mainframe5,text="Codigo:",font=("Book Antiqua",20),bg="#9D9BAC", fg="#5E0098", padx = 10, pady=10)
    titulo.grid(column=0,row=4)

    global codigo
    
    codigo = StringVar()
    codigo= Entry(mainframe5, textvariable=codigo)
    codigo.grid(column=1,row=4, pady=20, padx=20,ipadx = 40, ipady =3)
    
    titulo= Label(mainframe5,text="Producto:",font=("Book Antiqua",20),bg="#9D9BAC", fg="#5E0098", padx = 10, pady=10)
    titulo.grid(column=0,row=5)

    global producto_sr
    
    producto_sr = StringVar()
    producto_sr = Entry(mainframe5, textvariable=producto_sr)
    producto_sr.grid(column=1,row=5, pady=20, padx=10,ipadx = 40, ipady =3)
    
    titulo= Label(mainframe5,text="Precio:",font=("Book Antiqua",20),bg="#9D9BAC", fg="#5E0098", padx = 10, pady=10)
    titulo.grid(column=0,row=6)
    
    global precio
    
    precio = StringVar()
    precio= Entry(mainframe5, textvariable=precio)
    precio.grid(column=1,row=6, pady=20, padx=10,ipadx = 40, ipady =3)
    
    titulo2= Label(mainframe5,text="Unidades:",font=("Book Antiqua",20),bg="#9D9BAC", fg="#5E0098", padx = 10, pady=10)
    titulo2.grid(column=0,row=7)

    global unidad
    
    unidad = StringVar()
    unidad = Entry(mainframe5, textvariable=unidad )
    unidad.grid(column=1,row=7, pady=20, padx=10,ipadx = 40, ipady =3)

    titulo4= Label(mainframer,text="Productos en la tienda",font=("Book Antiqua",17),bg="#9D9BAC", fg="#5E0098", padx = 10, pady=10)
    titulo4.grid(column=2,row=4, pady=10, ipadx = 20)
    titulo3= Label(mainframer,text="{:<9}\t{:<15}\t{:<10}".format('Codigo','Nombre','Precio'),font=("Book Antiqua",13),bg="#9D9BAC", fg="#5E0098", padx = 10, pady=10)
    titulo3.grid(column=2,row=5, pady=10, ipadx = 20)
    
    for i in range (len(productos)):
        producto= Button(mainframer, text="{:<9}\t{:<15}\t{:<10}".format(productos[i][0], productos[i][1], productos[i][2]), fg="#5E0098", bg="white", font=("Book Antiqua",12),activebackground="#5E0098",activeforeground="white")
        producto.grid(column=2,row=i+6, pady=10, ipadx = 20)
    surti2=Button(mainframe5,text="Surtir", fg="#5E0098", bg="white", font=("Book Antiqua",15),activebackground="#5E0098",activeforeground="white", command=agregarprod)
    surti2.grid(column=1,row=i+20, pady=10, ipadx = 20)

def agregarprod():
    
    cod = codigo.get()
    prod = producto_sr.get()
    prec = precio.get()
    unid = unidad.get()
    total = int (prec)* int (unid)

    if cod!="" and prod!="" and prec!="" :
        productos.append([cod,prod,prec])
        perdidas.append(total)
        messagebox.showinfo("Correcto",f"Se realizo el registro de {prod} con exito")
        
    else:
        messagebox.showerror("Error","No puede registrarse sin llenar todos los campos")
    actuasurtir()

def inventario_tienda():
    ganan = (sum(ganancias)-sum(perdidas))
    
    pag_prin.withdraw()
    global inventario
    ahora = time.strftime("%x")
    inventario = Toplevel()
    global mainframe6
    mainframe6= Frame(inventario)
    mainframe6.pack(side =LEFT,padx = 150, ipady = 40)
    mainframe6.config(width=460,height=460,bg="#9D9BAC")
    
    mainframet= Frame(inventario)
    mainframet.pack(side =LEFT,padx = 50, ipady = 40)
    mainframet.config(width=460,height=460,bg="#9D9BAC")
    
    inventario.title("SURTIR TIENDA")
    inventario.geometry("1422x734")
    inventario.configure(bg='#B9B8FA')

    #fondo=PhotoImage(file="fondoventa.gif")
    #lblFondo=Label(venta,image=fondo)
    #lblFondo.place(x=0,y=0)
    

    volver=Button(inventario,text="Volver", fg="#5E0098", bg="white", font=("Book Antiqua",12),activebackground="#5E0098",activeforeground="white", command=cerrarin).place(x=1000, y=10)

    titulo= Label(inventario,text="INVENTARIO",font=("Book Antiqua",30),bg="#B9B8FA", fg="#5E0098")
    titulo.place(x=600,y=10)

    titulo4= Label(mainframe6,text="Productos en la tienda",font=("Book Antiqua",17),bg="#9D9BAC", fg="#5E0098")
    titulo4.grid(column=0,row=4, padx=50,pady =30)
    
    titulo3= Label(mainframe6,text="{:<9}\t{:<15}\t{:<10}".format('Codigo','Nombre','Precio'),font=("Book Antiqua",13),bg="#9D9BAC", fg="#5E0098")
    titulo3.grid(column=0,row=7)
    
    for i in range (len(productos)):
        producto= Button(mainframe6, text="{:<9}\t{:<15}\t{:<10}".format(productos[i][0], productos[i][1], productos[i][2]), fg="#5E0098", bg="white", font=("Book Antiqua",12),activebackground="#5E0098",activeforeground="white")
        producto.grid(column=0,row=i+8,columnspan=2, pady=5)

    titulo4= Label(mainframet,text="Historial ventas y compras:",font=("Book Antiqua",17),bg="#9D9BAC", fg="#5E0098")
    titulo4.grid(column=0,row=0, padx=50,pady =30)
    for i in range (len(perdidas)):
        perdida= Button(mainframet, text="{:<9}\t-{:<15}".format(ahora,perdidas[i]), fg="#5E0098", bg="white", font=("Book Antiqua",12),activebackground="#5E0098",activeforeground="white")
        perdida.grid(column=0,row=i+1,columnspan=2, pady=5)
    for i in range (len(ganancias)):
        gananci= Button(mainframet, text="{:<9}\t+{:<15}".format(ahora,ganancias[i]), fg="#5E0098", bg="white", font=("Book Antiqua",12),activebackground="#5E0098",activeforeground="white")
        gananci.grid(column=0,row=i+2,columnspan=2, pady=5)

    titulog= Label(mainframet,text=f"Ganancias: {ganan}",font=("Book Antiqua",17),bg="#9D9BAC", fg="#5E0098")
    titulog.grid(column=0,row=i+3, padx=50,pady =30)
    
def factura_tienda():
    cerrarvent()
    pag_prin.withdraw()
    ahora = time.strftime("%x")
    global factura
    factura = Toplevel()
    global mainframe7
    mainframe7= Frame(factura)
    mainframe7.pack(pady = 5)
    mainframe7.config(width=460,height=460,bg="#9D9BAC")
    
    factura.title("FACTURA")
    factura.geometry("1422x734")
    factura.configure(bg='#B9B8FA')

    volver=Button(factura,text="Volver", fg="#5E0098", bg="white", font=("Book Antiqua",15),activebackground="#5E0098",activeforeground="white", command=cerrarfactura).place(x=1000, y=10)

    titulo1= Label(mainframe7,text="FACTURA MINIMARKET",font=("Book Antiqua",30), fg="#5E0098",bg="#9D9BAC")
    titulo1.grid(column=1,row=2,padx = 20, pady = 30)
    titulo3= Label(mainframe7,text="Distribuidora MiniMarket",font=("Book Antiqua",12), fg="#000000",bg="#9D9BAC")
    titulo3.grid(column=1,row=3, padx = 80)
    titulo4= Label(mainframe7,text=f"Identificación comprador: {identificador}",font=("Book Antiqua",15), fg="#000000",bg="#9D9BAC")
    titulo4.grid(column=1,row=6,padx = 20, pady = 10)
    titulo4= Label(mainframe7,text=f"Fecha: {ahora}",font=("Book Antiqua",15), fg="#000000",bg="#9D9BAC")
    titulo4.grid(column=1,row=5,padx = 20, pady = 10)
    titulo2= Label(mainframe7,text="Productos comprados:",font=("Book Antiqua",15), fg="#000000",bg="#9D9BAC")
    titulo2.grid(column=1,row=7,padx = 20, pady = 10)
    
    for i in range (len(ventafac)):
        fac= Button(mainframe7, text="{:<15}\t{:<10}".format(ventafac[i][1], ventafac[i][2]), fg="#5E0098", bg="white", font=("Book Antiqua",12),activebackground="#5E0098",activeforeground="white")
        fac.grid(column=1,row=i+8,columnspan=2, pady=5, ipadx = 80)
    labeltotal = Label(mainframe7,text=f"Total: {suma}",font=("Book Antiqua",13), fg="#FFFFFF",bg="#5E0098")
    labeltotal.grid(column=1,row=i+9,padx = 20, pady = 40, ipadx = 40, ipady = 2)
    ventafac.clear()
    ganancias.append(suma)

    
        
def mostrar():
    
        pag_prin.deiconify()

def producven():
        titulo2= Label(venta,text="HOLAAA",font=("Book Antiqua",37),bg="#B9B8FA", fg="#5E0098")

#Habilitar el boton de facturar
def habilitar():
    facturar.configure(state="normal")

def regusu():
    pag_prin.withdraw()
    global reg_usu
    reg_usu= Tk()
    mainframe3= Frame(reg_usu)
    mainframe3.pack(padx=80, pady = 50)
    mainframe3.config(width=460,height=460,bg="#9D9BAC")
    reg_usu.title("REGISTRO DE USUARIO")
    reg_usu.geometry("1422x734")
    reg_usu.configure(bg='#B9B8FA')

    titulo= Label(mainframe3,text="REGISTRO DE USUARIO",fg="#5E0098", bg="#9D9BAC", font=("Book Antiqua",40))
    titulo.grid(column=0,row=1,padx=200,pady=20,columnspan=2)

    btncanc=Button(mainframe3,text="‎Ver usuarios‏‎‎‏‏‎‎", fg="#5E0098", bg="white", font=("Book Antiqua",20),activebackground="#5E0098",activeforeground="white", command=listusu)
    btncanc.grid(column=1,row=0,padx=10,pady=10)

    userlabel= Label(mainframe3, text="Nombre: ",bg="#9D9BAC",fg="#5E0098", font=("Book Antiqua",18))
    userlabel.grid(column=0,row=3,padx=60,pady=10,columnspan=2)
    
    contralabel= Label(mainframe3, text="Cédula: ",bg="#9D9BAC",fg="#5E0098", font=("Book Antiqua",18))
    contralabel.grid(column=0,row=6,padx=60,pady=10,columnspan=2)
    
    global nomUsuario
    global cedUsuario
    
    nomUsuario=StringVar()
    cedUsuario=StringVar()
    
    nomUsuario= Entry(mainframe3, width=80, textvariable=nomUsuario)
    nomUsuario.grid(column=0,row=4,padx=200,pady=20,columnspan=2,ipady=5)

    
    cedUsuario= Entry(mainframe3,width=80,textvariable=cedUsuario)
    cedUsuario.grid(column=0,row=7,padx=200,pady=20,columnspan=2,ipady=5)

    btnreg=Button(mainframe3,text="‎Registrar‏‎‎‏‏‎‎", fg="#5E0098", bg="white", font=("Book Antiqua",22),activebackground="#5E0098",activeforeground="white", command=regisesion)
    btnreg.grid(column=0,row=9,padx=200,pady=20,columnspan=2)
    btncanc=Button(mainframe3,text="‎Cancelar‏‎‎‏‏‎‎", fg="#5E0098", bg="white", font=("Book Antiqua",22),activebackground="#5E0098",activeforeground="white", command=cerreg)
    btncanc.grid(column=1,row=9,padx=200,pady=20,columnspan=2)

    reg_usu.mainloop()

def listusu():
    reg_usu.withdraw()
    pag_prin.withdraw()
    global listausu
    listausu = Toplevel()
    global mainframe4
    listausu.geometry("1422x734")
    listausu.configure(bg='#B9B8FA')
    mainframe4= Frame(listausu)
    mainframe4.pack(padx=80, pady = 45)
    mainframe4.config(width=460,height=460,bg="#9D9BAC")
    
    listausu.title("LISTADO DE USUARIOS")
    listausu.configure(bg='#B9B8FA')
    volvers=Button(listausu,text="Volver", fg="#5E0098", bg="white", font=("Book Antiqua",13),activebackground="#5E0098",activeforeground="white", command=cerlist).place(x=1060, y=10)
    titulo= Label(mainframe4,text="LISTADO DE USUARIOS",fg="#5E0098", bg="#9D9BAC", font=("Book Antiqua",40))
    titulo.grid(column=0,row=1,padx=200,pady=20,columnspan=2)
    #fondo=PhotoImage(file="fondoventa.gif")
    #lblFondo=Label(venta,image=fondo)
    #lblFondo.place(x=0,y=0)
    btnel=Button(mainframe4,text="‎Eliminar‏‎‎‏‏‎‎", fg="#5E0098", bg="white", font=("Book Antiqua",15),activebackground="#5E0098",activeforeground="white", command=eliminar)
    btnel.grid(column=0,row=(len(users))+20,padx=200,pady=30,columnspan=2)
    global userlabels 
    for i in range (len(users)):
        userlabels= Label(mainframe4,text="{:<9}\t{:<15}\t{:<10}".format(i+1, users[i][0], users[i][1]), fg="#5E0098", bg="white", font=("Book Antiqua",15))
        userlabels.grid(column=0,row=i+6,padx=200,pady=5,columnspan=2,ipadx=100)
        
    
def regisesion():
    nombre= nomUsuario.get()
    passwd = cedUsuario.get()
    if nomUsuario.get()!="" and cedUsuario.get()!="":
        users.append([nombre,passwd])
        messagebox.showinfo("Correcto",f"Se realizo el registro de {nombre} con exito")
    else:
        messagebox.showerror("Error","No puede registrarse sin llenar todos los campos")
    cerrarregis()
    
    
def eliminar():
    elemento=askinteger('ELIMINAR: ', 'Ingrese el indice del elemento que desea eliminar: ')
    for i in range (len(users)):
        if elemento == i+1:
            messagebox.showinfo("Bien",f"Usuario {users[i]} eliminado con éxito")
            users.remove(users[i])
            userlabels.configure(text="{:<9} {:<15} {:<10}".format(i, users[i][0], users[i][1]))
            cerrarlist()

def cerrarregis():
    reg_usu.destroy()
    regusu()
    
def cerreg():
    reg_usu.destroy()
    mostrar()
    
def cerrarlist():
    listausu.destroy()
    listusu()

def cerlist():
    listausu.destroy()
    reg_usu.deiconify()
    
def cerrarsurtir():
    surtir.destroy()
    mostrar()

def actuasurtir():
    surtir.destroy()
    surtir_tienda()

def cerrarfactura():
    factura.destroy()
    mostrar()

def cerrarvent():
    venta.destroy()
    mostrar()

def cerrarin():
    inventario.destroy()
    mostrar()
    
if __name__=="__main__":
    pagprin()


