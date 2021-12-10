from os import O_TRUNC
from tkinter import *

root =Tk()
insert_pozicija = 0
boja_dugmeta = "white"
#------------------------------------------------------------
def jednako():
    global ukupno
    global insert_pozicija
    global krajni_rezultat
    ukupno = izlaz.get()
    krajni_rezultat = str(eval(ukupno))
    izlaz.delete(0,END)
    izlaz.insert(0,krajni_rezultat)

def tacka():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,".")
    insert_pozicija = insert_pozicija + 1
#------------------------------------------------------------
def dugme_sedam():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"7")
    insert_pozicija = insert_pozicija + 1

def dugme_osam():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"8")
    insert_pozicija = insert_pozicija + 1

def dugme_devet():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"9")
    insert_pozicija = insert_pozicija + 1

def karakter_minus():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"-")
    insert_pozicija = insert_pozicija + 1
#-------------------------------------------------------------
def dugme_cetiri():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"4")
    insert_pozicija = insert_pozicija + 1

def dugme_pet():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"5")
    insert_pozicija = insert_pozicija + 1

def dugme_sest():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"6")
    insert_pozicija = insert_pozicija + 1

def karakter_plus():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"+")
    insert_pozicija = insert_pozicija + 1
#-----------------------------------------------
def dugme_jedan():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"1")
    insert_pozicija = insert_pozicija + 1

def dugme_dva():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"2")
    insert_pozicija = insert_pozicija + 1

def dugme_tri():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"3")
    insert_pozicija = insert_pozicija + 1

def karakter_puta():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"*")
    insert_pozicija = insert_pozicija + 1
#-----------------------------------------------
def funkcija_backspace():
    global insert_pozicija
    insert_pozicija = insert_pozicija - 1 
    komanda = izlaz.delete(insert_pozicija,END)
    
def dugme_nula():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"0")
    insert_pozicija = insert_pozicija + 1

def funkcija_clear():
    global insert_pozicija
    komanda = izlaz.delete(0,END)
    insert_pozicija = 0

def karakter_podeljeno():
    global insert_pozicija
    komanda = izlaz.insert(insert_pozicija,"/")
    insert_pozicija = insert_pozicija + 1

def unos_pomoc():
    novi_prozor = Toplevel()
    tekst = Message(novi_prozor, text="Mišem pritisnite na odredjeni broj/karakter. Broj/karakter će biti ispisan u prozoru iznad brojeva/karaktera. Kada završite unos, mišem pritisnite na dugme '=', zatim će se Vaš rezultat prikazati u prozoru.")
    tekst.pack()
    novi_prozor.configure(bg="white")
    novi_prozor.resizable(False,False)
    novi_prozor.iconbitmap("C:\Ikonice za pyth\question-mark-sign-ico-icon-png-favpng-1J5Xr2AjTRj1msgv9EXizTCB4.ico")
    novi_prozor.title("")
def pomoć_brisanje():
    novi_prozor = Toplevel()
    tekst = Message(novi_prozor,text = "Kako bi ste obrisali jedan karakter potrebno je da mišem kliknete na karakter  '<-'.\nZa brisanje celog izraza kliknite na karakter 'C'.")
    tekst.pack()
    novi_prozor.configure(bg="white")
    novi_prozor.resizable(False,False)
    novi_prozor.iconbitmap("C:\Ikonice za pyth\question-mark-sign-ico-icon-png-favpng-1J5Xr2AjTRj1msgv9EXizTCB4.ico")
    novi_prozor.title("")

def o_autoru():
    novi_prozor = Toplevel()
    tekst = Message(novi_prozor,text = "Yt:Drawing&Making")
    tekst.pack()
    novi_prozor.configure(bg="white")
    novi_prozor.resizable(False,False)
    novi_prozor.iconbitmap("C:\Ikonice za pyth\question-mark-sign-ico-icon-png-favpng-1J5Xr2AjTRj1msgv9EXizTCB4.ico")
    novi_prozor.title("")

def zatvori():
    root.destroy()

    

#----------------------------------------------------------------------------------------

izlaz = Entry(root)
izlaz.grid(row=0,column=0,columnspan=4)
jednako1 = Button(root,text="=",command=jednako)
jednako1.grid(row=0,column=3,columnspan=2)
clear = Button(root, text="C",command=funkcija_clear)
clear.grid(row=0, column=0)
#------------------------------------------------------------------------------------------
broj_sedam = Button(root, text="7",width=5,height = 2,command=dugme_sedam,bg=boja_dugmeta)
broj_sedam.grid(row=1,column=0)

broj_osam = Button(root, text = "8",width=5,height = 2,command=dugme_osam,bg=boja_dugmeta)
broj_osam.grid(row=1, column=1)

broj_devet = Button(root, text="9",width=5,height = 2,command=dugme_devet,bg=boja_dugmeta)
broj_devet.grid(row=1, column=2)

minus = Button(root, text="-",width=5,height = 2,command=karakter_minus,bg=boja_dugmeta)
minus.grid(row=1, column=3)
#-------------------------------------------------------------------------------------
broj_cetiri = Button(root, text="4",width=5,height = 2,command=dugme_cetiri,bg=boja_dugmeta)
broj_cetiri.grid(row=2,column=0)

broj_pet = Button(root, text = "5",width=5,height = 2,command=dugme_pet,bg=boja_dugmeta)
broj_pet.grid(row=2, column=1)

broj_sest = Button(root, text="6",width=5,height = 2,command=dugme_sest,bg=boja_dugmeta)
broj_sest.grid(row=2, column=2)

plus = Button(root, text="+",width=5,height = 2,command=karakter_plus,bg=boja_dugmeta)
plus.grid(row=2, column=3)
#-----------------------------------------------------------------------------------------
broj_jedan = Button(root, text="1",width=5,height = 2,command=dugme_jedan,bg=boja_dugmeta)
broj_jedan.grid(row=3,column=0)

broj_dva = Button(root, text = "2",width=5,height = 2,command=dugme_dva,bg=boja_dugmeta)
broj_dva.grid(row=3, column=1)

broj_tri = Button(root, text="3",width=5,height = 2,command=dugme_tri,bg=boja_dugmeta)
broj_tri.grid(row=3, column=2)

puta = Button(root, text="*",width=5,height = 2,command=karakter_puta,bg=boja_dugmeta)
puta.grid(row=3, column=3)
#--------------------------------------------------------------------------------
backspace = Button(root, text="<-",width=5,height = 2,command=funkcija_backspace,bg=boja_dugmeta)
backspace.grid(row=4,column=0)

broj_nula = Button(root, text = "0",width=5,height = 2,command=dugme_nula,bg=boja_dugmeta)
broj_nula.grid(row=4, column=1)

tacka = Button(root,text=".",width=5,height=2,command=tacka,bg=boja_dugmeta)
tacka.grid(row=4,column=2)

podeljeno = Button(root, text="/",width=5,height = 2,command=karakter_podeljeno,bg=boja_dugmeta)
podeljeno.grid(row=4, column=3)

meni = Menu(root)
pomoć = Menu(meni,tearoff=0)
o_autoru1 = Menu(meni,tearoff=0)
zatvori1 = Menu(meni,tearoff=0)
meni.add_cascade(label="Pomoć",menu=pomoć)
pomoć.add_command(label="Unos",command=unos_pomoc)
pomoć.add_command(label="Brisanje",command=pomoć_brisanje)
meni.add_cascade(label="O autoru",menu=o_autoru1)
o_autoru1.add_command(label="O autoru",command=o_autoru)
meni.add_command(label="Zatvori",command=zatvori)







root.configure(menu=meni)
root.resizable(False,False)
root.title("")
root.mainloop()
