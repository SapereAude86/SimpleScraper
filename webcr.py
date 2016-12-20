from lxml import html
import requests

def grab_pages(websites):
	page = requests.get(websites)
	tree = html.fromstring(page.content)
	images = tree.xpath('//img/@src')
	return images
for image in grab_pages('http://nu.nl'):
	print image