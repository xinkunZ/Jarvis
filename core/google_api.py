import os
from pprint import pprint

import httplib2
from googleapiclient import discovery
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from cfg.R import get_ini_path

auth_file_name_path = get_ini_path() + os.path.sep + "auth.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = auth_file_name_path
os.environ['GRPC_PROXY_EXP'] = '127.0.0.1:1080'
project = 'booming-bonito-196507'
zone = 'asia-east1-c'
scopes = ['https://www.googleapis.com/auth/cloud-platform',
          'https://www.googleapis.com/auth/compute',
          'https://www.googleapis.com/auth/compute.readonly',
          'https://www.googleapis.com/auth/devstorage.full_control',
          'https://www.googleapis.com/auth/devstorage.read_only',
          'https://www.googleapis.com/auth/devstorage.read_write']


def list_instances():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_file_name_path, scopes=scopes)
    http = Http(timeout=10,
                proxy_info=httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, '127.0.0.1', 1080))
    http_auth = credentials.authorize(http)
    service = discovery.build('compute', 'v1', http=http_auth)
    request = service.instances().aggregatedList(project=project)
    response = request.execute()
    for name, instances_scoped_list in response['items'].items():
        if instances_scoped_list.get('warning', None) is None:
            pprint((name, instances_scoped_list))


__all__ = ['list_instances']

list_instances()
