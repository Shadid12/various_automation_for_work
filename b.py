import os, json

path_to_json = './'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

_html = ""
for js in json_files:
    with open(os.path.join(path_to_json, js)) as json_file:
        data  = json.load(json_file)
        desc  = data["product"]["title"]
        _id   = data["product"]["variants"][0]["id"]
        img = data["product"]["images"][0]["src"]

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