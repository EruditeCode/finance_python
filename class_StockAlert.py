# Support class for finance programs.

import yfinance as yf

class StockAlert:
	def __init__(self, symbol:str, name:str, alert_price:float):
		self.symbol = symbol
		self.name = name
		self.alert_price = alert_price
		self.status = False

	def update(self):
		ticker = yf.Ticker(self.symbol).info
		current_price = ticker["currentPrice"]
		if current_price <= self.alert_price:
			self.status = True
		else:
			self.status = False
