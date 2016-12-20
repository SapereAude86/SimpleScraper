from lxml import html
import requests
import os
import getpass
import subprocess


def grab_pages(websites):
	page = requests.get(websites)
	tree = html.fromstring(page.content)
	images = tree.xpath('//img/@src')
	return images

website = raw_input("geef website: ")
username = getpass.getuser()
image_dir = '/Users/' + username + '/Desktop/crawler_images/'
if not os.path.isdir(image_dir):
	print "Creating directory..."
	os.mkdir(image_dir)

for image in grab_pages(website):
	commando = "curl -o " + image_dir + image.split("/")[-1] + " " + image
	if "http" in commando or "www" in commando:
		p1 = subprocess.Popen(commando, shell=True)
		p1.communicate()
	else:
		print "Geef goede url..."
		print commando


	
