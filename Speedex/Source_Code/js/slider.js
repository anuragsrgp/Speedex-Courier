//alert("ok")
var arr=["rr.jpg","oo.jpg","market.jpg","lpoot.jpg","cloth.jpg","book.jpg"];
var i=0;
function slider()
{
var img=document.getElementById("slide");
img.src="images/"+arr[i];
i++;
if(i==6)
   {
    i=0;
   }
   window.setTimeout("slider()",2000);
   
}