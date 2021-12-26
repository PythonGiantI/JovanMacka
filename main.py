from tkinter import *
from tkinter import messagebox

root= Tk()



def button_click(b):
	global x_clicked,count,won
	if b["text"] == "" and x_clicked == False:
		b["text"] = "X"
		x_clicked = True
		count += 1
		check_if_won()
	elif b["text"] == "" and x_clicked == True:
		b["text"] = "O"
		x_clicked = False
		count += 1
		check_if_won()
	else:
		messagebox.showerror("Tic Tac Toe","Chose another box!")
	if count == 9 and won == False:
		messagebox.showinfo("Tic Tac Toe"," Draw! ")

def check_if_won():
	global won
	if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
		button1.config(bg="red")
		button2.config(bg="red")
		button3.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, X won!")
	elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
		button4.config(bg="red")
		button5.config(bg="red")
		button6.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, X won!")
	elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
		button7.config(bg="red")
		button8.config(bg="red")
		button9.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, X won!")
	elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
		button1.config(bg="red")
		button4.config(bg="red")
		button7.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, X won!")
	elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
		button2.config(bg="red")
		button5.config(bg="red")
		button8.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, X won!")
	elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
		button3.config(bg="red")
		button6.config(bg="red")
		button9.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, X won!")
	elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
		button1.config(bg="red")
		button5.config(bg="red")
		button9.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, X won!")
	elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
		button3.config(bg="red")
		button5.config(bg="red")
		button7.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, X won!")
	elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
		button1.config(bg="red")
		button2.config(bg="red")
		button3.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, O won!")
	elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
		button4.config(bg="red")
		button5.config(bg="red")
		button6.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, O won!")
	elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
		button7.config(bg="red")
		button8.config(bg="red")
		button9.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, O won!")
	elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
		button1.config(bg="red")
		button4.config(bg="red")
		button7.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, O won!")
	elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
		button2.config(bg="red")
		button5.config(bg="red")
		button8.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, O won!")
	elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
		button3.config(bg="red")
		button6.config(bg="red")
		button9.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, O won!")
	elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
		button1.config(bg="red")
		button5.config(bg="red")
		button9.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, O won!")
	elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
		button3.config(bg="red")
		button5.config(bg="red")
		button7.config(bg="red")
		won = True
		messagebox.showinfo("Tic Tac Toe","Congratulations, O won!")
def start_restart():
	global root,x_clicked,count,won,button1,button2,button3,button4,button5,button6,button7,button8,button9
	root.config(menu=menu)
	x_clicked = False
	count = 0
	won = False
	bg = PhotoImage(file="download (1).png")
	background = Label(root, image=bg)
	background.grid(row=0,column=0)
	button1 = Button(root,text="",bg="white",command=lambda: button_click(button1),width=4,height=1,font=("Comic Sans MS", 20, "bold"))
	button2 = Button(root,text="",bg="white",command=lambda: button_click(button2),width=4,height=1,font=("Comic Sans MS", 20, "bold"))
	button3 = Button(root,text="",bg="white",command=lambda: button_click(button3),width=4,height=1,font=("Comic Sans MS", 20, "bold"))
	button4 = Button(root,text="",bg="white",command=lambda: button_click(button4),width=4,height=1,font=("Comic Sans MS", 20, "bold"))
	button5 = Button(root,text="",bg="white",command=lambda: button_click(button5),width=4,height=1,font=("Comic Sans MS", 20, "bold"))
	button6 = Button(root,text="",bg="white",command=lambda: button_click(button6),width=4,height=1,font=("Comic Sans MS", 20, "bold"))
	button7 = Button(root,text="",bg="white",command=lambda: button_click(button7),width=4,height=1,font=("Comic Sans MS", 20, "bold"))
	button8 = Button(root,text="",bg="white",command=lambda: button_click(button8),width=4,height=1,font=("Comic Sans MS", 20, "bold"))
	button9 = Button(root,text="",bg="white",command=lambda: button_click(button9),width=4,height=1,font=("Comic Sans MS", 20, "bold"))
	button1.place(x=0,y=0)
	button2.place(x=0,y=65)
	button3.place(x=0,y=130)
	button4.place(x=75,y=0)
	button5.place(x=75,y=65)
	button6.place(x=75,y=130)
	button7.place(x=150,y=0)
	button8.place(x=150,y=65)
	button9.place(x=150,y=130)
	

bg = PhotoImage(file="download (1).png")
background = Label(root, image=bg)
background.place(x=0,y=0,relwidth=1,relheight=1)
start_button = Button(root,text="Start",command=start_restart,width=6,font=("Comic Sans MS", 10, "bold"))
start_button.place(x=85,y=110)

menu = Menu(root)
restart_menu = Menu(menu)
menu.add_command(label="Restart",command=start_restart)



root.iconbitmap("download.ico")
root.title("Tic Tac Toe")
root.resizable(False,False)
root.geometry("225x195")
root.mainloop()
