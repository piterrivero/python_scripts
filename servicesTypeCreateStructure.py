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

# create the key mwconfig:serviceTypes
conn.hset("mwconfig:serviceTypes", "1", "ssl_client")
conn.hset("mwconfig:serviceTypes", "2", "cns_like")
conn.hset("mwconfig:serviceTypes", "3", "dsig_procaut")
conn.hset("mwconfig:serviceTypes", "4", "encryption")
conn.hset("mwconfig:serviceTypes", "5", "generic")
conn.hset("mwconfig:serviceTypes", "6", "mobile_client")
conn.hset("mwconfig:serviceTypes", "7", "ssl_codesign_ov")
conn.hset("mwconfig:serviceTypes", "8", "ssl_server_dv")
conn.hset("mwconfig:serviceTypes", "9", "ssl_server_ev")
conn.hset("mwconfig:serviceTypes", "10", "ssl_server_ms_dv")
conn.hset("mwconfig:serviceTypes", "11", "ssl_server_ms_ev")
conn.hset("mwconfig:serviceTypes", "12", "ssl_server_ms_ov")
conn.hset("mwconfig:serviceTypes", "13", "ssl_server_ov")
conn.hset("mwconfig:serviceTypes", "14", "ssl_server_wild_multi")
conn.hset("mwconfig:serviceTypes", "15", "ssl_server_wildcard")
conn.hset("mwconfig:serviceTypes", "16", "ssl_server_wildcard_dv")
conn.hset("mwconfig:serviceTypes", "17", "winlogon")
conn.hset("mwconfig:serviceTypes", "18", "doc_sign")
	
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
regexMap["ssl_codesign_ov"] = "([a-zA-Z0-9'\\s\\-\\:\\.\\&\\,\\@])+"
regexMap["ssl_server_wild_multi"] = "(\\*\\.)*((?=[a-zA-Z0-9\\-]{1,63}\\.)(xn--)?[a-zA-Z0-9]+(\\-[a-zA-Z0-9]+)*\\.)+(((xn--)?)[a-zA-Z0-9\\-]{2,63})"
regexMap["ssl_encryption"] = "([A-Za-z0-9\\s]+)*"
regexMap["winlogon"] = "([A-Za-z0-9\\s]+)*"
regexMap["ssl_client"] = "([A-Za-z0-9\\s\\/]+)*"
regexMap["mobile_client"] = "([A-Za-z0-9@\\.\\s]+)*"
regexMap["dsig_procaut"] = "([A-Za-z0-9@\\.\\s]+)*"
regexMap["generic"] = "([a-zA-Z0-9'\\s\\-\\:\\.\\&\\,\\@\\/])+"

descriptionMap = {}
descriptionMap["dsig_procaut"] = "Generic Qualified Digital Signature"
descriptionMap["winlogon"] = "Windows Logon"
descriptionMap["ssl_client"] = "SSL Client"
descriptionMap["mobile_client"] = "Mobile Client"
descriptionMap["encryption"] = "Encryption"
descriptionMap["ssl_server_ev"] = "SSL Server EV single host"
descriptionMap["ssl_server_ms_ev"] = "SSL Server EV multiple host"
descriptionMap["ssl_server_ov"] = "SSL Server OV single host"
descriptionMap["ssl_server_ms_ov"] = "SSL Server OV multiple host"
descriptionMap["ssl_server_wildcard"] = "SSL Server wild card"
descriptionMap["ssl_server_wild_multi"] = "SSL Server wild card multiple host"
descriptionMap["ssl_codesign_ov"] = "Code Signing OV"
descriptionMap["ssl_server_dv"] = "SSL Server DV single host"
descriptionMap["ssl_server_wildcard_dv"] = "SSL Server DV wildcard"
descriptionMap["ssl_server_ms_dv"] = "SSL Server DV multiple host"
descriptionMap["cns_like"] = "Autenticazione CNS like"
descriptionMap["doc_sign"] = "Document Signing"
descriptionMap["timestamping"] = "Timestamping"
descriptionMap["generic"] = "Generic"

for key, value in serviceTypesList.items():
	typeId = key.decode('utf-8')
	typeName = value.decode('utf-8')

	key_name = 'mwconfig:serviceType:'+typeId;
	
	regex = regexMap.get(typeName);
	if (regex is None):
		regex = "";
	conn.hset(key_name, 'regex', regex)
	
	description = descriptionMap.get(typeName);
	if (description is None):
		description = "";
	conn.hset(key_name, 'description', description)
	
	conn.hset(key_name, 'dcvMethods', 'whois,email-admin,email-contact,website-change,dns-change,query-aruba')
	
	
	
	
	
	
	
	
	
	
	


				
	



	

	


