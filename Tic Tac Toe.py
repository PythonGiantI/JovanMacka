from tkinter import*
from tkinter import messagebox
from typing import Counter
root = Tk()

clicked = True
count = 0 
boja_precrta_= "red"
rez_x = 0
rez_o = 0


def crvena_boja():
    global boja_precrta_
    boja_precrta_ = "red"
def zuta_boja():
    global boja_precrta_
    boja_precrta_ = "yellow"
def narandzasta_boja():
    global boja_precrta_
    boja_precrta_ = "orange"
def plava_boja():
    global boja_precrta_
    boja_precrta_ = "blue"
def zelena_boja():
    global boja_precrta_
    boja_precrta_ = "green"

def disable_all_buttons():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def check_if_won(x,y,z,m,a,s):
    global pobeda
    pobeda = False
    if x["text"] == m and y["text"] == m and z["text"] == m:
        x.config(bg=boja_precrta_)
        y.config(bg=boja_precrta_)
        z.config(bg=boja_precrta_)
        pobeda = True
        s = s+1
        disable_all_buttons()
        messagebox.showinfo("Tic Tac Toe",a)
    elif clicked == 8 and pobeda== False:
        messagebox.showinfo("Tic Tac Toe", "Nerešeno!")    

def provera_da_li_je_neko_pobedio():
    global x, o
    check_if_won(b1,b2,b3,"X","Čestitamo, X je pobedio!",rez_x)
    check_if_won(b4,b5,b6,"X","Čestitamo, X je pobedio!",rez_x)
    check_if_won(b7,b8,b9,"X","Čestitamo, X je pobedio!",rez_x)
    check_if_won(b1,b4,b7,"X","Čestitamo, X je pobedio!",rez_x)
    check_if_won(b2,b5,b8,"X","Čestitamo, X je pobedio!",rez_x)
    check_if_won(b3,b6,b9,"X","Čestitamo, X je pobedio!",rez_x)
    check_if_won(b1,b5,b9,"X","Čestitamo, X je pobedio!",rez_x)
    check_if_won(b3,b5,b7,"X","Čestitamo, X je pobedio!",rez_x)
#--------------------------------------------------------
    check_if_won(b1,b2,b3,"O","Čestitamo, O je pobedio!",rez_o)
    check_if_won(b4,b5,b6,"O","Čestitamo, O je pobedio!",rez_o)
    check_if_won(b7,b8,b9,"O","Čestitamo, O je pobedio!",rez_o)
    check_if_won(b1,b4,b7,"O","Čestitamo, O je pobedio!",rez_o)
    check_if_won(b2,b5,b8,"O","Čestitamo, O je pobedio!",rez_o)
    check_if_won(b3,b6,b9,"O","Čestitamo, O je pobedio!",rez_o)
    check_if_won(b1,b5,b9,"O","Čestitamo, O je pobedio!",rez_o)
    check_if_won(b3,b5,b7,"O","Čestitamo, O je pobedio!",rez_o)

def b_click(b):
    global count, clicked
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        provera_da_li_je_neko_pobedio()
        count += 1
        if count == 9:
            messagebox.showinfo("Tic Tac Toe","Nerešeno!")
            disable_all_buttons()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        provera_da_li_je_neko_pobedio()
        count += 1
    else:
        messagebox.showerror("Tic Tac Toe", "Ovo polje je već popunjeno! Izaberite drugo polje...")
    
def restart():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked, count
    clicked = True
    count = 0
    b1 = Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(b1))
    b2 = Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(b2))
    b3 = Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(b3))

    b4 = Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(b4))
    b5 = Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(b5))
    b6 = Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(b6))

    b7 = Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(b7))
    b8 = Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(b8))
    b9 = Button(root, text=" ",width=6,height=3,pady=4,padx=4,font=("Helvetica",20),bg="SystemButtonFace",command=lambda: b_click(b9))

    b1.grid(row=1,column=0)
    b2.grid(row=1,column=1)
    b3.grid(row=1,column=2)
    b4.grid(row=2,column=0)
    b5.grid(row=2,column=1)
    b6.grid(row=2,column=2)
    b7.grid(row=3,column=0)
    b8.grid(row=3,column=1)
    b9.grid(row=3,column=2)

restart()


meni = Menu(root)
options_meni =Menu(meni,tearoff=0)
boje_meni = Menu(meni,tearoff=0)
meni.add_cascade(label="Opcije",menu=options_meni)
options_meni.add_cascade(label="Boje precrta", menu=boje_meni)
boje_meni.add_command(label="Crvena",command=crvena_boja)
boje_meni.add_command(label="Narandžasta",command=narandzasta_boja)
boje_meni.add_command(label="Žuta",command=zuta_boja)
boje_meni.add_command(label="Zelena",command=zelena_boja)
boje_meni.add_command(label="Plava",command=plava_boja)
options_meni.add_command(label="Restart",command=restart)




root.title("Tic Tac Toe")
root.configure(menu=meni)
root.resizable(False, False)
root.mainloop()
