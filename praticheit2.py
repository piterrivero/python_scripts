import requests
url = 'http://automation.pratiche.it:8080/requests/383751'

response = requests.get(url)
print (response.text)