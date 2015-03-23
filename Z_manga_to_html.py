from glob import glob
import webbrowser
images = glob("*.jpg") + glob("*.png")
f = open(".comic.html","w")
imgbegin = '<img src="'
#imgend = '">'
imgspec='"width="1100" height="1200">'
i=0;
images.sort()
f1=open('.part2.html','w') 
for src in images:
	f.write(imgbegin+src+imgspec+"<br><br><BR><BR>")
	f.write(str(i))
	f.write("\n")
	i=i+1
	if(i==183):
		f.write("<a href=.part2.html> Part 2--> </a></html>")
	if(i>182):
		f1.write(imgbegin+src+imgspec+"<BR><BR><BR>")
f.close()
f1.close() 
webbrowser.open(".comic.html")
