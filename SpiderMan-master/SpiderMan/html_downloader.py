import urllib3
import urllib.request


class HtmlDownLoader(object):

    def download(self,url):
        print ("in html_downloader")
        http = urllib3.PoolManager()
        if url is None:
            return None
        #print(urllib.request.urlopen(url).read())
        response = urllib.request.urlopen(url)
        #response = http.request('GET', url)
        #print("response code is %s" % (response.read()))
        if response.getcode == 200:
            return None
        else:
            return response.read()