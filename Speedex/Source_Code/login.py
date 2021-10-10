#!C:\Python27\python.exe 
print "Content-Type:text/html\n\n"

print """
<html>
<head>
<link href="css/login.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<div id="outer">
          <div id="header">
            <div id="logo">
			<img src="images/sp.png" height="150px" width="300px"/>
			</div>
			<div id="pt">
			<img src="images/exd.png" height="150px" width="100%" style="margin-left:fixed;" />
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
  <div id="loginbox">
    <h2>Admin Login</h2>
   <form action="logincode.py" method="post">
    <p>Enter Email Id</p>
	<input type="email" name="aid" placeholder="Enter Email" required >
	<p>Enter Password Id</p>
	<input type="password" name="password" placeholder="Enter Password" required />
	<input type="submit" value="LOGIN" />
</form>
</div>
</div>
 <!---slider div end--->
 <!---main div start--->
 
 
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