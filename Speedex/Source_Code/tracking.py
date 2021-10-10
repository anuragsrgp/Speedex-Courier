#!C:\Python27\python.exe 
print "Content-Type:text/html\n\n"

print """
<html>
<head>
<link href="css/tracking.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<div id="outer">
          <div id="header">
            <div id="logo">
			<img src="images/sp.png" height="150px" width="300px"/>
			</div>
			<div id="pt">
			<img src="images/exd.png" height="150px" width="100%" />
		 </div>
			</div>
                
<!--------menu start----->   
   <div id="menu"> 
  
     <ul>
 
     <li><a href="inde.py">HOME</a></li> 
	  <li><a href="aboutus.py">ABOUT US</a></li>  
	 <li><a href="register.py">REGISTER</a></li>  
	  <li><a href="contactus.py">CONTACT US</a></li>  
	  <li><a href="complain.py">COMPLAIN</a></li>  
	  <li><a href="tracking.py">TRACKING</a></li>  
	  <li><a href="login.py">LOGIN</a></li> 
	
 
 
    </ul> 
 
 </div>
 
 <!--------menu end------>
 <!---slider div start--->
 <div id="slider">
  <h1 style="text-align:center;color:#003847;font-weight:bold;">TRACKING</h1>
<hr style="color:#3f729b" />
<table style="margin:0px auto;width:80%;margin-top:12px;color:#fff;" border="1">
  <tr>
  
  <th>Reference No.</th>
  <th>Source Location</th>
  <th>Current Location</th>
  <th>Destination Location</th>
  <th>Status</th>
  </tr>
"""
import MySQLdb
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="select * from consignment"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print "<tr>"
 print "<td>",r[0],"</td>"
 print "<td>",r[7],"</td>"
 print "<td>",r[8],"</td>"
 print "<td>",r[9],"</td>"
 print "<td>",r[10],"</td>"
 print "</tr>"

print """
 
 
 
</table>

  
  
  </div>
 <!---slider div end--->
 <!---main div start--->
 
 
  <div id="main1">
    <div id="a">
	<img src="images/flat.jpg" height="450px" width="350px"/>
	</div>
	<div id="b">
	<img src="images/bkp.jpg" height="450px" width="350px"/>
	</div>
	<div id="c">
	<img src="images/comli.jpg" height="450px" width="350px"/>
	</div>
	 </div>
 
 
 
 <!---main div end--->
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
    <h3 style="color:green;">SPEEDEX WORLDWIDE</h3>
	<br/>
	<p>Sinamangal, Airport Road
   Opp. of Oil Corporation Building
  Sinamangal, Kathmandu, Nepal</p>
  <br/>
  <p>
    +977 - 1-4480405 / 4481232
   www.speedexworldwide.com</p>
   <br/>
   <p ><i class="fa fa-phone" style="font-size:22px;color:green;"></i>+977 1 4481232</p>
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