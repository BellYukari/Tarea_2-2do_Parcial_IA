import tkinter as tk
from tkinter import font

# Leer contenido del reporte
with open("reporte_formas.txt", "r") as archivo:
    contenido = archivo.read()

# Crear ventana
ventana = tk.Tk()
ventana.title("Reporte de Formas Detectadas")
ventana.geometry("400x300")

titulo = font.Font(family="Arial", size=16, weight="bold")
etiqueta = tk.Label(ventana, text="Reporte de Detección", font=titulo)
etiqueta.pack(pady=10)

texto = tk.Text(ventana, wrap=tk.WORD, font=("Arial", 12))
texto.insert(tk.END, contenido)
texto.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

ventana.mainloop()
