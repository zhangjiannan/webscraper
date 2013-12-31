import re
import urllib
from bs4 import BeautifulSoup
from selenium import webdriver

img_urls = []
formatted_images = []

br = webdriver.Firefox()

br.get('https://www.google.com/search?newwindow=1&site=imghp&tbm=isch&source=hp&biw=1422&bih=748&q=christmas&oq=christmas')

print br.title

search = br.find_elements_by_tag_name('a')

htmltext = br.page_source

soup = BeautifulSoup(htmltext)

pattern = re.compile(u'imgurl=(.+?)&',re.UNICODE)

error_count=0
for tag in soup.find_all('a'):	
	try:
		if(hasattr(tag,'href')):
		    if "imgres?" in tag['href']:
		    	#print tag['href']
		    	match = re.findall(pattern,tag['href'])
		    	img_urls.append(match[0])
		    	print match[0]
	except:
		error_count+=1

br.quit()