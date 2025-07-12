import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

# Datos del correo
remitente = "bellyukari123@gmail.com"
destinatario = "bellyukari123@gmail.com"
password = "uwvf fxjm nwtb wjiu"  # Coloca aquí tu contraseña de aplicación

# Crear mensaje multipart
mensaje = MIMEMultipart()
mensaje['Subject'] = "📊 Reporte de Formas Detectadas con Imagen y Excel"
mensaje['From'] = remitente
mensaje['To'] = destinatario

# Cuerpo de texto
with open("reporte_formas.txt", "r") as archivo:
    cuerpo = archivo.read()

mensaje.attach(MIMEText(cuerpo, "plain"))

# Adjuntar imagen resaltada
with open("formas_detectadas.jpg", "rb") as img:
    imagen_adjunto = MIMEImage(img.read())
    imagen_adjunto.add_header('Content-Disposition', 'attachment', filename="formas_detectadas.jpg")
    mensaje.attach(imagen_adjunto)

# Adjuntar archivo Excel
with open("conteo_formas.xlsx", "rb") as excel_file:
    parte_excel = MIMEBase("application", "octet-stream")
    parte_excel.set_payload(excel_file.read())
    encoders.encode_base64(parte_excel)
    parte_excel.add_header(
        "Content-Disposition",
        f"attachment; filename=conteo_formas.xlsx"
    )
    mensaje.attach(parte_excel)

# Enviar correo
try:
    servidor = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    servidor.login(remitente, password)
    servidor.send_message(mensaje)
    servidor.quit()
    print("[✅] Correo enviado con imagen y archivo Excel adjuntos.")
except Exception as e:
    print(f"[❌] Error al enviar correo: {e}")


