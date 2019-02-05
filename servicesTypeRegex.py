#!/usr/bin/env python
import redis

node1 = 'devbe01.svil.actalis.it'
node2 = 'devbe02.svil.actalis.it'
node3 = 'devbe03.svil.actalis.it'

try:
    conn = redis.StrictRedis(
    host=node2,
    port=16379,
    password='$redis0123!')
#    print (conn)
    conn.ping()
#    print ('Connected!')
except Exception as ex:
    print ('Error:', ex)
    exit('Failed to connect, terminating.')

#print(test.decode('utf-8'))
	
serviceTypesList = conn.hgetall('mwconfig:serviceTypes')	

regexMap = {}
regexMap["ssl_server_ev"] = "((?=[a-zA-Z0-9\\-]{1,63}\\.)(xn--)?[a-zA-Z0-9]+(\\-[a-zA-Z0-9]+)*\\.)+(((xn--)?)[a-zA-Z0-9\\-]{2,63})" 
regexMap["ssl_server_ov"] = "((?=[a-zA-Z0-9\\-]{1,63}\\.)(xn--)?[a-zA-Z0-9]+(\\-[a-zA-Z0-9]+)*\\.)+(((xn--)?)[a-zA-Z0-9\\-]{2,63})"
regexMap["ssl_server_dv"] = "((?=[a-zA-Z0-9\\-]{1,63}\\.)(xn--)?[a-zA-Z0-9]+(\\-[a-zA-Z0-9]+)*\\.)+(((xn--)?)[a-zA-Z0-9\\-]{2,63})"
regexMap["ssl_server_ms_ev"] = "((?=[a-zA-Z0-9\\-]{1,63}\\.)(xn--)?[a-zA-Z0-9]+(\\-[a-zA-Z0-9]+)*\\.)+(((xn--)?)[a-zA-Z0-9\\-]{2,63})"
regexMap["ssl_server_ms_ov"] = "((?=[a-zA-Z0-9\\-]{1,63}\\.)(xn--)?[a-zA-Z0-9]+(\\-[a-zA-Z0-9]+)*\\.)+(((xn--)?)[a-zA-Z0-9\\-]{2,63})"
regexMap["ssl_server_ms_dv"] = "((?=[a-zA-Z0-9\\-]{1,63}\\.)(xn--)?[a-zA-Z0-9]+(\\-[a-zA-Z0-9]+)*\\.)+(((xn--)?)[a-zA-Z0-9\\-]{2,63})"
regexMap["ssl_server_wildcard"] = "\\*\\.((?=[a-zA-Z0-9\\-]{1,63}\\.)(xn--)?[a-zA-Z0-9]+(\\-[a-zA-Z0-9]+)*\\.)+(((xn--)?)[a-zA-Z0-9\\-]{2,63})"
regexMap["ssl_server_wildcard_dv"] = "\\*\\.((?=[a-zA-Z0-9\\-]{1,63}\\.)(xn--)?[a-zA-Z0-9]+(\\-[a-zA-Z0-9]+)*\\.)+(((xn--)?)[a-zA-Z0-9\\-]{2,63})"
regexMap["ssl_codesign_ev"] = "([a-zA-Z0-9'\\s\\-\\:\\.\\&\\,\\@])+"
regexMap["ssl_codesign_ov"] = "([a-zA-Z0-9'\\s\\-\\:\\.\\&\\,\\@])+"
regexMap["ssl_server_wild_multi"] = "(\\*\\.)*((?=[a-zA-Z0-9\\-]{1,63}\\.)(xn--)?[a-zA-Z0-9]+(\\-[a-zA-Z0-9]+)*\\.)+(((xn--)?)[a-zA-Z0-9\\-]{2,63})"
regexMap["ssl_encryption"] = "([A-Za-z0-9\\s]+)*"
regexMap["winlogon"] = "([A-Za-z0-9\\s]+)*"
regexMap["ssl_client"] = "([A-Za-z0-9\\s\\/]+)*"
regexMap["mobile_client"] = "([A-Za-z0-9@\\.\\s]+)*"
regexMap["dsig_procaut"] = "([A-Za-z0-9@\\.\\s]+)*"
regexMap["generic"] = "([a-zA-Z0-9'\\s\\-\\:\\.\\&\\,\\@\\/])+"

#print(streetno.get("0"))

for key, value in serviceTypesList.items():
	typeId = key.decode('utf-8')
	typeName = value.decode('utf-8')

	key_name = 'mwconfig:serviceType:'+typeId;
	
	regex = regexMap.get(typeName);
	
	if (regex is None):
		regex = "";
		
	conn.hset(key_name, 'regex', regex)
	
	
	
	
	
	
	
	
	
	


				
	



	

	


