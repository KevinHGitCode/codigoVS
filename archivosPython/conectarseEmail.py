#conectarse a gmail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#datos de la cuenta de correo
gmail_user = 'alguien@gmail.com'
gmail_password = 'contraseña'

#datos del mensaje a enviar
asunto = 'Prueba de envio de correo'
sender = 'mensaje'
receivers = 'receptor.gmail.com'

#TODO: completar este codigo
