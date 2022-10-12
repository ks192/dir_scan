from my_lib import cmd_par
from rich.progress import track
from rich import print
import requests


def read(file):
    try:
        with open(file, 'rb') as f:
            content = f.readlines()
            return content
    except:
        print("地址>>> {} <<<未找到文件,请检查地址是否正确".format(file))
        exit(0)


def url_pool(parame):
    global urls, url, ports, url_list
    global num
    num = 0
    urls = []
    ports = []
    url_list = []
    url = ''
    if parame.load_file is not None and parame.url is None:
        urls_path = read(parame.load_file)

        for i in track(sequence=urls_path, description="URL连通性验证。", transient=True):
            for port_ok in parame.port:
                url,flag = check(i.strip().decode() + ":" + str(port_ok))
                if flag is False and (i != urls_path[-1] or port_ok != parame.port[-1]):
                    print("访问失败===>{}该地址将跳过扫描".format(url))
                    continue
                elif flag is False and i == urls_path[-1] and port_ok == parame.port[-1] \
                        and len(urls) == 0:
                    cmd_par.param("没有可用url，请检查格式是否正确！")
                elif flag is False:
                    print("访问失败===>{}该地址将跳过扫描".format(url))
                    continue
                else:
                    parame_url = read(parame.wordlist)
                    num += len(parame_url)
                    for j in parame_url:
                        url_parame = j.strip().decode()
                        urls.append(i.strip().decode() + url_parame)
    elif parame.load_file is None and parame.url is None:
        param.error('请设置目标地址 -u 或 -l')
    elif parame.load_file is not None and parame.url is not None:
        param.error('url或者url文件请选择一个')
    else:
        for port_ok in track(parame.port,description="URL连通性验证。",transient=True):
            url,flag = check(parame.url + ":" + str(port_ok))
            if port_ok != parame.port[-1] and flag is False:
                print("访问失败===>{}该地址将跳过扫描".format(parame.url + ":" + str(port_ok)))
                continue
            elif flag is False and port_ok == parame.port[-1]  and len(urls) == 0:
                cmd_par.param("请检查目标连通性，给定端口{}连接失败".format(parame.port))
            elif flag is False:
                print("访问失败===>{}该地址将跳过扫描".format(parame.url + ":" + str(port_ok)))
                continue
            else:
                parame_url = read(parame.wordlist)
                num = len(parame_url)
                for i in parame_url:
                    url_parame = i.strip().decode()
                    if url_parame[-1] !='/':
                        url_parame = url_parame+'/'
                    urls.append(str(url) + url_parame)

    if parame.suffix is not None:
        for i in urls:
            if i[-1]=='/':
                i = i[:-1]
            for j in parame.suffix:
                url_list.append(i+j)
    else:
        url_list = urls

    return url_list, num


def check(url):
    try:
        requests.get(url, headers={'Connection': 'close'}, timeout=2)
        return url,True
    except KeyboardInterrupt as Key:
        exit(0)
    except Exception as ex:

        return url ,False

