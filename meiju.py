#coding:utf-8
import urllib2
from BeautifulSoup import *                              # ALL

response = urllib2.urlopen("http://www.ttmeiju.com/meiju/Elementary.html?page=1")
#print response.read()
html_doc = response.read()

soup = BeautifulSoup(html_doc)
#print soup.body
#print soup.findAll('tr')
#print soup.findAll(attrs={'class':'Scontent'}) #天天美剧里的列表

def isMeiJu(tag):
	print "**************************************tag"
	print str(tag)
	print "******dir start"
	print dir(tag) #内置dir函数可以查看模块的所有方法
	print "******dir end"
	#return tag.find("a") and tag.get("class") == "Scontent"
	return tag.find("tr") #and tag.get("class") == "Scontent"

result = soup.findAll(isMeiJu)
print result
print len(result)