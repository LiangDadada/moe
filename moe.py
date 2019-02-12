import urllib.request as ur
import urllib.error as ue
import re
import time

def open_url(url):
    req = ur.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    try:
        response = ur.urlopen(req)
        html = response.read().decode('utf-8')
    except ur.HTTPError as reason:
        print(reason)
        html = ''
    except:
        print('未知错误，尝试跳过')
        html = ''
    return html

def find_img(url):
    html = open_url(url)
    #src="http://www.005.tv/uploads/allimg/190123/55-1Z123103FE47.jpg"
    pattern = r'src="(.{,100}?\.jpg)"'
    img_list = re.findall(pattern, html)
    return img_list

def find_page(url):
    html = open_url(url)
    #<a href='76557_2.html'><span class='pageicon'><i style='margin-bottom: 16px;'></i></span><span class='pagenum'>2</span>
    pattern = r"<a href='(\d+?_\d.html)'>"
    page_list = re.findall(pattern, html)
    return_list = []
    for each in page_list:
        return_list.append("http://moe.005.tv/"+each)
    return return_list

def find_addr(url):
    html = open_url(url)
    pattern = r'<li><a href="(http://moe.005.tv/\d+?.html)"'
    addr_list = re.findall(pattern, html)
    addr_list = list(set(addr_list))
    return addr_list

def page_download_img(url):
    img_list = find_img(url)
    for each in img_list:
        #print('正在下载：'+each)
        file_name = each.split('/')[-1]
		try:
			ur.urlretrieve(each, file_name)
        except:
			print("下载图片出现异常，尝试跳过")
		#time.sleep(1)
        

def addr_download_img(url):
    page_list = find_page(url)
    page_list.append(url)
    for each in page_list:
        print('正在下载：'+each)
        page_download_img(each)

def download_img(url):
    addr_list = find_addr(url)
    #addr_list = ['http://moe.005.tv/76610.html', 'http://moe.005.tv/68555.html', 'http://moe.005.tv/76610.html']
    for each in addr_list:
        print('打开地址： '+each)
        addr_download_img(each)
		
if __name__ == '__main__':
    print('这是moe主模块')
    download_img('http://moe.005.tv/moeimg')
