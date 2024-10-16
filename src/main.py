from tkinter import  *
import tkinter as tk
from tkinter import messagebox
from patentes import determinar_precio_patentes, verificar_patente

def clear():
  nro_patente_var.set('')
  modelo_var.set('')
  valor_auto_var.set('')
  resultado.set('')


def determinar_precio(nro_patente, modelo, valor_auto):
    pat = nro_patente.get().upper()
    mod = modelo.get()
    valAuto = valor_auto.get()
    patente = determinar_precio_patentes(pat, mod, valAuto)
    if patente == 'Error en el numero de patente':
        messagebox.showerror('Error','Error en el numero de patente')
        clear()
    elif patente == 'Error en la fecha del modelo':
        messagebox.showerror('Error','Error en la fecha del modelo')
        clear()
    elif patente == 'Error en el valor del auto':
          messagebox.showerror('Error','Error en el valor del auto')
          clear()
    else: 
        resultado.set(patente)
        messagebox.showinfo(title= f'Patente {pat}', message = f'El precio de la patente es: $ {patente}')
        clear()
    return patente

ventana = tk.Tk()
ventana.title("Calculadora de precio de Patente")
nro_patente_var = tk.StringVar()
modelo_var = tk.StringVar()
valor_auto_var = tk.StringVar()
resultado = tk.StringVar()

# Crear la ventana
tk.Label(ventana, text="Número de Patente:").grid(row=0, column=0, padx=10, pady=10)
entry_patente = tk.Entry(ventana, textvariable=nro_patente_var)
entry_patente.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Año del Modelo:").grid(row=1, column=0, padx=10, pady=10)
entry_modelo = tk.Entry(ventana, textvariable=modelo_var)
entry_modelo.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Valor del Auto:").grid(row=2, column=0, padx=10, pady=10)
entry_valor = tk.Entry(ventana, textvariable=valor_auto_var)
entry_valor.grid(row=2, column=1, padx=10, pady=10)

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=lambda: determinar_precio(nro_patente_var, modelo_var, valor_auto_var))
boton_calcular.grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()