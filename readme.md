

> 简单易用的目录扫描器，使用了rich的输出方式。显示干净，用法简单，下载即用。
>
> 免责声明：请不要使用该工具进行非法渗透，该工具只做学习交流使用。

## 文件夹介绍

- config

  - 用来存放配置文件，目前开发功能还未用到等后续使用

- dic

  - 存放字典文件

- my_lib

  - cmd_par.py      实现命令行参数获取
  - display.py         实现扫描信息的显示
  - req.py                实现网络请求
  - ThreadRun.py   实现线程池的控制
  - urls.py                实现url的组合

  ## 说明文档

```
'-w', '--wordlist', '如 -w ./dic/top7000.txt'

'-u', '--url', '如 -u http://127.0.0.1'

'-l', '--load_file', '目标URL文件(每个url用换行隔开，包含协议如http:localhost)'

'-p', '--port',default=[80,443], '目标端口默认80,443，如需自定义请使用，-p 80 443 8080'
                   
'-m', '--method',default='get', '输入使用的请求方式默认get，如需post请添加参数 -m post'

'-d', '--data', '输入请求的参数,非post模式不必设置值,默认GET'

'--cookies', '输入cookie，如果flag1=ctf多个参数用空格隔开'

'--ua', '输入user-agent，有默认的ua'

'--proxies', "输入要使用的代理。不支持socks5如 --proxies http://127.0.0.1:10809 "

'--head', default='',nargs='*' , '输入要添加的head数据，如果使用的话。如--head abc:123 def:456'

'--diyhead',default=None, '纯自定义headers。如--diyhead abc:123 def:456'

'-t', '--time''每个线程请求时间间隔，默认0，使用方法 -t 1 表示间隔1秒'

'-to', '--timeout', default=1, '请求超时时间，默认一秒。用法： -to 3设置超时时间为3秒 '

'--pool', '线程数量,默认为10用法： --pool 1 线程设置为1'

'-s', '--suffix',default=None, '字典后缀,如-s .txt .php .jsp'

'-c', '--code', default=[200,403,502], '要显示的响应状态码，如-c 404 403'
```



> 或许这个工具不是很好，但是把参数都标记清楚了。真的很无语一些工具好多功能还要查不查都不知道要怎么用，说明文档也不清楚，所以写了这个工具，该工具会一边使用一边迭代升级。
