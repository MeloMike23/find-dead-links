import requests
from bs4 import BeautifulSoup
from sys import argv

def fdl(url, depth):
	#List of all links
	aLinks = []

	#List of good links
	gLinks = []

	#Checks to make sure url is good
	try:
		r = requests.get(url)
		if r.status_code not in [200, 302]:
			print('Bad Link')
	except:
		print(url, ' = Bad Link')
	
	soup = BeautifulSoup(r.text, "html.praser")

	#Looking for links in URL
	for i in soup.find_all("a"):
		link = i.get("href")
		if link.startswith("/"):
			if url.endswith("/"):
				link = url[:-1] + link
			else:
				link = url + link
		aLinks.append(link)
	
	#Looks for and prints bad links
	for link in aLinks:
		try:
			r = requests.get(link)
			#If link is bad print
			if r.status_code not in [200,302]:
				print(link, "is a bad link.")
			#Good links
			else:
				gLinks.append(link)
		except:
			print(link, " is a bad link.")
	
	#Checks depth and calls fdl(url, depth) on good links
	if depth > 0:
		for link in gLinks:
		fdl(link, depth-1)


if __name__ == "__main__":
	if len(argv) == 2:
		#Find dead links with no depth
		url = argv[1]
		fdl(url, 0)
	elif len(argv) == 3:
		#Find dead links with depth restricitons
		url = argv[2]
		depth_url = argv[1]
		if depth_url.statswith("-"):
			try:
				depth_url = int(depth_url[1:])
			except:
				print("ERROR: DEPTH INVALID")
				exit(1)
		fdl(url, depth)
	else:
		print("ERROR: find-dead-links [-<depth] <URL>")	
