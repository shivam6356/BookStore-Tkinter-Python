import sqlite3

def connect():
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS BOOK (id INTEGER PRIMARY KEY, title text,author text, year integer, isbn integer)")
	conn.commit()
	conn.close()
	
connect()

def insertbookinfo(title ,author,year,isbn):
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO BOOK VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
	conn.commit()
	conn.close()

def ViewAll():
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM BOOK")
	rows=cur.fetchall()
	return rows

def search(title="" ,author="",year="",isbn=""):
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM BOOK where author=? or title=? or year=? or isbn=?",(author,title,year,isbn))
	rows=cur.fetchall()
	return rows

	
def delete(id):
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM BOOK WHERE ID=?",(id,))
	conn.commit()
	conn.close()
def Update(id,title="" ,author="",year="",isbn=""):
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("Update BOOK set author=? or title=? or year=? or isbn=? where id=?",(author,title,year,isbn,id))
	conn.commit()
	conn.close()
#insertbookinfo('fifty shades','Shivam',1999,1234567)
delete(3)
print(ViewAll())
print(search(year=1999))
