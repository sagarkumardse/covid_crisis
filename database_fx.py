import sqlite3 
import hashlib
conn = sqlite3.connect('data.db')


def create_usertable():
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS userstable(
	 username text,
	 email_id text,
	 password text)''')


def add_userdata(username,email_id,password):
	c = conn.cursor()
	c.execute('INSERT INTO userstable(username,email_id,password) VALUES (?,?,?)',(username,email_id,password))
	conn.commit()

def login_user(email_id,password):
	c = conn.cursor()
	c.execute('SELECT * FROM userstable WHERE email_id = ? AND password = ?',(email_id,password))
	data = c.fetchall()
	return data
def check_pass(password):
	c = conn.cursor()
	c.execute('SELECT * FROM userstable WHERE password = ?',(password,))
	data = c.fetchall()
	return data

def existing_user(email_id):
	c = conn.cursor()
	c.execute('SELECT * FROM userstable WHERE email_id =?',(email_id,))
	data = c.fetchall()
	return data
def create_sp():
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS sp_table(
	 email_id text,
	 oxy int,
	 plasma int,
	 rem int,
	 pin text,
	 city text,
	 state text,
	 phone int,
	 upi text
	 )''')
def add_service_provider(email_id, oxy, plasma, rem,pin,city,state, phone, upi):
	c = conn.cursor()
	c.execute('''INSERT INTO	
		sp_table(email_id, oxy, plasma, rem, pin, city, state,phone,upi) VALUES (?,?,?,?,?,?,?,?,?)
		''',(email_id,oxy, plasma, rem,pin,city,state,phone,upi))
	conn.commit()

def find_donors(pin,needed):
	c = conn.cursor()
	if needed=='Oxygen Cylinders':
		if len(pin)==0:
			c.execute("""SELECT * FROM sp_table WHERE oxy=1""")
			data = c.fetchall()
		else:
			c.execute("""SELECT * FROM sp_table WHERE pin = ? and oxy=1""", (pin,))
			data = c.fetchall()
		return data
	elif needed=='Plasma':
		if len(pin)==0:
			c.execute("""SELECT * FROM sp_table WHERE plasma=1""")
			data = c.fetchall()
		else:
			c.execute("SELECT * FROM sp_table WHERE pin = ? and plasma=1", (pin,))
			data = c.fetchall()
		return data
	elif needed=='Remdesivir Doses':
		if len(pin)==0:
			c.execute("""SELECT * FROM sp_table WHERE rem=1""")
			data = c.fetchall()
		else:
			c.execute("SELECT * FROM sp_table WHERE pin = ? and rem=1", (pin,))
			data = c.fetchall()
		return data
	else:
		c.execute("SELECT * FROM sp_table WHERE pin = ? ", (pin,))
		data = c.fetchall()
		return data
def refine_donors(email):
	c = conn.cursor()
	c.execute("SELECT * FROM userstable WHERE email_id=?",(email,))
	data = c.fetchall()
	return data
	
def make_hashes(password):
	c = conn.cursor()
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	c = conn.cursor()
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
#c = conn.cursor()
#c.execute('drop table if exists userstable')
#c.execute('drop table if exists sp_table')


