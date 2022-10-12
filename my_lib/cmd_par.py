import argparse
from rich import print

def param(msg=None):
    param = argparse.ArgumentParser()

    param.add_argument('-w', '--wordlist', type=str, help='字典位置，当前命令行相对路径或绝对路径')
    param.add_argument('-u', '--url', type=str, help='输入目标URL')
    param.add_argument('-l', '--load_file', type=str, help='目标URL文件(每个url用换行隔开，包含协议如http:localhost)')
    param.add_argument('-p', '--port', type=int, nargs='*',
                       default=[80,443], help='目标端口默认80,443，如需自定义请使用，-p 80 443 8080')
    param.add_argument('-m', '--method', type=str, default='get', help='输入请求的参数,默认get,小写')
    param.add_argument('-d', '--data', help='输入请求的参数,非post模式不必设置值,默认GET')
    param.add_argument('--cookies', type=str, default=None,nargs='*', help='输入cookie，如果flag=ctf')
    param.add_argument('--ua', type=str,
                       default=None, help='输入user-agent，有默认的ua')
    param.add_argument('--proxies', type=str,default=None, help="输入要使用的代理。不支持socks5如 --proxies http://127.0.0.1:10809 ")
    param.add_argument('--head', type=str,default='',nargs='*' , help='输入要添加的head数据，如果使用的话。如--head abc:123 def:456')
    param.add_argument('--diyhead', type=str,default=None,nargs='*' , help='纯自定义headers。如--diyhead abc:123 def:456')
    param.add_argument('-t', '--time', type=float, default=0, help='每个线程请求时间间隔，默认0')
    param.add_argument('-to', '--timeout', type=int, default=1, help='请求超时时间，默认一秒')
    param.add_argument('--pool', type=int, default=5, help='线程数量,默认为10')
    param.add_argument('-s', '--suffix', type=str,nargs='*',default=None, help='字典后缀,如-s .txt .php .jsp')
    param.add_argument('-c', '--code', type=int, nargs='*', default=[200,403,502], help='要显示的响应状态码，如-c 404 403')

    res = param.parse_args()
    if msg is not None:
        print(param.error(msg + "python dir_scan.py -h 获取帮助"))
    elif res.url is None and res.load_file is None or res.wordlist is None:
        param.print_help()
        param.error('缺少必须的参数，添加扫描地址、字典地址，如 python dir_scan.py -u http://127.0.0.1 -w DictPath')
    return res
