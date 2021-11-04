#! /usr/bin/python
# -*- coding: utf-8 -*-
# Create by zhoubaicun
"""
download.py
"""

import requests
from concurrent.futures import ThreadPoolExecutor, wait
import time


def download(url, thread=1):
    """下载某个文件并转为文件对象"""
    def download_part(url, start, end):
        headers = {'Range': 'bytes=%d-%d' % (start, end)}
        r = requests.get(url, headers=headers, stream=True)
        content = r.content
        r.close()
        return content
    tp = ThreadPoolExecutor(thread)
    print(f"Download from {url}")
    try:
        r = requests.get(url, stream=True)
        c_l = int(r.headers["Content-Length"])
        r.close()
        block_size= c_l // thread + 1
        tasks = []
        for start in range(0, c_l + 1, block_size):
            tasks.append(tp.submit(download_part, url, start, min(c_l, start + block_size - 1)))
        content = b''.join([task.result() for task in tasks])
        file = io.BytesIO(content)
        return file
    except Exception as e:
        print(f"Download failed")
        return None
