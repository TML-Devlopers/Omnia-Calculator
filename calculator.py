import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import math

def hakkinda_penceresi_ac():
    hakkinda_pencere = tk.Toplevel(pencere)
    hakkinda_pencere.title("About - Omnia")
    hakkinda_pencere.geometry("500x250")
    hakkinda_pencere.resizable(False, False)
    hakkinda_pencere.grab_set()

    # Simgeyi yükle ve boyutunu küçült
    try:
        icon_image = Image.open("icon.png")
        icon_image = icon_image.resize((32, 32))
        icon_photo = ImageTk.PhotoImage(icon_image)

        baslik_etiketi = tk.Label(hakkinda_pencere, text=" Omnia Calculator", font=("Arial", 18, "bold"), image=icon_photo, compound="left")
        baslik_etiketi.image = icon_photo # Resmin kaybolmaması için referansı tut
    except:
        baslik_etiketi = tk.Label(hakkinda_pencere, text="Omnia Calculator", font=("Arial", 18, "bold"))

    baslik_etiketi.pack(pady=10)

    cizgi1 = tk.Canvas(hakkinda_pencere, height=1, bg="black")
    cizgi1.pack(fill="x", padx=15)

    versiyon_yazi = """
Version 1.0 (Build 2025-08-11)
© 2025 Omnia. All rights reserved.
"""
    versiyon_etiketi = tk.Label(hakkinda_pencere, text=versiyon_yazi, font=("Arial", 10), justify="left")
    versiyon_etiketi.pack(padx=20, pady=10)

    tamam_butonu = tk.Button(hakkinda_pencere, text="Ok", width=10, command=hakkinda_pencere.destroy)
    tamam_butonu.pack(side="right", padx=20, pady=10)


def tus_basildi(tus_degeri):
    global ifade
    if tus_degeri == 'C':
        ifade = ""
    elif tus_degeri == 'CE':
        ifade = ""
    elif tus_degeri == '√':
        try:
            sonuc = str(math.sqrt(float(ifade)))
            if 'e' in sonuc:
                ifade = "Error"
            else:
                ifade = sonuc
        except:
            ifade = "Error"
    elif tus_degeri == '=':
        try:
            if 'x' in ifade:
                ifade = ifade.replace('x', '*')
            if '÷' in ifade:
                ifade = ifade.replace('÷', '/')
            sonuc = str(eval(ifade))
            ifade = sonuc
        except:
            ifade = "Error"
    elif tus_degeri == 'BackSpace':
        ifade = ifade[:-1]
    else:
        if ifade == "0" or ifade == "Error":
            ifade = ""
        ifade += str(tus_degeri)
    sonuc_ekrani.set(ifade)

def klavye_tus_basildi(event):
    tus_adi = event.keysym
    if tus_adi == 'Return':
        tus_basildi('=')
    elif tus_adi == 'Escape':
        tus_basildi('C')
    elif tus_adi == 'BackSpace':
        tus_basildi('BackSpace')
    elif tus_adi == 'asterisk':
        tus_basildi('x')
    elif tus_adi == 'slash':
        tus_basildi('÷')
    else:
        tus_basildi(event.char)

pencere = tk.Tk()
pencere.title("Calculator - Omnia")
pencere.geometry("350x500")
pencere.resizable(False, False)

pencere.iconbitmap('icon.ico')

pencere.bind('<Key>', klavye_tus_basildi)

style = ttk.Style(pencere)
style.configure('Aero.TButton', 
    font=('Arial', 18), 
    padding=(8, 8),
    relief="ridge",  
    borderwidth=2,
    background='#D6DCE7', 
    foreground='black'
)
style.map('Aero.TButton', background=[('active', '#F2F5F8')])

menu_bar = tk.Menu(pencere)
pencere.config(menu=menu_bar)

yardim_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=yardim_menu)
yardim_menu.add_command(label="About", command=hakkinda_penceresi_ac)

ifade = ""
sonuc_ekrani = tk.StringVar()
sonuc_ekrani.set("0")

ekran = tk.Label(pencere, textvariable=sonuc_ekrani, font=("Arial", 24), bg="white", anchor="e", padx=10, relief="sunken", bd=3)
ekran.pack(fill="x", pady=10)

tuslar_cercevesi = tk.Frame(pencere)
tuslar_cercevesi.pack()

tuslar = [
    ('√', 1, 0), ('CE', 1, 1), ('C', 1, 2), ('÷', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('x', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2),
    ('{', 6, 0), ('}', 6, 1), ('∪', 6, 2), ('∩', 6, 3),
]

for (tus_degeri, satir, sutun) in tuslar:
    tus = ttk.Button(tuslar_cercevesi, text=tus_degeri, style='Aero.TButton', width=4, command=lambda tus_degeri=tus_degeri: tus_basildi(tus_degeri))
    tus.grid(row=satir, column=sutun, padx=5, pady=5)

pencere.mainloop()