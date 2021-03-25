import requests

url = "https://api.careeronestop.org/v1/jobsearch/USER_ACCOUNT_HERE/15-1252/TX/100/0/0/0/50000/0?source=NLx&showFilters=true"

payload={}
headers = {
  'Authorization': 'Bearer API_KEY_HERE'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
