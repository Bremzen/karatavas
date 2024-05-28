from tkinter import *
from random import randint

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

vārdi = ["atkals","ābols","žāvāties"]

def jauns_vārds(vārdi):
    return vārdi[randint(0,len(vārdi)-1)]

'''
=======GUI izveide========
'''

root = Tk()
ekrans = Canvas(root, width=600, height=500)
ekrans.pack()

ekrans.create_text(280, 100, text="Karātavas", fill="black", font=("Helvetica", 30))

class KarātavasDaļas:
    def __init__(self,detaļas):
        self.detaļas = list(detaļas)
        self.skaits = 0

    def parādīt_detaļu(self):
        command = getattr(ekrans, self.detaļas[self.skaits][0][0])
        command(*self.detaļas[self.skaits][1])
        self.skaits+=1

Char = KarātavasDaļas(Nāve)

def pogas_spiediens(event):
    global char
    char = event.char.lower()
    if char.isalpha():
        minēt()
        #print("Pressed", repr(char))

def izdzēst_char(word, char):
    return word.replace(char, '')

'''
=======Tastatūras pogu noteikšana========
'''
def minēt():
    global char, vārds, kļūdas, atminētie_burti
    if char in vārds:
        print("cepums tev")
        vārds = izdzēst_char(vārds,char)
        atminētie_burti += char
        print(vārds)
        if vārds == '':
            print("woow, malacītis!")
    elif char in atminētie_burti:
        print("dunduk,",char,"burts jau minēts")
    else:
        atminētie_burti+=char
        kļūdas+=1
        Char.parādīt_detaļu()
        print("ahahah tu alkāns. Kļūdu skaits:",kļūdas)
        if kļūdas > pieļaujamais_kļūdu_skaits:
            #piesaista funkciju, kas displejo zaudes ekrānu
            print("losis")
            pass


root.bind("<Key>", pogas_spiediens)



#lietas, kuras būs jāatjauno, kad izveido jaunu spēli. NOT FINISHED (nav pat funkcijas lol)
vārds = jauns_vārds(vārdi)
print(vārds)#priekš testēšanas
char = ''
kļūdas = 0
pieļaujamais_kļūdu_skaits = 10
atminētie_burti = ''

root.mainloop()
