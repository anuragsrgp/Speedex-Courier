#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "index project"


print """
<html>
<head>
<style>
*
{
margin:0px;
padding:0px;
}

#outer
{
 height:auto;
 width:100%;
 border:1px solid green;
}
body
{
background-image:url('../images/bd.jpg');
height:100vh;
background-position:center;
background-size:cover;
}
#header
{
    height:150px;
	width:100%;
	background-color:#FFF;
	
}
#logo
{
     width:316px;
     height:150px;
	 background-color:#fff;
	 float:left;
	 
}
#pt
{
    width:1033px;
	height:150px;
	background-color:#8080c0;
	float:right;
}
#menu
{
height:50px;
width:100%;
border:1px solid;
background-color:black;
border-radius:0px;
margin-top:8px;
}
#menu ul 
{
list-style:none;
padding:0px;
margin:0px;
position:absolute;
}
#menu ul li
{
float:left;
margin-top:2px;
}
#menu ul li a
{
  width:171px;
  height:30px;
  color:white;
  display:block;
  text-decoration:none;
  font-size:20px;
  text-align:center;
  padding:8px;
  border-radius:10px;
  font-family:Century Gothic;
  font-weight:bold;
  margin-left:8%;
}
#menu li a:hover
{
     background-color:#f56600;
	 
}
#main 
{
  height:750px;
  width:100%;
  border:2px solid;
  margin-top:15px;
 background-color:#f56600;
}
 </style>
</head>
<body>
<div id="outer">
    <div id="header">
	      <div id="logo"> 
		 
		    <img src="images/sp.png" height="150px" width="300px"/>  
	     </div>
         <div id="pt"> 
            <img src="images/exd.png" height="150px" width="1033px" />
		 </div> 
	</div>
<!--menu div start-->
<div id="menu">
     
     <ul>
 
    <li><a href="adminhome.py">HOME</a></li>
	<li><a href="complains.py">COMALAINS</a></li>
	<li><a href="contactmgmt.py">CONTACT MGMT</a></li>
	<li><a href="changepwd.py">CHANGE PWD</a></li>
	<li><a href="consignment.py">CONSIGNMENT</a></li>
	<li><a href="addcity.py">ADD CITY</a></li>
	<li><a href="logout.py">LOGOUT</a></li>
	
 
 
   </ul>
 </div>
<!--menu div end-->
<!--------main div start------->
<div id="main">
  <h1 style="text-align:center;color:darkred;">Update Tracking Status</h1>
  <hr>
  <form action="statuscode.py" method="post">
  <table>
  <tr>
  <td>Change Status</td>
  <td>
  <select name="status" required>
    <option value="">Select Status</option>
   <option>Initiated</option>
   <option>Pipeline</option>
   <option>Delivered</option>
   <option>Cancelled</option>
   </select>
  </td>
  </tr>
"""
import MySQLdb
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="select * from city"
cur.execute(q)
res1=cur.fetchall()

print "<tr>" 
print "<td>Select Source Location :</td>"
print "<td><select name='curcity'>"
print "<option>Select Source</option>"
for r in res1:
 print "<option>"+str(r[1])+"</option>"
print "</select>"
print "</td>"
print "</tr>"
print "<tr>"
import cgi 
id=cgi.FieldStorage().getvalue('id')
print "<td><input type='hidden' name='id' value='"+str(id)+"'/></td>" 
print "</tr>"
 
print """

<tr>
<td colspan="2" align="center">
<input type="submit" value="Update">
</td>
</tr>


</table>
  </form>
  
</div>
<!--------main div end------->
 	
	
	
	
</div>
</body>
</html>







""" 











