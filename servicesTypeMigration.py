#!/usr/bin/env python
import redis

try:
    conn = redis.StrictRedis(
    host='devbe01.svil.actalis.it',
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
		serviceTypeList = conn.hgetall('mwconfig:serviceTypes')
		for serviceType in serviceTypeList:
			print (serviceType)
	
	


	

	


