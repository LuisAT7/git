import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class email:

	def __init__(self):
		self.user = 'luis_pruebalab@gmail.com'
		self.pasw = 'poderosafusufum'
		self.email = 'luis.trejo.tovar@gmail.com'
		self.subj = 'Test correo'
		self.body = 'Cuerpo del mensaje donde va lo que sea jeje'


	def enviarcorreo(self,x):
		conex = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=conex) as ser:
			ser.login(self.user, self.pasw)
			ser.sendmail(self.user, self.email, x)


	def crearcorreo(self):
		mail = MIMEMultipart("alternative")
		mail["Subject"] = self.subj
		mail["From"] = self.user
		mail["To"] = self.email
		html = """\
		<html>
		  <body> 
		    <p>
		      """+self.body+"""
		    </p>
		  </body>
		</html>
		"""
		mailhtml = MIMEText(html, "html")
		mail.attach(mailhtml)
		ncorreo = mail.as_string()
		self.correo(ncorreo)


send = email()
send.crearcorreo()
