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
 //border:1px solid green;
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
  height:500px;
  width:100%;
  border:2px solid;
  margin-top:15px;
 background-color:#f56600;
}
#main1
{
	height:600px;
	width:100%;
	//background-color:lightgrey;
	margin-top:10px;
	background-image:linear-gradient(rgba(0,0,0,0.5),rgba(0,0,0,0.5)),url('../images/dnk.jpeg');
	background-attachment:fixed;
}
#a
{
	height:450px;
	width:350px;
	//background-color:yellow;
	margin-right:55px;
	margin-top:55px;
	float:right;

}
#b
{
	
	height:450px;
	width:350px;
	//background-color:pink;
	margin-left:520px;
	float:left;
	margin-top:55px;
}
#c
{
	height:450px;
	width:350px;
	//background-color:green;
	float:left;
	margin-left:55px;
	margin-top:-450px;
	
}
 #footer
{
	height:300px;
	width:100%;
	background-color:rgba(0,0,0,0.8);
	margin-top:2px;
}
#f1
{
	height:290px;
	width:250px;
	//border:1px solid yellow;
	float:left;
	margin-left:30px;
	margin-top:4px;
}
#f1 ul li
{
	text-decoration:none;
	list-style:none;
	margin-left:8%;
	margin-top:2%;
	
}
#f2
{
	height:290px;
	width:300px;
	//border:1px solid red;
	float:left;
	margin-left:100px;
	margin-top:4px;
}
#f3
{
	height:90px;
	width:300px;
	//border:1px solid tan;
	float:right;
	margin-right:310px;
	margin-top:4px;
}
#f4
{
	height:280px;
	width:180px;
	//border:1px solid orange;
	float:right;
	margin-right:100px;
	margin-top:-6.5%;
}	
#f4one
{
	height:80px;
	width:180px;
	//background-color:red;
	margin-top:111%;
	background-image:url('../images/hong.jpg');
}
#f4two
{
	height:80px;
	width:180px;
	//background-color:tan;
	margin-top:-89%;
	background-image:url('../images/overtime.jpg');
}
#f4three
{
	height:80px;
	width:180px;
	//background-color:yellow;
	margin-top:-89%;
	background-image:url('../images/sam.png');
}
#fone
{
	height:70px;
	width:100%;
	background-color:black;
}
#cop
{
	height:30px;
	width:200px;
	//border:1px solid brown;
	float:left;
	margin-left:100px;
	margin-top:12px;
}
#crea
{
	height:40px;
	width:400px;
	//border:1px solid grey;
	float:right;
	margin-right:30px;
	margin-top:8px;
	
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
<!--main div start-->
<div id="main">
  <h1 style="text-align:center;color:darkred;">Contact Management</h1>
  <hr style="color:#f56600"/>
 <table style="margin:0px auto;width:95%;color:#FFF;margin-top:10px;" border="1">
  <tr>
  <th>Id</th>
  <th>Name</th>
  <th>Mobile No</th>
  <th>Email Id</th>
  <th>Address</th>
  <th>Purpose</th> 
  <th>Post Date</th> 
  <th>Delete</th>
 </tr>
"""
import MySQLdb
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="select * from contactus"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print "<tr>"
 print "<td>",r[0],"</td>"
 print "<td>",r[1],"</td>"
 print "<td>",r[2],"</td>"
 print "<td>",r[3],"</td>"
 print "<td>",r[4],"</td>"
 print "<td>",r[5],"</td>"
 print "<td>",r[6],"</td>"
 print "<td><a href='dcon.py?id="+str(r[0])+"'>Delete</a></td>"
 print "</tr>"



print """
 </table>
</div>
<!--------main div end------->
<div id="main1">
    <div id="a">
	<marquee><img src="images/flat.jpg" height="450px" width="350px"/></marquee>
	</div>
	<div id="b">
<marquee><img src="images/bkp.jpg" height="450px" width="350px"/></marquee>
	</div>
	<div id="c">
	<marquee><img src="images/market.jpg" height="450px" width="350px"/></marquee>
	</div>
	 </div>	
<!--------footer start------->
 <div id="footer">
   <div id="f1">
    <ul>
	 <font color="white" size="3px"><ul><li>HOME</li><br/>
	  <li>CAREER</li><br/>
	  <li>TREM OF USE</li><br/>
	  <li>PRAIVACY POLICY</li><br/>
	  <li>PAYMENT PROCESS</li><br/>
	  <li>CONTACT US</li>
	</ul>
  </div>
   
   <div id="f2">
    <h2 style="color:green;">SPEEDEX WORLDWIDE</h2>
	<br/>
	<p>Sinamangal, Airport Road
   Opp. of Oil Corporation Building
  Sinamangal, Kathmandu, Nepal</p>
  <br/>
  <p>
    +977 - 1-4480405 / 4481232
   www.speedexworldwide.com</p>
   <br/>
   <p>+977 1 4481232</p>
    <p>cuscare@speedexworldwide.com</p>
  </p>
   </div>
   
   
   <div id="f3">
     <h3 style="color:green;">OPENING HOURS</h3><br/>&nbsp &nbsp 
	     Sunday - Friday: 9:30am-6pm 
   </div>
   <div id="f4">
     
       <div id="f4one"></div>
     <div id="f4two"></div>
	 <div id="f4three"></div>
   </div>
   </div>
<!--------footer end------->
<div id="fone">
    <div id="cop">
	<p style="color:white;font-size:15px;">copyright &copy; SPEEDEX</p>
	</div>
  
   <div id="crea">
   <p style="cloor:white;font-size:20px;">Developed By: Praveen Yadav</p>
   </div>
  
  
  </div>	
	
	
	
	
	
	
	
	
</div>
</body>
</html>







""" 