from concurrent.futures import ThreadPoolExecutor
from rich.progress import Progress
from my_lib import req
from my_lib.display import dis
from time import sleep


def pool(param_arr, urls, total,table):
    with Progress(auto_refresh=False) as progress:
        is_exit = [False]
        task1 = progress.add_task("[cyan]扫描进度", total=total)
        ThreadPool = ThreadPoolExecutor(param_arr.pool)
        try:
            for url in urls:
                res = ThreadPool.submit(req.Req, url, param_arr, progress, task1, table, ThreadPool, id(is_exit))
                res.add_done_callback(dis)
            while not progress.finished:
                sleep(3)
            ThreadPool.shutdown(True)
        except KeyboardInterrupt:
            is_exit[0] = True
    return ThreadPool






