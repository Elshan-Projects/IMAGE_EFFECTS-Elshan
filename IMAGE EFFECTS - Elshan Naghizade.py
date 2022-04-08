from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


filename = 'defaultim.png'

def shekilUP(event=None):
    global filename
    filename = filedialog.askopenfilename()
    image1 = Image.open(filename)
    image1.thumbnail((590, 350))

    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test

    label1.grid(column=0, row=1, pady=(10,4),columnspan = 2,padx=(5,5))
    
def bagla():
    window.destroy()
    
    
window = Tk()

window.title("Image Effects - Elshan Naghizade")
window.resizable(False, False)
window.geometry("600x450+3+3")

lbl1 = Label(window, text="Click to select >>>>",font=("Arial",12))
lbl1.grid(column=0, row=0, columnspan = 1, padx=(10,10),pady=(10,5))

button = Button(window, text='Select an image', command=shekilUP,font=("Arial",12), width=35, height=1)
button.grid(column=1, row=0, columnspan = 1, padx=(10,10),pady=(5,5))

image1 = Image.open(filename)
image1.thumbnail((590, 310))

test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

label1.grid(column=0, row=1, pady=(4,4),columnspan = 2,padx=(5,5))

button1 = Button(window, text='Move To The Effects Menu', command=bagla,font=("Arial",12), width=55, height=1)
button1.grid(column=0, row=2, columnspan = 2, padx=(40,10),pady=(4,4))

window.mainloop()


from PIL import Image, ImageEnhance, ImageOps

window = Tk()

window.title("Effects Menu - Elshan Naghizade")
window.resizable(False, False)
window.geometry("600x470+3+3")
window.configure(background='#e0ebeb')


def sola():
    image_or1 = Image.open(filename)
    image_sol = image_or1.rotate(90)
    image_sol.save('sol.png')
    image_sol.thumbnail((280, 280))

    test = ImageTk.PhotoImage(image_sol)
    l2 = Label(image=test)
    l2.image = test
    l2.grid(row=2, column=2, pady=(15,5),columnspan = 2,padx=(5,5))

def sag():
    image_or1 = Image.open(filename)
    image_sag = image_or1.rotate(270)
    image_sag.save('sag.png')
    image_sag.thumbnail((280, 280))

    test = ImageTk.PhotoImage(image_sag)
    l2 = Label(image=test)
    l2.image = test
    l2.grid(row=2, column=2, pady=(15,5),columnspan = 2,padx=(5,5))


def vert():
    image_or1 = Image.open(filename)
    image_vert = image_or1.transpose(Image.FLIP_LEFT_RIGHT)
    image_vert.save('vert.png')
    image_vert.thumbnail((280, 280))

    test = ImageTk.PhotoImage(image_vert)
    l2 = Label(image=test)
    l2.image = test
    l2.grid(row=2, column=2, pady=(15,5),columnspan = 2,padx=(5,5))


def hor():
    image_or1 = Image.open(filename)
    image_hor = image_or1.transpose(Image.FLIP_TOP_BOTTOM)
    image_hor.save('hor.png')
    image_hor.thumbnail((280, 280))

    test = ImageTk.PhotoImage(image_hor)
    l2 = Label(image=test)
    l2.image = test
    l2.grid(row=2, column=2, pady=(15,5),columnspan = 2,padx=(5,5))

    
    
def kon():
    image_or1 = Image.open(filename)
    contrast = ImageEnhance.Contrast(image_or1)
    image_kon = contrast.enhance(1.7)
    image_kon.save('kon.png')
    image_kon.thumbnail((280, 280))

    test = ImageTk.PhotoImage(image_kon)
    l2 = Label(image=test)
    l2.image = test
    l2.grid(row=2, column=2, pady=(15,5),columnspan = 2,padx=(5,5))

    
    
def par():
    image_or1 = Image.open(filename)
    brightness = ImageEnhance.Brightness(image_or1)
    image_par = brightness.enhance(1.7)
    image_par.save('par.png')
    image_par.thumbnail((280, 280))

    test = ImageTk.PhotoImage(image_par)
    l2 = Label(image=test)
    l2.image = test
    l2.grid(row=2, column=2, pady=(15,5),columnspan = 2,padx=(5,5))

def qar():
    image_or1 = Image.open(filename)
    image_qar = image_or1.convert('L')
    image_qar.save('qar.png')
    image_qar.thumbnail((280, 280))

    test = ImageTk.PhotoImage(image_qar)
    l2 = Label(image=test)
    l2.image = test
    l2.grid(row=2, column=2, pady=(15,5),columnspan = 2,padx=(5,5))




b1 = Button(window, text='Rotate to the left', command=sola,font=("Arial",10), width=16, height=1, bg='#000066',fg='white')
b1.grid(row=0, column=0 , columnspan = 1, padx=(7,5),pady=(8,5))


b2 = Button(window, text='Rotate to the right', command=sag,font=("Arial",10), width=16, height=1, bg='#000066',fg='white')
b2.grid(row=0, column=1 , columnspan = 1, padx=(5,5),pady=(8,5))


b3 = Button(window, text='Reflect Vertically', command=vert,font=("Arial",10), width=16, height=1, bg='#000066',fg='white')
b3.grid(row=0, column=2 , columnspan = 1, padx=(5,5),pady=(8,5))


b4 = Button(window, text='Reflect Horizontally', command=hor,font=("Arial",10), width=16, height=1, bg='#000066',fg='white')
b4.grid(row=0, column=3 , columnspan = 1, padx=(5,5),pady=(8,5))


b5 = Button(window, text='Enhance Contrast', command=kon,font=("Arial",10), width=16, height=1, bg='#006622',fg='white')
b5.grid(row=1, column=0 , columnspan = 1, padx=(7,5),pady=(5,5))


b6 = Button(window, text='Enhance Brightness', command=par,font=("Arial",10), width=16, height=1, bg='#006622',fg='white')
b6.grid(row=1, column=1 , columnspan = 1, padx=(5,5),pady=(5,5))


b7 = Button(window, text='Shades of Grey', command=qar,font=("Arial",10), width=35, height=1, bg='#800000',fg='white')
b7.grid(row=1, column=2 , columnspan = 2, padx=(5,5),pady=(5,5))





image_or = Image.open(filename)
image_or.thumbnail((280, 280))
test = ImageTk.PhotoImage(image_or)
l1 = Label(image=test)
l1.image = test
l1.grid(row=2, column=0, pady=(15,5),columnspan = 2,padx=(5,5))


image_or1 = Image.open("def_eff.png")
image_or1.thumbnail((280, 280))
test = ImageTk.PhotoImage(image_or1)
l2 = Label(image=test)
l2.image = test
l2.grid(row=2, column=2, pady=(15,5),columnspan = 2,padx=(5,5))


window.mainloop()