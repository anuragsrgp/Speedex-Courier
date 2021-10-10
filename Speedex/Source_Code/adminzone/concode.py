#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"

import cgi,MySQLdb
f=cgi.FieldStorage()
refno=f.getvalue('refno')
sname=f.getvalue('sname')
saddress=f.getvalue('saddress')
scontact=f.getvalue('scontact')
rname=f.getvalue('rname')
raddress=f.getvalue('raddress')
rcontact=f.getvalue('rcontact')
source=f.getvalue('source')
curcity=f.getvalue('curcity')
destination=f.getvalue('destination')
status=f.getvalue('status')

con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="insert into consignment values('"+refno+"','"+sname+"','"+saddress+"','"+scontact+"','"+rname+"','"+raddress+"','"+rcontact+"','"+source+"','"+curcity+"','"+destination+"','"+status+"',sysdate())"

n=cur.execute(q)
if n==1:
 print "<script>alert('Success');window.location.href='consignment.py';</script>"
else:
 print "<script>alert('Not Succses');window.location.href='consignment.py';</script>"