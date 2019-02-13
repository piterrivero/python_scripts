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
	
conn.hset('uiconfig:fieldsShownUI', '1', 'row_certificate_allowed_num_san')	
conn.hset('uiconfig:fieldsShownUI', '2', 'row_email_san_management')	

conn.hset('mwconfig:serviceType:11:uiField:1', 'rendered_row', 'true')
conn.hset('mwconfig:serviceType:11:uiField:1', 'description', 'ExternalRA\CertificatesAuthorizeComplete\step4.xhtml')

conn.hset('mwconfig:serviceType:11:uiField:2', 'rendered_row', 'true')
conn.hset('mwconfig:serviceType:11:uiField:2', 'description', 'ExternalRA\CertificatesAuthorizeComplete\step4.xhtml')

conn.hset('mwconfig:serviceType:12:uiField:1', 'rendered_row', 'true')
conn.hset('mwconfig:serviceType:12:uiField:1', 'description', 'ExternalRA\CertificatesAuthorizeComplete\step4.xhtml')

conn.hset('mwconfig:serviceType:12:uiField:2', 'rendered_row', 'true')
conn.hset('mwconfig:serviceType:12:uiField:2', 'description', 'ExternalRA\CertificatesAuthorizeComplete\step4.xhtml')

conn.hset('mwconfig:serviceType:10:uiField:1', 'rendered_row', 'true')
conn.hset('mwconfig:serviceType:10:uiField:1', 'description', 'ExternalRA\CertificatesAuthorizeComplete\step4.xhtml')

conn.hset('mwconfig:serviceType:10:uiField:2', 'rendered_row', 'true')
conn.hset('mwconfig:serviceType:10:uiField:2', 'description', 'ExternalRA\CertificatesAuthorizeComplete\step4.xhtml')

conn.hset('mwconfig:serviceType:14:uiField:1', 'rendered_row', 'true')
conn.hset('mwconfig:serviceType:14:uiField:1', 'description', 'ExternalRA\CertificatesAuthorizeComplete\step4.xhtml')

conn.hset('mwconfig:serviceType:14:uiField:2', 'rendered_row', 'true')
conn.hset('mwconfig:serviceType:14:uiField:2', 'description', 'ExternalRA\CertificatesAuthorizeComplete\step4.xhtml')


	
	
	
	
	
	
	
	
	
	


				
	



	

	



	