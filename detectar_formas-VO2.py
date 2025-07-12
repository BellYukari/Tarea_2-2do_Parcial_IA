import cv2
import numpy as np
import openpyxl  # Para crear el archivo Excel

# Cargar imagen
imagen = cv2.imread("formas.jpg")
if imagen is None:
    print("[ERROR] No se encontró 'formas.jpg'")
    exit()

# Preprocesamiento
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_, umbral = cv2.threshold(gris, 240, 255, cv2.THRESH_BINARY_INV)

# Encontrar contornos
contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Contadores de figuras
triangulos = 0
cuadrados = 0
circulos = 0

# Analizar cada contorno
for contorno in contornos:
    perimetro = cv2.arcLength(contorno, True)
    aproximacion = cv2.approxPolyDP(contorno, 0.04 * perimetro, True)
    vertices = len(aproximacion)

    x, y, w, h = cv2.boundingRect(aproximacion)

    if vertices == 3:
        triangulos += 1
        cv2.putText(imagen, "Triangulo", (x, y - 5), 1, 1, (0, 255, 0), 2)
        cv2.drawContours(imagen, [aproximacion], 0, (0, 255, 0), 2)

    elif vertices == 4:
        aspect_ratio = float(w) / h
        if 0.90 <= aspect_ratio <= 1.10:
            cuadrados += 1
            texto = "Cuadrado"
        else:
            cuadrados += 1
            texto = "Rectangulo"
        cv2.putText(imagen, texto, (x, y - 5), 1, 1, (255, 0, 0), 2)
        cv2.drawContours(imagen, [aproximacion], 0, (255, 0, 0), 2)

    elif vertices > 4:
        circulos += 1
        cv2.putText(imagen, "Circulo", (x, y - 5), 1, 1, (0, 0, 255), 2)
        cv2.drawContours(imagen, [aproximacion], 0, (0, 0, 255), 2)

# Guardar imagen con formas detectadas
cv2.imwrite("formas_detectadas.jpg", imagen)

# Crear archivo de reporte de texto
with open("reporte_formas.txt", "w") as reporte:
    reporte.write("📄 Reporte de Formas Detectadas\n")
    reporte.write("===============================\n")
    reporte.write(f"🔺 Triángulos: {triangulos}\n")
    reporte.write(f"🟦 Cuadrados/Rectángulos: {cuadrados}\n")
    reporte.write(f"⚪ Círculos: {circulos}\n")

# Crear archivo Excel
wb = openpyxl.Workbook()
hoja = wb.active
hoja.title = "Conteo de Formas"

# Encabezado
hoja.append(["Forma", "Cantidad"])
# Datos
hoja.append(["Triángulos", triangulos])
hoja.append(["Cuadrados/Rectángulos", cuadrados])
hoja.append(["Círculos", circulos])

# Guardar archivo Excel
wb.save("conteo_formas.xlsx")

print("[✅] Análisis completado. Resultados guardados en:")
print("- formas_detectadas.jpg")
print("- reporte_formas.txt")
print("- conteo_formas.xlsx")