# import xplore

# query = xplore.xploreapi.XPLORE('cmvp85nujeda5s27qhyeze28')
# query.abstractText('SOA')
# data = query.callAPI()  
# print(data)
# cmvp85nujeda5s27qhyeze28
import requests 
import datetime
import json

## file name setting
dt = datetime.datetime.now()
timestamp = dt.timestamp()
filename = "ieee " + str(hex(int(timestamp)))
file_ext = ".json"

## IEEE Explore API
url = "https://ieeexploreapi.ieee.org/api/v1/search/articles?parameter&apikey=cmvp85nujeda5s27qhyeze28"
## search parameter
querytext = "(SOA or ""service oriented architecture"")"
resp_format = "json"
## sorting and paging
max_records = 200
sort_field = "article_number"
sort_order = "asc"
start_record = 4001

params = {'querytext': querytext, 'format':resp_format, 'max_records':max_records, 'sort_field':sort_field, 'sort_order':sort_order, 'start_record':start_record}

request_cnt = 20
for i in range(0, request_cnt):
    resp = requests.get(url, params=params, verify=False)
    params = {'querytext': querytext, 'format':resp_format, 'max_records':max_records, 'sort_field':sort_field, 'sort_order':sort_order, 'start_record':start_record} 
    print("params is " + str(params))
    # print("request count is " + str(i) + ", Status Code is " + str(resp.status_code) + ", and start record is " + str(start_record))
    start_record = start_record + max_records
    with open(filename + "-" + str(start_record) + file_ext, "a") as json_file :
        json_obj = resp.json()
        json.dump(json_obj["articles"], json_file)
        # json_file.write(", ")
        # json.dump(resp.json(), json_file) 

print("file name is " + json_file.name) 
