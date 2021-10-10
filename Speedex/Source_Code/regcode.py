#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
name=f.getvalue('name')
#print name
gender=f.getvalue('gender')
#print gender
mobileno=f.getvalue('mobileno')
#print mobileno
email=f.getvalue('email')
#print email
address=f.getvalue('address')
#print address
pinno=f.getvalue('pinno')
#print pinno
sum=f.getvalue('sum')
total=f.getvalue('t')

con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
query="insert into register values('"+name+"','"+gender+"','"+mobileno+"','"+email+"','"+address+"','"+pinno+"',sysdate())"
if sum==total:
 n=cur.execute(query)
 if n==1:
  print "<script>alert('Registration Successfull submitted');window.location.href='register.py';</script>"
 else:
  print "<script>alert('Registration not Successfull');window.location.href='register.py';</script>"
else:
 print "<script>alert('In Chaptcha');window.location.href='register.py';</script>"