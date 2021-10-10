#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "index project"


print """
<html>
<head>
<link href="admincss/logout.css" rel="stylesheet" type="text/css"/>
<script>
       function logout()
       {
          window.history.forward();
       window.setTimeout("window.location.href='../login.py';",2000);
       }
  </script>
</head>
<body onload="logout()">
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
  <h1 style="text-align:center;color:darkred;">LOGOUT</h1>
</div>
<!--------main div end------->
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

