with open("stuff.txt") as file:
    
    _html = ""
    
    for line in file:
        a = line.split(",")
        
        
        desc   = a[0]
        _id = a[1]
        img   = a[2].replace("\n", "")
        
        _html = _html + """
<tr>
	<td>
		<img width="45" height="45" style="display: block; margin-left: auto; margin-right: auto;" alt="" src="{0}" /></td>
	<td>
		<h5> {1} </h5>
	</td>
	<td style="text-align: center;">
		<a class="btn btn-info" role="button" href="http://bigboyswithcooltoys.myshopify.com/cart/add?id={2}&amp;quantity=1">Add to Cart</a>
	</td>
</tr>
""".format(img,desc,_id)
        
    with open("output.html", "w") as o:
        o.write(_html)