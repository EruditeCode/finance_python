# Support class for finance programs.

# Email function setup has a walkthrough video.
# Video Walkthrough Link: https://www.youtube.com/watch?v=JLLE11Eo4fc

import yfinance as yf
import smtplib, ssl
from email.message import EmailMessage

class StockAlert:
	def __init__(self, symbol:str, name:str, alert_price:float):
		self.symbol = symbol
		self.name = name
		self.alert_price = alert_price
		self.status = False
		self.active = True

	def update(self):
		ticker = yf.Ticker(self.symbol).info
		current_price = ticker["currentPrice"]
		if current_price <= self.alert_price:
			self.status = True
		else:
			self.status = False

		if self.status and self.active:
			print("Sending Email...")
			# To activate the email functionality remove the comment below.
			# self.email_handler()
			self.active = False

	def email_handler(self):
		source_email = "" # - Your source email.
		source_pass = "" # - The 16 character app password.

		recipient = "" # - Your recipient email.
		msg = EmailMessage()
		msg["Subject"] = f"{self.symbol} Stock Alert"
		msg["From"] = source_email
		msg["To"] = recipient
		msg.set_content(f"Alert price reached for {self.name}.")

		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(source_email, source_pass)
			server.send_message(msg)
