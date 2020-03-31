import urllib2
# from future import division
import time
import requests
import json
import cfscrape
#attempt to evade cloudflare Not required
scraper = cfscrape.create_scraper(delay=20)


#Urls needed
url='https://blockchain.info/rawaddr/'
urlt1="https://blockchain.info/rawaddr/15hzoz4YzGnj9Pqu8eNmhw4tBpDGjNgwj9"
urlt2="https://blockchain.info/rawaddr/36bt43aDDvsMJRd48YiRh6LLrNm3qnGZW5"
urlt3="https://blockchain.info/rawaddr/19ere2oJzJh81A5Q64SExDZYz54RvWHqZz"
#User agents to pass with get request
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}


r=requests.get(urlt2,headers=headers)
json_response=json.loads(r.text)
trans=0
add1=[] 
add2=[]

#Save the group of addresses used as input into different lists
#We then ignore the addresses not linked to the address provided in the 
outer=[]
for k,v in json_response.items():
	if k=='address':
		print "###########################"
		print "bitcoin address:",v
		#save the btc address provided
		btc_add=str(v)
		add1.append(v)
		print "###########################"
	elif k=='txs':
		
		for v1 in v[:-1]:
			inner=[]
			trans=trans+1
			for k1,v2 in v1.items():
				# print k1
				if k1=='inputs':
				# 	#loop the address remove the last one as thats how the given address is created
					
					for vs in v2:
						
						for k3,vs1 in vs.items():
							if k3=='prev_out':
								for k4,vs2 in vs1.items():
									if k4=='addr':
										# print vs2
										# add2.append(vs2.encode("utf-8"))
										inner.append(vs2.encode("utf-8"))
			outer.append(inner)

# print outer,len(outer)
final_list=[]
# removing the addresses used for sending BTC to the provided BTC address
for out in outer:
	if btc_add in out:
		for o in out:
			if o not in final_list:
				final_list.append(o)

print "# of addresses linked with ",btc_add, "is ", len(final_list)
"###########################"
# #creating a dictionary with address 
#this was done for visualization
adict = {}
for a1 in add1:
	adict[a1] =  final_list
	
balance=[]
#Error urls can be used to make more requests if HTTP errors are raised
error_url=[]
# sumb=0
for key,value in adict.items():
	for val in value:
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
		except Exception as e:
			error_url.append(url+val,e)
			# print "Error Url:"+ url+val
			continue

print "#################################################"
print "Total Balance is:",sum(balance)/ float((10**7))
print "#################################################"