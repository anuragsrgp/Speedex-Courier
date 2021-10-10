#!C:\Python27\python.exe 
print "Content-Type:text/html\n\n"

print """
<html>
<head>
  <link href="css/contactus.css" rel="stylesheet" type="text/css" />
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
 <!--------menu end------->
 <!---slider div start--->
 <div id="slider">
    <div id="loginbox">
    <h1 style="margin:0px;padding:0 0 20px;color:#f56600;text-align:center;margin-top:-40px;"><u>Contact Us</u></h1> 
      <form action="contactuscode.py" method="post"> 
	  <p>Enter Name</p>
	            <input type="text" name="name"   placeholder="enter name"  required />
	  <p>Enter Mobile No</p>
	            <input type="number" name="mobileno"   placeholder="enter mobile no." required  /> 
	  <p>Enter Email Id</p>
	            <input type="email" name="email"  placeholder="email" required />
	  <p>Enetr Address </p>
	            <textarea name="address"  placeholder="enter address"  required></textarea>
	  <p>Enter Purpose </p> 
	            <textarea name="purpose"  placeholder="enter purpose" required></textarea> 
	       <p><input type="submit" value="SUBMIT"/></p>
	</form>	  
   </div> 
   </div>
<!--main div start-->
    
	
	
	<div id="con" style="margin-top:8px;">
	<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14234.67795370525!2d80.94821!3d26.88224!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x730fe46201abc68a!2sSoftpro+India!5e0!3m2!1sen!2sin!4v1411887056855" width="100%" height="100%"></iframe>
	
	
	
	
	</div>
	
 <!--main div end -->
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