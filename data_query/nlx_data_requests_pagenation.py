'''
This will query for specific job positings using keyword for example: software and filtering on states from NLX API.
More documentation on the URL is here: https://www.careeronestop.org/Developers/WebAPI/Jobs/list-jobs.aspx
'''

import requests, json

KEYWORD = '15-1252'
STATE = 'WA'
LIMIT = 500
START_RECORD = 0
SOURCE ='NLx'
url = "https://api.careeronestop.org/v1/jobsearch/USERACCOUNT_KEY_HERE/"+KEYWORD+"/"+STATE+"/100/0/0/"+str(START_RECORD)+"/"+str(LIMIT)+"/0?source="+SOURCE+"&showFilters=true"

payload = {}
headers = {
  'Authorization': 'Bearer API_KEY_HERE'
}


try:  
    response = requests.request("GET", url, headers=headers, data = payload) 
    op = json.loads(response.text.encode('utf8')) 
    print(op["Jobcount"])
    ttl_pages = (int(op["Jobcount"])//500)+1
    print(ttl_pages)
    for i in range(ttl_pages):
        START_RECORD = i*500
        url = "https://api.careeronestop.org/v1/jobsearch/yrgzrx6QRk8WHjb/"+KEYWORD+"/"+STATE+"/100/0/0/"+str(START_RECORD)+"/"+str(LIMIT)+"/0?source="+SOURCE+"&showFilters=true"

        response = requests.request("GET", url, headers=headers, data = payload)
        op = json.loads(response.text.encode('utf8'))
        print(op)

except Exception as e:
    raise (e)