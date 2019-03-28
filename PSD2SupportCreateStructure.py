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

# create the key uiconfig:ncaList
conn.hset("uiconfig:ncaList", "1", "Austria")
conn.hset("uiconfig:ncaDetails:1", "id", "AT-FMA")
conn.hset("uiconfig:ncaDetails:1", "name", "Austria Financial Market Authority")

conn.hset("uiconfig:ncaList", "2", "Belgium")
conn.hset("uiconfig:ncaDetails:2", "id", "BE-NBB")
conn.hset("uiconfig:ncaDetails:2", "name", "National Bank of Belgium")

conn.hset("uiconfig:ncaList", "3", "Bulgaria")
conn.hset("uiconfig:ncaDetails:3", "id", "BG-BNB")
conn.hset("uiconfig:ncaDetails:3", "name", "Bulgarian National Bank")

conn.hset("uiconfig:ncaList", "4", "Croatia")
conn.hset("uiconfig:ncaDetails:4", "id", "HR-CNB")
conn.hset("uiconfig:ncaDetails:4", "name", "Croatian National Bank")

conn.hset("uiconfig:ncaList", "5", "Cyprus")
conn.hset("uiconfig:ncaDetails:5", "id", "CY-CBC")
conn.hset("uiconfig:ncaDetails:5", "name", "Central Bank of Cyprus")

conn.hset("uiconfig:ncaList", "6", "Czech")
conn.hset("uiconfig:ncaDetails:6", "id", "CZ-CNB")
conn.hset("uiconfig:ncaDetails:6", "name", "Czech National Bank")

conn.hset("uiconfig:ncaList", "7", "Denmark")
conn.hset("uiconfig:ncaDetails:7", "id", "DK-DFSA")
conn.hset("uiconfig:ncaDetails:7", "name", "Danish Financial Supervisory Authority")

conn.hset("uiconfig:ncaList", "8", "Estonia")
conn.hset("uiconfig:ncaDetails:8", "id", "EE-FI")
conn.hset("uiconfig:ncaDetails:8", "name", "Estonia Financial Supervisory Authority")

conn.hset("uiconfig:ncaList", "9", "Finland")
conn.hset("uiconfig:ncaDetails:9", "id", "FI-FINFSA")
conn.hset("uiconfig:ncaDetails:9", "name", "Finnish Financial Supervisory Authority")

conn.hset("uiconfig:ncaList", "10", "France")
conn.hset("uiconfig:ncaDetails:10", "id", "FR-ACPR")
conn.hset("uiconfig:ncaDetails:10", "name", "Prudential Supervisory and Resolution Authority")

conn.hset("uiconfig:ncaList", "11", "Germany")
conn.hset("uiconfig:ncaDetails:11", "id", "DE-BAFIN")
conn.hset("uiconfig:ncaDetails:11", "name", "Federal Financial Supervisory Authority")

conn.hset("uiconfig:ncaList", "12", "Greece")
conn.hset("uiconfig:ncaDetails:12", "id", "GR-BOG")
conn.hset("uiconfig:ncaDetails:12", "name", "Bank of Greece")

conn.hset("uiconfig:ncaList", "13", "Hungary")
conn.hset("uiconfig:ncaDetails:13", "id", "HU-CBH")
conn.hset("uiconfig:ncaDetails:13", "name", "Central Bank of Hungary")

conn.hset("uiconfig:ncaList", "14", "Iceland")
conn.hset("uiconfig:ncaDetails:14", "id", "IS-FME")
conn.hset("uiconfig:ncaDetails:14", "name", "Financial Supervisory Authority")

conn.hset("uiconfig:ncaList", "15", "Ireland")
conn.hset("uiconfig:ncaDetails:15", "id", "IE-CBI")
conn.hset("uiconfig:ncaDetails:15", "name", "Central Bank of Ireland")

conn.hset("uiconfig:ncaList", "16", "Italy")
conn.hset("uiconfig:ncaDetails:16", "id", "IT-BI")
conn.hset("uiconfig:ncaDetails:16", "name", "Bank of Italy")

conn.hset("uiconfig:ncaList", "17", "Liechtenstein")
conn.hset("uiconfig:ncaDetails:17", "id", "LI-FMA")
conn.hset("uiconfig:ncaDetails:17", "name", "Financial Market Authority Liechtenstein")

conn.hset("uiconfig:ncaList", "18", "Latvia")
conn.hset("uiconfig:ncaDetails:18", "id", "LV-FCMC")
conn.hset("uiconfig:ncaDetails:18", "name", "Financial and Capital Markets Commission")

conn.hset("uiconfig:ncaList", "19", "Lithuania")
conn.hset("uiconfig:ncaDetails:19", "id", "LT-BL")
conn.hset("uiconfig:ncaDetails:19", "name", "Bank of Lithuania")

conn.hset("uiconfig:ncaList", "20", "Luxembourg")
conn.hset("uiconfig:ncaDetails:20", "id", "LU-CSSF")
conn.hset("uiconfig:ncaDetails:20", "name", "Commission for the Supervision of Financial Sector")

conn.hset("uiconfig:ncaList", "21", "Norway")
conn.hset("uiconfig:ncaDetails:21", "id", "NO-FSA")
conn.hset("uiconfig:ncaDetails:21", "name", "The Financial Supervisory Authority of Norway")

conn.hset("uiconfig:ncaList", "22", "Malta")
conn.hset("uiconfig:ncaDetails:22", "id", "MT-MFSA")
conn.hset("uiconfig:ncaDetails:22", "name", "Malta Financial Services Authority")

conn.hset("uiconfig:ncaList", "23", "Netherlands")
conn.hset("uiconfig:ncaDetails:23", "id", "NL-DNB")
conn.hset("uiconfig:ncaDetails:23", "name", "The Netherlands Bank")

conn.hset("uiconfig:ncaList", "24", "Poland")
conn.hset("uiconfig:ncaDetails:24", "id", "PL-PFSA")
conn.hset("uiconfig:ncaDetails:24", "name", "Polish Financial Supervision Authority")

conn.hset("uiconfig:ncaList", "25", "Portugal")
conn.hset("uiconfig:ncaDetails:25", "id", "PT-BP")
conn.hset("uiconfig:ncaDetails:25", "name", "Bank of Portugal")

conn.hset("uiconfig:ncaList", "26", "Romania")
conn.hset("uiconfig:ncaDetails:26", "id", "RO-NBR")
conn.hset("uiconfig:ncaDetails:26", "name", "National Bank of Romania")

conn.hset("uiconfig:ncaList", "27", "Slovakia")
conn.hset("uiconfig:ncaDetails:27", "id", "SK-NBS")
conn.hset("uiconfig:ncaDetails:27", "name", "National Bank of Slovakia")

conn.hset("uiconfig:ncaList", "28", "Slovenia")
conn.hset("uiconfig:ncaDetails:28", "id", "SI-BS")
conn.hset("uiconfig:ncaDetails:28", "name", "Bank of Slovenia")

conn.hset("uiconfig:ncaList", "29", "Spain")
conn.hset("uiconfig:ncaDetails:29", "id", "ES-BE")
conn.hset("uiconfig:ncaDetails:29", "name", "Bank of Spain")

conn.hset("uiconfig:ncaList", "30", "Sweden")
conn.hset("uiconfig:ncaDetails:30", "id", "SE-FINA ")
conn.hset("uiconfig:ncaDetails:30", "name", "Swedish Financial Supervision Authority")

conn.hset("uiconfig:ncaList", "31", "United Kingdom")
conn.hset("uiconfig:ncaDetails:31", "id", "GB-FCA")
conn.hset("uiconfig:ncaDetails:31", "name", "Financial Conduct Authority")

conn.lpush("uiconfig:ncaRoles", "Account servicing (PSP_AS)")
conn.lpush("uiconfig:ncaRoles", "Payment initiation (PSP_PI)")
conn.lpush("uiconfig:ncaRoles", "Account information (PSP_AI)")
conn.lpush("uiconfig:ncaRoles", "Issuing of card-based payment instruments (PSP_IC)")

conn.hset("mwconfig:serviceTypes", "19", "nca")
conn.hset("mwconfig:serviceType:19", "description", "nca")
	
	
	
	
	
	
	
	
	
	


				
	



	

	


