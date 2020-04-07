import urllib2
import time  #use time.sleep(number of seconds) to wait between requests
import requests
import json

sleeptime=11
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}

# address_list=['19ere2oJzJh81A5Q64SExDZYz54RvWHqZz']
address_list=[
	# '15hzoz4YzGnj9Pqu8eNmhw4tBpDGjNgwj9',
	# '36bt43aDDvsMJRd48YiRh6LLrNm3qnGZW5',
	'19ere2oJzJh81A5Q64SExDZYz54RvWHqZz',
	# '19QDGMRKdZ9BpDZP2Re6yaDqNQ7zN4wo1D'
        ]

address_list=list(set(address_list))
url='https://blockchain.info/rawaddr/'
outer=[]
# print "###########################"
# print "bitcoin address:",address_list[0]
# print "###########################"
for al in address_list:
	# print "bitcoin address:",v
	r=requests.get(url+al,headers=headers)
	json_response=json.loads(r.text)
	time.sleep(sleeptime)
	add1=[] 
	
	# print "###########################"
	# print "Processing",url+al
	# print "###########################"
	#Save the group of addresses used as input into different lists
	#We then ignore the addresses not linked to the address provided in the 
	
	for k,v in json_response.items():
		if k=='address':
			
			print "Processing bitcoin address:",v
			#save the btc address provided
			btc_add=str(v)
			add1.append(v)
			print "#################################################"
		elif k=='txs':
			# print len(v)
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
print "#################################################"
print "bitcoin address:",address_list[0]
# print "###########################"
print "#################################################"
print "# of addresses linked with ",address_list[0], "is ", len(address_list)

#get final balances

error_url=[]
baseurl = 'https://blockchain.info/balance?active='
query = "|".join(address_list)
new_url=baseurl+query
r1=requests.get(new_url,headers=headers)

json_response1=json.loads(r1.text)

final_balance=[]
for k,v in json_response1.items():
	
	balance=str(v['final_balance'])
	balance=int(balance)/float((10**8))
	print "balance of ",k,"is:",balance
	final_balance.append(balance)


# print final_balance	
print "#################################################"
print "Total Balance is:",sum(final_balance)#/ float((10**7))
print "#################################################"	

	
