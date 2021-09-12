from tkinter import *
t=Tk()
t.resizable(0,0)
t.title("village sunset")
w=760
h=550
x=(t.winfo_screenwidth()-w)/2
y=(t.winfo_screenheight()-h)/2
t.geometry("%dx%d+%d+%d"%(w,h,x,y))
c=Canvas(width=800,height=550,bg="brown")
c.pack()
f1=PhotoImage(file='flying-bird-sunset-scene.gif')
c.create_image(400,270,image=f1)
c.create_rectangle(0,560,800,500,width=2,outline="green",fill="black")
c.create_polygon(150,300,250,200,350,300,350,500,150,500,width=2,outline="black",fill="brown")
c.create_rectangle(350,500,610,300,width=2,outline="black",fill="brown")
c.create_line(150,300,600,300,width=2,fill="black")
c.create_line(250,200,510,200,width=2,fill="black")
x1,y1=250,200
x2,y2=360,310
for i in range(0,53):
    c.create_line(x1,y1,x2,y2,width=3,fill="black")
    x1+=5
    x2+=5
c.create_rectangle(200,500,300,350,width=2,outline="black",fill="blue")
c.create_rectangle(205,500,295,355,width=2,outline="black",fill="yellow")
c.create_rectangle(410,460,550,355,width=2,outline="black",fill="blue")
c.create_rectangle(415,455,550,355,width=2,outline="black",fill="yellow")
x3,y3=0,450
x4,y4=150,550
for i in range(2):
    c.create_arc(x3,y3,x4,y4,start=0,extent=180,fill="green")
    x3+=610
    x4+=610
x5,y5=415,370
x6,y6=550,370
for i in range(0,7):
    c.create_line(x5,y5,x6,y6,width=2,fill="black")
    y5+=15
    y6+=15

x7,y7=415,355
x8,y8=415,455
for i in range(0,27):
    c.create_line(x7,y7,x8,y8,width=2,fill="black")
    x7+=5
    x8+=5

x9,y9=205,500
x10,y10=205,355
for i in range(0,18):
    c.create_line(x9,y9,x10,y10,width=2,fill="black")
    x9+=5
    x10+=5

x11,y11=205,365
x12,y12=295,365
for i in range(0,16):
    c.create_line(x11,y11,x12,y12,width=3,fill="black")
    y11+=10
    y12+=10    
u1=Label(text="\"Stay HOME Stay SAFE\"",font=("",15),bg="orange",fg="black")
u1.place(x=0,y=510,width=760,height=25) 
t.mainloop()