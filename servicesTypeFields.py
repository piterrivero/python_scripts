#!/usr/bin/env python
import redis

node1 = 'devbe01.svil.actalis.it'
node2 = 'devbe02.svil.actalis.it'
node3 = 'devbe03.svil.actalis.it'

try:
    conn = redis.StrictRedis(
    host=node1,
    port=16379,
    password='')
#    print (conn)
    conn.ping()
#    print ('Connected!')
except Exception as ex:
    print ('Error:', ex)
    exit('Failed to connect, terminating.')

#print(test.decode('utf-8'))
	
conn.delete('uiconfig:fieldsShownUI')
conn.rpush('uiconfig:fieldsShownUI', 'special_fields_for_certs_ms')	
conn.rpush('uiconfig:fieldsShownUI', 'user_identified_by_tin')
conn.rpush('uiconfig:fieldsShownUI', 'cns_like_common_name_msg')
conn.rpush('uiconfig:fieldsShownUI', 'ssl_client_common_name_msg')

conn.hset('mwconfig:serviceType:10:uiField:special_fields_for_certs_ms', 'rendered', 'true')
conn.hset('mwconfig:serviceType:11:uiField:special_fields_for_certs_ms', 'rendered', 'true')
conn.hset('mwconfig:serviceType:12:uiField:special_fields_for_certs_ms', 'rendered', 'true')
conn.hset('mwconfig:serviceType:14:uiField:special_fields_for_certs_ms', 'rendered', 'true')
conn.hset('mwconfig:serviceType:3:uiField:user_identified_by_tin', 'rendered', 'true')
conn.hset('mwconfig:serviceType:2:uiField:cns_like_common_name_msg', 'rendered', 'true')
conn.hset('mwconfig:serviceType:1:uiField:ssl_client_common_name_msg', 'rendered', 'true')



	
	
	
	
	
	
	
	
	
	


				
	



	

	



	