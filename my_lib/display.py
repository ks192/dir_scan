from rich import print
from time import sleep
from my_lib import cmd_par



def dis(content):
    try:
        req_class = content.result()
        response = req_class.content
    except:
        print("程序异常终止,Ctrl + C 停止运行")
        response = None
        req_class =None
        sleep(3)
    if response is None:
        pass
    else:
        # 打印响应数据
        headers = response.request.headers
        body = response.request.body
        # print(response.request.method)
        # print(headers)
        url = response.request.url
        # http请求响应内容
        text = response.text
        # 响应状态码
        code = response.status_code
        # 程序运行的字典
        wordlist = req_class.param.wordlist
        # 输出信息
        table = req_class.table
        if code in req_class.param.code:
            print("[*] {} {}".format(url, code))
            table.add_row(str(url), str(code), str(len(text)))
        # 刷新进度条
        req_class.progress.update(req_class.task, advance=1)
        req_class.progress.refresh()






