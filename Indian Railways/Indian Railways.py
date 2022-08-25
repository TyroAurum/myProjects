from tkinter import *
from tkinter import messagebox

#Create main window
root = Tk()
root.geometry("1920x1280")
root.title("Indian Railways")
root.attributes("-fullscreen",True)

wag12 = PhotoImage(file = 'Train.png')

#Locomotive Class
class Loco:
   def __init__(self,name, built, builder, power, speed, mass):
      self.name = name
      self.built = built
      self.builder = builder
      self.power = power
      self.speed = speed
      self.mass =mass

   def show_info(self):
    frame6.pack_forget()
    lbl1 = Label(frame7, text = self.name, font = ('Bold'))
    lbl1.grid(row=2, column=1)
    lbl2 = Label(frame7, text = 'Built     :   ' + str(self.built), font = ('Bold'))
    lbl2.grid(row=5, column=1)
    lbl3 = Label(frame7, text = 'Builder     :    ' + self.builder, font = ('Bold'))
    lbl3.grid(row=7, column=1)
    lbl4 = Label(frame7, text = 'Power     :    ' + self.power, font = ('Bold'))
    lbl4.grid(row=9, column=1)
    lbl5 = Label(frame7, text = 'Maximum Speed     :    ' + self.speed, font = ('Bold'))
    lbl5.grid(row=11, column=1)
    lbl6 = Label(frame7, text = 'Mass     :    ' + self.mass, font = ('Bold'))
    lbl6.grid(row=13, column=1)
    def loco_back():
        frame7.pack_forget()
        frame6.pack(padx = 20, pady = 200)
    
    btn1 = Button(frame7, text = 'Back', font = ('Bold'), command = loco_back)
    btn1.grid(row=15, column=1)
    frame7.pack(padx = 20, pady = 200)


#List of Locomotives
wag_1 = Loco('WAG - 1', '1963-66', '50 cycles European group', '2930 hp', '80 km/h', '85 t')
wag_2 = Loco('WAG - 2', '1964-65', 'Mitsubishi, Toshiba, Hitachi', '3450 hp', '80 km/h', '86 t')
wag_3 = Loco('WAG - 3', 1965, 'Henschel', '3590 hp', '80 km/h', '87 t')
wag_4 = Loco('WAG - 4', '1966-71', 'CLW', '3590 hp', '80 km/h', '88 t')
wag_5 = Loco('WAG - 5', '1988-98', 'CLW, BHEL', '4360 hp', '100 km/h', '119 t')
wag_6 = Loco('WAG - 6', 1988, 'Hitachi', '6110 hp', '100 km/h', '123 t')
wag_7 = Loco('WAG - 7', 1992, 'CLW', '5350 hp', '100 km/h', '123 t')
wag_8 = Loco('WAG - 8', 1996, 'BHEL', '5000 hp', '100 km/h', '128 t')
wag_9 = Loco('WAG - 9', 1996, 'CLW', '6112 hp', '120 km/h', '123 t')
wag_11 = Loco('WAG - 11', 2019, 'BLW', '12000 hp', '105 km/h', '252 t')
wag_12 = Loco('WAG - 12', 2017, 'Alstom', '12000 hp', '120 km/h', '180 t')

wap_1 = Loco('WAP - 1', '1980-96', 'CLW', '3900 hp', '130 km/h', '112 t')
wap_2 = Loco('WAP - 2', '1998-2002', 'Mitsubishi, Toshiba, Hitachi', '2910 hp', '120 km/h', '76 t')
wap_3 = Loco('WAP - 3', '1987-88', 'CLW', '3900 hp', '130 km/h', '112 t')
wap_4 = Loco('WAP - 4', '1993-2015', 'CLW', '5350 hp', '140 km/h', '113 t')
wap_5 = Loco('WAP - 5', '1995', 'ABB, CLW', '6000 hp', '160 km/h', '79 t')
wap_6 = Loco('WAP - 6', '1997', 'CLW', '5350 hp', '140 km/h', '114 t')
wap_7 = Loco('WAP - 7', 2000, 'CLW', '6350 hp', '140 km/h', '123t')




#Home page functions
def rolstock():
    frame1.pack_forget()
    frame2.pack()

def history():
    frame1.pack_forget()
    frame3.pack()

def options():
    frame1.pack_forget()
    frame5.pack()

#Rolling stock page functions
def loco():
    frame2.pack_forget()
    frame6.pack(padx = 20, pady = 200)

def back1():
    frame2.pack_forget()
    frame1.pack()



#Options page functions
def back4():
    frame5.pack_forget()
    frame1.pack()

#Locomotive page functions
def back5():
    frame6.pack_forget()
    frame2.pack()

#History page functions
def back2():
    frame3.pack_forget()
    frame1.pack()

def hist_scale():
    if int(hisscale.get()) == 1858:
        sclbl1.config( text = 'Indian Railways was founded.')
    elif int(hisscale.get()) == 1853:
        sclbl1.config( text = 'India’s first passenger train set off on a 34km journey between Bombay’s BoriBunder station and Thane.\nIt consisted of 14 cars being hauled by three steam locomotives, and carried 400 passengers.')
    elif int(hisscale.get()) == 1854:
        sclbl1.config( text = 'The mountain trains, now called as the toy trains were first proposed.')
    elif int(hisscale.get()) == 1860:
        sclbl1.config( text = 'Eight railway companies were launched in the country including Eastern India Railway, Madras Railway, Great India Peninsula Company and others.')
    elif int(hisscale.get()) == 1891:
        sclbl1.config( text = 'Toilets were first introduced in the first class coaches.')
    elif int(hisscale.get()) == 1907:
        sclbl1.config( text = 'The lower classes were provided with toilets.')
    elif int(hisscale.get()) == 1925:
        sclbl1.config( text = 'The first electric train ran between Bombay and Kurla on 3 February 1925.')
    elif int(hisscale.get()) == 1950:
        sclbl1.config( text = 'Chittaranjan Locomotive Works was founded.')
    elif int(hisscale.get()) == 1951:
        sclbl1.config( text = 'Southern, Central and Western Railways were established.')
    elif int(hisscale.get()) == 1952:
        sclbl1.config( text = 'Northern, Eastern and North Eastern Railway were established.')
    elif int(hisscale.get()) == 1955:
        sclbl1.config( text = 'South Eastern Railway was established.\nIntegral Coach Factory, manufacturer of rail coaches was established.')
    elif int(hisscale.get()) == 1958:
        sclbl1.config( text = 'Northeast Frontier Railway was established.')
    elif int(hisscale.get()) == 1961:
        sclbl1.config( text = 'Banaras Locomotive Works was founded.')
    elif int(hisscale.get()) == 1966:
        sclbl1.config( text = 'South Central Railway was established.')
    elif int(hisscale.get()) == 1986:
        sclbl1.config( text = 'Indian Railway Finance Corporation was established.')
    elif int(hisscale.get()) == 1998:
        sclbl1.config( text = 'Konkan Railway was established.')
    elif int(hisscale.get()) == 1999:
        sclbl1.config( text = 'Indian Railway Catering and Tourism Corporation was established.')
    elif int(hisscale.get()) == 2002:
        sclbl1.config( text = 'North Western Railway and East Central Railway were established.')
    elif int(hisscale.get()) == 2003:
        sclbl1.config( text = ' South Western Railway, West Central Railway, North Central Railway, South East Central Railway and East Coast Railway were established.')
    else:
        sclbl1.config( text = '  ')


#wagon page functions
def wagon():
    frame2.pack_forget()
    frame8.pack()

def back6():
    frame8.pack_forget()
    frame2.pack()


#Frame initialising
frame1 = Frame(root)
frame1.pack()

frame2 = Frame(root)

frame3 = Frame(root)

frame5 = Frame(root)

frame6 = Frame(root)

frame7 = Frame(root)

frame8 = Frame(root)

#Home page Widgets
btn1 = Button(frame1, text = 'Rolling Stock', bg = "Black", fg = "White", font = ('Bold'), width = 40, height = 2, command = rolstock)
btn1.pack(padx = 20, pady = 50)
btn2 = Button(frame1, text = 'History', bg = "Black", fg = "White", font = ('Bold'), width = 40, height = 2, command = history)
btn2.pack(padx = 20, pady = 50)
btn3 = Button(frame1, text = 'Photos', bg = "Black", fg = "White", font = ('Bold'), width = 40, height = 2)
btn3.pack(padx = 20, pady = 50)
btn4 = Button(frame1, text = 'Options', bg = "Black", fg = "White", font = ('Bold'), width = 40, height = 2, command = options)
btn4.pack(padx = 20, pady = 50)
btn5 = Button(frame1, text = 'Quit', bg = "Black", fg = "White", font = ('Bold'), width = 40, height = 2, command = root.quit)
btn5.pack(padx = 20, pady = 50)



#Rolling stock page Widgets
rsbtn6 = Button(frame2, text = 'Locomoties', bg = "Black", fg = "White", font = ('Bold'), width = 40, height = 2, command = loco)
rsbtn6.pack(padx = 20, pady = 50)
rsbtn7 = Button(frame2, text = 'Wagons', bg = "Black", fg = "White", font = ('Bold'), width = 40, height = 2, command = wagon)
rsbtn7.pack(padx = 20, pady = 50)
rsbtn9 = Button(frame2, text = 'Production units', bg = "Black", fg = "White", font = ('Bold'), width = 40, height = 2)
rsbtn9.pack(padx = 20, pady = 50)
rsbtn8 = Button(frame2, text = 'Back', bg = "Black", fg = "White", font = ('Bold'), width = 40, height = 2, command = back1)
rsbtn8.pack(padx = 20, pady = 50)

#History page Widgets
hisscale = Scale(frame3, orient = HORIZONTAL, from_ = 1853, to = 2021, tickinterval = 10, length = 1100)
hisscale.pack(padx = 20, pady = 130)
hisbtn2 = Button(frame3, text = 'View History', bg = "Black", fg = "White", font = ('Bold'), width = 40, height = 2, command = hist_scale)
hisbtn2.pack(anchor=CENTER)
hisbtn1 = Button(frame3, text = 'Back', bg = "Black", fg = "White", font = ('Bold'), width = 40, height = 2, command = back2)
hisbtn1.pack(anchor=CENTER)
sclbl1 = Label(frame3, font = ('bold'))
sclbl1.pack(padx = 20, pady = 50)



#Options page Widgets
optbtn2 = Button(frame5, text = 'BG Color',  bg = "Black", fg = "White", font = ('Bold'), width = 40, height = 2).pack(pady = 100)
optbtn1 = Button(frame5, text = 'Back', bg = "Black", fg = "White", font = ('Bold'), width = 40, height = 2, command = back4)
optbtn1.pack(side = BOTTOM)

#Locomotives page Widgets
wagbtn1 = Button(frame6, text = 'WAG - 1', bg = 'black', fg = 'white', command=lambda: wag_1.show_info())
wagbtn1.grid(row=2, column=0)
wagbtn2 = Button(frame6, text = 'WAG - 2', bg = 'black', fg = 'white', command=lambda: wag_2.show_info())
wagbtn2.grid(row=4, column=0)
wagbtn3 = Button(frame6, text = 'WAG - 3', bg = 'black', fg = 'white', command=lambda: wag_3.show_info())
wagbtn3.grid(row=6, column=0)
wagbtn4 = Button(frame6, text = 'WAG - 4', bg = 'black', fg = 'white', command=lambda: wag_4.show_info())
wagbtn4.grid(row=8, column=0)
wagbtn5 = Button(frame6, text = 'WAG - 5', bg = 'black', fg = 'white', command=lambda: wag_5.show_info())
wagbtn5.grid(row=10, column=0)
wagbtn6 = Button(frame6, text = 'WAG - 6', bg = 'black', fg = 'white', command=lambda: wag_6.show_info())
wagbtn6.grid(row=12, column=0)
wagbtn7 = Button(frame6, text = 'WAG - 7', bg = 'black', fg = 'white', command=lambda: wag_7.show_info())
wagbtn7.grid(row=14, column=0)
wagbtn8 = Button(frame6, text = 'WAG - 8', bg = 'black', fg = 'white', command=lambda: wag_8.show_info())
wagbtn8.grid(row=16, column=0)
wagbtn9 = Button(frame6, text = 'WAG - 9', bg = 'black', fg = 'white', command =lambda: wag_9.show_info())
wagbtn9.grid(row=18, column=0)
wagbtn10 = Button(frame6, text = 'WAG - 10', bg = 'black', fg = 'white', command =lambda: wag_10.show_info())
wagbtn10.grid(row=20, column=0)
wagbtn11 = Button(frame6, text = 'WAG - 11', bg = 'black', fg = 'white', command =lambda: wag_11.show_info())
wagbtn11.grid(row=22, column=0)
wagbtn12 = Button(frame6, text = 'WAG - 12', bg = 'black', fg = 'white', command =lambda: wag_12.show_info())
wagbtn12.grid(row=24, column=0)

wapbtn1 = Button(frame6, text = 'WAP - 1', bg = 'black', fg = 'white', command =lambda: wap_1.show_info())
wapbtn1.grid(row=2, column=2)
wapbtn2 = Button(frame6, text = 'WAP - 2', bg = 'black', fg = 'white', command =lambda: wap_2.show_info())
wapbtn2.grid(row=4, column=2)
wapbtn3 = Button(frame6, text = 'WAP - 3', bg = 'black', fg = 'white', command =lambda: wap_3.show_info())
wapbtn3.grid(row=6, column=2)
wapbtn4 = Button(frame6, text = 'WAP - 4', bg = 'black', fg = 'white', command =lambda: wap_4.show_info())
wapbtn4.grid(row=8, column=2)
wapbtn5 = Button(frame6, text = 'WAP - 5', bg = 'black', fg = 'white', command =lambda: wap_5.show_info())
wapbtn5.grid(row=10, column=2)
wapbtn6 = Button(frame6, text = 'WAP - 6', bg = 'black', fg = 'white', command =lambda: wap_6.show_info())
wapbtn6.grid(row=12, column=2)
wapbtn7 = Button(frame6, text = 'WAP - 7', bg = 'black', fg = 'white', command =lambda: wap_7.show_info())
wapbtn7.grid(row=14, column=2)




lobtn100 = Button(frame6, text = 'Back', bg = "Black", fg = "White", font = ('Bold'), command = back5)
lobtn100.grid(row=16, column=1)


#Wagons page widgets
wgbtn1 = Button(frame8, text = 'Goods Wagons',  bg = "Black", fg = "White", font = ('Bold'))
wgbtn1.pack(padx = 20, pady = 50)
wgbtn2 = Button(frame8, text = 'Passengers Coaches',  bg = "Black", fg = "White", font = ('Bold'))
wgbtn2.pack(padx = 20, pady = 50)
wgbtn3 = Button(frame8, text = 'Back',  bg = "Black", fg = "White", font = ('Bold'), command = back6)
wgbtn3.pack(padx = 20, pady = 50)


root.mainloop()