import requests
url = 'http://automation.pratiche.it:8080/requests'
data = [{
			"input": {
         	   "vatNumber": "03000300123",
			   "format": "xml"
			},
			"service_id": 27
		}]		

response = requests.post(url, data=data)
print (response.text)