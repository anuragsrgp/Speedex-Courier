#!C:\Python27\python.exe 
print "Content-Type:text/html\n\n"

print """
<html>
<head>
  <link href="css/regist.css" rel="stylesheet" type="text/css" />
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
 
 <!---slider div end--->
 <!--------main div start------->
  <div id="main">
     <div id="reg">
    <h1>REGISTRATION FORM</h1>
	
       <form action="regcode.py" method="post">
	   <table style="margin:0px auto;width:60%;height:450px;">
           <tr>
	   <td>Enter User Name :</td>
	 <td>
	   <input type="text" name="name" required  placeholder="enter name"/>
	 </td>
	 </tr>
	 <tr>
	 <td>Select Gender :</td>
	    <td>
		 <input type="radio" name="gender" value="male"/>Male
		 <input type="radio" name="gender" value="female"/>Female
		</td>
	 </tr>
	 <tr>
	    <td>Enter Mobile No :</td>
          <td>
		  <input type="number" name="mobileno" required  placeholder="enter mobile No" />
		  </td>
		  </tr>
		<tr>
		<td>Enter Email Id :</td>
		<td>
		  <input type="email" name="email" required  placeholder="enter email"/>
		</td>
		</tr>
    <tr>
	   <td>Enter Address :</td>
	  <td>
	    <textarea name="address" required placeholder="enter address"></textarea> 
	  </td>
	</tr>	 
          <tr>
          <td>Pin Code :</td>
            <td>
			<input type="number" name="pinno" required  placeholder="enter pin code"/>
             </td>			
	   </tr>
		
		 		
<tr>				
"""
import random
a=[0,1,2,3,4,5,6,7,8,9]	
n1=random.choice(a)
n2=random.choice(a)
sum=n1+n2
print "<td colspan='2' align='center'> <input type='hidden' value='"+str(sum)+"' name='sum' />"
print "<input value='"+str(n1)+"' style='width:20px' readonly   /> +"  
print "<input value='"+str(n2)+"' style='width:20px' readonly   />"
print " = <input type='number' name='t' style='width:50px' required />"
print "</td>"

  
print """			
</tr>
	   
  <tr>
 <td colspan="2" align="center">  
   <input type="submit" value="SUBMIT"/>
   </tr>
	  
   </table>
  </form>
    </div>
  </div>  
  
     <div id="main1">
    <div id="a">
	<img src="images/flat.jpg" height="450px" width="350px"/>
	</div>
	<div id="b">
	<img src="images/bkp.jpg" height="450px" width="350px"/>
	</div>
	<div id="c">
	<img src="images/girl.jpg" height="450px" width="350px"/>
	</div>
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