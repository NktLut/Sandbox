import gdown
import re

import requests 
from urllib.parse import urlencode


def csv_from_google_drive(file_link, save_path):
    """
    Params:
        file_link - open link to a file on google drive
        save_path - name of the output file without format
        
    Returns:
        Nothing. Downloading a file from drive with entered name.
    """    
    
    file_id = re.search(r'd/(.+)/', file_link).group(1)    
    save_path = save_path + '.csv'    
    gdown.download(id=file_id, output=save_path, quiet=False)


def link_from_ya_disk(data_keys):
    
    """
    Params:
        - list of public urls to ya disk files        
    Return:
        - list of download urls
    """
    
    # Base url
    ya_disk_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?' 
    
    # Direct URLs to the files
    download_urls = []
    
    for k in data_keys:
        public_key  = urlencode(dict(public_key=k))
        request_url = ya_disk_url + public_key
        r = requests.get(request_url) 
        download_urls.append(r.json()['href'])
        
    return download_urls