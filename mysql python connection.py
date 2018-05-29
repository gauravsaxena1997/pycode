import mysql.connector as pysql

conn = pysql.connect ( user='root',password='m487',host='localhost' )

def db():
	if ( conn.is_connected() ):
		print ('Database connected successfully...')
		cur = conn.cursor()

		cur.execute ("""create database if not exists test""")

		cur.execute ("use test")

		cur.execute ("""create table if not exists details (  
						sno INT(5) NOT NULL PRIMARY KEY AUTO_INCREMENT,
						name CHAR(20) NOT NULL,
						email CHAR(30) NOT NULL,
						contact INT(11)  )""")


		sno = input ("Enter sno.: ")
		name = input ("Enter name: ")
		email = input ("Enter email: ")
		contact= input ("Enter contact: ")
		# cur.execute (""" insert into details(name,email,contact) values ( 
		# 	         'Gaurav6','sv@g.com',2143658709 ) """)
		add_salary = ("INSERT INTO details "
              "(sno, name, email, contact) "
              "VALUES (%s, %s, %s, %s)" % (sno,name,email,contact) )
		
		cur.execute (add_salary)

		conn.commit()


	else:
		print ('Something went wrong...')


if __name__ == "__main__":
	db()