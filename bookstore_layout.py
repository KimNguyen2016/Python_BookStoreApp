from tkinter import *
from bookstore_script import Database

database = Database("books.db")

def get_selected_row(event):
	global selected_tuple
	index=list1.curselection()[0]	
	selected_tuple=list1.get(index)	
	
	e1.delete(0, END)
	e1.insert(END, selected_tuple[1])
	
	e2.delete(0, END)
	e2.insert(END, selected_tuple[2])
	
	e3.delete(0, END)
	e3.insert(END, selected_tuple[3])
	
	e4.delete(0, END)
	e4.insert(END, selected_tuple[4])
			

def view_command():
	list1.delete(0, END)
	for row in database.view():
		list1.insert(END, row)

		
def search_command():
	list1.delete(0,END)
	for row in database.search(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()):
		list1.insert(END, row)
			
def add_command():
	database.insert(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
	list1.delete(0, END)
	list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()))

def delete_command():
	database.delete(selected_tuple[0])

def update_command():
	database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
	
	
def __del__(self):
	self.conn.close()
	
window=Tk()
window.wm_title("Book Store Application")
window.configure(background="#875401")

window.resizable(width=False, height=False)

#Logo
logo = PhotoImage(file="Book_logo.gif")
w1 = Label(window, image=logo)
w1.grid(row=0, column=0, sticky=W)

#Header
l_app = Label(window, text= "BOOK STORE ", fg='white', font="Verdana 20 bold", bg="#875401")
l_app.grid(sticky=W)
l_app.grid(row=0, column = 1, padx=(5,0))


# create labels
l1= Label(window,text="Title of Book", fg = "white", font="Verdana 10 ", bg="#875401")
l1.grid(sticky=E)
l1.grid(row=1,column=0, pady=(10,10))

l2=Label(window,text="Author", fg = "white", font="Verdana 10 ", bg="#875401")
l2.grid(sticky=E)
l2.grid(row=3,column=0, pady=(10,10))

l3=Label(window,text="Publish Year", fg = "white", font="Verdana 10 ", bg="#875401")
l3.grid(sticky=E)
l3.grid(row=2,column=0, pady=(10,10))

l4=Label(window,text="ISBN No.", fg = "white", font="Verdana 10 ", bg="#875401")
l4.grid(sticky=E)
l4.grid(row=4,column=0, pady=(10,10))

# create text fields
title_text = StringVar()
e1=Entry(window, textvariable= title_text, fg = "#875401", font="Verdana 12 ", bg='white', width="50")
e1.grid(sticky=W)
e1.grid(row=1,column=1, pady=(10,10), padx=(10,0))

author_text = StringVar()
e2=Entry(window, textvariable= author_text, fg = "#875401", font="Verdana 12 ", bg='white', width="50")
e2.grid(sticky=W)
e2.grid(row=3,column=1, pady=(10,10), padx=(10,0))

year_text = StringVar()
e3=Entry(window, textvariable= year_text, fg = "#875401", font="Verdana 12 ", bg='white', width="25")
e3.grid(sticky=W)
e3.grid(row=2,column=1, pady=(10,10), padx=(10,0))

ISBN_text = StringVar()
e4=Entry(window, textvariable= ISBN_text, fg = "#875401", font="Verdana 12 ", bg='white', width="25")
e4.grid(sticky=W)
e4.grid(row=4,column=1, pady=(10,10), padx=(10,0))

# create List View 
list1 = Listbox(window, height=20, width=83, fg="#ffff33", font="Verdana 13", bg="#ff9933")
list1.grid(sticky=E)
list1.grid(row=5,column=0, rowspan=8, columnspan= 2)

# create scrollbar
sb1=Scrollbar(window)
sb1.grid(sticky=N+S+E)
sb1.grid(row=5, column=3,rowspan=8)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

# create buttons
b1=Button(window, text="View Books", width=14, fg="#ffff33", font="Verdana 13 bold", bg="#ff9933", command = view_command)
b1.grid(row=6, column=4)

b2=Button(window, text="Search Books", width=14, fg="#ffff33", font="Verdana 13 bold", bg="#ff9933",  command=search_command)
b2.grid(row=7, column=4)

b3=Button(window, text="Add Book", width=14, fg="#ffff33", font="Verdana 13 bold", bg="#ff9933", command=add_command)
b3.grid(row=8, column=4)

b4=Button(window, text="Edit Book", width=14, fg="#ffff33", font="Verdana 13 bold", bg="#ff9933", command=update_command)
b4.grid(row=9, column=4)

b5=Button(window, text="Delete Book", width=14, fg="#ffff33", font="Verdana 13 bold", bg="#ff9933", command=delete_command)
b5.grid(row=10, column=4)

b6=Button(window, text="Exit App", width=14, fg="#ffff33", font="Verdana 13 bold", bg="#ff9933", command=window.destroy)
b6.grid(row=11, column=4)

window.mainloop()
