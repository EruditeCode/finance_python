# Support class for finance programs.

import yfinance as yf

class StockAlert:
	def __init__(self, symbol:str, name:str, alert_price:float):
		self.symbol = symbol
		self.name = name
		self.alert_price = alert_price
		self.status = False
