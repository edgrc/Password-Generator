import string
from random import randint, choice
from tkinter import *

def generate_password() :
    password_min = 12
    password_max = 16
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join((choice(all_chars)) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)



# creer la fenètre
window = Tk()
window.title ("Générateur de mot de passe")
window.geometry("950x800")
window.iconbitmap("password_icon.ico")
window.config(background='#4065A4')

# creer la frame principale
frame = Frame(window, bg='#4065A4')

# création d'image
width = 600
height = 600
image = PhotoImage(file="Sans titre(67).png")
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(300, 350, image=image)
canvas.pack()

# creer un titre
label_title = Label(frame, text="Votre nouveau mot de passe", font=("Impact", 30), bg='#4065A4', fg='white')
label_title.pack()

# creer un input
password_entry = Entry(frame, text="Mot de passe", font=("Arial", 20), bg='#4065A4', fg='white')
password_entry.pack()

# creer un bouton
generate_password_button = Button(frame, text="Générer ici", font=("Helvetica", 22), bg='#e3702a', fg='white', command=generate_password)
generate_password_button.pack()


#affciher la frame
frame.pack(expand=YES)


#creation d'une barre de menu
menu_bar = Menu(window)
#creer un premier menu
file_menu= Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade (label="Fichier", menu=file_menu)

# configuer notre fenetre pour ajouter cette menu bar
window.config(menu=menu_bar)

# aficher la fenetre
window.mainloop()


