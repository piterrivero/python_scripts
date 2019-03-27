#!/usr/bin/env python
import redis

node1 = 'devbe01.svil.actalis.it'
node2 = 'devbe02.svil.actalis.it'
node3 = 'devbe03.svil.actalis.it'

try:
    conn = redis.StrictRedis(
    host=node3,
    port=16379,
    password='')
#    print (conn)
    conn.ping()
#    print ('Connected!')
except Exception as ex:
    print ('Error:', ex)
    exit('Failed to connect, terminating.')

#print(test.decode('utf-8'))

trustChainList = conn.hgetall('mwconfig:trustChains')

cont = 1

for key, value in trustChainList.items():
	trustChainName = key.decode('utf-8')
	p7b = value.decode('utf-8')
	conn.hset("mwconfig:trustChains", cont, trustChainName)
	conn.hset("mwconfig:trustChain:"+str(cont), "p7b", p7b)
	conn.hdel("mwconfig:trustChains",trustChainName)
	cont = cont + 1






	



	

	


