from tkinter import *
import back_end

window=Tk()
window.wm_title("BOOK Store")
#1
def getselectedentry(event):
	global selected_data
	index=list1.curselection()[0]
	selected_data=list1.get(index)
	return selected_data[0]
	

def Add_entry():
	list1.delete(0,END)
	back_end.insertbookinfo(
	e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())
	
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)
b1=Button(window,text="Add Entry", command=Add_entry)
b1.grid(row=2,column=4)

#2
def View_entry():
	list1.delete(0,END)
	for data in back_end.search(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()):
		list1.insert(END,data)
			

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=3)
b2=Button(window,text="View Entry", command=View_entry)
b2.grid(row=3,column=4)

#3


def Delete_entry():
	back_end.delete(selected_data[0])
	#list1.insert(selected_data)
l3=Label(window,text="Year")
l3.grid(row=1,column=0)

e3_value=StringVar()
e3=Entry(window,textvariable=e3_value)
e3.grid(row=1,column=1)
b3=Button(window,text="Delete Entry", command=Delete_entry)
b3.grid(row=4,column=4)


#4

def Searchall_entry():
	list1.delete(0,END)
	for data in back_end.ViewAll():
		list1.insert(END,data)


	
	
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

e4_value=StringVar()
e4=Entry(window,textvariable=e4_value)
e4.grid(row=1,column=3)
b4=Button(window,text="SearchALL Entry", command=Searchall_entry)
b4.grid(row=5,column=4)
b5=Button(window,text="CLOSE",command=window.destroy)
b5.grid(row=8,column=4)

list1=Listbox(window,height=10,width=45)
list1.grid(row=2,column=0, rowspan=3,columnspan=2)

list1.bind('<<ListboxSelect>>',getselectedentry)
sb1=Scrollbar(window)
sb1.grid(row=1,column=2,rowspan=3,columnspan=3)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


window.mainloop()

