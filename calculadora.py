from tkinter import *

ventana = Tk()
ventana.title("calculadora")

i = 0
base_numerica = 10 #Inicialmente, la base es decimal

#entrada
e_texto = Entry(ventana, font = ("slant 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady=5)
ventana.configure(background='pink')



#Funciones
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1
    
def borrar():
    e_texto.delete(0, END)
    i = 0
    
def hacer_operacion():
    ecuacion = e_texto.get()
    resultado = ""
    try:
        if base_numerica == 10:
            resultado = str(eval(ecuacion))
        elif base_numerica == 2:
            resultado = bin(eval(ecuacion))[2:]
        elif base_numerica == 16:
            resultado = hex(eval(ecuacion))[2:]
        borrar()
        e_texto.insert(0, resultado)
    except Exception as e:
        borrar()
        e_texto.insert(0, "Error")
    
def BACK(): 
    global i 
    i = i-1
    e_texto.delete(i, END)
    
def cambiar_base(base):
    global base_numerica
    base_numerica = base
    borrar()
    
def switchButtonState():
    if (boton_ON['text'] == 'ON'):
     boton_ON ['text'] = 'OFF'
    else:
        boton_ON ['text'] = 'ON' 
    
    if (boton1 ['state'] == NORMAL ):
        boton1['state'] = DISABLED
    
    else: 
        boton1['state']= NORMAL     
        
    if (boton2 ['state'] == NORMAL ):
        boton2['state'] = DISABLED
    
    else: 
        boton2['state']= NORMAL  
        
    if (boton3 ['state'] == NORMAL ):
        boton3['state'] = DISABLED
    
    else: 
        boton3['state']= NORMAL  
        
    if (boton4 ['state'] == NORMAL ):
        boton4['state'] = DISABLED
        
    else: 
        boton4['state']= NORMAL  
        
        
#Botones
boton_ON = Button(ventana, text = "ON", width = 7, height = 5,  command = lambda: switchButtonState(), background= 'medium violet red')

boton1 = Button(ventana, text = "1", width = 7, height = 5, state= NORMAL, command = lambda: click_boton(1), background= 'medium orchid')
boton2 = Button(ventana, text = "2", width = 7, height = 5, state= NORMAL, command = lambda: click_boton(2), background= 'medium orchid')
boton3 = Button(ventana, text = "3", width = 7, height = 5, state= NORMAL, command = lambda: click_boton(3), background= 'medium orchid')
boton4 = Button(ventana, text = "4", width = 7, height = 5, state= NORMAL, command = lambda: click_boton(4), background= 'medium purple')
boton5 = Button(ventana, text = "5", width = 7, height = 5, command = lambda: click_boton(5), background= 'medium purple')
boton6 = Button(ventana, text = "6", width = 7, height = 5, command = lambda: click_boton(6), background= 'medium purple')
boton7 = Button(ventana, text = "7", width = 7, height = 5, command = lambda: click_boton(7), background= 'medium orchid')
boton8 = Button(ventana, text = "8", width = 7, height = 5, command = lambda: click_boton(8), background= 'medium orchid')
boton9 = Button(ventana, text = "9", width = 7, height = 5, command = lambda: click_boton(9), background= 'medium orchid')
boton0 = Button(ventana, text = "0", width = 13, height = 4, command = lambda: click_boton(0), background= 'medium purple')

boton_borrar = Button(ventana, text = "AC", width = 7, height = 5,command = lambda: borrar(), background= 'medium violet red')
boton_parentesis1 = Button(ventana, text = "(", width = 7, height = 5,command = lambda: click_boton("("), background= 'medium purple')
boton_parentesis2 = Button(ventana, text = ")", width = 7, height = 5, command = lambda: click_boton(")"), background= 'medium purple')
boton_punto = Button(ventana, text = ".", width = 7, height = 4,command = lambda: click_boton("."), background= 'medium purple')

boton_div = Button(ventana, text = "/", width = 7, height = 5,command = lambda: click_boton("/"), background= 'medium orchid')
boton_mult = Button(ventana, text = "x", width = 7, height = 5,command = lambda: click_boton("*"), background= 'medium orchid')
boton_sum = Button(ventana, text = "+", width = 7, height = 5,command = lambda: click_boton("+"), background= 'medium orchid')
boton_rest = Button(ventana, text = "-", width = 7, height = 5,command = lambda: click_boton("-"), background= 'medium orchid')
boton_igual = Button(ventana, text = "=", width = 7, height = 4,command = lambda: hacer_operacion(), background= 'medium violet red')

boton_Decimal = Button(ventana, text = "Dec", width = 7, height = 5, command = lambda: cambiar_base(10), background= 'medium purple') 
boton_Binario = Button(ventana, text = "Bin", width = 7, height = 5, command = lambda: cambiar_base(2), background= 'medium purple')
boton_Hexa = Button(ventana, text = "Hexa", width = 7, height = 5,command = lambda: cambiar_base(16), background= 'medium purple') 
boton_back = Button(ventana, text = "<-", width = 7, height = 4,command = lambda: BACK(),background= 'medium violet red')

#agregar  botones en pantalla
boton_borrar.grid(row = 1, column= 0, padx= 5, pady = 5)
boton_parentesis1.grid(row = 1, column= 1, padx= 5, pady = 5)
boton_parentesis2.grid(row = 1, column= 2, padx= 5, pady = 5)
boton_div.grid(row = 1, column= 3, padx= 5, pady = 5)
boton_ON.grid(row = 1, column= 4, padx= 5, pady = 5)

boton7.grid(row = 2, column= 0, padx= 5, pady = 5)
boton8.grid(row = 2, column= 1, padx= 5, pady = 5)
boton9.grid(row = 2, column= 2, padx= 5, pady = 5)
boton_mult.grid(row = 2, column= 3, padx= 5, pady = 5)
boton_Decimal.grid(row = 2, column= 4, padx= 5, pady = 5)


boton4.grid(row = 3, column= 0, padx= 5, pady = 5)
boton5.grid(row = 3, column= 1, padx= 5, pady = 5)
boton6.grid(row = 3, column= 2, padx= 5, pady = 5)
boton_sum.grid(row = 3, column= 3, padx= 5, pady = 5)
boton_Binario.grid(row = 3, column= 4, padx= 5, pady = 5)

boton1.grid(row = 4, column= 0, padx= 5, pady = 5)
boton2.grid(row = 4, column= 1, padx= 5, pady = 5)
boton3.grid(row = 4, column= 2, padx= 5, pady = 5)
boton_rest.grid(row = 4, column= 3, padx= 5, pady = 5)
boton_Hexa.grid(row = 4, column= 4, padx= 5, pady = 5)

boton0.grid(row = 5, column= 0,columnspan = 2, padx= 5, pady = 5)
boton_punto.grid(row = 5, column= 2, padx= 5, pady = 5)
boton_igual.grid(row = 5, column= 3, padx= 5, pady = 5)
boton_back.grid(row = 5, column= 4, padx= 5, pady = 5)


ventana.mainloop()

