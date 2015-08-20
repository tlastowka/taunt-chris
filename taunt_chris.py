#!/usr/bin/env python

import requests
import re
import random
import time

url = """http://home.online.no/~rkaste/jokes/insults.htm"""
page = requests.get(url)

insults = [j for j in [str(i) for i in re.split('\r\n',page.text) if len(i)>0] if j[0].isalpha()]

laugh_letters = ['a','h','A','H']
while True:
	print("HEY CHRIS!")
	time.sleep(1)
	print("GUESS WHAT?")
	time.sleep(1)
	print(random.choice(insults))
	time.sleep(1)
	laugh_count = random.randint(10,100)
	print("".join(([random.choice(laugh_letters) for r in range(laugh_count)])))
	time.sleep(2)
	


#for i in page.text.split('\n'):
#	if i[0].isalpha():
#		print(i)
