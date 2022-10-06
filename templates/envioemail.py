import smtplib 
from email.message import EmailMessage 

def enviar(email_destino,codigo):
    email_origen="rshernandez@uninorte.edu.co"
    password=""
    email = EmailMessage()
    email["From"] = email_origen
    email["To"] = email_destino
    email["Subject"] = "Codigo de Activacion"
    email.set_content("Sr, usuario su codigo de activacion es :\n\n"+codigo+ "\n\n Recuerde copiarlo y pegarlo para validarlo en la seccion de login y activar su cuenta.\n\nMuchas Gracias")

    # Send Email
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(email_origen, password)
    smtp.sendmail(email_origen, email_destino, email.as_string())
    smtp.quit()