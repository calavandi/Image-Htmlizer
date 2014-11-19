f=open(".sample.txt",'w')
import os
a=os.popen('ls').read()
print(a)
f.write(a)
f=open('.sample.txt','r')
p=open('.part1.html','w')
Lines=f.readlines()
i=0
p.write('<html>')
p.write('<center>')
print(Lines)
p.write('<div id="pad">')
q=('"width="1000" height="1200">')
i=0
np=open('.part2.html','w')
for each_item in Lines:
	if(i>=100):
		if(i==100):
			np.write('<html>')
			np.write('<center>')
			np.write('<a href=".part1.html"> <<---Back to previous page</a>')
		Lines[i]=(Lines[i]+str(q))
		np.write('<div id="'+str(i))
		np.write('">')
		np.write("\n")
		np.write('<img src="'+Lines[i])
		print Lines[i]
		i=i+1
	else:
		Lines[i]=(Lines[i]+str(q))
		p.write('<div id="'+str(i))
		p.write('">')
		p.write("\n")
		p.write('<img src="'+Lines[i])
		print Lines[i]
		if(i==99):
			p.write('\n<b><i><a href=".part2.html">Next page--->> </b></i></a>')
			p.write('</html>')
		i=i+1
np.write("</div>")
np.write('<a href=".part1.html"> <<---Back to previous pag </a><br>')
np.write('\n\n<a href=".part2.html"> <<-- Back to Top</a>')
np.write("</html>")
p.close()
np.close()
os.popen('firefox .part1.html || chromium-browser .part1.html || google-chrome .part1.html')
os.popen('exit')
