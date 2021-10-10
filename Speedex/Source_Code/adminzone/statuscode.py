#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"

import cgi,MySQLdb
f=cgi.FieldStorage()
id=f.getvalue('id')
status=f.getvalue('status')
curcity=f.getvalue('curcity')

con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()

q="update consignment set curcity='"+curcity+"',status='"+status+"' where refno='"+id+"'"
cur.execute(q)
print "<script>window.location.href='showconsignment.py';</script>"