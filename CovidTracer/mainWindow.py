from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from covid import Covid
import country

def get_dropdown():
    covid = Covid()
    print(country.get())
    name=country.get()
    virusdata = covid.get_status_by_country_name(name)
    remove = ['id', 'country', 'latitude', 'longitude', 'last_update']

    for i in remove:
        virusdata.pop(i)

    tot = virusdata.pop('confirmed')

    id = list(virusdata.keys())
    values = [str(i) for i in virusdata.values()]

    fig = plt.Figure(figsize=(5, 5), dpi=100)
    a=fig.add_subplot(111)
    a.pie(values, labels=id, colors=['r', 'y', 'g', 'b'], autopct='%1.1f%%')
    a.set_title("COUNTRY : "+name.upper()+"\nTOTAL CASES : "+str(tot))
    fig.savefig("output.png")
    canvas=FigureCanvasTkAgg(fig,win)
    canvas.get_tk_widget().place(x=400,y=50)
    canvas.draw()

cnames=country.clist
win=Tk()
win.title("Covid Tracer")
win.geometry("1000x600")

l1=Label(win,text="WELCOME TO COVID TRACER",bg="black",fg="white",font="times 20").pack()

l2=Label(win,text="Select Country : ",bg="blue",fg="white",font="times 12").place(x=20,y=100)

country=StringVar()
country.set("Select")
clist=OptionMenu(win,country,*cnames).place(x=180,y=100)

Button(win,text="Get Details",bg="blue",fg="white",font="times 12",command=get_dropdown).place(x=100,y=200)




win.mainloop()
