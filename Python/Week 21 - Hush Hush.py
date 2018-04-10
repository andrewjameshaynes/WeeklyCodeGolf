def p(s):
	l=[]
	for i in s.split(" "):
		l.append(i[1:]+" "+i[0]+"ay")
	print(' '.join(l))

p("speaking pig latin is fun")
p("I am speaking pig latin")

def e(s):
	l=[]
	y=s.replace("ay", "").split(" ")
	for i in range(0,int(len(y)/2)):
		l.append(y[2*i+1]+y[2*i])
	print(y)
	print(" ".join(l))

#e("peaking say ig pay atin lay s iay un fay")
e("Iay m aay peaking say ig pay atin lay")