from tkinter import *
from random import randint


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

#def cilvēks():
    
'''
Linija1=ekrans.create_line(550, 100, 550, 420)
Linija2=ekrans.create_line(500, 100, 550, 150)
Linija3=ekrans.create_line(400, 100, 550, 100)
Linija4=ekrans.create_line(400, 100, 400, 150)
Ovals1=ekrans.create_oval(375, 150, 425, 200)
Linija6=ekrans.create_line(400, 200, 400, 300)
Linija7=ekrans.create_line(400, 200, 450, 250)
Linija8=ekrans.create_line(400, 200, 350, 250)
Linija9=ekrans.create_line(400, 300, 450, 350)
Linija10=ekrans.create_line(400, 300, 350, 350)
'''

#def spoks():

Linija1=ekrans.create_line(550, 100, 550, 420)
Linija2=ekrans.create_line(500, 100, 550, 150)
Linija3=ekrans.create_line(400, 100, 550, 100)
Linija4=ekrans.create_line(400, 100, 400, 150)
points1 = [400, 150, 360, 150, 340, 180, 340, 200, 340, 220, 340, 350]
Linija5=ekrans.create_line(points1)
points2 = [400, 150, 440, 150, 460, 180, 460, 200, 460, 220, 460, 350]
Linija6=ekrans.create_line(points2)
points3 = [340, 350, 360, 325, 380, 350, 400, 325, 420, 350, 440, 325, 460, 350]
Linija7=ekrans.create_line(points3)
Ovals1=ekrans.create_oval(350, 180, 390, 240)
Ovals2=ekrans.create_oval(410, 180, 450, 240)
Linija10=ekrans.create_line(380, 260, 420, 260)

#def nāve():

'''
Linija1=ekrans.create_line(550, 100, 550, 420)
Linija2=ekrans.create_line(500, 100, 550, 150)
Linija3=ekrans.create_line(400, 100, 550, 100)
Linija4=ekrans.create_line(400, 100, 400, 150)
Ovals1=ekrans.create_oval(375, 150, 425, 200)
Trijstūris1=ekrans.create_polygon(340, 350, 400, 200, 460, 350)
Linija7=ekrans.create_line(400, 200, 450, 250)
Linija8=ekrans.create_line(400, 200, 350, 250)
Linija9=ekrans.create_line(350, 160, 350, 310)
Trijstūris1=ekrans.create_polygon(250, 165, 350, 160, 350, 170)
'''

'''
=======Tastatūras pogu noteikšana========
Vajag pievienot:
-displeju
-karātavas
-...
'''

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
        print("dunduk,",char,"burts jau atminēts")
    else:
        kļūdas+=1
        print("ahahah tu alkāns. Kļūdu skaits:",kļūdas)
        if kļūdas > pieļaujamais_kļūdu_skaits:
            #piesaista funkciju, kas displejo zaudes ekrānu
            print("losis")
            pass


root.bind("<Key>", pogas_spiediens)

#strādā linijas ja atseviški pie karātavām uzliek tā vismaz man nestrādā
def linijas():
    global vārds, char
    if vārds == "atkals":
        a=ekrans.create_line(50, 100, 70, 100)
        t=ekrans.create_line(80, 100, 100, 100)
        k=ekrans.create_line(110, 100, 130, 100)
        a=ekrans.create_line(140, 100, 160, 100)
        l=ekrans.create_line(170, 100, 190, 100)
        s=ekrans.create_line(200, 100, 220, 100)
    elif vārds == "ābols":
        ā=ekrans.create_line(50, 100, 70, 100)
        b=ekrans.create_line(80, 100, 100, 100)
        o=ekrans.create_line(110, 100, 130, 100)
        l=ekrans.create_line(140, 100, 160, 100)
        s=ekrans.create_line(170, 100, 190, 100)
    else:
        ž=ekrans.create_line(50, 100, 70, 100)
        ā=ekrans.create_line(80, 100, 100, 100)
        v=ekrans.create_line(110, 100, 130, 100)
        ā=ekrans.create_line(140, 100, 160, 100)
        t=ekrans.create_line(170, 100, 190, 100)
        i=ekrans.create_line(200, 100, 220, 100)
        e=ekrans.create_line(230, 100, 250, 100)
        s=ekrans.create_line(260, 100, 280, 100)

def atkals():
    global vārds, char
    if char == "a" in vārds == "atkals":
        ekrans.create_text(60, 85, text="a", fill="black", font=("Helvetica", 30))
        ekrans.create_text(150, 85, text="a", fill="black", font=("Helvetica", 30))
    elif char == "t" in vārds == "atkals":
        ekrans.create_text(90, 85, text="t", fill="black", font=("Helvetica", 30))
    elif char == "k" in vārds == "atkals":
       ekrans.create_text(120, 85, text="k", fill="black", font=("Helvetica", 30))
    elif char == "l" in vārds == "atkals":
       ekrans.create_text(180, 85, text="l", fill="black", font=("Helvetica", 30))
    elif char == "s" in vārds == "atkals":
       ekrans.create_text(210, 85, text="s", fill="black", font=("Helvetica", 30))
    else:
        ekrans.create_text(60, 150, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(120, 150, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(180, 150, text=char =='', fill="black", font=("Helvetica", 30))

        ekrans.create_text(60, 200, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(120, 200, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(180, 200, text=char =='', fill="black", font=("Helvetica", 30))

        ekrans.create_text(60, 250, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(120, 250, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(180, 250, text=char =='', fill="black", font=("Helvetica", 30))

        ekrans.create_text(60, 300, text=char =='', fill="black", font=("Helvetica", 30))


def ābols():
    global vārds, char
    if char == "ā" in vārds == "ābols":
        ekrans.create_text(60, 85, text="ā", fill="black", font=("Helvetica", 30))
    elif char == "b" in vārds == "ābols":
        ekrans.create_text(90, 85, text="b", fill="black", font=("Helvetica", 30))
    elif char == "o" in vārds == "ābols":
       ekrans.create_text(120, 85, text="o", fill="black", font=("Helvetica", 30))
    elif char == "l" in vārds == "ābols":
      ekrans.create_text(150, 85, text="l", fill="black", font=("Helvetica", 30))
    elif char == "s" in vārds == "ābols":
       ekrans.create_text(180, 85, text="s", fill="black", font=("Helvetica", 30))
    else:
        ekrans.create_text(60, 150, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(120, 150, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(180, 150, text=char =='', fill="black", font=("Helvetica", 30))

        ekrans.create_text(60, 200, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(120, 200, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(180, 200, text=char =='', fill="black", font=("Helvetica", 30))

        ekrans.create_text(60, 250, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(120, 250, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(180, 250, text=char =='', fill="black", font=("Helvetica", 30))

        ekrans.create_text(60, 300, text=char =='', fill="black", font=("Helvetica", 30))

def žāvāties():
    global vārds, char
    if char == "ā" in vārds == "žāvāties":
        ekrans.create_text(90, 85, text="ā", fill="black", font=("Helvetica", 30))
        ekrans.create_text(150, 85, text="ā", fill="black", font=("Helvetica", 30))
    elif char == "ž" in vārds == "žāvāties":
        ekrans.create_text(60, 85, text="ž", fill="black", font=("Helvetica", 30))
    elif char == "v" in vārds == "žāvāties":
       ekrans.create_text(120, 85, text="v", fill="black", font=("Helvetica", 30))
    elif char == "t" in vārds == "žāvāties":
       ekrans.create_text(180, 85, text="t", fill="black", font=("Helvetica", 30))
    elif char == "i" in vārds == "žāvāties":
       ekrans.create_text(210, 85, text="i", fill="black", font=("Helvetica", 30))
    elif char == "e" in vārds == "žāvāties":
        ekrans.create_text(240, 85, text="e", fill="black", font=("Helvetica", 30))
    elif char == "s" in vārds == "žāvāties":
        ekrans.create_text(270, 85, text="s", fill="black", font=("Helvetica", 30))
    else:
        ekrans.create_text(60, 150, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(120, 150, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(180, 150, text=char =='', fill="black", font=("Helvetica", 30))

        ekrans.create_text(60, 200, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(120, 200, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(180, 200, text=char =='', fill="black", font=("Helvetica", 30))

        ekrans.create_text(60, 250, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(120, 250, text=char =='', fill="black", font=("Helvetica", 30))
        ekrans.create_text(180, 250, text=char =='', fill="black", font=("Helvetica", 30))

        ekrans.create_text(60, 300, text=char =='', fill="black", font=("Helvetica", 30))

def kļūdas_cilvēks():
    global kļūdas
    if kļūdas == 1:
        Linija1=ekrans.create_line(550, 100, 550, 420)
    elif kļūdas == 2:
        Linija2=ekrans.create_line(500, 100, 550, 150)
    elif kļūdas == 3:
        Linija3=ekrans.create_line(400, 100, 550, 100)
    elif kļūdas == 4:
        Linija4=ekrans.create_line(400, 100, 400, 150)
    elif kļūdas == 5:
        Ovals1=ekrans.create_oval(375, 150, 425, 200)
    elif kļūdas == 6:
        Linija6=ekrans.create_line(400, 200, 400, 300)
    elif kļūdas == 7:
        Linija7=ekrans.create_line(400, 200, 450, 250)
    elif kļūdas == 8:
        Linija8=ekrans.create_line(400, 200, 350, 250)
    elif kļūdas == 9:
        Linija9=ekrans.create_line(400, 300, 450, 350)
    elif kļūdas == 10:
        Linija10=ekrans.create_line(400, 300, 350, 350)

def kļūdas_spoks():
    global kļūdas
    if kļūdas == 1:
        Linija1=ekrans.create_line(550, 100, 550, 420)
    elif kļūdas == 2:
        Linija2=ekrans.create_line(500, 100, 550, 150)
    elif kļūdas == 3:
        Linija3=ekrans.create_line(400, 100, 550, 100)
    elif kļūdas == 4:
        Linija4=ekrans.create_line(400, 100, 400, 150)
    elif kļūdas == 5:
        points1 = [400, 150, 360, 150, 340, 180, 340, 200, 340, 220, 340, 350]
        Linija5=ekrans.create_line(points1)
    elif kļūdas == 6:
        points2 = [400, 150, 440, 150, 460, 180, 460, 200, 460, 220, 460, 350]
        Linija6=ekrans.create_line(points2)
    elif kļūdas == 7:
        points3 = [340, 350, 360, 325, 380, 350, 400, 325, 420, 350, 440, 325, 460, 350]
        Linija7=ekrans.create_line(points3)
    elif kļūdas == 8:
        Ovals1=ekrans.create_oval(350, 180, 390, 240)
    elif kļūdas == 9:
        Ovals2=ekrans.create_oval(410, 180, 450, 240)
    elif kļūdas == 10:
        Linija10=ekrans.create_line(380, 260, 420, 260)

def kļūdas_nāve():
    global kļūdas
    if kļūdas == 1:
        Linija1=ekrans.create_line(550, 100, 550, 420)
    elif kļūdas == 2:
        Linija2=ekrans.create_line(500, 100, 550, 150)
    elif kļūdas == 3:
        Linija3=ekrans.create_line(400, 100, 550, 100)
    elif kļūdas == 4:
        Linija4=ekrans.create_line(400, 100, 400, 150)
    elif kļūdas == 5:
        Ovals1=ekrans.create_oval(375, 150, 425, 200)
    elif kļūdas == 6:
        Trijstūris1=ekrans.create_polygon(340, 350, 400, 200, 460, 350)
    elif kļūdas == 7:
        Linija7=ekrans.create_line(400, 200, 450, 250)
    elif kļūdas == 8:
        Linija8=ekrans.create_line(400, 200, 350, 250)
    elif kļūdas == 9:
        Linija9=ekrans.create_line(350, 160, 350, 310)
    elif kļūdas == 10:
        Trijstūris1=ekrans.create_polygon(250, 165, 350, 160, 350, 170)

#lietas, kuras būs jāatjauno, kad izveido jaunu spēli. NOT FINISHED (nav pat funkcijas lol)
vārds = jauns_vārds(vārdi)
print(vārds)#priekš testēšanas
char = ''
kļūdas = 0
pieļaujamais_kļūdu_skaits = 10
atminētie_burti = ''

root.mainloop()
