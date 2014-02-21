#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import subprocess
import shlex
import os
import glob

def download_unzip():
    base_url = 'http://www.sacred-texts.com'
    r = requests.get(base_url+'/download.htm')
    soup = BeautifulSoup(r.text)
    for e in soup.find_all('br'):
        e.extract()    
    main_list = soup.find('ol')
    all_links = main_list.find_all('a')
    urls = ['{}/{}'.format(base_url,link['href']) for link in all_links]
    if not os.path.exists('input'):
        os.makedirs('input')
    len_urls = len(urls)
    for i,url in enumerate(urls):
        local_filename = 'input/'+'_'.join(url.split('/')[-3:])
        r = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        print '{} [{}/{}]'.format(local_filename, i, len_urls)
        subprocess.call(['gunzip', '-f', local_filename])
    print 'Download and unzip done!'
    return len_urls
    
def main():
    len_urls = download_unzip()
    if not len_urls:
        len_urls = 351
    # clean up bad .gz files
    files = glob.glob("input/*.gz")
    [os.remove(f) for f in files]
    p1 = subprocess.Popen(shlex.split('ls input'), stdout=subprocess.PIPE)
    p2 = subprocess.Popen(shlex.split('wc -l'), stdin = p1.stdout, stdout=subprocess.PIPE)
    p2_out, _ = p2.communicate()
    print '{}/{} Files processed'.format(p2_out.strip(), len_urls)

if __name__=="__main__":
    main()


