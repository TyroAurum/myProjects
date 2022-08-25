from tkinter import *
from tkcalendar import Calendar, DateEntry
import sqlite3
from tkinter import messagebox

#create root window
#root = Tk()
#root.title('Invesment Entry')
#root.geometry('1000x750')

#connect to sqlite database
conect = sqlite3.connect('invesment_registry.db')
cur = conect.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS invesment
	(trade_id INTEGER PRIMARY KEY NOT NULL,
	 stock  text,
	 trade_name text,
	 invest_began text, 
	 price_began number,
	 invest_type text
	 )''')

conect.commit()

#define register function
def submit():
	cur.execute("INSERT INTO invesment VALUES (:trade_id, :stock, :trade_name, :invesment_began, :price_began, :invesment_type)",
			(	None,
				stock.get(),
				trade_name.get(),
				date_began.get(),
				price_began.get(),
				itype.get(),
			))
	conect.commit()
	messagebox.showinfo('Record Saved','Record saved successfully.')

#create registry window
registry = Tk()
registry.title('Invesment Registry')
registry.geometry('425x350')
frame1=Frame(registry).place()




hlbl1=Label(frame1, text='Invesment Report', font=('Bold')).grid(row=0,column=3)
elbl1=Label(frame1,text='     ').grid(row=1,column=0)
elbl2=Label(frame1,text='    ').grid(row=1,column=6)
elbl3=Label(frame1,text='    ').grid(row=2,column=2)
elbl4=Label(frame1,text='    ').grid(row=2,column=4)
stock_label=Label(frame1,text='Stock Name').grid(row=3,column=3)
stock=Entry(frame1)
stock.grid(row=4,column=3)
date_began_label=Label(frame1,text='Invesment Date').grid(row=3,column=1)
date_began=DateEntry(frame1)
date_began.grid(row=4,column=1)
price_began_label=Label(frame1,text='Price Began').grid(row=3,column=5)
price_began=Entry(frame1)
price_began.grid(row=4,column=5)
elbl5=Label(frame1, text='  ').grid(row=6,column=2)
slabel4=Label(frame1, text='Invesment Type').grid(row=7,column=3)

#invest_type = Entry(frame1)
#invest_type.grid(row=8,column=3)

#create radiobutton
TYPES = [
		("Intraday","Intraday"),
		("Short-Term","Short-Term"),
		("Mid-Term","Mid-Term"),
		("Long-Term","Long-Term"),	

]

itype = StringVar()
itype.set("Short-Term")


for text,types in TYPES:
	Radiobutton(frame1, text=text, variable=itype, value=types).grid(column=1)


#sradio2=Radiobutton(frame1, text='Short-Term', variable='Invesment type', value='short-term').grid(row=8,column=3)
#sradio3=Radiobutton(frame1, text='Mid-Term', variable='Invesment type', value='mid-term').grid(row=8,column=5)
#sradio4=Radiobutton(frame1, text='Long-Term', variable='Invesment type', value='long-term').grid(row=9,column=3)
elbl6=Label(frame1, text='   ').grid(row=10,column=3)
trade_name_label=Label(frame1,text='Trade Name').grid(row=11,column=3)
trade_name=Entry(frame1)
trade_name.grid(row=12,column=3)
elbl7=Label(frame1, text='   ').grid(row=13,column=3)
button1=Button(frame1, text='Enter registry', padx=5,pady=2, command = submit).grid(row=14,column=3)
registry.mainloop()