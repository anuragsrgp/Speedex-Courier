#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()

f=cgi.FieldStorage()
oldpass=f.getvalue('oldpass')
newpass=f.getvalue('newpass')
cpass=f.getvalue('cpass')

q="update adminlogin set password='"+newpass+"' where aid='admin@gmail.com' and password='"+oldpass+"'"


if newpass==cpass:
 n=cur.execute(q) 
 if n==1:
  print "<script>alert('New Password update');window.location.href='../login.py';</script>"
 else:
  print "<script>alert('New Password is not updated');window.location.href='changepwd.py';</script>"
else:
 print "<script>alert('New password is not confimred)window.location.href='changepwd.py';</script>"