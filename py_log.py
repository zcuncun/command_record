import logging

#记录器
logger = logging.getLogger('server')
logger.propagate = False  # 不向上透传  避免重复输出
logger.setLevel(logging.INFO)  # 日志level  DEBUG INFO WARN ERROR CRITICAL 

#处理器
## 1.标准输出
sh = logging.StreamHandler()
sh.setLevel(logging.WARN)  # 设置输出级别, 只可设置不低于logger的输出级别
## 2.文件输出
fh = logging.FileHandler(filename="test.log",mode='w')  # 写入同一个文件用 mode='a'

# 格式器
fmt = logging.Formatter(fmt="[%(asctime)s][%(process)d][%(levelname)s] %(message)s" ,datefmt="%Y-%m-%d %H:%M:%S")

sh.setFormatter(fmt)
fh.setFormatter(fmt)
logger.addHandler(sh)
logger.addHandler(fh)
