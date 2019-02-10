import urllib.request as ur
import re
import time

def open_url(url):
    req = ur.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.1')
    response = ur.urlopen(req)
    html = response.read()
    return html

def find_img_addr(html):
    #pat = r'class="BDE_Image" (?:height="\d\d\d" ){0,1}pic_type="0" src="(.+\.(jpg))"'
    pat = r'src="(.{,100}\.(?:jpg|png))"'
    img_list = re.findall(pat, html)
    '''
    for each in img_list:
        print(each)
    '''
    return img_list
    
def download_img(img_list):
    for each in img_list:
        if each[0:4] != 'http':
            continue
        print('downloading: '+each)
        file_name = each.split('/')[-1]
        ur.urlretrieve(each, file_name)
        time.sleep(0.5)

def find_page_first(html):
    pat = r'76582_2.html'
    page_list = re.findall(pat, html)
    for each in page_list:
        print(each)

if __name__ == '__main__':
    find_page_first(open_url('http://moe.005.tv/76582.html').decode('utf-8'))
