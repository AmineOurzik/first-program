import tkinter as tk
from random import *

#configuration des fonctions
def jeu(outil):
    comp_pick = randint(-1,1)


#configuration de la fenêtre
window = tk.Tk()
window.title("Jeu de pierre, feuille, ciseaux")
window_width = 725
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
window.iconbitmap("icone jeu.ico")
bg_color = "#4b3832"
window.configure(bg= bg_color)
titre = tk.Label(
    master = window, 
    text ="Pierre, Feuille, Ciseaux", 
    font = ("Cooper Black", 22),
    relief = tk.GROOVE,
    borderwidth= 6,
    bg = "#fff4e6",
    fg = "#3c2f2f"
                )
button_pierre = tk.Button(
    master = window,
    text = "Pierre",
    font = ("Berlin Sans FB", 18),
    bg= "#be9b7b",
    fg= "#3c2f2f",
    borderwidth= 2)
button_feuille = tk.Button(
    master = window,
    text = "Feuille",
    font = ("Berlin Sans FB", 18),
    bg= "#be9b7b",
    fg= "#3c2f2f",
    borderwidth= 2)
button_ciseaux = tk.Button(
    master = window,
    text = "Ciseaux",
    font = ("Berlin Sans FB", 18),
    bg= "#be9b7b",
    fg= "#3c2f2f",
    borderwidth= 2)

window.columnconfigure((0,1,2,3,4,5,6), weight=1)
window.rowconfigure((0,1,2,3,4,5,6), weight=1)
titre.grid(row=0, column=2, sticky="n", columnspan= 3)
button_pierre.grid(column=2, row=5)
button_feuille.grid(column=3, row=5)
button_ciseaux.grid(column=4, row= 5)



window.mainloop()