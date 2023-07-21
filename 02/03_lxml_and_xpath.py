from lxml import html
import requests

page_html = requests.get("http://localhost:8080/planets.html").text

# the first thing we do is to load html into the lxml tree
tree = html.fromstring(page_html)

selected_rows = tree.xpath("/html/body/div[@id='planets']/table/tr[@id!=planetHeader]")