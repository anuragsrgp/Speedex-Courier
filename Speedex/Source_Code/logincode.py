#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "index project"
import cgi,MySQLdb
f=cgi.FieldStorage()
aid=f.getvalue('aid')
password=f.getvalue('password')
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="select * from adminlogin where aid='"+str(aid)+"'"
cur.execute(q)
res=cur.fetchall()
status="false"
for r in res:
 if password==r[1]:
  status="true"
if status=="true":
 print "<script>window.location.href='adminzone/adminhome.py';</script>"
else:
 print "<script>window.location.href='login.py';</script>"