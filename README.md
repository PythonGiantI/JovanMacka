#Uvodjenje biblioteka
from tkinter import*
from tkinter import messagebox
#Otvaranje prozora
root = Tk()
#Promenljive za komandu za unosenje X-a i O-a
clicked = True
count = 0
#Promenljiva za boju precrtne linije 
boja_promene = "red"
#Definisanje komande za onesposobljavanje dugmadi nako necije pobede
def disable_all_buttons():
    dugme_1.config(state=DISABLED)
    dugme_2.config(state=DISABLED)
    dugme_3.config(state=DISABLED)
    dugme_4.config(state=DISABLED)
    dugme_5.config(state=DISABLED)
    dugme_6.config(state=DISABLED)
    dugme_7.config(state=DISABLED)
    dugme_8.config(state=DISABLED)
    dugme_9.config(state=DISABLED)
#Definisanje lambde za komandu koja sluzi za proveru da li je neko pobedio
def da_li_je_neko_pobedio(x,y,z,m,a):
    if x["text"] == m and y["text"] == m and z["text"] == m:
        x.config(bg=boja_promene)
        y.config(bg=boja_promene)
        z.config(bg=boja_promene)
        pobeda = True
        messagebox.showinfo("Tic Tac Toe",a)
        disable_all_buttons()
#Definisanje komande za proveru da li je neko pobedio
def check_if_won():
    da_li_je_neko_pobedio(dugme_1,dugme_2,dugme_3,"X","Čestitamo, X je pobedio!!!")
    da_li_je_neko_pobedio(dugme_4,dugme_5,dugme_6,"X","Čestitamo, X je pobedio!!!")
    da_li_je_neko_pobedio(dugme_7,dugme_8,dugme_9,"X","Čestitamo, X je pobedio!!!")
    da_li_je_neko_pobedio(dugme_1,dugme_4,dugme_7,"X","Čestitamo, X je pobedio!!!")
    da_li_je_neko_pobedio(dugme_2,dugme_5,dugme_8,"X","Čestitamo, X je pobedio!!!")
    da_li_je_neko_pobedio(dugme_3,dugme_6,dugme_9,"X","Čestitamo, X je pobedio!!!")
    da_li_je_neko_pobedio(dugme_3,dugme_5,dugme_7,"X","Čestitamo, X je pobedio!!!")
    da_li_je_neko_pobedio(dugme_1,dugme_5,dugme_9,"X","Čestitamo, X je pobedio!!!")
    #---------------------------------------------------------------------------
    da_li_je_neko_pobedio(dugme_1,dugme_2,dugme_3,"O","Čestitamo, O je pobedio!!!")
    da_li_je_neko_pobedio(dugme_4,dugme_5,dugme_6,"O","Čestitamo, O je pobedio!!!")
    da_li_je_neko_pobedio(dugme_7,dugme_8,dugme_9,"O","Čestitamo, O je pobedio!!!")
    da_li_je_neko_pobedio(dugme_1,dugme_4,dugme_7,"O","Čestitamo, O je pobedio!!!")
    da_li_je_neko_pobedio(dugme_2,dugme_5,dugme_8,"O","Čestitamo, O je pobedio!!!")
    da_li_je_neko_pobedio(dugme_3,dugme_6,dugme_9,"O","Čestitamo, O je pobedio!!!")
    da_li_je_neko_pobedio(dugme_3,dugme_5,dugme_7,"O","Čestitamo, O je pobedio!!!")
    da_li_je_neko_pobedio(dugme_1,dugme_5,dugme_9,"O","Čestitamo, O je pobedio!!!")
#Definisanje komande za unosenje X-a i O-a
def b_click(b):
    global clicked,count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        check_if_won()
        count += 1
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        check_if_won()
        count += 1
    else:
        messagebox.showerror("Tic Tac Toe","Ovo polje je već popunjeno.\nIzaberi drugo polje...")
#Definisanje komande za meni boja
def crvena_boja():
    global boja_promene
    boja_promene = "red"
def plava_boja():
    global boja_promene
    boja_promene = "blue"
def zuta_boja():
    global boja_promene
    boja_promene = "yellow"
def narandzasta_boja():
    global boja_promene
    boja_promene = "orange"
def zelena_boja():
    global boja_promene
    boja_promene = "green"
#Dugmadi
dugme_1= Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(dugme_1))
dugme_2= Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(dugme_2))
dugme_3= Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(dugme_3))
dugme_4= Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(dugme_4))
dugme_5= Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(dugme_5))
dugme_6= Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(dugme_6))
dugme_7= Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(dugme_7))
dugme_8= Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(dugme_8))
dugme_9= Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(dugme_9))
#Prikazivanje dugmadi
dugme_1.grid(row=0,column=0)
dugme_2.grid(row=0,column=1)
dugme_3.grid(row=0,column=2)
dugme_4.grid(row=1,column=0)
dugme_5.grid(row=1,column=1)
dugme_6.grid(row=1,column=2)
dugme_7.grid(row=2,column=0)
dugme_8.grid(row=2,column=1)
dugme_9.grid(row=2,column=2)
#Meni
meni = Menu(root)
opcije = Menu(meni,tearoff=0)
boja_promene_meni = Menu(opcije,tearoff=0)
meni.add_cascade(label='Opcije', menu=opcije)
opcije.add_cascade(label="Boja precrta",menu=boja_promene_meni)
opcije.add_cascade(label="Restart",menu=opcije)
boja_promene_meni.add_command(label="Crvena",command=crvena_boja)
boja_promene_meni.add_command(label="Plava",command=plava_boja)
boja_promene_meni.add_command(label="Žuta",command=zuta_boja)
boja_promene_meni.add_command(label="Narandžasta",command=narandzasta_boja)
boja_promene_meni.add_command(label="Zelena",command=zelena_boja)
#Konfiguracija prozora
root.configure(menu=meni)
root.config(bg="black")
root.title("Tic Tac Toe")
root.resizable(False,False)
root.mainloop()                                                                                                                            
