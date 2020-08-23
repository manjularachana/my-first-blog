import sys
import urllib.request
import urllib.parse
import re
import pafy
import pytube


arglist=sys.argv[1:]
urllist=[]

api_key="AIzaSyBlD0AohE5yC5xFN20KGH24L7gmqIy9OWc"
from apiclient.discovery import build
youtube=build('youtube','v3',developerKey=api_key)

req=youtube.search().list(q=arglist[0], part='snippet', type='video', maxResults=int(arglist[1]))
i=0
res=req.execute()
for item in res['items']:
	print(item['snippet']['title'])
	query_string = urllib.parse.urlencode({"search_query" : item['snippet']['title']})
	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	urllist.append("http://www.youtube.com/watch?v=" + search_results[i])
	print(urllist[i])	
	i+=1

import os
from random import randint
x=randint(1000,10000)
print(x)
newpath = r'yt'+str(x) 
if not os.path.exists(newpath):
    os.makedirs(newpath)	

j=0
for j in range(0,len(urllist)):
	link=urllist[j]
	try:
        	yt=pytube.YouTube(link)
	except:
        	print('not linking')

	stream = yt.streams.first()
	stream.download(newpath)
	print('Downloaded')