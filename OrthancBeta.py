import requests
import datetime
import json
from pprint import pprint

data = '{"PatientID": "445718"}'

url = 'http://10.100.0.19:80/modalities/SRV-ORTH-01/find-study'


response = requests.post(url, data=data)
result = response.json()

data_string = json.loads(response.text)

pprint(data_string)

date = print(data_string['LastUpdate'])
pl = (data_string['MainDicomTags']['AccessionNumber'])
uuid = print(data_string['ID'])


#
# listsa = []
# for i in range(len(orthanc_user_ids)):
#     pidsa = requests.get(url + '/' + orthanc_user_ids[i] )
#     data=json.loads(pidsa.text)
#     pprint(data)
