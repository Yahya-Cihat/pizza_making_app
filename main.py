from tkinter import *
c = False
s = False
b = False
v = False
def sausage():
    global s 
    s = True
    print("sausage added!")
def Cheese():
    global c
    c = True
    print("Cheese added!")
def bacon():
    global b
    b = True
def beans():
    global v 
    v = True
def submit():
    canvas = Canvas(window,height=500,width=500)
    if c == True:
        canvas.create_arc(0,0,500,500,fill="#FFBF00",extent=350,width=0)
        canvas.pack()
        if s == True:
            canvas.create_image(350,350,image=sausageimg)
            canvas.create_image(150,100,image=sausageimg)
            canvas.create_image(150,300,image=sausageimg)
            canvas.create_image(350,100,image=sausageimg)
            canvas.create_image(250,400,image=sausageimg)
            canvas.create_image(250,200,image=sausageimg)
            if b == True:
                canvas.create_image(250,200,image=baconimg)
                canvas.create_image(400,200,image=baconimg)
                canvas.create_image(120,200,image=baconimg)
                canvas.create_image(250,100,image=baconimg)
                canvas.create_image(150,400,image=baconimg)
                canvas.create_image(350,400,image=baconimg)
                if v == True:
                    canvas.create_image(400,100,image=beanimg)
                    canvas.create_image(400,300,image=beanimg)
                    canvas.create_image(300,200,image=beanimg)
                    canvas.create_image(100,300,image=beanimg)
                    canvas.create_image(250,300,image=beanimg)
                    canvas.create_image(100,200,image=beanimg)
                    canvas.create_image(200,400,image=beanimg)
                    canvas.create_image(100,100,image=beanimg)
            else:
                canvas.create_image(400,100,image=beanimg)
                canvas.create_image(400,300,image=beanimg)
                canvas.create_image(300,200,image=beanimg)
                canvas.create_image(100,300,image=beanimg)
                canvas.create_image(250,300,image=beanimg)
                canvas.create_image(100,200,image=beanimg)
                canvas.create_image(200,400,image=beanimg)
                canvas.create_image(100,100,image=beanimg)

        else:
            if b == True:
                canvas.create_image(250,200,image=baconimg)
                canvas.create_image(400,200,image=baconimg)
                canvas.create_image(120,200,image=baconimg)
                canvas.create_image(250,100,image=baconimg)
                canvas.create_image(150,400,image=baconimg)
                canvas.create_image(350,400,image=baconimg)
                if v == True:
                    canvas.create_image(400,100,image=beanimg)
                    canvas.create_image(400,300,image=beanimg)
                    canvas.create_image(300,200,image=beanimg)
                    canvas.create_image(100,300,image=beanimg)
                    canvas.create_image(250,300,image=beanimg)
                    canvas.create_image(100,200,image=beanimg)
                    canvas.create_image(200,400,image=beanimg)
                    canvas.create_image(100,100,image=beanimg)
            else:
                canvas.create_image(400,100,image=beanimg)
                canvas.create_image(400,300,image=beanimg)
                canvas.create_image(300,200,image=beanimg)
                canvas.create_image(100,300,image=beanimg)
                canvas.create_image(250,300,image=beanimg)
                canvas.create_image(100,200,image=beanimg)
                canvas.create_image(200,400,image=beanimg)
                canvas.create_image(100,100,image=beanimg)
    else:
        canvas.create_arc(0,0,500,500,fill="#B20101",extent=350,width=0)
        canvas.pack()
        if s == True:
            canvas.create_image(350,350,image=sausageimg)
            canvas.create_image(150,100,image=sausageimg)
            canvas.create_image(150,300,image=sausageimg)
            canvas.create_image(350,100,image=sausageimg)
            canvas.create_image(250,400,image=sausageimg)
            canvas.create_image(250,200,image=sausageimg)
            if b == True:
                canvas.create_image(250,200,image=baconimg)
                canvas.create_image(400,200,image=baconimg)
                canvas.create_image(120,200,image=baconimg)
                canvas.create_image(250,100,image=baconimg)
                canvas.create_image(150,400,image=baconimg)
                canvas.create_image(350,400,image=baconimg)
            else:
                canvas.create_image(400,100,image=beanimg)
                canvas.create_image(400,300,image=beanimg)
                canvas.create_image(300,200,image=beanimg)
                canvas.create_image(100,300,image=beanimg)
                canvas.create_image(250,300,image=beanimg)
                canvas.create_image(100,200,image=beanimg)
                canvas.create_image(200,400,image=beanimg)
                canvas.create_image(100,100,image=beanimg)
        if b == True:
            canvas.create_image(250,200,image=baconimg)
            canvas.create_image(400,200,image=baconimg)
            canvas.create_image(120,200,image=baconimg)
            canvas.create_image(250,100,image=baconimg)
            canvas.create_image(150,400,image=baconimg)
            canvas.create_image(350,400,image=baconimg)
            if v ==True:
                canvas.create_image(400,100,image=beanimg)
                canvas.create_image(400,300,image=beanimg)
                canvas.create_image(300,200,image=beanimg)
                canvas.create_image(100,300,image=beanimg)
                canvas.create_image(250,300,image=beanimg)
                canvas.create_image(100,200,image=beanimg)
                canvas.create_image(200,400,image=beanimg)
                canvas.create_image(100,100,image=beanimg)
        if v == True:
            canvas.create_image(400,100,image=beanimg)
            canvas.create_image(400,300,image=beanimg)
            canvas.create_image(300,200,image=beanimg)
            canvas.create_image(100,300,image=beanimg)
            canvas.create_image(250,300,image=beanimg)
            canvas.create_image(100,200,image=beanimg)
            canvas.create_image(200,400,image=beanimg)
            canvas.create_image(100,100,image=beanimg)

window = Tk()
window.geometry("3000x2000")
sausageimg=PhotoImage(file="sausage.png")
baconimg = PhotoImage(file="bacon.png")
beanimg = PhotoImage(file="bean.png")
label = Label(text="What toppings would you like on the pizza?",font=("Arial",30))
label.pack()
button1 = Button(text="sausage",font=("Arial",30),command=sausage)
button1.place(x=0,y=150)
button2 = Button(text="Cheese",font=("Arial",30),command=Cheese)
button2.place(x=200,y=150)
button3 = Button(text="bacon",font=("Arial",30),command=bacon)
button3.place(x=400,y=150)
button4 = Button(text="beans",font=("Arial",30),command=beans)
button4.place(x=0,y=300)
button5 = Button(text="Bake!",font=("Arial",30),command=submit)
button5.pack()
window.mainloop()
