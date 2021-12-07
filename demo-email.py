import os
import smtplib

EMAIL_SENDER = os.environ.get('EMAIL_USER')  #os.environ para seguridad y no mostrar los datos delicados
GOOGLE_KEY = os.environ.get('GOOGLE_KEY')     
EMAIL_RECIEVER = os.environ.get('EMAIL_OTHER')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp: # Conexion
  smtp.ehlo()  # nos identifica con el servidor principal
  smtp.starttls()  # Encriptar trafico
  smtp.ehlo()  # Reidentificar

  smtp.login(EMAIL_SENDER, GOOGLE_KEY)  # mail y clave de seguridad

  subject = 'te amo'
  body = ' mucho [UwU]'
  msg = f"Subject: {subject}\n\n{body}"

  smtp.sendmail(EMAIL_SENDER, EMAIL_RECIEVER, msg)