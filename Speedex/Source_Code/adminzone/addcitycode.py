#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb

cityname=cgi.FieldStorage().getvalue('cityname')

con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()

q="insert into city(cityname) values ('"+cityname+"')"

n=cur.execute(q)

if n==1:
 print "<script>alert('Added');window.location.href='addcity.py';</script>"
else:
 print "<script>alret('not Added');window.location.href='addcity.py';</script>"