from __future__ import division
import json
from requests import request
from termcolor import colored
from math import ceil

import sevenbridges as sbg
import os

api = sbg.Api(url='https://api.sbgenomics.com/v2', token='f060ce1cf6fd4c28b8d82e99114d7553')


print api.limit
print api.remaining
print api.reset_time


def api_call(path, method='GET', query=None, data=None, token=None):
    base_url = 'https://cgc-datasets-api.sbgenomics.com/datasets/tcga/v0/'

    data = json.dumps(data) if isinstance(data, dict) \
                               or isinstance(data, list) else None

    headers = {
        'X-SBG-Auth-Token': token,
        'Accept': 'application/json',
        'Content-type': 'application/json',
    }

    response = request(method, base_url + path, params=query,
                       data=data, headers=headers)
    response_dict = json.loads(response.text) if \
        response.text else {}

    if response.status_code / 100 != 2:
        print(response_dict)
        print(response_dict['message'])
        print('Error Code: %i.' % (response_dict['code']))
        print(response_dict['more_info'])
        raise Exception('Server responded with status code %s.' \
                        % response.status_code)
    return response_dict

auth_token = 'f060ce1cf6fd4c28b8d82e99114d7553'

query_body = {
    "entity": "files",
    "hasAccessLevel" : "Open",
    "hasDataType" : "Gene expression",
    "hasExperimentalStrategy": "RNA-Seq",
    "hasCase": {
        "hasDiseaseType" : "Breast Invasive Carcinoma",
        "hasGender" : "FEMALE",
        "hasVitalStatus" : "Alive"
    }
}

total = api_call(method='POST', path ='query/total', \
                 token=auth_token, data=query_body)

print colored(total['total'], 'red')

files_in_query = []



loops = int(ceil(total['total'] / 100))

for ii in range(0, loops):
    files_in_query.append(api_call(method='POST', \
                                   path=("query?offset=%i" % (100 * ii)), \
                                   token=auth_token, data=query_body))
    print("%3.1f percent of files added" % (100 * (ii + 1) / loops))

# NOTE: each item in file_list is a list of 100 files from the query. Example below:
print('\n \n')
print(files_in_query[0]['_embedded']['files'][0])
print(files_in_query[1]['_embedded']['files'][0])

file_list = []
for f in files_in_query[0]['_embedded']['files'][0:10]:
    file_list.append(api.files.get(id = f['id']))
    print(file_list[-1].name)

dl_list = []
for f in file_list:
    dl_list.append(f.download_info())

dl_dir = 'downloads'
try:
    os.stat(dl_dir)
except:
    os.mkdir(dl_dir)

for f in file_list:
    f.download(path = ("%s/%s" % (dl_dir, f.name)))