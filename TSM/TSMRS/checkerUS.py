By ruks
import requests
from user_agent import generate_user_agent
class check:
	def Instagram(self,user):
		print(user)		
		pass
	def Facebook(self):
		print(user)		
		pass
	def Snapchat(self,user):
		req=requests.get(f"https://story.snapchat.com/@{user}",headers={'Host': 'story.snapchat.com',
'cache-control': 'max-age=0',
'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"','save-data': 'on',
'upgrade-insecure-requests': '1',
'user-agent': generate_user_agent(),
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document'}).status_code
		return req	
		pass
	def Telegram(self,user):
		print(user)		
		pass
	def Twitter(self,user):
		print(user)		
		pass
	def YouTube(self,user):
		print(user)		
		pass
