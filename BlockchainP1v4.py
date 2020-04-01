import urllib2
import time  #use time.sleep(number of seconds) to wait between requests
import requests
import json

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
address_list=['19ere2oJzJh81A5Q64SExDZYz54RvWHqZz']
address_list=list(set(address_list))
url='https://blockchain.info/rawaddr/'
outer=[]
for al in address_list:
	
	r=requests.get(url+al,headers=headers)
	json_response=json.loads(r.text)
	time.sleep(20)
	add1=[] 
	add2=[]
	# print "###########################"
	# print "Processing",url+al
	# print "###########################"
	#Save the group of addresses used as input into different lists
	#We then ignore the addresses not linked to the address provided in the 
	addlwadd=[]
	for k,v in json_response.items():
		if k=='address':
			print "###########################"
			print "bitcoin address:",v
			#save the btc address provided
			btc_add=str(v)
			add1.append(v)
			print "###########################"
		elif k=='txs':
			
			for v1 in v[:50]:
				inner=[]
				# trans=trans+1
				for k1,v2 in v1.items():
					# print k1
					if k1=='inputs':
					# 	#loop the address remove the last one as thats how the given address is created
						
						for vs in v2:
							
							for k3,vs1 in vs.items():
								if k3=='prev_out':
									for k4,vs2 in vs1.items():
										if k4=='addr':
											inner.append(vs2.encode("utf-8"))

							
				outer.append(inner)		# print inner
				for out in outer:
					if btc_add in out:
						for o in out:
							if o not in address_list:
								# print o
								# final_list.append(o)

								address_list.append(o)
								# print address_list

print "# of addresses linked with ",address_list[0], "is ", len(address_list)

balance=[]
#Error urls can be used to make more requests if HTTP errors are raised
error_url=[]

for add in address_list:
		# print url+val
		try:

			r1=requests.get(url+add,headers=headers)
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
					print "balance of",add,"is", v1/float((10**7))
		except Exception as e:
			error_url.append(url+val,e)
			# print "Error Url:"+ url+val
			continue

print "#################################################"
print "Total Balance is:",sum(balance)/ float((10**7))
print "#################################################"

# print address_list
# print address_list

# print addlwadd
