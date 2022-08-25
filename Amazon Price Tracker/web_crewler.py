from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


ser = Service("chromedriver.exe")
op = webdriver.ChromeOptions()
price_link = """//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]"""
product_link = """//*[@id="productTitle"]"""

def scrap():
	asin = ety1.get()
	link = """https://www.amazon.in/webcrawler/dp/""" + asin
	driver = webdriver.Chrome(service=ser,options=op)
	driver.get(link)
	product = driver.find_element_by_xpath(product_link)
	product = product.text
	price = driver.find_element_by_xpath(price_link)
	price=price.text
	lbl2 = Label(root,text=product + price).pack()
	driver.close()

root = Tk()
root.title("Web Crawler")
root.geometry("700x450")




lbl0 = Label(root,text="Web Crawler")
lbl1 = Label(root,text="Enter your Product's ASIN").pack(pady=20)
ety1 = Entry(root)
ety1.pack()
btn1 = Button(root,text="Go",command=scrap).pack()









root.mainloop()