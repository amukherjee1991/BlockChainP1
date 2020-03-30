import urllib2
# from future import division
import time
# import datetime
# import pymysql
# import re
# import httplib
import requests
import json
# import csv
# from urllib2 import HTTPError
# import ssl

import cfscrape
#attempt to evade cloudflare Not required
scraper = cfscrape.create_scraper(delay=20)

#Urls needed
url='https://blockchain.info/rawaddr/'
urlt1="https://blockchain.info/rawaddr/15hzoz4YzGnj9Pqu8eNmhw4tBpDGjNgwj9"
urlt2="https://blockchain.info/rawaddr/36bt43aDDvsMJRd48YiRh6LLrNm3qnGZW5"

#User agents to pass with get request
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}


r=requests.get(urlt1,headers=headers)
json_response=json.loads(r.text)

add1=[] 
add2=[]	
for k,v in json_response.items():
	if k=='address':
		print "###########################"
		print "bitcoin address:",v
		add1.append(v)
		print "###########################"
	elif k=='txs':
		for v1 in v:
			for k1,v2 in v1.items():
				if k1=='inputs':
					#loop the address remove the last one as thats how the given address is created
					for vs in v2[:-1]:
						# print k1,vs
						for k3,vs1 in vs.items():
							if k3=='prev_out':
								for k4,vs2 in vs1.items():
									if k4=='addr':
										# print vs2
										add2.append(vs2)

# print add2
#get unique address
add2=list(set(add2))
print len(add2)

#creating a dictionary with address
adict = {}
for a1 in add1:
	adict[a1] =  add2
	
balance=[]
#Error urls can be used to make more requests if HTTP errors are raised
error_url=[]
# sumb=0
for key,value in adict.items():
	for val in value[:3]:
		# print url+val
		try:

			r1=requests.get(url+val,headers=headers)
			# r1=scraper.get(url+val).content
			# print r1
			# print type(r1)
			json_response1=json.loads(r1.text)
			# print json_response1
			#delay to ensure we are not making a lot of request within a short span of time
			time.sleep(20)	
			for k1,v1 in json_response1.items():
				if k1 == 'final_balance':
					balance.append(int(v1))
					print "balance of",val,"is", v1/float((10**7))
		except:
			# error_url.append(url+val)
			# print "Error Url:"+ url+val
			continue
# print balance

print "Total Balance is:",sum(balance)/ float((10**7))
