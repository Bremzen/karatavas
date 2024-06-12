from tkinter import *
from random import randint
import time

'''
=======Spēles mošķi========
'''
Chars = {"Cilvēks": "Cilvēks", "Spoks": "Spoks", "Nāve": "Nāve"}
Cilvēks = [
    [["create_line"], [550, 100, 550, 420]],
    [["create_line"], [500, 100, 550, 150]],
    [["create_line"], [400, 100, 550, 100]],
    [["create_line"], [400, 100, 400, 150]],
    [["create_oval"], [375, 150, 425, 200]],
    [["create_line"], [400, 200, 400, 300]],
    [["create_line"], [400, 200, 450, 250]],
    [["create_line"], [400, 200, 350, 250]],
    [["create_line"], [400, 300, 450, 350]],
    [["create_line"], [400, 300, 350, 350]],
]
Spoks = [
    [["create_line"], [550, 100, 550, 420]],
    [["create_line"], [500, 100, 550, 150]],
    [["create_line"], [400, 100, 550, 100]],
    [["create_line"], [400, 100, 400, 150]],
    [["create_line"], [400, 150, 360, 150, 340, 180, 340, 200, 340, 220, 340, 350]],
    [["create_line"], [400, 150, 440, 150, 460, 180, 460, 200, 460, 220, 460, 350]],
    [["create_line"], [340, 350, 360, 325, 380, 350, 400, 325, 420, 350, 440, 325, 460, 350]],
    [["create_oval"], [350, 180, 390, 240]],
    [["create_oval"], [410, 180, 450, 240]],
    [["create_line"], [380, 260, 420, 260]],
]
Nāve = [
    [["create_line"], [550, 100, 550, 420]],
    [["create_line"], [500, 100, 550, 150]],
    [["create_line"], [400, 100, 550, 100]],
    [["create_line"], [400, 100, 400, 150]],
    [["create_oval"], [375, 150, 425, 200]],
    [["create_polygon"], [340, 350, 400, 200, 460, 350]],
    [["create_line"], [400, 200, 450, 250]],
    [["create_line"], [400, 200, 350, 250]],
    [["create_line"], [350, 160, 350, 310]],
    [["create_polygon"], [250, 165, 350, 160, 350, 170]],
]

'''
=======Vārda iegūšana========
'''
with open("vārdi.txt", "r", encoding="utf-8") as f:
    vārdi = [rinda.strip() for rinda in f]

def jauns_vārds(vārdi):
    return vārdi[randint(0, len(vārdi) - 1)]

'''
=======Jauna spēle========
'''

def jauna_spēle():
    global vārds, char, kļūdas, pieļaujamais_kļūdu_skaits, minētie_burti, vārds2, Char
    root.bind("<Key>", pogas_spiediens)
    vārds = jauns_vārds(vārdi)
    vārds2 = vārds
    #print(vārds)  # priekš testēšanas
    char = ''
    kļūdas = 0
    pieļaujamais_kļūdu_skaits = 10
    minētie_burti = ''
    dzēst_minēšanas_vārda_gui()
    Char.dzēst_parādītās_detaļas()  # nodzēš iepriekšējo mošķi
    # noņem sākuma ekrānu
    ekrans.delete(nosaukums)
    ekrans.delete(mošķa_teksts)
    poga.destroy()
    mošķu_izvēle.destroy()
    galvenais_gui()

def pirms_jauna_spēle():
    if 'zaudes_teksts' in globals():
        ekrans.delete(zaudes_teksts)
    if 'uzvaras_teksts' in globals():
        ekrans.delete(uzvaras_teksts)
    poga_spēlēt_atkal.place_forget()
    dzēst_minēšanas_vārda_gui()
    dzēst_minēšanas_burta_gui()
    jauna_spēle()

'''
=======GUI izveide=================================
'''

root = Tk()
root.title('Karātavas')
ekrans = Canvas(root, width=600, height=500)
ekrans.pack()
x, y = 600, 500
chosen_char = StringVar(root)
chosen_char.set("Cilvēks")  # Default value

def galvenais_gui():
    global minējuma_burts, minējuma_teksts, Char
    selected = chosen_char.get()
    if selected == "Cilvēks":
        Char = KarātavasDaļas(Cilvēks)
    elif selected == "Spoks":
        Char = KarātavasDaļas(Spoks)
    else:
        Char = KarātavasDaļas(Nāve)
    
    minējuma_teksts = ekrans.create_text(30, 200, text='Tavs minētais burts: ', font=("Times New Roman", 20), anchor="w")
    minējuma_burts = ekrans.create_text(250, 200, text=char, font=("Times New Roman", 20), anchor="w")
    minēšanas_vārda_gui()

def minēšanas_vārda_gui():
    for i in range(len(vārds2)):
        var_name = f'varline_{i}'
        globals()[var_name] = ekrans.create_line(30 + i * 40, 250, 50 + i * 40, 250)

def minēšanas_burta_gui():
    global vārds2
    while char in vārds2:
        i = vārds2.index(char)
        var_name = f'varlet_{i}'
        globals()[var_name] = ekrans.create_text(40 + i * 40, 240, text=char.upper(), font=("Times New Roman", 20))
        vārds2 = vārds2[:i] + '0' + vārds2[i + 1:]

def dzēst_minēšanas_vārda_gui():
    for i in range(len(vārds2)):
        var_name = f'varline_{i}'
        if var_name in globals():
            ekrans.delete(globals()[var_name])

def dzēst_minēšanas_burta_gui():
    for i in range(len(vārds2)):
        var_name = f'varlet_{i}'
        if var_name in globals():
            ekrans.delete(globals()[var_name])

def zaudēšanas_gui():
    global zaudes_teksts
    ekrans.delete(minējuma_burts, minējuma_teksts)
    zaudes_teksts = ekrans.create_text(80, 150, anchor='w', text="Tu zaudēji!", fill="black", font=("Helvetica", 30))
    poga_spēlēt_atkal.place(x=120, y=460, anchor="center", height='30', width='150')

def uzvaras_gui():
    global uzvaras_teksts
    root.unbind("<Key>")
    ekrans.delete(minējuma_burts,minējuma_teksts)
    uzvaras_teksts = ekrans.create_text(80, 150, anchor='w', text="Tu uzvarēji!", fill="black", font=("Helvetica", 30))
    poga_spēlēt_atkal.place(x=120, y=460, anchor="center", height='30', width='150')
    dzēst_minēšanas_vārda_gui()

'''
=======Sākuma ekrāns, pogas========
'''
nosaukums = ekrans.create_text(x/2, 150, anchor="center", text="Karātavas", fill="black", font=("Helvetica", 30))
mošķa_teksts = ekrans.create_text(x/2, 300, anchor="center", text="Izvēlies mošķi", fill="black", font=("Helvetica", 15))
mošķu_izvēle = OptionMenu(root, chosen_char, *Chars.values())
mošķu_izvēle.place(x=x/2, y=350, anchor="center", height='25', width='150')
poga = Button(root, text='Spēlēt', command=jauna_spēle)
poga_spēlēt_atkal = Button(root, text='Spēlēt atkal?', command=pirms_jauna_spēle)
poga.place(x=x/2, y=220, anchor="center", height='30', width='150')

'''
=======Zīmējuma daļu rādīšana========
'''

class KarātavasDaļas:
    def __init__(self, detaļas):
        self.detaļas = list(detaļas)
        self.skaits = 0

    def parādīt_detaļu(self):
        if self.skaits < len(self.detaļas):
            command_name = self.detaļas[self.skaits][0][0]
            command_args = self.detaļas[self.skaits][1]
            command = getattr(ekrans, command_name)
            var_name = f'var_{self.skaits}'
            globals()[var_name] = command(*command_args)
            self.skaits += 1

    def dzēst_parādītās_detaļas(self):
        for i in range(self.skaits):
            var_name = f'var_{i}'
            if var_name in globals():
                ekrans.delete(globals()[var_name])
        self.skaits = 0

Char = KarātavasDaļas(Spoks)

'''
=======Spēles loģiskā daļa========
'''
def pogas_spiediens(event):
    global char, minējuma_burts
    char = event.char.lower()
    if char.isalpha() and kļūdas < pieļaujamais_kļūdu_skaits:
        minēt()
        ekrans.itemconfig(minējuma_burts, text=char)

def minēt():
    global char, vārds, kļūdas, minētie_burti
    if char in vārds:
        
        vārds = izdzēst_char(vārds, char)
        minētie_burti += char
        #print(vārds)
        minēšanas_burta_gui()
        if vārds == '':
            uzvaras_gui()
    elif char in minētie_burti:
        pass #not used
    else:
        minētie_burti += char
        kļūdas += 1
        Char.parādīt_detaļu()
        #print("Kļūdu skaits:", kļūdas, char)
        if kļūdas == pieļaujamais_kļūdu_skaits:
            zaudēšanas_gui()
            ekrans.after(1000)

def izdzēst_char(word, char):
    return word.replace(char, '')


root.mainloop()