#!/usr/bin/env python
import redis

node1 = 'devbe01.svil.actalis.it'
node2 = 'devbe02.svil.actalis.it'
node3 = 'devbe03.svil.actalis.it'

try:
    conn = redis.StrictRedis(
    host=node3,
    port=16379,
    password='$redis0123!')
#    print (conn)
    conn.ping()
#    print ('Connected!')
except Exception as ex:
    print ('Error:', ex)
    exit('Failed to connect, terminating.')

#print(test.decode('utf-8'))
	
serviceList = conn.hgetall('mwconfig:services')	

for service in serviceList:
	trustChainCertificate = conn.hget('mwconfig:service:'+service.decode('utf-8'),'trustChainCertificate').decode('utf-8')
	if trustChainCertificate is not None:
		trustchainList = conn.hgetall('mwconfig:trustChains')
		for key, value in trustchainList.items():
			if trustChainCertificate == value.decode('utf-8') :
				conn.hset('mwconfig:service:'+service.decode('utf-8'), "trustChainCertificate", key.decode('utf-8'))
				
	



	

	


