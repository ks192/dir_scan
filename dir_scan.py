# coding:utf-8
import time
from rich.align import Align
from my_lib.cmd_par import param
from my_lib.urls import *
from my_lib.ThreadRun import pool
from rich.table import  Table
from time import sleep

def logo():
    logo = """
oooooo     oooo ooooo   .oooooo.   ooooooooooooo   .oooooo.   ooooooooo.   oooooo   oooo 
 `888.     .8'  `888'  d8P'  `Y8b  8'   888   `8  d8P'  `Y8b  `888   `Y88.  `888.   .8'  
  `888.   .8'    888  888               888      888      888  888   .d88'   `888. .8'   
   `888. .8'     888  888               888      888      888  888ooo88P'     `888.8'    
    `888.8'      888  888               888      888      888  888`88b.        `888'     
     `888'       888  `88b    ooo       888      `88b    d88'  888  `88b.       888      
      `8'       o888o  `Y8bood8P'      o888o      `Y8bood8P'  o888o  o888o     o888o     
    """

    return logo


def main():
    print(Align.center(logo()))

    param_arr = param()  # 获取命令行参数
    url_list, num = url_pool(param_arr)  # 拼接url以及字典后的列表
    #表格系统
    table = Table(show_header=True, header_style="bold magenta", show_lines=True)
    table.add_column("URL", style="dim", justify="left")
    table.add_column("Code", justify="left")
    table.add_column("Content-Length")
    # table.add_column("Parameter", justify="right")

    pool(param_arr, url_list, num,table)

    return table



if __name__ == '__main__':

    table = main()
    print(table)
