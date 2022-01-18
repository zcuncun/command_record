#! /usr/bin/python
# -*- coding: utf-8 -*-
# Create by zhoubaicun
"""
download.py
"""

import requests
from concurrent.futures import ThreadPoolExecutor, wait
import time
import logging

def download(url, thread=1):
    """下载某个文件并转为文件对象"""
    def download_part(url, start, end, retry=3):
        # 每个分片至多尝试下载三次
        headers = {'Range': 'bytes=%d-%d' % (start, end - 1)}
        while retry:
            r = requests.get(url, headers=headers)
            content = r.content
            r.close()
            if len(content) == (end - start):
                break
            retry -= 1
        return content
    tp = ThreadPoolExecutor(thread)
    bytedlogger.logging.info(f"Download from {url}")
    try:
        r = requests.get(url, stream=True)
        c_l = int(r.headers["Content-Length"])
        r.close()
        block_size= c_l // thread + 1
        tasks = []
        for start in range(0, c_l, block_size):
            tasks.append(tp.submit(download_part, url, start, min(c_l, start + block_size)))
        content = b''.join([task.result() for task in tasks])
        r = requests.get(url)
        file = io.BytesIO(content)
        return file
    except Exception as e:
        logging.error(f"Download failed")
        raise
