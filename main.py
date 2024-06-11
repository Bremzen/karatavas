from tkinter import *
from random import randint
import time

'''
=======Spēles mošķi========
'''

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
    [["create_line"],[550, 100, 550, 420]], 
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
with open("vārdi.txt","r", encoding="utf-8") as f:
    vārdi = [rinda.strip() for rinda in f]

def jauns_vārds(vārdi):
    return vārdi[randint(0,len(vārdi)-1)]

'''
=======Jauna spēle========
'''

def jauna_spēle():
    global vārds, char, kļūdas, pieļaujamais_kļūdu_skaits, minētie_burti, vārds2
    vārds = jauns_vārds(vārdi)
    vārds2 = vārds
    print(vārds)#priekš testēšanas
    char = ''
    kļūdas = 0
    pieļaujamais_kļūdu_skaits = 10
    minētie_burti = ''
    dzēst_minēšanas_vārda_gui()
    Char.dzēst_parādītās_detaļas() #nodzēš iepriekšējo mošķi
    #noņem sākuma ekrānu
    ekrans.delete(nosaukums)
    poga.destroy()
    galvenais_gui()

def pirms_jauna_spēle():
    ekrans.delete(zaudes_teksts)
    pogaZaude.place_forget()
    dzēst_minēšanas_burta_gui()
    jauna_spēle()

'''
=======GUI izveide=================================
'''

root = Tk()
root.title('Karātavas')
ekrans = Canvas(root, width=600, height=500)
ekrans.pack()
x,y = 600,500
def galvenais_gui():
    global minējuma_burts, minējuma_teksts
    minējuma_teksts = ekrans.create_text(10,200, text='Tavs minētais burts: ', font=("Times New Roman", 20), anchor="w")
    minējuma_burts = ekrans.create_text(230,200, text=char, font=("Times New Roman", 20), anchor="w")
    minēšanas_vārda_gui()

def minēšanas_vārda_gui():
    for i in range(len(vārds2)):
        var_name = f'varline_{i}'
        globals()[var_name] = ekrans.create_line(30+i*40,250,50+i*40,250)

def minēšanas_burta_gui():
    global vārds2
    while char in vārds2:
         i = vārds2.index(char)
         print(i)
         var_name = f'varlet_{i}'
         globals()[var_name] = ekrans.create_text(40 + i * 40, 240, text=char.upper(), font=("Times New Roman", 20))
         vārds2 = vārds2[:i] + '0' + vārds2[i+1:]
            

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
    ekrans.delete(minējuma_burts,minējuma_teksts)
    zaudes_teksts = ekrans.create_text(80, 150, anchor='w', text="Tu zaudēji!", fill="black", font=("Helvetica", 30))
    pogaZaude.place(x=x/2,y=y/2, anchor="center", height='30',width='150')

'''
=======Sākuma ekrāns, pogas========
'''
nosaukums = ekrans.create_text(x/2, 150, anchor="center", text="Karātavas", fill="black", font=("Helvetica", 30))
poga = Button(ekrans, text='Spēlēt',command=jauna_spēle)
pogaZaude = Button(ekrans,text='Spēlēt atkal?',command=pirms_jauna_spēle)
poga.place(x=x/2,y=y/2, anchor="center", height='30',width='150')

'''
=======Zīmējuma daļu rādīšana========
'''

class KarātavasDaļas:
    def __init__(self,detaļas):
        self.detaļas = list(detaļas)
        self.skaits = 0

    def parādīt_detaļu(self):
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
        print("cepums tev")
        vārds = izdzēst_char(vārds,char)
        minētie_burti += char
        print(vārds)
        minēšanas_burta_gui()
        if vārds == '':
            print("woow, malacītis!")
    elif char in minētie_burti:
        print("dunduk,",char,"burts jau minēts")
    else:
        minētie_burti+=char
        kļūdas+=1
        Char.parādīt_detaļu()
        print("Kļūdu skaits:",kļūdas,char)
        if kļūdas == pieļaujamais_kļūdu_skaits:
            print("losis")
            ekrans.after(1000)
            zaudēšanas_gui()
            pass

def izdzēst_char(word, char):
    return word.replace(char, '')


root.bind("<Key>", pogas_spiediens)

root.mainloop()
