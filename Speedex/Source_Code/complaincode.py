#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
name=f.getvalue('name') 
mobileno=f.getvalue('mobileno')
email=f.getvalue('email')
refno=f.getvalue('refno')
ctext=f.getvalue('ctext')


con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()

q="insert into complain(name,mobileno,email,refno,ctext,cdate) values('"+name+"','"+mobileno+"','"+email+"','"+refno+"','"+ctext+"',sysdate())"
n=cur.execute(q)

if n==1:
 print "<script>alert('Complain Successful submitted');window.location.href='inde.py';</script>"
else:
 print "<script>alert('Complain is not success');window.location.href='inde.py';</script>"