#!C:\Python27\python.exe 
print "Content-Type:text/html\n\n"

print """
<html>
<head>
<link href="css/complain.css" rel="stylesheet" type="text/css"/>
<link rel="stylesheet" href="css/all.css" type="text/css" />
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
   <h1 style="text-align:center;color:#fff;;font-weight:bold;">COMPLAIN FROM</h1>
<hr/>
 <form action="complaincode.py" method="post">
 <table style="margin:0px auto;width:55%;height:450px;margin-left:300px;margin-top:3%;background-color:#e0f2f1;">
 <tr>
   <td style="font-size:18px;">Enter name :</td>
   <td>
    <input type="text" name="name" required />
   </td>
 </tr>
            <tr>
			<td style="font-size:18px;">Enter Moboile No :</td> 
			<td>
			<input type="number" name="mobileno" required />
			</td>
			</tr>
   <tr>
   <td style="font-size:18px;">Enter Email Id :</td>
   <td>
   <input type="email" name="email" required />
   </td>
   </tr>
            <tr>
			<td style="font-size:18px;">Reference No.</td>
			<td>
			<input type="number" name="refno" required />
			</td>
			</tr>
   <tr>
   <td style="font-size:18px;">Enter Complain Text :</td>
   <td>
     <textarea name="ctext" required /></textarea>
   </td>
   </tr>
         <tr>
	       <td colspan="2" align="center">
           <input type="submit" value="SUBMIT" id="sub"/></td>
			  </tr>
 </table>
 </form>
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