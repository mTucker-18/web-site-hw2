a = open("templates/top.html").read() 
b = open("content/index.html").read()
c = open("templates/bottom.html").read()

d = a + b + c

open("docs/index.html", "w+").write(d)

e = open("templates/top.html").read() 
f = open("content/projects.html").read()
g = open("templates/bottom.html").read()

h = e + f + g

open("docs/projects.html", "w+").write(h)

k = open("templates/top.html").read() 
l = open("content/blog.html").read()
m = open("templates/bottom.html").read()

n = k + l + m

open("docs/blog.html", "w+").write(n)
