#!/usr/bin/env python
import redis

node1 = 'devbe01.svil.actalis.it'
node2 = 'devbe02.svil.actalis.it'
node3 = 'devbe03.svil.actalis.it'

try:
    conn = redis.StrictRedis(
    host=node1,
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
	idType = conn.hget('mwconfig:service:'+service.decode('utf-8'),'idType')
	if idType is None:
		type = conn.hget('mwconfig:service:'+service.decode('utf-8'),'type')
		type = type.decode('utf-8')
		serviceTypeList = conn.hgetall('mwconfig:serviceTypes')
		for key, value in serviceTypeList.items():
			if type == value.decode('utf-8') :
				key_name = 'mwconfig:service:'+service.decode('utf-8')
				idTypeValue = key.decode('utf-8')
				conn.hset(key_name, 'idType', idTypeValue)
				
	



	

	


