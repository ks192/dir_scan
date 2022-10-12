import requests
from my_lib import cmd_par
from time import sleep
from rich import print
import ctypes


class Req():
    headers = {'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104"',
               'sec-ch-ua-mobile': '?0',
               'sec-ch-ua-platform': 'Windows',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Sec-Fetch-Site': 'none',
               'Sec-Fetch-Mode': 'navigate',
               'Sec-Fetch-User': '?1',
               'Sec-Fetch-Dest': 'document',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'close'
               }
    cookies = {

    }
    protocol = None
    address = None

    proxies = {

    }

    def __init__(self, url, param_arr, progress, task, table, ThreadPool, is_exit):
        self.is_exit = ctypes.cast(is_exit, ctypes.py_object).value[0]
        self.ThreadPool=ThreadPool
        if self.is_exit:
            self.ThreadPool.shutdown(cancel_futures=True)
        else:
            pass
        self.table = table
        self.url = url
        self.protocol = url.split(':')[0]
        self.address = param_arr.proxies
        if self.address is None:
            self.proxies = None
        else:
            self.proxies = {'{}'.format(self.protocol): '{}'.format(self.address)}
        self.param = param_arr
        self.ua = self.param.ua
        self.cookie = param_arr.cookies
        self.diyhead = param_arr.diyhead
        self.data = param_arr.data
        self.method = param_arr.method
        self.progress = progress
        self.task = task
        self.timeout = param_arr.timeout
        self.head(self.param.head, 'headers')
        self.head(self.diyhead, 'diy')
        self.head(self.ua, 'user-agent')
        self.head(self.cookie, 'cookies')
        self.ThreadPool = ThreadPool
        self.main()

    def head(self, str_dic, flag):
        if flag == 'headers' and str_dic is not None:
            for i in str_dic:
                i_d = i.split(':')
                self.headers[i_d[0]] = i_d[1]
        elif flag == 'diy' and str_dic is not None:
            self.headers = {}
            for i in str_dic:
                i_d = i.split(':')
                self.headers[i_d[0]] = i_d[1]
        elif flag == 'cookies' and str_dic is not None:
            for i in str_dic:
                i_d = i.split('=')
                self.cookies[i_d[0]] = i_d[1]
        elif flag == 'user-agent' and str_dic is not None:
            self.headers['User-Agent'] = str_dic

    def get(self):
        self.content = requests.get(url=self.url, cookies=self.cookies,
                                headers=self.headers, timeout=self.timeout, proxies=self.proxies)
        self.over()

    def post(self):

        self.content = requests.post(url=self.url, cookies=self.cookies,
                                 data=self.data,
                                 timeout=self.timeout, proxies=self.proxies)

        self.over()


    def over(self):

        # self.progress.update(self.task, advance=1)
        # self.progress.refresh()
        return self

    def main(self):
        try:
            sleep(self.param.time)
            if self.method == 'get':
                self.get()
            elif self.method == 'post':
                self.post()
        except KeyboardInterrupt:
            self.ThreadPool.shutdown(cancel_futures=True)
