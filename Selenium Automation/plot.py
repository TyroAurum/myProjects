from matplotlib import pyplot as plt
from csv import reader
from csv import writer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import sqlite3


ser = Service("chromedriver.exe")
op = webdriver.ChromeOptions()


conect = sqlite3.connect('stock_price.db')
cur=conect.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS stock_price
	(stock_ID TEXT PRIMARY KEY,
	stock TEXT,
	price INTEGER
	)""")
conect.commit()



x=[]
y=[]
i=0

with open('NSE companies list.csv','r') as csv_reader:
	csv_read = reader(csv_reader)

	next(csv_read)

	for row in csv_read:
		y.append(row[0])



		

while i<len(y):
	driver = webdriver.Chrome(service=ser,options=op)
	link="""https://www.google.com/search?q=""" + y[i] + " share price"
	driver.get(link)
	price=driver.find_element("xpath","""//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]""")
	price=price.text
	stockname = driver.find_element("xpath","""//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[1]/div/div/span""")
	stockname=stockname.text
	cur.execute("INSERT INTO stock_price VALUES(:stock_ID, :stock, :price)",
		(y[i],
		stockname,
		price,
		))
	conect.commit()
	i=i+1
	driver.close()

