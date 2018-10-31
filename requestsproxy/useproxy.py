import requests
from bs4 import BeautifulSoup
class User_Ip():
    def userIp(self):
        """
        爬取西刺代理网的免费IP
        """
        ip_ports=[]
        url="http://www.xicidaili.com/nn"   #西刺免费代理IP的国内高匿代理
        headers = {
            "Host": "www.xicidaili.com",
            "Referer": "http://www.xicidaili.com/",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
        }
        response=requests.get(url=url,headers=headers)
        text=BeautifulSoup(response.text,"html.parser")
        ips=text.select("#ip_list > tr > td:nth-of-type(2)")        #获取IP，注意：select查找元素，括号里面的标签之间要空格(tr > td)
        ports = text.select("#ip_list > tr > td:nth-of-type(3)")    #获取IP端口号
        for i in range(len(ips)):
            ip=str(str(ips[i]).split("<td>")[1]).split("</td>")[0]
            port = str(str(ports[i]).split("<td>")[1]).split("</td>")[0]
            ip_ports.append(ip+":"+port)       #把IP和端口号拼接起来，放入列表里面
        return ip_ports     #返回IP+端口号的列表
    def useProxiesList(self,ip_ports):
        """
        筛选出有用的IP代理
        :param ip_ports:
        :return:
        """
        UseProxiesList = []
        n = 0
        for i in range(len(ip_ports)):
            print('正在发送第%s个请求。\n\r' % i)
            proxies = {
                'http': 'http://' + ip_ports[i],
                'https': 'https://' + ip_ports[i],
            }
            try:
                requests.get('http://www,baidu.com', proxies=proxies, timeout=3)
                UseProxiesList.append(ip_ports[i])
            except:
                n += 1
                print('***已经有%s个代理被淘汰***' % n)
                print('可用代理数量%s' % len(UseProxiesList))
        return ('可用的IP代理列表：', UseProxiesList)
if __name__=="__main__":
    """因为IP数量比较多，建议建立多进程，线程或者协程"""
    print(User_Ip().useProxiesList(User_Ip().userIp()))