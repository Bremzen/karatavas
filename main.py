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
    global vārds, char, kļūdas, pieļaujamais_kļūdu_skaits, minētie_burti
    vārds = jauns_vārds(vārdi)
    print(vārds)#priekš testēšanas
    char = ''
    kļūdas = 0
    pieļaujamais_kļūdu_skaits = 10
    minētie_burti = ''
    Char.dzēst_parādītās_detaļas() #nodzēš iepriekšējo mošķi
    #noņem sākuma ekrānu
    ekrans.delete(nosaukums)
    poga.destroy()


'''
=======GUI izveide=================================
'''

root = Tk()
root.title('Karātavas')
ekrans = Canvas(root, width=600, height=500)
ekrans.pack()
x,y = 600,500

'''
=======Sākuma ekrāns========
'''
nosaukums = ekrans.create_text(x/2, 150, anchor="center", text="Karātavas", fill="black", font=("Helvetica", 30))
poga = Button(ekrans, text='Spēlēt',command=jauna_spēle)
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
    global char
    char = event.char.lower()
    if char.isalpha() and kļūdas < pieļaujamais_kļūdu_skaits:
        minēt()

def minēt():
    global char, vārds, kļūdas, minētie_burti
    if char in vārds:
        print("cepums tev")
        vārds = izdzēst_char(vārds,char)
        minētie_burti += char
        print(vārds)
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
            ekrans.after(1000)
            #piesaista funkciju, kas displejo zaudes ekrānu
            print("losis")
            pass

def izdzēst_char(word, char):
    return word.replace(char, '')


root.bind("<Key>", pogas_spiediens)

root.mainloop()
