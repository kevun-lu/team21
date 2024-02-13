from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import *

w=Tk()


width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

w.overrideredirect(1)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

#############progressbar          33333333333333333333333333333
def new_win():
  # w.destroy()
    q=Tk()
    q.title('Main window')
    q.geometry('427x250')
    l1=Label(q,text='ADD TEXT HERE ',fg='grey',bg=None)
    l=('Calibri (Body)',24,'bold')
    l1.config(font=l)
    l1.place(x=80,y=100)
    
    q.mainloop()

def bar():

    l4=Label(w,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.01)
        r=r+1
    
    w.destroy()
    new_win()
    
progress.place(x=-10,y=235)

#############
# frame 333333333333333333333333
#
###########

'''
def rgb(r):
    return "#%02x%02x%02x" % r
#Frame(w,width=432,height=241,bg=rgb((100,100,100))).
'''
a='#249794'
Frame(w,width=427,height=241,bg=a).place(x=0,y=0)  #249794
b1=Button(w,width=10,height=1,text='Game Starte',command=bar,border=0,fg=a,bg='white')
b1.place(x=170,y=200)


######## Label

l1=Label(w,text='SPLASH',fg='white',bg=a)
lst1=('Calibri (Body)',18,'bold')
l1.config(font=lst1)
l1.place(x=50,y=80)

l2=Label(w,text='SCREEN',fg='white',bg=a)
lst2=('Calibri (Body)',18, 'bold')
l2.config(font=lst2)
l2.place(x=155,y=82)

l3=Label(w,text='PROGRAMMED',fg='white',bg=a)
lst3=('Calibri (Body)',13)
l3.config(font=lst3)
l3.place(x=50,y=110)

# Load the background image
# background_image = PhotoImage(file="entry_terminal.jpg")  # Update this path to your image file
# # Create a Label to use as the background
# background_label = Label(w, image=background_image)
# # Place the label as a background
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# # Make sure you keep references to PhotoImage instances to prevent garbage collection
# w.image = background_image

w.mainloop()


